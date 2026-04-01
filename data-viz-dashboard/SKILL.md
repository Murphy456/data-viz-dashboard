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
| Distribution analysis | `HistogramChart.tsx` | Age distribution, price ranges |
| Statistical summary | `BoxPlotChart.tsx` | Salary ranges, performance quartiles |
| Combined trend+comparison | `BarLineChart.tsx` | Sales volume + growth rate |

### Extended Chart Types

| Chart Type | Component | Best For | Data Requirements |
|------------|-----------|----------|-------------------|
| **BarLineChart** | `BarLineChart.tsx` | Compare volume + trend simultaneously | 1 categorical + 2 numerical (different scales) |
| **ScatterPlot** | `ScatterChart.tsx` | Correlation between 2 variables | 2 numerical variables |
| **BubbleChart** | `ScatterChart.tsx` | Correlation with size dimension | 3 numerical variables |
| **Histogram** | `HistogramChart.tsx` | Frequency distribution | 1 numerical variable |
| **BoxPlot** | `BoxPlotChart.tsx` | Statistical distribution (quartiles, outliers) | 1 categorical + 1 numerical |
| **Heatmap** | `HeatmapChart.tsx` | 2D density, correlation matrix | 2 categorical + 1 numerical |
| **RadarChart** | `RadarChart.tsx` | Multi-dimensional comparison | 1 categorical + 3+ numerical |
| **Treemap** | `TreemapChart.tsx` | Hierarchical part-to-whole | Hierarchical categories + 1 numerical |

## Business Metrics Library

The skill includes a comprehensive metrics library in `references/domain-knowledge.md` covering:

### Supported Industries

| Industry | Core Metrics | Typical Use Cases |
|----------|--------------|-------------------|
| Marketing | ROI, CVR, CAC, LTV, ROAS | Campaign performance, channel attribution |
| Product | DAU/MAU, Retention, NPS | User engagement, feature adoption |
| Finance | Revenue, Margin, Cash Flow | Financial health, budget tracking |
| Operations | Throughput, SLA, Defect Rate | Process efficiency, quality control |
| E-commerce | GMV, AOV, Cart Abandonment | Sales funnel, conversion optimization |
| SaaS | MRR, ARR, Churn, NRR | Subscription growth, revenue retention |
| Education | Completion, Engagement, Scores | Learning outcomes, course effectiveness |
| Healthcare | Wait Time, Readmission, Satisfaction | Patient care, operational efficiency |

### Using the Metrics Library

1. **Domain Detection**: Automatically identify the business domain from user input
2. **Metric Selection**: Look up relevant metrics with formulas and typical ranges
3. **Benchmark Reference**: Compare against industry benchmarks for realistic mock data
4. **Relationship Mapping**: Understand metric dependencies (e.g., CAC → LTV relationship)

### Metric Relationships

The library includes metric relationship diagrams:
- Marketing Funnel: Impressions → Clicks → Visits → Leads → Customers
- Product Journey: Acquisition → Activation → Retention → Referral → Revenue
- SaaS Revenue: New MRR + Expansion - Churn = Net New MRR

## Core Workflow: 6-Step Guided Process

### ⚠️ CRITICAL: Sequential Execution Required

**ALL steps MUST be executed in order. Never skip any step.**

```
Step 0 → Step 1 → Step 2 → Step 3 → Step 4 → Step 5
```

**Enforcement Rules**:
1. Each step MUST complete and receive user confirmation before proceeding
2. If user requests changes in any step, complete that step first, then proceed to next
3. NEVER jump from Step 0/1 directly to Step 3/4/5
4. Step 2 (Design + Wireframe) is MANDATORY - it cannot be skipped even if metrics are clear
5. Track progress: Before starting any step, verify all previous steps are completed

**Step Completion Checklist** (must be verified before proceeding):
- [ ] Step 0: UserIntent captured and confirmed
- [ ] Step 1: MetricSystem defined and confirmed
- [ ] Step 2: DesignDoc created and approved
- [ ] Step 3: DevPlan generated and approved
- [ ] Step 4: Code generated with tests passing
- [ ] Step 5: Deliverables packaged

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

**Display Format Options**:

| Format | Description | Best For |
|--------|-------------|----------|
| Single-page | One screen, all info visible | Executive summary, team dashboards |
| Multi-page | Tab navigation, multiple views | Detailed analytics, drill-down |
| Big-screen | Large display, dark theme | NOC, operations center, presentations |

**Big-Screen Layout Frameworks** (when user selects big-screen format):

