# Chart Type Mapping Rules

Rules for mapping metrics and dimensions to appropriate chart types.

## Decision Matrix

### By Metric Category

| Metric Category | Primary Chart | Alternative | Use Case |
|-----------------|---------------|-------------|----------|
| **Trend** | Line Chart | Area Chart | Show change over time |
| **Comparison** | Bar Chart | Column Chart | Compare categories |
| **Composition** | Pie Chart | Donut, Stacked Bar | Show part-to-whole |
| **Distribution** | Histogram | Box Plot, Scatter | Show data spread |
| **KPI** | KPI Card | Gauge | Single value display |
| **Correlation** | Scatter Plot | Bubble Chart | Show relationships |
| **Ranking** | Horizontal Bar | Column Chart | Ordered comparison |
| **Flow** | Funnel | Sankey | Process stages |

### By Dimension Type

| Dimension Type | Suitable Charts | Notes |
|----------------|-----------------|-------|
| **Temporal** (time) | Line, Area, Column | X-axis = time |
| **Categorical** | Bar, Pie, Column | Limited categories (<10) |
| **Geographic** | Map, Choropleth | Location-based |
| **Hierarchical** | Treemap, Sunburst | Nested categories |

### By Data Characteristics

| Characteristic | Recommended | Avoid |
|----------------|-------------|-------|
| Many categories (>10) | Horizontal Bar | Pie |
| Time series | Line, Area | Pie |
| Part-to-whole | Pie, Stacked Bar | Line |
| Negative values | Bar, Line | Pie |
| Large value range | Log scale Bar/Line | Linear scale |

## Built-in Chart Templates

### 1. Bar Chart (`bar.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["comparison", "ranking"],
  "dimensionTypes": ["categorical"],
  "maxDimensions": 2,
  "maxMetrics": 3
}
```

**Variants**:
- `vertical` - Standard column chart
- `horizontal` - Better for long labels
- `stacked` - Show composition within comparison
- `grouped` - Compare multiple metrics side-by-side

**Best For**:
- Sales by region
- Performance by team
- Revenue by product

### 2. Line Chart (`line.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["trend"],
  "dimensionTypes": ["temporal"],
  "maxDimensions": 1,
  "maxMetrics": 5
}
```

**Variants**:
- `basic` - Single line
- `multi` - Multiple series
- `smooth` - Curved lines

**Best For**:
- Revenue over time
- User growth trends
- Stock prices

### 3. Pie Chart (`pie.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["composition"],
  "dimensionTypes": ["categorical"],
  "maxDimensions": 1,
  "maxMetrics": 1,
  "maxCategories": 8
}
```

**Variants**:
- `basic` - Standard pie
- `donut` - With center space
- `rose` - Nightingale chart

**Best For**:
- Market share
- Budget allocation
- Revenue breakdown

### 4. Area Chart (`area.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["trend", "composition"],
  "dimensionTypes": ["temporal"],
  "maxDimensions": 1,
  "maxMetrics": 4
}
```

**Variants**:
- `basic` - Single area
- `stacked` - Cumulative composition
- `stream` - Centered stream graph

**Best For**:
- Cumulative revenue
- Traffic sources over time
- Market share evolution

### 5. Scatter Plot (`scatter.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["correlation", "distribution"],
  "dimensionTypes": ["continuous"],
  "maxDimensions": 2,
  "maxMetrics": 3
}
```

**Variants**:
- `basic` - Two variables
- `bubble` - Third variable as size
- `scatter-matrix` - Multiple comparisons

**Best For**:
- Price vs. volume
- Correlation analysis
- Outlier detection

### 6. KPI Card (`kpi-card.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["kpi"],
  "dimensionTypes": [],
  "maxDimensions": 0,
  "maxMetrics": 1
}
```

**Variants**:
- `basic` - Value + label
- `with-trend` - Include trend indicator
- `with-sparkline` - Mini trend chart

**Best For**:
- Total revenue
- Current users
- Conversion rate

### 7. Table (`table.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["any"],
  "dimensionTypes": ["any"],
  "maxDimensions": 5,
  "maxMetrics": 10
}
```

**Variants**:
- `basic` - Simple data table
- `sortable` - Click to sort
- `paginated` - Large datasets

**Best For**:
- Detailed data view
- Export-ready format
- High-dimensional data

### 8. Funnel Chart (`funnel.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["flow"],
  "dimensionTypes": ["sequential"],
  "maxDimensions": 1,
  "maxMetrics": 1
}
```

**Best For**:
- Conversion funnel
- Sales pipeline
- User onboarding flow

### 9. Radar Chart (`radar.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["comparison"],
  "dimensionTypes": ["categorical"],
  "minDimensions": 3,
  "maxDimensions": 8,
  "maxMetrics": 3
}
```

**Best For**:
- Multi-dimensional comparison
- Skill assessment
- Performance across categories

### 10. Heatmap (`heatmap.chart.json`)

**Match Rules**:
```json
{
  "metricTypes": ["distribution", "comparison"],
  "dimensionTypes": ["categorical", "temporal"],
  "minDimensions": 2,
  "maxDimensions": 2
}
```

**Best For**:
- Time-of-day patterns
- Correlation matrix
- Geographic density

## Component Resolution Algorithm

```typescript
function resolveChartType(
  metrics: Metric[],
  dimensions: Dimension[],
  userPreference?: ChartType
): ChartResolution {

  // 1. User preference takes priority
  if (userPreference) {
    return { source: 'template', chart: getTemplate(userPreference) }
  }

  // 2. Classify metric type
  const metricType = classifyMetric(metrics)

  // 3. Check dimension constraints
  const dimCount = dimensions.length
  const dimTypes = dimensions.map(d => d.type)

  // 4. Find matching templates
  const candidates = registry.findByRules({
    metricTypes: [metricType],
    dimensionTypes: dimTypes,
    maxDimensions: dimCount,
    maxMetrics: metrics.length
  })

  // 5. Return best match or AI-generated
  if (candidates.length > 0) {
    return { source: 'template', chart: candidates[0] }
  }

  return { source: 'ai-generated', description: 'No matching template' }
}

