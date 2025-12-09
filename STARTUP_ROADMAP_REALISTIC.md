# 🚀 IA PME: Roadmap Startup Réaliste (Budget €0 → €200+)

**Créateur**: Rudy Willoquet  
**Status**: Draft - À affiner avec tes retours  
**Horizon**: 6-12 mois jusqu'à première levée fonds  

---

## 📊 STRATÉGIE PRICING (nouveau market + budget limité)

### Ton avantage compétitif: **Efficace + Pas cher + Support français**

```
Marché actuel (France, outils IA):
├─ ChatGPT: €20/mois (généraliste, pas dédié)
├─ Make.com: €10-30/mois (automation, complexe)
├─ Zapier: €20-50/mois (flows, pas IA native)
└─ Solutions custom: €500-2000/mois (chère, lente)

NOTRE POSITIONNEMENT:
├─ IA PME Email: €29/mois (vs ChatGPT €20)
│  └─ Justif: Dédié email, zéro setup, français
├─ IA PME PDF: €39/mois
│  └─ Justif: Auto-génération docs, branded, audit trail
├─ IA PME Excel: €39/mois
│  └─ Justif: Auto-detect bugs, suggestions, zero-code
└─ BUNDLE 3 apps: €79/mois
   └─ Justif: -30%, killer deal pour PME

Vs concurrence: 30-40% MOINS CHER
Target: PME 5-50 salariés (y'a 150K+ en France)
```

### Pricing stratégique (pas charity, mais accessible):

```
TIER 1 - Starter (€29/mois ou €290/an -15%)
├─ 1000 emails/mois classifiés
├─ 50 PDFs générés/mois
├─ 25 analyses Excel/mois
├─ Support email (24h)
├─ 1 utilisateur
└─ Idéal: Freelance, micro-PME

TIER 2 - Professional (€79/mois ou €790/an -15%)
├─ 50K emails/mois classifiés
├─ 500 PDFs générés/mois
├─ 250 analyses Excel/mois
├─ Support email (4h) + chat
├─ 5 utilisateurs
└─ Idéal: PME 10-30 salariés

TIER 3 - Enterprise (Custom)
├─ Unlimited usage
├─ API dedicated
├─ Support phone + direct
├─ Multi-équipe + SSO
├─ Custom SLA
└─ Commencer à €500/mois

ACHETEURS CIBLES:
├─ Tier 1 (€29): Microentreprises, freelances (5000+ PME France)
├─ Tier 2 (€79): PME établies (50000+ PME France)
└─ Tier 3 (€500+): Grands compts, cabinets (1000+ potentiel)

STRATÉGIE ACQUISITION:
├─ MONTH 1: Gratuit pour 10 clients pilotes (collecte cas d'usage)
├─ MONTH 2-3: Freemium limité (100 emails/mois) → convert payant
├─ MONTH 4+: Plan tarifé standard
└─ ALWAYS: 30 jours gratuit full version (no card)
```

---

## 🗓️ ROADMAP PAR PHASE (RÉALISTE)

### **PHASE 0: NOW - 2 SEMAINES (Budget €0, Toi seul)**
**Objectif**: Démo + Portfolio solide pour clients + emploi

```
QU'ON A DÉJÀ (✅):
├─ 3 apps production-ready
├─ Tests complets + edge cases
├─ Demo runner validant tout
├─ Interactive demos (demos.html)
├─ Landing page (index.html)
└─ Documentation complète

À FAIRE CETTE SEMAINE (2 jours max):
├─ JOUR 1: Push GitHub + configure GitHub Pages
│  ├─ git add + commit + push
│  ├─ Enable GitHub Pages from /docs ou /root
│  └─ Verify: https://username.github.io
│
├─ JOUR 2: Portfolio/LinkedIn updates
│  ├─ Update LinkedIn: "Launched 3 AI apps for SMEs"
│  ├─ Share GitHub repo link
│  ├─ Create README in repo explaining architecture
│  └─ Add credentials: Tests pass, edge cases covered
│
└─ JOUR 3: Create simple metrics doc
   ├─ Show architecture (3 microservices)
   ├─ Show test coverage (18/18 pass)
   ├─ Show francization (23/23 checks pass)
   ├─ Show demo working (video or screenshot)
   └─ Conclusion: "Production-ready, ready to serve 100+ users"

RÉSULTAT:
- Portfolio impressionnant pour emploi/freelance
- Démo fonctionnelle visible par futurs clients
- GitHub profile complète (bonne pour recruting)
- Prêt pour "soft launch" quand tu commences à bosser
```

