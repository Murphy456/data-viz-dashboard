#!/usr/bin/env python3
"""
Generate mock data for data visualization dashboards based on metric specifications.
"""

import argparse
import json
import random
import math
from datetime import datetime, timedelta
from typing import Any, Optional
from dataclasses import dataclass
from enum import Enum


class Distribution(Enum):
    UNIFORM = "uniform"
    NORMAL = "normal"
    BETA = "beta"
    LOGNORMAL = "lognormal"
    EXPONENTIAL = "exponential"


@dataclass
class MockSpec:
    """Mock data specification for a metric."""
    range_min: float
    range_max: float
    distribution: Distribution
    typical_value: float
    decimals: int = 2
    outlier_probability: float = 0.0
    outlier_range: Optional[tuple[float, float]] = None


@dataclass
class Dimension:
    """Dimension definition."""
    name: str
    values: list[str]
    type: str = "categorical"  # categorical, temporal, geographic


def generate_uniform(spec: MockSpec) -> float:
    """Generate a value from uniform distribution."""
    value = random.uniform(spec.range_min, spec.range_max)
    return round(value, spec.decimals)


def generate_normal(spec: MockSpec) -> float:
    """Generate a value from normal distribution."""
    mean = (spec.range_min + spec.range_max) / 2
    std = (spec.range_max - spec.range_min) / 6  # 99.7% within range

    value = random.gauss(mean, std)
    value = max(spec.range_min, min(spec.range_max, value))
    return round(value, spec.decimals)


def generate_beta(spec: MockSpec) -> float:
    """Generate a value from beta distribution (for rates/percentages)."""
    # Beta distribution is good for values between 0 and 1
    # Scale to the desired range
    alpha, beta_param = 2, 5  # Right-skewed, typical for conversion rates

    value = random.betavariate(alpha, beta_param)
    # Scale to range
    scaled = spec.range_min + value * (spec.range_max - spec.range_min)
    return round(scaled, spec.decimals)


def generate_lognormal(spec: MockSpec) -> float:
    """Generate a value from log-normal distribution (for revenue, counts)."""
    # Log-normal is good for always-positive, right-skewed data
    mu = math.log(spec.typical_value)
    sigma = 0.5  # Moderate spread

    value = random.lognormvariate(mu, sigma)
    value = max(spec.range_min, min(spec.range_max, value))
    return round(value, spec.decimals)


def generate_exponential(spec: MockSpec) -> float:
    """Generate a value from exponential distribution (for time durations)."""
    lambda_param = 1 / spec.typical_value
    value = random.expovariate(lambda_param)
    value = max(spec.range_min, min(spec.range_max, value))
    return round(value, spec.decimals)


def generate_value(spec: MockSpec) -> float:
    """Generate a single value based on the distribution."""
    generators = {
        Distribution.UNIFORM: generate_uniform,
        Distribution.NORMAL: generate_normal,
        Distribution.BETA: generate_beta,
        Distribution.LOGNORMAL: generate_lognormal,
        Distribution.EXPONENTIAL: generate_exponential,
    }

    generator = generators.get(spec.distribution, generate_normal)
    value = generator(spec)

    # Inject outlier with probability
    if spec.outlier_probability > 0 and spec.outlier_range:
        if random.random() < spec.outlier_probability:
            value = random.uniform(spec.outlier_range[0], spec.outlier_range[1])
            value = round(value, spec.decimals)

    return value


def generate_categorical_data(
    dimension: Dimension,
    metrics: dict[str, MockSpec],
    sample_size: int = 100
) -> list[dict[str, Any]]:
    """Generate data for categorical dimension."""
    data = []

    for _ in range(sample_size):
        row = {dimension.name: random.choice(dimension.values)}
        for metric_name, spec in metrics.items():
            row[metric_name] = generate_value(spec)
        data.append(row)

    return data


def generate_time_series_data(
    start_date: str,
    end_date: str,
    metrics: dict[str, MockSpec],
    granularity: str = "daily"
) -> list[dict[str, Any]]:
    """Generate time series data."""
    data = []

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")

    delta_map = {
        "hourly": timedelta(hours=1),
        "daily": timedelta(days=1),
        "weekly": timedelta(weeks=1),
        "monthly": timedelta(days=30),
    }

    delta = delta_map.get(granularity, timedelta(days=1))
    current = start

    while current <= end:
        row = {"date": current.strftime("%Y-%m-%d")}
        for metric_name, spec in metrics.items():
            row[metric_name] = generate_value(spec)
        data.append(row)
        current += delta

    return data