```
┌─────────────────────────────────────────────────────────────┐
│ Layout A: Left 1 + Center Map + Right 1                     │
├──────────┬─────────────────────────────┬──────────┤
│          │                             │          │
│  KPIs    │       MAP / CENTER          │  KPIs    │
│  Charts  │       VISUALIZATION         │  Charts  │
│          │                             │          │
│  (1 col) │         (3 cols)            │  (1 col) │
└──────────┴─────────────────────────────┴──────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ Layout B: Left 2 + Center Map + Right 2                     │
├────────────────┬─────────────────────┬────────────────┤
│                │                     │                │
│  KPIs          │    MAP / CENTER     │  KPIs          │
│  Charts (1)    │    VISUALIZATION    │  Charts (1)    │
│  Charts (2)    │      (2 cols)       │  Charts (2)    │
│                │                     │                │
│  (2 cols)      │                     │  (2 cols)      │
└────────────────┴─────────────────────┴────────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ Layout C: Left 1 + Center 2 + Right 1                       │
├──────────┬───────────────────────────┬──────────┤
│          │                           │          │
│  KPIs    │   MAIN CHARTS             │  KPIs    │
│  Charts  │   (Multiple charts)       │  Charts  │
│          │                           │          │
│  (1 col) │        (2 cols)           │  (1 col) │
└──────────┴───────────────────────────┴──────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ Layout D: Left-Center-Right Equal (1-1-1)                   │
├──────────────┬──────────────┬──────────────┤
│              │              │              │
│  Charts      │   Charts     │   Charts     │
│  Group A     │   Group B    │   Group C    │
│              │              │              │
│  (1 col)     │   (1 col)    │   (1 col)    │
└──────────────┴──────────────┴──────────────┘
```

```
┌─────────────────────────────────────────────────────────────┐
│ Layout E: Top Banner + Left-Right Split                     │
├─────────────────────────────────────────────────────────────┤
│                    TOP BANNER / TITLE                       │
├─────────────────────────────┬───────────────────────────────┤
│                             │                               │
│    LEFT CHARTS              │    RIGHT CHARTS               │
│    (2 cols)                 │    (2 cols)                   │
│                             │                               │
└─────────────────────────────┴───────────────────────────────┘
```

**Output**: Structured `UserIntent` summary

**⚠️ After Step 0**: MUST proceed to Step 1. Do not skip to Step 2 or later.

### Step 1: Story + Metrics Definition

**Goal**: Convert intent into quantifiable metrics with mock data specifications.

**Process**:
1. Generate story narrative from dialogue history
2. Define core metrics (1-3 KPIs) with formulas
3. Define support metrics with mock specifications
4. Map data dimensions and granularity
5. Generate data source schema
6. **Output metrics checklist and PRD document for user confirmation**

**Output Artifacts**:

1. **Metrics Checklist** (`metrics-checklist.md`):
```markdown
# Metrics Checklist: [Dashboard Name]

## Core Metrics (KPIs)
| Metric | Definition | Formula | Unit | Data Source |
|--------|------------|---------|------|-------------|
| [Metric 1] | [Definition] | [Formula] | [Unit] | [Source] |
| [Metric 2] | [Definition] | [Formula] | [Unit] | [Source] |
| [Metric 3] | [Definition] | [Formula] | [Unit] | [Source] |

## Support Metrics
| Metric | Definition | Unit | Purpose |
|--------|------------|------|---------|
| [Metric 4] | [Definition] | [Unit] | [Context purpose] |

## Dimensions
| Dimension | Type | Values | Hierarchy |
|-----------|------|--------|-----------|
| [Dim 1] | categorical/temporal/geographic | [values] | [if applicable] |

## Mock Data Specifications
| Metric | Range | Distribution | Typical Value |
|--------|-------|--------------|---------------|
| [Metric 1] | [min, max] | normal/beta/uniform | [value] |

---
✅ Please confirm the metrics above are correct before proceeding.
```

2. **PRD Document** (`prd-[dashboard-name].md`):
```markdown
# Product Requirements Document: [Dashboard Name]

## 1. Overview
- **Product Name**: [Name]
- **Target Users**: [From Step 0]
- **Business Domain**: [Domain]
- **Primary Goal**: [What decisions this supports]

## 2. Business Context
- **Problem Statement**: [What problem does this solve]
- **Success Criteria**: [How to measure success]
- **Stakeholders**: [Who will use this]

## 3. Metrics Specification
### Core KPIs
1. **[KPI 1]**: [Definition and why it matters]
2. **[KPI 2]**: [Definition and why it matters]
3. **[KPI 3]**: [Definition and why it matters]

### Support Metrics
- [List with purposes]

## 4. Data Requirements
- **Data Sources**: [Where data comes from]
- **Update Frequency**: [Real-time/Daily/Weekly]
- **Data Granularity**: [Hourly/Daily/Weekly/Monthly]
- **Historical Range**: [How far back]

## 5. Layout Preference
- **Display Format**: [Single-page/Multi-page/Big-screen]
- **Layout Framework**: [If big-screen, which layout]
- **Resolution**: [Target resolution]

## 6. Functional Requirements
- [ ] Display [KPI 1] with trend indicator
- [ ] Compare [dimension] across [metrics]
- [ ] Filter by [dimensions]
- [ ] [Other requirements from dialogue]

## 7. Non-Functional Requirements
- **Performance**: Page load < 3s
- **Accessibility**: WCAG 2.1 AA
- **Browser Support**: Chrome, Firefox, Safari, Edge

## 8. Acceptance Criteria
- [ ] All core metrics displayed correctly
- [ ] Charts render with mock data
- [ ] Filters work as expected
- [ ] Responsive on target resolution

---
**Status**: Draft - Awaiting User Confirmation
**Created**: [Date]
```