### **PHASE 1: WEEKS 3-8 (Budget €0, Toi seul + travail)**
**Objectif**: Soft launch + 5-10 clients pilotes (gratuit/freemium)

```
CONCURRENCE/TEMPS:
- Tu travailles (salaire fixe ✅)
- Soir/week-end: 5-10 heures/semaine sur startup
- Objectif: Pas encore gagner argent, valider produit

À FAIRE:

1. SEMAINE 3-4: GitHub + Deploy gratuit
   ├─ Push final code GitHub
   ├─ Deploy sur Railway gratuit (500h/mois free tier)
   │  ├─ Email Classifier service (port 8001)
   │  ├─ PDF Generator service (port 8002)
   │  └─ Excel Analyzer service (port 8003)
   ├─ Setup custom domain: app.ia-pme.fr (€1/mois DNS)
   └─ Test endpoints: curl https://app.ia-pme.fr/health

   COÛT: €0 (Railway free) + €1 domain = €1 total
   TEMPS: 3-4 heures (tuto Railway + DNS)

2. SEMAINE 5: Simple Landing page + waitlist
   ├─ Créer: pages/waitlist.html
   ├─ Integrate: Formspree (email collection, gratuit)
   ├─ Update: index.html → "Coming soon, join waitlist"
   ├─ Add: Email capture form
   └─ Setup: CNAME ia-pme.fr → GitHub Pages

   COÛT: €0 (Formspree free)
   TEMPS: 2 heures

3. SEMAINE 6: Create freemium (limited features)
   ├─ Add: rate limiting (100 requests/day free)
   ├─ Add: "Sign up with email" (no Stripe yet)
   ├─ Database: Simple SQLite first (no Postgres needed)
   ├─ Email users: "You're on waitlist, get free access"
   └─ Start: Gather feature requests from free users

   COÛT: €0
   TEMPS: 6-8 heures (SQLite + auth email)

4. SEMAINE 7-8: Pilot testing + feedback loop
   ├─ Email 10 contacts: "Free access to test, give feedback"
   ├─ Schedule: 15min calls with each (understand pain)
   ├─ Document: What they use most, what breaks, what they'd pay
   ├─ Track: Email classifier = 80% usage? PDF = 20%? Excel = 10%?
   └─ Iterate: Fix bugs, improve UX based on feedback

   COÛT: €0 + your time
   TEMPS: 10-15 hours total (calls + iterations)

RÉSULTAT PHASE 1:
✅ 5-10 users testing for free
✅ Real feedback on what matters
✅ Bugs caught + fixed in production
✅ 3 case studies: "This is what they use it for"
✅ Clear picture: Should I pivot? Scale? What's most valuable?

DÉPLOIEMENT:
- Live: https://app.ia-pme.fr (freemium)
- Waitlist: https://ia-pme.fr (landing page)
- GitHub: All code public + issues tracked
```

### **PHASE 2: WEEKS 9-16 (Budget €100-200/mois, Toi + 1 contractor)**
**Objectif**: 20-30 paying customers, €500-1500 MRR

