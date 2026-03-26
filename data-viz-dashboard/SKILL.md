---
name: data-viz-dashboard
description: >
  Generate interactive data visualization dashboards from vague ideas through a 6-step guided workflow.
  ALWAYS use this skill when users mention ANY data visualization need - dashboards, charts, reports,
  analytics, KPIs, metrics, or data presentation. Trigger even if they just say "show me the data",
  "visualize this", "make a chart", or mention comparing/analyzing data. Don't wait for explicit
  "dashboard" keyword. Examples: "create a sales dashboard", "visualize regional ROI comparison",
  "build an activity analysis report", "generate quarterly review charts", "make a KPI dashboard",
  "show me the numbers", "compare performance across teams", "what's the trend".
---

# Data Visualization Dashboard Generator

Transform vague data ideas into interactive, production-ready React dashboards through a structured 6-step workflow.

## When to Use This Skill

Trigger this skill when users request:
- Creating dashboards or data visualizations
- Building charts, graphs, or analytics interfaces
- Generating reports with visual data presentation
- Converting data ideas into interactive UI
- Comparing metrics, showing trends, or analyzing performance
- Any request involving "data", "metrics", "KPIs", "analytics"

## Example Triggers

| User Phrase | Domain | Likely Charts |
|-------------|--------|---------------|
| "帮我做一个销售看板" | Sales | KPI Cards + Bar Chart |
| "分析各渠道ROI对比" | Marketing | Horizontal Bar |
| "生成Q3活动效果报告" | Marketing | Funnel + Line |
| "展示用户留存趋势" | Product | Line + Area |
| "对比各区域业绩" | Sales | Grouped Bar |
| "财务报表可视化" | Finance | Table + Pie |
| "运营数据大屏" | Operations | KPI + Multi-chart |

## Quick Chart Selection Guide

| Metric Type | Chart Component | Use Case |
|------------|-----------------|----------|
| Trend over time | `LineChart.tsx` | Retention, growth, revenue trend |
| Category comparison | `BarChart.tsx` | Regional sales, channel performance |
| Part-to-whole | `PieChart.tsx` | Budget allocation, market share |
| Conversion stages | `FunnelChart.tsx` | Marketing funnel, user journey |
| Correlation | `ScatterChart.tsx` | Price vs sales, user behavior |
| KPI summary | `KPICard.tsx` | Total revenue, conversion rate |

## Core Workflow: 6-Step Guided Process

### Step 0: Socratic Dialogue (Requirement Gathering)

**Goal**: Transform vague ideas into structured requirements through guided questioning.

**Process**:
1. Detect business domain (marketing/product/finance/operations)
2. Ask 6-8 targeted questions with options + recommendations
3. Converge when >=3 dimensions captured and clarity score > 0.7

**Key Questions**:
- What business are you analyzing?
- Who will view this dashboard?
- What dimensions to compare? (region/channel/time)
- What core metrics matter most? (max 3)
- What's the time range?
- What decisions will this inform?
- Display format preference? (single-page/multi-page/big-screen)

**Output**: Structured `UserIntent` summary

### Step 1: Story + Metrics Definition

**Goal**: Convert intent into quantifiable metrics with mock data specifications.

**Process**:
1. Generate story narrative from dialogue history
2. Define core metrics (1-3 KPIs) with formulas
3. Define support metrics with mock specifications
4. Map data dimensions and granularity
5. Generate data source schema

**Output**: `MetricSystem` with `MockDataSpec` for each metric

**Mock Spec Structure**:
```typescript
interface MockDataSpec {
  range: [number, number]      // Value range
  distribution: 'normal' | 'beta' | 'uniform'
  typicalValue: number         // Typical value for realistic data
  outliers?: { probability: number; range: [number, number] }
}
```

### Step 2: Design + Wireframe

**Goal**: Create visual layout specification with user confirmation.

**Sub-steps**:
1. **2A**: Collect layout preferences (resolution/framework/navigation/theme)
2. **2B**: Generate wireframe layout with component mapping
3. **2C**: Render interactive wireframe preview
4. **2D**: User confirms wireframe (checklist mode, not one-click)
5. **2E**: Generate design document to local files
6. **2F**: Quick review with minor adjustments allowed

**Component Resolution**:
- Match metrics to built-in chart templates first
- Fall back to AI-generated components for complex cases

**Output**: `DesignDoc` (locked) stored as `design-docs/page-*.md`

