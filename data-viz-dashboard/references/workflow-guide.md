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

Generate to local file `design-docs/page-*.md`:

```markdown
# Design Document: [Dashboard Name]

## 1. Data Story Overview
## 2. Metrics Specification
## 3. Visualization Components
## 4. Page Layout
## 5. Interaction Logic
## 6. Data Model
## 7. External Integration
## 8. Edge Cases
```

### 2F: Document Review

Quick review with limited edits:
- ✅ Adjust wording
- ✅ Add clarifications
- ❌ Change layout (requires unlock)

---

## Step 3: Execution Plan Generation

### Objective
Create atomic, testable code generation steps.

### Process

#### 3.1 Parse Design Document

Extract file list from each section:
- Types from Data Model
- Components from Visualization
- Hooks from Interaction Logic
- Pages from Page Layout

#### 3.2 Dependency Analysis

Build dependency graph:
```
types/sales.ts
    ↓
mock/sales.mock.ts
    ↓
components/BarChart.tsx ←──┐
components/LineChart.tsx   │
    ↓                      │
hooks/useChartData.ts ─────┘
    ↓
pages/Dashboard.tsx
```

#### 3.3 Step Decomposition

Each file = one step:

```typescript
interface ExecutionStep {
  order: number
  description: string
  goal: string
  input: {
    designDocSections: string[]
    dependencyOutputs: number[]
    templateRef?: string
  }
  output: {
    files: GeneratedFile[]
    verificationCriteria: string[]
  }
  testSpec: TestSpec
  componentSource: 'template' | 'new'
  tokenBudget: TokenBudget
}
```

#### 3.4 Test Spec Generation

Generate quantified assertions:

```typescript
interface TestSpec {
  assertions: TestAssertion[]
  mockData: MockDataConfig
}

interface TestAssertion {
  description: string
  code: string                  // Executable test code
  expected: string              // Hard-coded expected value
}
```

Example:
```typescript
{
  description: "Bar chart renders 5 bars for 5 regions",
  code: "expect(container.querySelectorAll('.bar')).toHaveLength(5)",
  expected: "5"
}
```

### Output

```typescript
interface ExecutionPlan {
  id: string
  summary: string
  designDocRef: string
  steps: ExecutionStep[]
  totalEstimatedTokens: number
  warnings: string[]
}
```

---

## Step 4: TDD Code Generation

### Objective
Generate tested, production-ready code automatically.

### TDD Cycle

```
[READ] → [RED] → [GREEN] → [REFACTOR] → [VERIFY] → [CHECKPOINT]
```

### Template Path (Matched Components)

```
1. Read template source
2. Adapt types (replace generics)
3. Inject theme colors
4. Write files
5. Run tests
6. If fail → fix adaptation (max 2 rounds)
```

### New Generation Path

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
7. [CHECKPOINT] Save snapshot
```

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