```
CONTEXTE:
- Tu as maintenant salaire + petit budget
- Investis €100-200/mois dans infrastructure
- Embauche 1 contractor part-time (10h/sem)

À FAIRE:

1. SEMAINE 9-10: Stripe setup + billing
   ├─ Create Stripe account (free)
   ├─ Integrate into app:
   │  ├─ API: POST /api/checkout (create session)
   │  ├─ Webhook: customer.subscription.created
   │  ├─ Logic: Enable/disable features based on tier
   │  └─ Email: Invoice + receipt (auto-generated)
   ├─ Database migration: SQLite → Supabase free tier
   │  └─ Why: Supabase = PostgreSQL + auth, free 500MB
   └─ Test: Create test subscription, verify works

   COÛT: €0 (Stripe free for <€100 monthly volume)
           + €0 (Supabase free tier)
   TEMPS: 8-10 hours

2. SEMAINE 11: Client dashboard
   ├─ Create: /dashboard/index.html
   ├─ Show: Usage (emails classified, PDFs made, etc)
   ├─ Show: Billing history + next invoice date
   ├─ Show: API keys + documentation link
   ├─ Add: Password reset + account settings
   └─ Simple: No fancy UI, functional > beautiful

   COÛT: €0
   TEMPS: 6-8 hours

3. SEMAINE 12: Launch paid tier (quietly)
   ├─ Email existing free users: "Upgrade for €29/month"
   ├─ Create: Pricing page (simple markdown converted to HTML)
   ├─ Add: CTA buttons "Start free trial" (card required)
   ├─ Setup: Automated emails (welcome, invoice, churn alert)
   └─ Expect: 10-20% convert from free → paid

   COÛT: €0 + Email service
   TIME: 4-6 hours

4. SEMAINE 13: Contractor playbook (delegate prospecting)
   ├─ Create: /ops/contractor_playbook.md
   ├─ Include:
   │  ├─ Email templates (3: intro, follow-up, demo)
   │  ├─ Call script (5 min pitch)
   │  ├─ Closing process (get them to try free)
   │  ├─ Handoff to you (when they're ready to buy)
   │  └─ Commission: €20 per conversion
   ├─ Hire: 1 contractor via Upwork/Fiverr (€10-15/h)
   └─ Train: 2-3 hours onboarding

   COÛT: €200-400/month (contractor 10h/week)
           + Upwork fees (5%)
   TEMPS: 8-10 hours (playbook + hiring + training)

5. SEMAINE 14-16: Growth experiments
   ├─ A) LinkedIn prospecting (contractor does)
   ├─ B) Cold email (contractor does, use Lemlist free tier)
   ├─ C) Community (Product Hunt launch)
   ├─ D) Press (Email tech blogs: "Local startup launches SME AI")
   ├─ Track: Which channel gets best conversion
   └─ Iterate: Double down on best one

   COÛT: €0 (organic) or €50 (Lemlist premium)
   TIME: Contractor 10h/week

RÉSULTAT PHASE 2:
✅ 20-30 paying customers
✅ €500-1500 MRR (monthly recurring revenue)
✅ Churn rate known (target: <5%)
✅ LTV (lifetime value) per customer known
✅ 1 contractor trained + can scale prospecting
✅ Clear data: What works? What doesn't?

FINANCES PHASE 2:
Revenue:    €500-1500/month
Costs:      €100-200 (contractor) + €50 (tools) = €150-250
Profit:     €250-1350/month (back into R&D + living costs)

DÉPLOIEMENT:
- Live: https://app.ia-pme.fr (paid tiers active)
- Pricing: https://ia-pme.fr/pricing
- Emails: Automated (Resend or Mailgun free tier)
```

### **PHASE 3: WEEKS 17-24 (Budget €500-1000/mois, Toi + 2-3 contractors)**
**Objectif**: 50-100 customers, €2000-5000 MRR