### Step 3: Execution Plan Generation

**Goal**: Create atomic, testable code generation steps.

**Process**:
1. Parse design doc → extract file list
2. Analyze dependencies → topological sort
3. Decompose into atomic steps
4. Generate quantified test specs for each step
5. Allocate context budget per step
6. Mark component source (template vs new)

**Output**: `ExecutionPlan` with ordered steps

### Step 4: TDD Code Generation

**Goal**: Generate tested, production-ready code automatically.

**TDD Cycle per Step**:
```
[READ] → [RED: write tests] → [GREEN: write code] → [REFACTOR] → [VERIFY]
```

**Template Path** (for matched components):
- Read template → Adapt types → Inject theme → Write → Test

**New Generation Path** (for custom components):
- Read specs → Write tests first → Generate code → Run tests → Fix (max 3 rounds)

**Quality Gates**:
- All tests pass (unit + integration)
- ESLint + Prettier + TypeScript clean
- Design doc consistency check passed
- No regression in previous steps

**Output**: Complete React project with tests

### Step 5: Delivery

**Goal**: Package and deliver the final product.

**Deliverables**:
- Complete project code (runnable)
- Design document
- Test report
- README with usage instructions
- Preview server (local dev)

## Using Bundled Resources

### References

Load domain knowledge and chart mapping rules as needed:

- `references/domain-knowledge.md` - Industry metrics definitions (marketing/product/finance)
- `references/chart-mapping.md` - Rules for mapping metrics to chart types
- `references/workflow-guide.md` - Detailed workflow instructions

### Scripts

Execute for deterministic operations:

- `scripts/init_project.py` - Initialize React + Vite + Recharts project
- `scripts/generate_mock.py` - Generate mock data from specifications

### Assets

Copy or adapt for output:

- `assets/project-template/` - Base project structure
- `assets/chart-components/` - Reusable chart templates:
  - `BarChart.tsx` - Vertical/Horizontal/Stacked/Grouped variants
  - `LineChart.tsx` - Basic/Multi/Smooth variants
  - `AreaChart.tsx` - Basic/Stacked variants
  - `PieChart.tsx` - Pie/Donut variants
  - `ScatterChart.tsx` - Scatter/Bubble variants
  - `FunnelChart.tsx` - Conversion funnel
  - `KPICard.tsx` - KPI with trend indicator
- `assets/themes/` - Color theme configurations

## Technical Stack

| Layer | Technology |
|-------|------------|
| Framework | React 18 + TypeScript |
| Build | Vite |
| Styling | Tailwind CSS |
| Charts | Recharts |
| State | Zustand |
| Testing | Vitest + Testing Library |
| Mock | MSW + Faker.js |

## Required Output Files

**CRITICAL**: Every dashboard generation MUST include these files:

```
📁 project-output/
├── src/
│   ├── App.tsx              # ⚠️ REQUIRED - Main entry component
│   ├── main.tsx             # Entry point
│   ├── index.css            # Tailwind imports
│   ├── types/
│   │   └── index.ts         # TypeScript interfaces
│   ├── data/
│   │   └── mockData.ts      # Mock data for charts
│   └── components/
│       ├── index.ts         # Component exports
│       ├── KPICard.tsx      # KPI cards (if metrics need it)
│       └── [ChartType].tsx  # Required charts based on use case
├── package.json
├── vite.config.ts
├── tsconfig.json
└── tailwind.config.js
```

**Chart Component Selection** (generate ALL that apply):
- **Trend analysis** → LineChart.tsx + AreaChart.tsx
- **Comparison** → BarChart.tsx
- **Composition/Part-to-whole** → PieChart.tsx
- **Conversion/Funnel** → FunnelChart.tsx
- **Correlation** → ScatterChart.tsx
- **KPI summary** → KPICard.tsx

## Quality Standards

- Test coverage > 90% (core components 100%)
- All tests pass, 0 failures
- Code passes ESLint + Prettier + tsc
- Components match design specifications
- Mock data workflow complete
- **App.tsx MUST exist and render the dashboard**

## Important Principles

1. **User Confirmation at Each Step**: Never skip user validation
2. **Checklist Mode**: Multi-item confirmation, not one-click
3. **TDD First**: Write tests before code
4. **Template Priority**: Reuse built-in templates when possible
5. **Context Isolation**: Each step only carries necessary context
6. **Checkpoint Rollback**: Support recovery from any step
