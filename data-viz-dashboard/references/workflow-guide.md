# Workflow Guide

Detailed instructions for executing the 6-step data visualization dashboard generation workflow.

## Step 0: Socratic Dialogue

### Objective
Transform user's vague idea into structured, actionable requirements through guided questioning.

### Process

#### Phase 1: Intent Recognition + Domain Detection

1. Parse user input for keywords
2. Detect business domain:
   - Marketing: campaign, ROI, conversion, channel, funnel
   - Product: users, retention, feature, engagement, DAU/MAU
   - Finance: revenue, margin, cost, budget, cash flow
   - Operations: throughput, efficiency, SLA, process

3. Load corresponding domain knowledge from `references/domain-knowledge.md`

#### Phase 2: Guided Questioning (6-8 Questions)

**Question Template Structure**:
```
Question N: [Question text]
Options:
○ Option A (Recommended for [context])
○ Option B
○ Option C
○ Custom input
```

**Question Priority Order**:
1. **Business Object** - What are you analyzing?
2. **Analysis Action** - Compare? Trend? Find anomalies?
3. **Target Audience** - Who will view this?
4. **Comparison Dimensions** - Region? Channel? Time?
5. **Core Metrics** - What matters most? (max 3)
6. **Time Range** - How far back?
7. **Decision Intent** - What will you do with insights?
8. **Display Format** - Single page? Multi-page? Big screen?

#### Phase 3: Information Convergence

**Convergence Criteria**:
- At least 3 dimensions captured
- Core metrics defined (1-3)
- Time range specified
- Clarity score > 0.7

**Clarity Score Calculation**:
```typescript
function calculateClarity(info: ExtractedInfo): number {
  const weights = {
    object: 0.2,
    action: 0.15,
    audience: 0.1,
    dimensions: 0.2,
    metrics: 0.2,
    timeRange: 0.1,
    decision: 0.05
  }

  let score = 0
  for (const [key, weight] of Object.entries(weights)) {
    if (info[key] !== null && info[key] !== undefined) {
      score += weight
    }
  }
  return score
}
```

### Output

```typescript
interface UserIntent {
  domain: string                    // Detected domain
  object: string                    // Analysis object
  action: 'compare' | 'trend' | 'analyze' | 'monitor'
  audience: string                  // Target viewers
  dimensions: string[]              // Comparison dimensions
  coreMetrics: string[]             // Key metrics (1-3)
  supportMetrics: string[]          // Additional metrics
  timeRange: TimeRange              // Data period
  decisionIntent: string            // What decisions will be made
  displayFormat: DisplayFormat      // UI preference
  dialogueHistory: DialogueMessage[] // Full conversation
}
```

---

## Step 1: Story + Metrics Definition

### Objective
Convert structured intent into quantifiable metrics with mock data specifications.

### Process

#### 1.1 Story Narrative Generation

Generate a data story from the dialogue:

```markdown
## Data Story: [Title]

**Core Narrative**: [One-sentence story arc]

**Target Audience**: [Who will view this]

**Key Question**: [What question does this answer]

**Expected Insight**: [What the viewer should learn]

**Business Context**: [Why this matters]
```

#### 1.2 Core Metrics Definition

For each core metric (1-3):

```typescript
interface CoreMetric {
  name: string
  definition: string              // Clear definition
  formula: string                 // Calculation formula
  unit: string                    // Unit of measure
  priority: 'primary' | 'secondary'
  mockSpec: MockDataSpec          // Mock data constraints
}
```

**Mock Spec Generation**:
1. Look up typical range in domain knowledge
2. Adjust based on user context
3. Define distribution type
4. Set typical value

#### 1.3 Support Metrics

Additional metrics that provide context:

```typescript
interface SupportMetric {
  name: string
  definition: string
  unit: string
  formula?: string
  mockSpec: MockDataSpec
}
```

#### 1.4 Dimensions Definition

```typescript
interface Dimension {
  name: string
  type: 'categorical' | 'temporal' | 'geographic'
  values: string[]                // Possible values
  hierarchy?: string[]            // If hierarchical
}
```

#### 1.5 Data Granularity