```
CONTEXTE:
- Revenue is now paying for growth
- Invest 50% of profit back into team/tools
- Hire: 1 more BizDev + 1 Support contractor

À FAIRE:

1. SEMAINE 17-18: Standardize onboarding
   ├─ Create: Automated email sequence (5 emails over 7 days)
   │  ├─ Email 1: Welcome + quick start
   │  ├─ Email 2: Feature spotlight (what's most valuable)
   │  ├─ Email 3: Case study (another SME using it)
   │  ├─ Email 4: Tips to get more value
   │  └─ Email 5: Upgrade offer (upsell to Pro)
   ├─ Create: Video tutorials (30-60 sec each, Loom free)
   │  ├─ Video 1: First login
   │  ├─ Video 2: Classify email
   │  ├─ Video 3: Generate PDF
   │  ├─ Video 4: Analyze Excel
   │  └─ Video 5: View dashboard
   ├─ Reduce: Human onboarding time from 2 hours → 15 min
   └─ Scale: Support contractor can handle 20+ new customers/week

   COÛT: €0 (Loom free tier)
   TIME: 12-16 hours

2. SEMAINE 19: Analytics + metrics dashboard
   ├─ Create: /ops/metrics_dashboard.py
   │  ├─ Track: Signups, conversions, churn, LTV
   │  ├─ Track: Feature usage (what features convert best)
   │  ├─ Track: Revenue, costs, profit
   │  └─ Track: Contractor productivity (emails sent, calls, conversions)
   ├─ Setup: Daily email report to you (Google Sheets + automate)
   └─ Use: Data-driven decisions (what to double down on)

   COÛT: €0
   TIME: 6-8 hours

3. SEMAINE 20-21: Hire 2nd contractor
   ├─ BizDev contractor #2 (10h/week): Prospecting
   ├─ Support contractor (15h/week): Onboarding + tickets
   ├─ Training: 2-3 hours each
   └─ Commission: BizDev €20/conversion, Support €500/month

   COÛT: €400-600/month (2 contractors)
   TIME: 6-8 hours (hiring + onboarding)

4. SEMAINE 22-24: Launch Pro tier upsell
   ├─ Email all Starter users: "Try Pro for 7 days free"
   ├─ Create: Pro tier features (higher limits, priority support)
   ├─ Track: What % upgrade? Why?
   ├─ Create: Case study (e.g., "Cabinet used Email Classifier to save 5h/week")
   └─ Expand: Consider Enterprise tier (custom pricing)

   COÛT: €0
   TIME: 8-10 hours

RÉSULTAT PHASE 3:
✅ 50-100 paying customers
✅ €2000-5000 MRR (real revenue!)
✅ Standardized onboarding (contractor can scale 3x)
✅ Clear metrics (what's working, what's not)
✅ 2 contractors fully trained + productive
✅ Upsell strategy working (increase ARPU)

FINANCES PHASE 3:
Revenue:    €2000-5000/month
Costs:      €400-600 (contractors) + €100 (tools) = €500-700
Profit:     €1500-4300/month (Rudy salary + reinvest)

DÉPLOIEMENT:
- Live: https://app.ia-pme.fr (3 tiers live)
- Case studies: https://ia-pme.fr/case-studies
- Metrics: Private dashboard (only you access)
```

### **PHASE 4: MONTHS 7-12 (Budget €1000-2000/mois, Toi + 4-5 contractors)**
**Objectif**: 150-300 customers, €5000-10000 MRR (Series Seed ready)

```
CONTEXTE:
- Revenue growing 30-50% MoM
- Enough profit to support team
- Track: "This could be Series Seed candidate"

À FAIRE:

1. MONTH 7: Improve product + performance
   ├─ Hire: 1 backend contractor (PT) for optimization
   ├─ Goal: 
   │  ├─ API latency < 100ms (vs current 500ms)
   │  ├─ Add: API rate limits + logging
   │  ├─ Add: Better error messages
   │  └─ Test: Performance under 100 concurrent users
   └─ Result: Enterprise customers will consider you

   COÛT: €200-300/month
   TIME: 2 weeks sprint

2. MONTH 8: Create API for integrations
   ├─ Document: RESTful API (Swagger/OpenAPI)
   ├─ Add: Webhooks (email classified → Slack notification)
   ├─ Add: OAuth2 (customers can use your API in their apps)
   ├─ Create: 2-3 integration templates
   │  ├─ Slack integration (notify on email classified)
   │  ├─ Make.com integration (automate workflows)
   │  └─ Zapier integration (connect to 5000+ apps)
   └─ Market: "Your data, your workflow"

   COÛT: €0
   TIME: 3-4 weeks (API design + implementation)

3. MONTH 9: Expand to more languages
   ├─ Add: English support (open EU market)
   ├─ Add: Spanish (Spain + LATAM)
   └─ Translate: UI + documentation
   
   Impact: 3x new market

4. MONTH 10-11: Land first Enterprise customer
   ├─ BizDev focus: Approach 50+ big companies
   ├─ Pitch: "Custom SLA, dedicated support, white-label option"
   ├─ Goal: 1 Enterprise customer = €500-1000/month
   └─ Case study: Publish success story

5. MONTH 12: Prepare for Series Seed
   ├─ Create: Pitch deck (traction, market size, team)
   ├─ Track: 150-300 customers, €5-10K MRR, 30-50% MoM growth
   ├─ Network: Attend startup events, meet angels
   ├─ Plan: Use funds to hire CTO + VP Sales
   └─ Vision: "2000 customers, €100K MRR by end of Year 2"

RÉSULTAT PHASE 4:
✅ 150-300 paying customers
✅ €5000-10000 MRR
✅ Series Seed-ready (proven product-market fit)
✅ Team scaled (5-6 contractors)
✅ APIs + integrations (network effects)
✅ Multi-language support

FINANCES PHASE 4:
Revenue:    €5000-10000/month
Costs:      €800-1200 (team) + €200 (tools) = €1000-1400
Profit:     €4000-8600/month
Year 1 Total: €20-40K profit (before Series A)

NEXT: Raise €500K-1M Series Seed → Hire full team
```