function classifyMetric(metrics: Metric[]): MetricCategory {
  // Has time dimension → trend
  // Single value → kpi
  // Part-to-whole relationship → composition
  // Multiple categories → comparison
  // Two continuous variables → correlation
}
```

## Chart Selection Decision Tree

```
START
  │
  ├─ Single value to display?
  │   └─ YES → KPI Card
  │
  ├─ Time dimension present?
  │   ├─ YES + Single metric → Line Chart
  │   ├─ YES + Multiple metrics → Multi-Line or Area
  │   └─ YES + Cumulative → Stacked Area
  │
  ├─ Categorical comparison?
  │   ├─ Few categories (<5) → Column Chart
  │   ├─ Many categories (5-15) → Horizontal Bar
  │   └─ Many categories (>15) → Table
  │
  ├─ Part-to-whole?
  │   ├─ Few categories (<6) → Pie/Donut
  │   ├─ Many categories → Treemap
  │   └─ Over time → Stacked Area
  │
  ├─ Correlation between variables?
  │   ├─ Two variables → Scatter Plot
  │   └─ Three variables → Bubble Chart
  │
  ├─ Sequential stages?
  │   └─ YES → Funnel
  │
  └─ Multi-dimensional comparison?
      ├─ 3-8 dimensions → Radar Chart
      └─ 2 dimensions + density → Heatmap
```

## Interaction Patterns by Chart Type

| Chart Type | Default Interactions | Optional |
|------------|---------------------|----------|
| Bar | Hover tooltip, Click filter | Drill-down, Sort |
| Line | Hover tooltip, Brush zoom | Annotation, Compare |
| Pie | Hover highlight | Click filter |
| KPI Card | None | Click for details |
| Table | Sort, Paginate | Filter, Export |
| Scatter | Hover tooltip, Brush select | Zoom, Lasso |
| Funnel | Hover highlight | Click for stage details |

## Color Application Rules

### Sequential Data (Low to High)
- Use single hue gradient
- Lighter = lower, Darker = higher
- Example: Blues for revenue tiers

### Categorical Data
- Use distinct hues from theme palette
- Ensure sufficient contrast
- Limit to 7-8 distinct colors max

### Diverging Data (Negative to Positive)
- Two hues meeting at neutral
- Example: Red (negative) → White → Green (positive)

### Alert/KPI Colors
- Green: Positive/Good
- Red: Negative/Bad
- Yellow: Warning/Caution
- Blue: Neutral/Information