Determine based on time range:
- < 7 days → Hourly
- 7-90 days → Daily
- 90 days - 2 years → Weekly
- > 2 years → Monthly

### User Confirmation

Present metrics in checklist format:

```
📋 Metrics Confirmation

Core Metrics:
□ [Metric 1] - [Definition] ✅
□ [Metric 2] - [Definition] ✅
□ [Metric 3] - [Definition] ✅

Support Metrics:
□ [Metric 4] - [Definition] ✅
□ [Metric 5] - [Definition] ✅

Dimensions:
□ [Dimension 1]: [values] ✅
□ [Dimension 2]: [values] ✅

Mock Data Preview:
[Show 5 sample rows]

[Confirm] [Adjust] [Add More]
```

### Output

```typescript
interface MetricSystem {
  storyId: string
  coreMetrics: CoreMetric[]
  supportMetrics: SupportMetric[]
  dimensions: Dimension[]
  granularity: 'hourly' | 'daily' | 'weekly' | 'monthly'
  mockConfig: MockConfig
}
```

---

## Step 2: Design + Wireframe

### Objective
Create visual layout specification with user confirmation.

### 2A: Layout Preferences

Collect before generating wireframe:

| Preference | Options |
|------------|---------|
| Resolution | 1920x1080, 1440x900, 1024x768, Custom |
| Framework | Dashboard (grid), Report (flow), Big-screen (dark) |
| Navigation | Single-page, Multi-page, Tab-switch |
| Hierarchy | KPI-top, Sidebar-left, Full-width |
| Theme | Business-blue, Vibrant-orange, Fresh-green, Dark |
| Integration | None, iframe, API, Export PDF/PPT |

### 2B: Component Mapping

For each metric, determine chart type:

1. Classify metric (trend/comparison/composition/kpi)
2. Check dimension types
3. Match against chart templates
4. If no match → mark for AI generation

### 2C: Wireframe Generation

Generate layout structure:

```typescript
interface WireframeLayout {
  grid: {
    columns: number              // Usually 12
    rows: number
    gap: number
  }
  components: WireframeComponent[]
  theme: ThemeConfig
}

interface WireframeComponent {
  id: string
  type: ChartType
  title: string
  position: { col: number, row: number }
  size: { width: number, height: number }
  boundMetrics: string[]
  interactions: Interaction[]
  source: 'template' | 'ai-generated'
}
```

### 2D: Wireframe Confirmation

**Checklist Mode** (not one-click):

```
📋 Wireframe Confirmation

Page 1: [Page Name]
□ Layout structure ✅
□ Component selection ✅
□ Filter configuration [Edit]
□ Interaction logic ✅
□ Animation settings ✅

Page 2: [Page Name]
□ Layout structure [Pending]
...

⚠️ 2 pages not confirmed. Cannot proceed.

[Confirm All] [Back to Edit]
```

### 2E: Design Document Generation

Generate comprehensive design document using the template:

**Template Location**: `assets/templates/design-doc-template.md`

**Document Structure** (12 sections):
1. Executive Summary - Purpose, audience, key questions
2. Business Context - Domain, objectives, decision support
3. Metrics Specification - Core metrics, support metrics, dimensions
4. Visualization Components - Component map and details
5. Page Layout - Grid structure, layout diagram, responsive behavior
6. Interaction Logic - Filters, cross-filtering, drill-down, tooltips
7. Data Model - Sources, schema, mock data spec
8. Theme & Styling - Colors, typography, component styling
9. Technical Specifications - Tech stack, file structure, performance
10. Edge Cases & Error Handling - Data scenarios, error states
11. Acceptance Criteria - Functional and non-functional requirements
12. Approval - Review checklist, sign-off

**Output Location**: `design-docs/[dashboard-name].md`

**Approval Workflow**:
```
Draft → Review (checklist) → Revision (if needed) → Approved → Locked
```

### 2F: Document Review

Quick review with limited edits:
- ✅ Adjust wording
- ✅ Add clarifications
- ❌ Change layout (requires unlock)

**User Confirmation Required**: Design document must be approved before proceeding to Step 3.

---

## Step 3: Development Plan Generation

### Objective
Create detailed development plan from the approved design document.

### Process