---

## 💰 FINANCIAL PROJECTIONS (Realistic)

```
MONTH 1 (Dec):      €0 revenue (free users)
MONTH 2-3:          €0 revenue (freemium)
MONTH 4:            €300 MRR (10 customers × €30)
MONTH 5:            €500 MRR (15 customers + some upsells)
MONTH 6:            €800 MRR (25 customers)
MONTH 7:            €1,200 MRR (40 customers)
MONTH 8:            €2,000 MRR (60 customers)
MONTH 9:            €3,000 MRR (85 customers)
MONTH 10:           €4,500 MRR (120 customers, some Pro tier)
MONTH 11:           €6,000 MRR (160 customers)
MONTH 12:           €8,000 MRR (200 customers + 1 Enterprise)

CUMULATIVE REVENUE YEAR 1: €28,300
CUMULATIVE COSTS YEAR 1: €3,500 (contractors + tools)
PROFIT YEAR 1: €24,800

After Month 6: Profit covers Rudy salary (€2000/month) ✅
After Month 8: Can hire 2nd contractor ✅
After Month 12: Series Seed ready ✅
```

---

## 🛠️ TECH STACK (Free + Cheap tier)

### CURRENT (✅ already have):
```
├─ Python 3.14 + Flask
├─ PostgreSQL (free Supabase tier)
├─ Railway (free 500h/month)
└─ GitHub Pages (free)
```

### TO ADD (Phase 1):
```
├─ Stripe (free until €100/month)
├─ Supabase (free tier: 500MB, auth)
├─ Formspree (free form submissions)
└─ Mailgun (free tier: 100 emails/month)
```

### TO ADD (Phase 2-3):
```
├─ Resend (email service: €1 per 100 emails sent)
├─ Sentry (error tracking: free tier)
├─ Plausible Analytics (privacy-first: €9/month or self-host free)
├─ Loom (video: free tier)
└─ Upwork (contractor hiring)
```

---

## 📋 IMMEDIATE NEXT STEPS (THIS WEEK)

### ✅ DO THIS WEEKEND (2-3 hours):
```
1. [ ] Push GitHub with final code
2. [ ] Create README explaining architecture
3. [ ] Update LinkedIn profile
4. [ ] Screenshot/demo video of app working
5. [ ] List all technical achievements (tests, edge cases, etc)
```

### ✅ DO WEEK 1 OF EMPLOYMENT (4-5 hours after work):
```
1. [ ] Deploy to Railway (free tier)
2. [ ] Create simple landing page + waitlist (Formspree)
3. [ ] Custom domain (€1)
4. [ ] Email 20 people you know: "Join waitlist, test for free"
5. [ ] Start collecting feedback
```

### ✅ DO WEEKS 2-4 (5-10 hours/week):
```
1. [ ] Setup SQLite database + free signup
2. [ ] Add rate limiting (freemium features)
3. [ ] Schedule 10 calls with free users
4. [ ] Document feedback + feature requests
5. [ ] Prioritize: What to build next? What to cut?
```

---

