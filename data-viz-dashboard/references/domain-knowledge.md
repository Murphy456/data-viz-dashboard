# Domain Knowledge Base

Industry-specific metrics, dimensions, and analysis scenarios for data visualization.

## Quick Navigation

| Industry | Core Focus | Key Metrics |
|----------|------------|-------------|
| [Marketing](#marketing-domain) | Campaign & Channel | ROI, CVR, CAC, LTV, ROAS |
| [Product](#product-domain) | User & Engagement | DAU/MAU, Retention, NPS |
| [Finance](#finance-domain) | Revenue & Profit | Revenue, Margin, Cash Flow |
| [Operations](#operations-domain) | Efficiency & Quality | Throughput, SLA, Defect Rate |
| [E-commerce](#e-commerce-domain) | Sales & Conversion | GMV, AOV, Cart Abandonment |
| [SaaS](#saas-domain) | Subscription & Growth | MRR, ARR, Churn, NRR |
| [Education](#education-domain) | Learning & Outcomes | Completion, Engagement, Score |
| [Healthcare](#healthcare-domain) | Patient & Quality | Wait Time, Readmission, Satisfaction |

---

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

## E-commerce Domain

### Core Metrics

| Metric | Definition | Formula | Unit | Typical Range |
|--------|------------|---------|------|---------------|
| GMV | Gross Merchandise Value | Sum of all transactions | Currency | Varies |
| AOV | Average Order Value | Total Revenue / Orders | Currency | $50 - $300 |
| Cart Abandonment Rate | Abandoned carts / Total carts | (Carts - Checkouts) / Carts x 100% | % | 60% - 80% |
| Conversion Rate | Visitors who purchase | Purchases / Visitors x 100% | % | 1% - 5% |
| Repeat Purchase Rate | Returning customers | Repeat Customers / Total Customers x 100% | % | 20% - 50% |
| Product Return Rate | Returned items / Sold items | Returns / Sales x 100% | % | 5% - 30% |

### Support Metrics

| Metric | Definition | Unit |
|--------|------------|------|
| Add-to-Cart Rate | Add to cart / Product views | % |
| Checkout Rate | Checkouts / Carts | % |
| Time to Purchase | Avg time from visit to purchase | Minutes |
| Items per Order | Total items / Orders | Count |

### Typical Dimensions

- **Category**: Product categories (Electronics, Fashion, Home)
- **Channel**: Website, App, Marketplace
- **Customer Segment**: New, Returning, VIP
- **Region**: Geographic areas
- **Promotion**: Discount campaigns, coupons

### Common Analysis Scenarios

1. **Sales Performance**: GMV trend by category/channel
2. **Funnel Analysis**: Browse → Cart → Checkout → Purchase
3. **Customer LTV**: Revenue per customer over time
4. **Inventory Analysis**: Stock levels, sell-through rate

---

## SaaS Domain

### Core Metrics

| Metric | Definition | Formula | Unit | Typical Range |
|--------|------------|---------|------|---------------|
| MRR | Monthly Recurring Revenue | Sum of monthly subscriptions | Currency | Varies |
| ARR | Annual Recurring Revenue | MRR x 12 | Currency | Varies |
| ARR Growth Rate | Year-over-year ARR growth | (Current ARR - Prior ARR) / Prior ARR x 100% | % | 20% - 100%+ |
| Churn Rate | Customer attrition | Churned Customers / Total Customers x 100% | % | 2% - 10%/mo |
| NRR | Net Revenue Retention | (Start MRR + Expansion - Churn) / Start MRR x 100% | % | 90% - 130% |
| ARPU | Average Revenue Per User | MRR / Active Users | Currency | $10 - $500 |

### Support Metrics

| Metric | Definition | Unit |
|--------|------------|------|
| CAC Payback | Time to recover CAC | Months |
| LTV/CAC Ratio | Customer value vs acquisition cost | Ratio |
| Expansion Revenue | Upsell/cross-sell revenue | Currency |
| Logo Churn | Customer count churn | % |

### Typical Dimensions

- **Plan Tier**: Free, Starter, Pro, Enterprise
- **Customer Size**: SMB, Mid-market, Enterprise
- **Industry**: Vertical segments
- **Region**: Geographic distribution
- **Cohort**: Sign-up month/quarter

### Common Analysis Scenarios

1. **Revenue Growth**: MRR/ARR trend with breakdown
2. **Churn Analysis**: Why customers leave
3. **Expansion Opportunity**: Upsell potential
4. **Unit Economics**: LTV, CAC, Payback

---

## Education Domain

### Core Metrics

| Metric | Definition | Formula | Unit | Typical Range |
|--------|------------|---------|------|---------------|
| Completion Rate | Course completion | Completed / Enrolled x 100% | % | 10% - 60% |
| Engagement Score | Learning activity index | Weighted sum of activities | Score | 0 - 100 |
| Assessment Score | Test/quiz performance | Correct / Total x 100% | % | 60% - 90% |
| Time to Completion | Days to finish course | End date - Start date | Days | Varies |
| Active Learners | Users with recent activity | Unique active users | Count | Varies |
| Knowledge Retention | Post-course assessment | Follow-up score / Initial score x 100% | % | 70% - 90% |

### Support Metrics

| Metric | Definition | Unit |
|--------|------------|------|
| Video Watch Time | Total video viewing time | Hours |
| Assignment Submission Rate | Submitted / Assigned | % |
| Discussion Participation | Posts / Comments | Count |
| Help Requests | Support ticket count | Count |

### Typical Dimensions

- **Course**: Individual courses
- **Module**: Course sections
- **Learner Type**: Student, Professional, Corporate
- **Difficulty Level**: Beginner, Intermediate, Advanced
- **Learning Path**: Curriculum tracks

### Common Analysis Scenarios

1. **Learning Progress**: Enrollment → Completion funnel
2. **Content Effectiveness**: Which modules work best
3. **Learner Engagement**: Activity patterns over time
4. **Outcome Analysis**: Score distribution by cohort

---

## Healthcare Domain

### Core Metrics

| Metric | Definition | Formula | Unit | Typical Range |
|--------|------------|---------|------|---------------|
| Wait Time | Time to receive care | Treatment time - Arrival time | Minutes | 15 - 120 min |
| Readmission Rate | Return within 30 days | Readmissions / Discharges x 100% | % | 5% - 20% |
| Patient Satisfaction | Survey score | Average rating | Score | 3.0 - 5.0 |
| Bed Occupancy | Hospital capacity usage | Occupied beds / Total beds x 100% | % | 60% - 95% |
| Length of Stay | Hospital stay duration | Discharge date - Admission date | Days | 2 - 10 days |
| Treatment Success | Positive outcomes | Successful treatments / Total x 100% | % | 80% - 98% |

### Support Metrics

| Metric | Definition | Unit |
|--------|------------|------|
| Appointment No-Show | Missed appointments | % |
| Staff-to-Patient Ratio | Staff per patient | Ratio |
| Medication Adherence | Prescriptions filled | % |
| Cost per Patient | Average treatment cost | Currency |

### Typical Dimensions

- **Department**: ER, ICU, Surgery, Outpatient
- **Condition**: Diagnosis categories
- **Patient Age Group**: Age brackets
- **Insurance Type**: Medicare, Private, Self-pay
- **Facility**: Hospital/clinic locations

### Common Analysis Scenarios

1. **Patient Flow**: Arrival → Triage → Treatment → Discharge
2. **Quality Metrics**: Outcomes by department/condition
3. **Resource Utilization**: Staff, beds, equipment
4. **Cost Analysis**: Treatment costs by condition

---

## Metric Relationships & Dependencies

### Marketing → Sales Funnel

```
Impressions → Clicks → Visits → Leads → Opportunities → Customers
     ↓           ↓        ↓        ↓          ↓           ↓
   CTR        CPC      Bounce   CVR       Win Rate     CAC
```

### Product → User Journey

```
Acquisition → Activation → Retention → Referral → Revenue
      ↓            ↓           ↓           ↓          ↓
   CAC         Activation%   Retention%   Viral     ARPU
```

### SaaS → Revenue Engine

```
New MRR + Expansion MRR - Churn MRR = Net New MRR
                    ↓
               MRR Growth Rate
                    ↓
              ARR = MRR × 12
```

---

## Industry Benchmarks Reference

### E-commerce Benchmarks (2024)

| Metric | Low | Average | High | Top 10% |
|--------|-----|---------|------|---------|
| Conversion Rate | 1% | 2.5% | 4% | 6%+ |
| AOV | $50 | $120 | $200 | $300+ |
| Cart Abandonment | 80% | 70% | 60% | 50% |
| Repeat Purchase | 20% | 35% | 50% | 65%+ |

### SaaS Benchmarks (2024)

| Metric | Seed | Series A | Series B+ | Public |
|--------|------|----------|-----------|--------|
| ARR Growth | 100%+ | 80% | 50% | 20-30% |
| Net Retention | 90% | 100% | 110% | 120%+ |
| Gross Margin | 60% | 70% | 75% | 80%+ |
| CAC Payback | 24mo | 18mo | 12mo | <12mo |

### Education Benchmarks (2024)

| Metric | MOOC | Corporate | K-12 | Higher Ed |
|--------|------|-----------|------|-----------|
| Completion Rate | 10% | 40% | 60% | 30% |
| Engagement Score | 30 | 60 | 70 | 50 |
| Assessment Score | 65% | 80% | 75% | 70% |

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