#### 3.1 Parse Design Document

Extract all required artifacts:
- Types from Data Model section
- Components from Visualization Components section
- Hooks from Interaction Logic section
- Pages from Page Layout section
- Mock data specifications from Data Model section

#### 3.2 Dependency Analysis

Build dependency graph for all files:

```
types/index.ts
    ↓
data/mockData.ts
    ↓
components/KPICard.tsx ←──┐
components/BarChart.tsx   │
components/LineChart.tsx  │
    ↓                     │
hooks/useChartData.ts ────┘
    ↓
App.tsx
```

#### 3.3 Phase Breakdown

Organize tasks into 4 phases:

| Phase | Tasks | Est. Time |
|-------|-------|-----------|
| Foundation | Project setup, types, mock data | 2-3 hours |
| Components | All chart and UI components | 4-6 hours |
| Assembly | App.tsx, filters, state | 2-3 hours |
| QA | Testing, optimization, docs | 2-3 hours |

#### 3.4 Task Decomposition

For each task, define:

```typescript
interface DevelopmentTask {
  id: string                    // e.g., "2.1"
  name: string                  // e.g., "KPI Card Component"
  priority: 'P0' | 'P1' | 'P2'  // P0 = critical path
  estimatedTime: string         // e.g., "1 hour"
  dependencies: string[]        // Task IDs this depends on
  subtasks: Subtask[]
  acceptanceCriteria: string[]
  output: string[]              // Files produced
}
```

#### 3.5 Timeline Generation

Create timeline with milestones:

```
Day 1: Foundation Complete (M1)
Day 3: Components Ready (M2)
Day 4: Dashboard Assembled (M3)
Day 5: QA Passed (M4)
Day 5: Delivery (M5)
```

#### 3.6 Quality Gates Definition

Define quality gates for each phase:

| Gate | Criteria |
|------|----------|
| Foundation | Types compile, mock data generates |
| Components | All tests pass, coverage > 90% |
| Assembly | Integration tests pass, responsive |
| QA | Performance targets met, docs complete |

#### 3.7 Risk Assessment

Identify and document risks:

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Component complexity | Medium | High | Use templates |
| Performance issues | Low | High | Profile early |

### Output

Generate `dev-plan.md` using `assets/templates/dev-plan-template.md`:

```markdown
# Development Plan: [Dashboard Name]

## 1. Project Overview
## 2. Task Breakdown (by phase)
## 3. Dependency Graph
## 4. Timeline
## 5. Resource Allocation
## 6. Risk Assessment
## 7. Quality Gates
## 8. Rollback Plan
```

### User Confirmation

Present the development plan for review:
- [ ] Task breakdown looks complete
- [ ] Time estimates are reasonable
- [ ] Dependencies are correct
- [ ] Quality gates are appropriate

**Proceed to Step 4 only after plan approval.**

---

## Step 4: TDD Code Generation

### Objective
Generate tested, production-ready code following the development plan.

### TDD Cycle

```
[READ] → [RED] → [GREEN] → [REFACTOR] → [VERIFY] → [CHECKPOINT]
```

### Phase-by-Phase Execution

#### Phase 1: Foundation

Execute in order:
1. **Task 1.1**: Project Setup
   - Initialize Vite + React + TypeScript
   - Configure Tailwind CSS
   - Install dependencies
   - Create folder structure

2. **Task 1.2**: Type Definitions
   - Define data interfaces
   - Define component prop types
   - Define state interfaces

3. **Task 1.3**: Mock Data Generation
   - Create mock data generator
   - Generate realistic values per spec
   - Add data validation

**Checkpoint 1**: Foundation complete, types compile, mock data generates

#### Phase 2: Components

For each component task:

**Template Path** (matched components):
```
1. Read template source from assets/chart-components/
2. Adapt types (replace generics)
3. Inject theme colors
4. Write files
5. Run tests
6. If fail → fix adaptation (max 2 rounds)
```