## ⚠️ REALISTIC CHALLENGES + SOLUTIONS

```
CHALLENGE 1: "I'm working full-time, no time for startup"
SOLUTION: 
- Hire contractors early (Phase 1+)
- Focus: Only YOU do sales/product decisions (toi = 10 hours/week)
- Contractors do: Prospecting, support (flexible hours)
- Parallel: You work job, contractors work startup (no conflict)

CHALLENGE 2: "What if nobody wants to pay?"
SOLUTION:
- Pivot early (Phase 1 feedback)
- Maybe switch to: Email Classifier (80% interest) → ignore rest
- Or: Focus B2B vs B2C
- Or: Change pricing
- Early feedback = early pivots, saves 6 months

CHALLENGE 3: "Contractors cost money I don't have"
SOLUTION:
- Phase 1: No contractors (just you)
- Phase 2: Revenue covers contractors (profit-funded)
- Benefit: When growth slows, you can reduce contractor hours
- Risk: Slower growth, but zero cash burn

CHALLENGE 4: "I don't know if this is viable"
SOLUTION:
- Phase 1 FREE users will tell you
- If 0 signups → pivot fast
- If 100+ signups → pursue aggressively
- Data > opinion (yours or mine)

CHALLENGE 5: "Series Seed feels far away"
SOLUTION:
- Focus: Get to €1000 MRR (6-8 months)
- Then: €5000 MRR (9-12 months)
- Then: Angels/VCs notice (proven product-market fit)
- Then: Raise money (for team, not survival)
```

---

## 🎯 SUCCESS METRICS (Track monthly)

```
MONTH 1-3 (Validation):
├─ Signups: 50+
├─ Free users: 20+
└─ Churn rate: N/A (free users)

MONTH 4-6 (Product-market fit):
├─ Paying customers: 20+
├─ MRR: €500+
├─ Churn rate: <5%/month
└─ Net promoter score: >50

MONTH 7-12 (Growth):
├─ Paying customers: 150+
├─ MRR: €5000+
├─ Churn rate: <3%/month
├─ Customer LTV: €600+ (€30 × 20 months)
└─ Conversion rate: 5-10% (free → paid)

If you hit these: Series Seed = easy ✅
```

---

## 📞 DECISION POINT (After Phase 1, Month 4)

After you get 20-30 free users + feedback, ask yourself:

```
A. "People love this, demand is real"
   → Continue Phase 2: Hire contractors, launch paid, scale

B. "People don't care, or feedback is cold"
   → Pivot: Maybe different product? Different market?
   → Or: Pause, gather more data

C. "Love the product, but no time to manage"
   → Hire someone: Full-time contractor CTO to run product
   → You focus: Sales + vision only
```

**The roadmap is a hypothesis, not gospel. Adjust based on real data.** 📊

---

## 📞 QUESTIONS FOR YOU (To refine plan):

1. **Contractors**: Freelance EU-based, or remote worldwide?
2. **Support**: SLA? (24h response or 4h?)
3. **Market**: France only, or expand to EU immediately?
4. **Exit**: Acquisition (by big consulting firm), or IPO vision?
5. **Personal**: Want to be CEO long-term, or build + sell in 3 years?

Your answers → I can give you even more targeted roadmap. 

---

## 🚀 BOTTOM LINE

**Right now**: You have 3 killer apps + solid portfolio. Use this to get job + cash.

**Month 1 (with salary)**: Deploy free, collect users, validate hypothesis.

**Months 2-4**: If users love it, launch paid + hire 1 contractor.

**Months 5-12**: Scale to €5-10K MRR, prepare Series Seed pitch.

**Year 2+**: Hire team, raise capital, dominate SME AI market in France.

**Capital required to start**: €0 (pure sweat equity)

**Capital to scale fast**: €100-500/month (servers + contractors)

**Capital to raise**: €500K-1M Series Seed (if product-market fit confirmed)

---

**Status**: Ready to execute. Next step = your decision.

Do you want to:
1. ✅ Push GitHub now + start Phase 0?
2. ❓ Adjust something in this roadmap?
3. 🔄 Get more detail on a specific phase?

Let's go. 🚀
