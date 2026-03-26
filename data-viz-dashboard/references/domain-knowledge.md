# Domain Knowledge Base

Industry-specific metrics, dimensions, and analysis scenarios for data visualization.

## Marketing Domain

### Core Metrics

| Metric | Definition | Formula | Unit | Typical Range |
|--------|------------|---------|------|---------------|
| ROI | Return on Investment | (Revenue - Cost) / Cost x 100% | % | 0% - 500% |
| Conversion Rate (CVR) | Percentage of visitors who convert | Conversions / Visitors x 100% | % | 1% - 15% |
| CAC | Customer Acquisition Cost | Total Marketing Cost / New Customers | Currency | Varies |
| LTV | Customer Lifetime Value | Average Purchase x Frequency x Lifespan | Currency | Varies |
| ROAS | Return on Ad Spend | Revenue from Ads / Ad Spend | Ratio | 1x - 10x |
| Engagement Rate | User interaction rate | Engagements / Impressions x 100% | % | 1% - 20% |

### Support Metrics

| Metric | Definition | Unit |
|--------|------------|------|
| Click-through Rate (CTR) | Clicks / Impressions | % |
| Bounce Rate | Single-page sessions / Total sessions | % |
| Average Session Duration | Total session time / Sessions | Minutes |
| Page Views per Session | Total page views / Sessions | Count |

### Typical Dimensions

- **Channel**: Organic, Paid, Social, Email, Direct
- **Campaign**: Specific marketing campaigns
- **Region**: Geographic areas (East/West/North/South)
- **Device**: Desktop, Mobile, Tablet
- **Time**: Daily, Weekly, Monthly, Quarterly

### Common Analysis Scenarios

1. **Campaign Performance**: Compare ROI/ROAS across campaigns
2. **Channel Attribution**: Which channels drive conversions
3. **Funnel Analysis**: Where users drop off
4. **A/B Test Results**: Compare variant performance

---

## Product Domain

### Core Metrics

| Metric | Definition | Formula | Unit | Typical Range |
|--------|------------|---------|------|---------------|
| DAU/MAU | Daily/Monthly Active Users | Unique users in period | Count | Varies |
| Retention Rate | Users returning over time | Returning Users / Initial Users x 100% | % | 20% - 80% |
| NPS | Net Promoter Score | % Promoters - % Detractors | Score | -100 to 100 |
| Feature Adoption | Users using feature | Feature Users / Total Users x 100% | % | 5% - 60% |
| Session Duration | Time spent in product | Average session length | Minutes | 2 - 30 min |

### Support Metrics

| Metric | Definition | Unit |
|--------|------------|------|
| Crash Rate | Crashes / Sessions | % |
| Load Time | Page/app load duration | Seconds |
| Error Rate | Errors / Total requests | % |
| Support Tickets | Number of support requests | Count |

### Typical Dimensions

- **User Segment**: Free, Trial, Paid, Enterprise
- **Platform**: Web, iOS, Android
- **Feature**: Specific product features
- **User Cohort**: Sign-up date groups

---

## Finance Domain

### Core Metrics

| Metric | Definition | Formula | Unit | Typical Range |
|--------|------------|---------|------|---------------|
| Revenue | Total income | Sum of all income | Currency | Varies |
| Gross Margin | Profit after direct costs | (Revenue - COGS) / Revenue x 100% | % | 20% - 80% |
| Operating Margin | Operating profit / Revenue | Operating Income / Revenue x 100% | % | 5% - 30% |
| Cash Flow | Net cash movement | Inflows - Outflows | Currency | Varies |
| Burn Rate | Monthly cash consumption | Monthly expenses | Currency | Varies |

### Support Metrics

| Metric | Definition | Unit |
|--------|------------|------|
| Accounts Receivable | Money owed by customers | Currency |
| Accounts Payable | Money owed to vendors | Currency |
| Debt-to-Equity | Total debt / Total equity | Ratio |
| Quick Ratio | Liquid assets / Current liabilities | Ratio |

### Typical Dimensions

- **Department**: Sales, Marketing, Engineering, Operations
- **Cost Center**: Budget allocation areas
- **Time Period**: Monthly, Quarterly, Yearly
- **Region**: Geographic business units

---

## Operations Domain

### Core Metrics

| Metric | Definition | Formula | Unit | Typical Range |
|--------|------------|---------|------|---------------|
| Throughput | Output per time unit | Units / Time | Count/time | Varies |
| Utilization | Resource usage efficiency | Actual / Capacity x 100% | % | 60% - 90% |
| Cycle Time | Time to complete process | End time - Start time | Hours/Days | Varies |
| Defect Rate | Errors / Total output | Defects / Total x 100% | % | 0.1% - 5% |
| SLA Compliance | Meeting service level | Met SLAs / Total SLAs x 100% | % | 95% - 99.9% |

### Typical Dimensions

- **Process**: Workflow stages
- **Team**: Responsible groups
- **Shift**: Time periods
- **Equipment**: Machines/systems involved

---

## Metric Classification for Chart Selection

### Trend Metrics (Time Series)
- Best for: Line charts, Area charts
- Examples: Revenue over time, User growth, Stock prices

### Comparison Metrics (Categorical)
- Best for: Bar charts, Column charts
- Examples: Sales by region, Performance by team

### Composition Metrics (Part-to-Whole)
- Best for: Pie charts, Donut charts, Stacked bars
- Examples: Revenue breakdown, Budget allocation

### Distribution Metrics (Spread)
- Best for: Histograms, Box plots, Scatter plots
- Examples: Customer age distribution, Price ranges

### KPI Metrics (Single Value)
- Best for: KPI cards, Gauges
- Examples: Total revenue, Current users, Conversion rate

---

## Mock Data Generation Guidelines

### Distribution Selection

| Metric Type | Recommended Distribution | Reason |
|-------------|-------------------------|--------|
| Conversion rates | Beta(α=2, β=40) | Bounded 0-1, right-skewed |
| Revenue | Log-normal | Always positive, right-skewed |
| User counts | Poisson or Negative Binomial | Count data, variance > mean |
| Ratings | Beta(α=2, β=2) | Bounded 0-1, centered |
| Time durations | Gamma or Exponential | Always positive, right-skewed |

### Realistic Value Ranges

```json
{
  "marketing": {
    "cvr": { "min": 0.01, "max": 0.15, "typical": 0.05 },
    "ctr": { "min": 0.01, "max": 0.10, "typical": 0.03 },
    "roi": { "min": 0, "max": 5, "typical": 1.5 }
  },
  "product": {
    "retention_d1": { "min": 0.30, "max": 0.80, "typical": 0.50 },
    "retention_d7": { "min": 0.15, "max": 0.50, "typical": 0.25 },
    "retention_d30": { "min": 0.05, "max": 0.30, "typical": 0.10 }
  },
  "finance": {
    "gross_margin": { "min": 0.20, "max": 0.80, "typical": 0.45 },
    "operating_margin": { "min": 0.05, "max": 0.30, "typical": 0.15 }
  }
}
```

### Outlier Injection

For realistic data, inject outliers with:
- Probability: 2-5% of records
- Range: 2-3 standard deviations from mean
- Types: Extreme highs, extreme lows, missing values