**New Generation Path** (custom components):
```
1. Read specs + dependencies
2. [RED] Write tests first
   - Generate from TestSpec
   - Verify tests fail (no tautology)
3. [GREEN] Generate code
   - Use prompt with specs + tests
   - Run tests
4. [REPAIR] If fail
   - Analyze failure (test/type/mock/code)
   - Fix by priority
   - Max 3 rounds
5. [REFACTOR] Quality check
   - ESLint, Prettier, tsc
6. [VERIFY] Regression test
   - All previous tests still pass
```

**Checkpoint 2**: All components complete, tests pass, coverage > 90%

#### Phase 3: Assembly

1. **Task 3.1**: Main Dashboard Component
   - Create App.tsx layout
   - Integrate all components
   - Implement responsive grid

2. **Task 3.2**: Filters and Interactions
   - Implement filter controls
   - Add state management
   - Connect filters to charts

**Checkpoint 3**: Dashboard assembled, integration tests pass

#### Phase 4: QA

1. **Task 4.1**: Integration Testing
2. **Task 4.2**: Performance Optimization
3. **Task 4.3**: Documentation

**Checkpoint 4**: QA complete, ready for delivery

### Repair Priority

| Priority | Check | Reason |
|----------|-------|--------|
| 1 | Test correctness | Wrong test = wrong code |
| 2 | Type definitions | Common frontend issue |
| 3 | Mock data | Test data problems |
| 4 | Code logic | Implementation bugs |

### Quality Gates

- All unit tests pass
- Coverage > 90%
- ESLint: 0 errors
- TypeScript: 0 errors
- Design consistency check passed

---

## Step 5: Delivery

### Objective
Package and deliver final product.

### Deliverables

```
📁 project-name/
├── README.md
├── package.json
├── vite.config.ts
├── tsconfig.json
├── tailwind.config.js
├── design-spec.md
├── test-report.md
├── src/
│   ├── types/
│   │   └── index.ts
│   ├── data/
│   │   └── mockData.ts
│   ├── components/
│   │   ├── index.ts
│   │   ├── KPICard.tsx
│   │   └── [ChartType].tsx
│   ├── App.tsx              # ⚠️ REQUIRED - Main dashboard component
│   └── main.tsx
└── __tests__/
```

**⚠️ CRITICAL REQUIREMENTS**:
1. **App.tsx MUST be generated** - This is the main entry that assembles all components
2. **All chart components must be generated** based on metric type:
   - Trend metrics → LineChart.tsx
   - Comparison metrics → BarChart.tsx
   - Composition metrics → PieChart.tsx
3. **Mock data must be provided** in `src/data/mockData.ts`

### Test Report

```markdown
# Test Report

## Unit Tests
- Total: X
- Passed: X ✅
- Failed: 0
- Coverage: X%

## Integration Tests
- Total: X
- Passed: X ✅

## Code Quality
- ESLint: 0 errors ✅
- TypeScript: 0 errors ✅
```

### Preview

```bash
npm install
npm run dev
# Open http://localhost:5173
```

---

## Checkpoint & Recovery

### Checkpoint Creation

After each step completes:
```typescript
interface Checkpoint {
  id: string
  stepOrder: number
  timestamp: Date
  files: FileSnapshot[]
  testResults: TestResult[]
}
```

### Rollback

On failure, rollback to last checkpoint:
1. Restore file snapshots
2. Clear generated files after checkpoint
3. Resume from checkpoint step

---

## Context Management

### Token Budget Per Step

| Step Type | Input Budget | Output Budget |
|-----------|--------------|---------------|
| Types | 3K | 2K |
| Mock | 4K | 3K |
| Template Component | 2K | 2K |
| New Component | 5K | 4K |
| Hooks | 5K | 3K |
| Page Assembly | 8K | 6K |

### Context Strategy

- **Minimal**: Design doc sections + previous output summary
- **Summary**: Summary + key dependency files
- **Full**: Complete context (final assembly only)

---

## Error Handling

### LLM Output Instability
- Structured prompts with examples
- Retry with temperature adjustment
- Fallback to templates

### Context Overflow
- Compress with summarization
- Split into smaller steps
- Use checkpoint recovery

### Test Tautology
- Generate tests from specs, not code
- Use independent mock data
- Hard-code expected values from design doc

### User Confusion
- Provide examples at each step
- Show preview before confirmation
- Allow natural language adjustments