def generate_comparison_data(
    dimensions: list[Dimension],
    metrics: dict[str, MockSpec]
) -> list[dict[str, Any]]:
    """Generate comparison data across multiple dimensions."""
    data = []

    # Generate all combinations
    def generate_combinations(dims: list[Dimension], index: int = 0, current: dict = None) -> list[dict]:
        if current is None:
            current = {}
        if index >= len(dims):
            return [current.copy()]

        results = []
        for value in dims[index].values:
            current[dims[index].name] = value
            results.extend(generate_combinations(dims, index + 1, current))
        return results

    combinations = generate_combinations(dimensions)

    for combo in combinations:
        for metric_name, spec in metrics.items():
            combo[metric_name] = generate_value(spec)
        data.append(combo)

    return data


def generate_kpi_data(
    metrics: dict[str, MockSpec],
    include_trend: bool = True
) -> dict[str, Any]:
    """Generate KPI card data."""
    data = {}

    for metric_name, spec in metrics.items():
        current_value = generate_value(spec)
        previous_value = generate_value(spec)

        change = current_value - previous_value
        change_percent = (change / previous_value * 100) if previous_value != 0 else 0

        data[metric_name] = {
            "value": current_value,
            "previousValue": previous_value,
            "change": round(change, spec.decimals),
            "changePercent": round(change_percent, 1),
            "trend": "up" if change > 0 else "down" if change < 0 else "neutral"
        }

    return data


def generate_funnel_data(
    stages: list[str],
    total_count: int,
    drop_off_rates: list[float]
) -> list[dict[str, Any]]:
    """Generate funnel data."""
    data = []
    current_count = total_count

    for i, stage in enumerate(stages):
        data.append({
            "stage": stage,
            "count": int(current_count),
            "percentage": round(current_count / total_count * 100, 1)
        })
        if i < len(drop_off_rates):
            current_count *= (1 - drop_off_rates[i])

    return data


def main():
    parser = argparse.ArgumentParser(description="Generate mock data for dashboards")
    parser.add_argument("--config", help="Path to config JSON file")
    parser.add_argument("--output", default="mock-data.json", help="Output file path")
    parser.add_argument("--type", choices=["categorical", "timeseries", "comparison", "kpi", "funnel"],
                       default="categorical", help="Type of data to generate")
    parser.add_argument("--sample-size", type=int, default=100, help="Number of samples")

    args = parser.parse_args()

    if args.config:
        with open(args.config, 'r', encoding='utf-8') as f:
            config = json.load(f)
    else:
        # Default demo configuration
        config = {
            "metrics": {
                "revenue": {
                    "range": [10000, 100000],
                    "distribution": "lognormal",
                    "typical_value": 50000,
                    "decimals": 0
                },
                "conversion_rate": {
                    "range": [0.01, 0.15],
                    "distribution": "beta",
                    "typical_value": 0.05,
                    "decimals": 4
                }
            },
            "dimensions": [
                {
                    "name": "region",
                    "values": ["East", "West", "North", "South"],
                    "type": "categorical"
                }
            ]
        }

    # Parse specs
    metrics = {}
    for name, spec_dict in config.get("metrics", {}).items():
        metrics[name] = MockSpec(
            range_min=spec_dict["range"][0],
            range_max=spec_dict["range"][1],
            distribution=Distribution(spec_dict.get("distribution", "normal")),
            typical_value=spec_dict.get("typical_value", (spec_dict["range"][0] + spec_dict["range"][1]) / 2),
            decimals=spec_dict.get("decimals", 2),
            outlier_probability=spec_dict.get("outlier_probability", 0),
            outlier_range=tuple(spec_dict["outlier_range"]) if "outlier_range" in spec_dict else None
        )

    dimensions = [
        Dimension(
            name=d["name"],
            values=d["values"],
            type=d.get("type", "categorical")
        )
        for d in config.get("dimensions", [])
    ]

    # Generate data based on type
    if args.type == "categorical":
        data = generate_categorical_data(dimensions[0], metrics, args.sample_size)
    elif args.type == "timeseries":
        data = generate_time_series_data(
            config.get("start_date", "2024-01-01"),
            config.get("end_date", "2024-12-31"),
            metrics,
            config.get("granularity", "daily")
        )
    elif args.type == "comparison":
        data = generate_comparison_data(dimensions, metrics)
    elif args.type == "kpi":
        data = generate_kpi_data(metrics)
    elif args.type == "funnel":
        data = generate_funnel_data(
            config.get("stages", ["Awareness", "Interest", "Consideration", "Conversion"]),
            config.get("total_count", 10000),
            config.get("drop_off_rates", [0.5, 0.4, 0.3])
        )
    else:
        data = []

    # Write output
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Generated {len(data)} records to {args.output}")


if __name__ == "__main__":
    main()