**User Confirmation Required**:
- Present metrics checklist and PRD document
- User must approve both before proceeding to Step 2
- Allow revisions: user can add/remove/modify metrics

**Mock Spec Structure**:
```typescript
interface MockDataSpec {
  range: [number, number]      // Value range
  distribution: 'normal' | 'beta' | 'uniform'
  typicalValue: number         // Typical value for realistic data
  outliers?: { probability: number; range: [number, number] }
}
```

**⚠️ After Step 1**: MUST proceed to Step 2 (Design + Wireframe).
- Even if metrics and layout preferences are discussed in Step 1, Step 2 is still REQUIRED
- Step 2 creates the formal design document with wireframe and component mapping
- User modifications in Step 1 do NOT satisfy Step 2 requirements
- NEVER skip Step 2 regardless of how detailed Step 1 discussions were

### Step 2: Design + Wireframe

**Goal**: Create visual layout specification with user confirmation.

**⚠️ MANDATORY STEP - This step CANNOT be skipped.**

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

**Design Document Generation**:
After wireframe confirmation, generate a comprehensive design document using `assets/templates/design-doc-template.md`:
- Save to `design-docs/[dashboard-name].md`
- Include all 12 sections: Executive Summary, Business Context, Metrics, Components, Layout, Interactions, Data Model, Theme, Technical Specs, Edge Cases, Acceptance Criteria, Approval
- User must approve before proceeding to development

**Output**: `DesignDoc` (locked) stored as `design-docs/[dashboard-name].md`

**⚠️ After Step 2**: MUST proceed to Step 3 (Development Plan).
- Design document approval is required before any code generation
- Do not proceed to Step 4 without completing Step 3

### Step 3: Development Plan Generation

**Goal**: Create detailed development plan from design document.

**Process**:
1. Parse design doc → extract all required files and components
2. Analyze dependencies → build dependency graph
3. Break into phases → Foundation, Components, Assembly, QA
4. Create task breakdown with:
   - Priority (P0/P1/P2)
   - Time estimates
   - Dependencies
   - Acceptance criteria
5. Generate timeline with milestones
6. Define quality gates and rollback points

**Development Plan Structure** (from `assets/templates/dev-plan-template.md`):
- Project Overview
- Task Breakdown (by phase)
- Dependency Graph
- Timeline (Gantt chart)
- Resource Allocation
- Risk Assessment
- Quality Gates
- Rollback Plan

**Output**: `dev-plan.md` with ordered, testable tasks

### Step 4: TDD Code Generation

**Goal**: Generate tested, production-ready code following the development plan.

**TDD Cycle per Task**:
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

**Checkpoint Strategy**:
- Create checkpoint after each phase
- Support rollback to any checkpoint
- Track test results at each checkpoint

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

- `references/domain-knowledge.md` - **Business Metrics Library** with 8 industries (Marketing, Product, Finance, Operations, E-commerce, SaaS, Education, Healthcare), metric relationships, and industry benchmarks
- `references/chart-mapping.md` - Rules for mapping metrics to chart types
- `references/workflow-guide.md` - Detailed workflow instructions

### Templates

Use templates for document generation:

- `assets/templates/design-doc-template.md` - Comprehensive design document template with approval workflow
- `assets/templates/dev-plan-template.md` - Development plan with task breakdown, timeline, and dependencies

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
  - `BarLineChart.tsx` - Combined bar + line (dual axis)
  - `HistogramChart.tsx` - Frequency distribution
  - `BoxPlotChart.tsx` - Box and whisker plot
  - `HeatmapChart.tsx` - 2D density visualization
  - `RadarChart.tsx` - Multi-dimensional comparison
  - `TreemapChart.tsx` - Hierarchical part-to-whole
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
- **Composition/Part-to-whole** → PieChart.tsx, Treemap.tsx
- **Conversion/Funnel** → FunnelChart.tsx
- **Correlation** → ScatterChart.tsx
- **KPI summary** → KPICard.tsx
- **Distribution** → HistogramChart.tsx, BoxPlotChart.tsx
- **Combined metrics** → BarLineChart.tsx (e.g., sales volume + growth rate)
- **Multi-dimensional** → RadarChart.tsx, HeatmapChart.tsx

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
7. **Sequential Execution**: ALL steps must be executed in order - NO SKIPPING

## Workflow State Tracking

At the start of each response, display current progress:

```
📊 Dashboard Generation Progress
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ Step 0: Socratic Dialogue (completed)
✅ Step 1: Story + Metrics (completed)
🔄 Step 2: Design + Wireframe (in progress)
⬜ Step 3: Development Plan
⬜ Step 4: TDD Code Generation
⬜ Step 5: Delivery
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**State Tracking Rules**:
- Always show progress indicator at start of response
- Mark current step as 🔄 (in progress)
- Mark completed steps as ✅
- Mark pending steps as ⬜
- Never mark a step complete until user confirms
- If user requests to go back, update state accordingly
