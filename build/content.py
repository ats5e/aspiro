# -*- coding: utf-8 -*-
"""All site content for aspiro.me. Edit here, then run `python3 build/build.py`."""

SITE = {
    "name": "Aspiro Management Consultants",
    "short": "Aspiro",
    "domain": "https://aspiro.me",
    "email": "info@aspiro.me",
    "phone_display": "+971 5230 8566",
    "phone_tel": "+97152308566",
    "address_lines": ["Office 102-031, Montana Building", "Al Karama, Dubai, UAE"],
    "linkedin": "https://www.linkedin.com/company/aspiro-me",
    "offices": ["Dubai", "Riyadh", "London"],
    "founded": 2015,
    "strapline": "Leading with clarity. Delivering the difference.",
    # Formspree endpoints, e.g. "https://formspree.io/f/XXXXXXXX". Empty contact endpoint = mailto fallback;
    # empty gate endpoint = whitepapers still unlock but no lead is recorded.
    "form_endpoint": "https://formspree.io/f/mvkgpdog",   # Contact form
    "gate_endpoint": "https://formspree.io/f/mgavwrwg",   # Whitepaper downloads
}

NAV = [
    ("About", "/about.html"),
    ("Services", "/services.html"),
    ("Approach", "/approach.html"),
    ("Work", "/work.html"),
    ("Insights", "/insights.html"),
    ("People", "/people.html"),
]

STATS = [
    ("100+", "Years of senior leadership experience"),
    ("8,000+", "Specialists in our global network"),
    ("100%", "Independent and investor-free"),
    ("24+", "Major transformation programmes delivered"),
]

CLIENT_LOGOS = [
    ("Mashreq", "Mashreq"), ("Emirates-NBD", "Emirates NBD"), ("Alrajhi-Bank", "Al Rajhi Bank"),
    ("HSBC", "HSBC"), ("Riyad-Bank", "Riyad Bank"), ("Rakbank", "RAKBANK"), ("SAB-Invest", "SAB Invest"),
    ("RBS", "RBS"), ("UBS", "UBS"), ("SNB", "SNB"), ("Noor-Bank", "Noor Bank"), ("FAB", "First Abu Dhabi Bank"),
    ("ADCB", "ADCB"), ("Tawuniya", "Tawuniya"), ("Alawwal-Bank", "Alawwal Bank"),
    ("Commerical-Bank", "Commercial Bank"), ("ABN-Amro", "ABN AMRO"), ("BSP", "BSP"), ("Network", "Network International"),
]

ICONS = {
    "target": '<svg viewBox="0 0 40 40" fill="none"><circle cx="20" cy="20" r="14"/><circle cx="20" cy="20" r="5"/><path d="M20 6v6M34 20h-6M20 34v-6M6 20h6"/></svg>',
    "chip": '<svg viewBox="0 0 40 40" fill="none"><rect x="11" y="11" width="18" height="18" rx="4"/><path d="M20 4v5M20 31v5M4 20h5M31 20h5"/><circle cx="20" cy="20" r="4"/></svg>',
    "chart": '<svg viewBox="0 0 40 40" fill="none"><path d="M7 30h26"/><path d="M10 25l6-6 5 4 9-10"/><circle cx="30" cy="13" r="2.5"/></svg>',
    "shield": '<svg viewBox="0 0 40 40" fill="none"><path d="M20 6 31 10v8c0 8-5.2 12.7-11 15-5.8-2.3-11-7-11-15v-8l11-4Z"/><path d="m14 20 4 4 8-8"/></svg>',
    "people": '<svg viewBox="0 0 40 40" fill="none"><circle cx="14" cy="16" r="4"/><circle cx="26" cy="14" r="3"/><path d="M8 29c1.8-4 4.6-6 8-6s6.2 2 8 6"/><path d="M22 28c1-2.6 2.8-4.1 5.2-4.5"/></svg>',
    "megaphone": '<svg viewBox="0 0 40 40" fill="none"><path d="M8 17v6h5l9 6V11l-9 6H8Z"/><path d="M27 15a6 6 0 0 1 0 10M30 11a11 11 0 0 1 0 18"/></svg>',
}

# ---------------------------------------------------------------------------
# SERVICES
# ---------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "transformation",
        "num": "01",
        "icon": "target",
        "name": "Transformation & Strategy",
        "short": "Transformation<br>&amp; Strategy",
        "photo": "svc-transformation",
        "photo_pos": "center",
        "summary": "Leading end-to-end transformations across banking, capital markets and financial services, from vision through to value realisation, by practitioners who have held the roles they now advise on.",
        "tags": ["M&A execution", "Target operating model", "PMO &amp; programme management", "Vendor selection"],
        "intro": "Most transformation programmes in the region do not fail for lack of ambition. They fail in the gap between the strategy the Board approved and the organisation that has to deliver it. We close that gap.",
        "body": [
            ("Strategy that survives contact with reality",
             "We start from the executive agenda, not a framework. Whether the mandate is a Vision 2030 growth plan, a merger, a new market entry or a wholesale operating-model reset, we validate the business case before capital is committed, translate intent into a target operating model that names owners and dates, and stay to run the programme office that delivers it."),
            ("Transformation management office, not just a PMO",
             "A conventional PMO reports status. Our transformation management office makes decisions faster: a single source of truth for scope, benefits, risks and dependencies, with Board-grade reporting that gives the CEO full line of sight. On a recent Saudi capital-markets mandate this discipline delivered six strategic initiatives ahead of Board-committed dates."),
            ("Merger and acquisition execution",
             "We have led integrations of the Kingdom's largest lenders and multi-business consolidations across asset management, brokerage, margin lending and wealth. Legal-day readiness, day-one customer experience, synergy tracking and regulator engagement are handled by people who have done it before, under the same regulators."),
            ("Vendor and platform selection",
             "Independence matters most when a core platform is at stake. We take no referral fees and have no alliance obligations, so the shortlist reflects your requirements alone, and the commercial negotiation is run by people who know where the value leaks in a bank technology contract."),
        ],
        "capabilities": [
            "Corporate and business-unit strategy", "Target operating model design", "Transformation management office",
            "M&amp;A due diligence and integration", "Post-merger synergy realisation", "Market entry strategy",
            "Vendor selection and contract negotiation", "Board and executive reporting",
        ],
        "outcomes": [("Top 5", "Market position targeted for a merged Saudi capital-markets institution"), ("6", "Strategic initiatives delivered ahead of Board dates"), ("Zero", "Customer disruption across a 200,000-customer integration")],
        "cases": ["saudi-capital-markets", "multi-business-integration"],
    },
    {
        "slug": "digital",
        "num": "02",
        "icon": "chip",
        "name": "AI, Automation & Digital",
        "short": "AI, Automation<br>&amp; Digital",
        "photo": "svc-digital",
        "photo_pos": "center",
        "summary": "Implementing next-generation AI and automation that creates genuine competitive advantage, from intelligent workflows to cloud-native digital banking ecosystems built for scale.",
        "tags": ["RPA &amp; AI automation", "Open banking &amp; PSD2", "AI risk analytics", "Digital transformation"],
        "intro": "The region's banks have no shortage of technology. What they lack is a disciplined route from pilot to production, and a way of automating that does not simply encode yesterday's inefficiency at scale.",
        "body": [
            ("Lean first, then automate",
             "Our Smart Ops framework builds a digital twin of the operation before a single bot is deployed. Waste is removed from the process first, controls are designed in, and only then is automation applied. The result is automation that pays back in weeks rather than a growing estate of bots maintaining a broken process."),
            ("Agentic AI where it earns its place",
             "We deploy agentic workflows in the parts of a bank where the economics are unambiguous: onboarding, KYC refresh, credit operations, reconciliations, complaints and regulatory reporting. Every deployment is measured against a baseline, governed under a model-risk framework, and designed to be explainable to the regulator."),
            ("Digital banking propositions",
             "We have helped a local bank launch a competitive digital-only proposition on cloud-native architecture, with WhatsApp banking and onboarding in minutes rather than days. Proposition, architecture, vendor selection and launch were run as one programme, with the cost-to-income impact tracked from day one."),
            ("Open banking and open finance",
             "With SAMA's open banking framework and the CBUAE's open finance regulation now live, incumbents face a choice between compliance and advantage. We help banks design the API strategy, partner model and data governance that turns a regulatory obligation into new distribution."),
        ],
        "capabilities": [
            "Smart Ops and process digital twin", "Intelligent automation and RPA", "Agentic AI deployment and governance",
            "Digital banking proposition design", "Cloud-native architecture", "Open banking and open finance strategy",
            "AI risk analytics", "Technology partner and vendor management",
        ],
        "outcomes": [("Minutes", "Customer onboarding time, down from days"), ("70%", "Reduction in manual processing time"), ("Weeks", "Time to first measurable ROI through quick-fix deployment")],
        "cases": ["digital-banking-launch", "automated-esg"],
    },
    {
        "slug": "revenue-cost",
        "num": "03",
        "icon": "chart",
        "name": "Revenue & Cost Optimisation",
        "short": "Revenue &amp; Cost<br>Optimisation",
        "photo": "svc-revenue-cost",
        "photo_pos": "center",
        "summary": "Driving measurable financial performance through strategic sourcing, Lean process re-engineering and disciplined cost management that shows up on the P&amp;L, not just on slides.",
        "tags": ["Strategic sourcing", "Lean re-engineering", "Cost-to-income improvement", "Business case development"],
        "intro": "Cost programmes announced with a percentage target rarely deliver it. We work at the level of the process, the contract and the balance sheet, where cost is actually created, and we stay until the saving is banked.",
        "body": [
            ("Front-to-back Lean",
             "A comprehensive Lean review of a global bank's primary loans and credit processes across London and New York eliminated manual waste, optimised risk-weighted asset allocation and released capital. Twenty-five million dollars of cost was taken out and 1.1 billion dollars of RWA reduction released 150 million dollars of capital, through disciplined process redesign rather than headcount theatre."),
            ("Cost-to-income, lever by lever",
             "We decompose the cost-to-income ratio into the handful of levers that actually move it in a GCC bank: operations productivity, technology run cost, third-party spend, distribution footprint and the revenue denominator. Each lever gets an owner, a baseline and a monthly tracking cadence."),
            ("Strategic sourcing and third-party spend",
             "Third-party spend is often the largest addressable cost pool and the least governed. We run category strategies, renegotiate the contracts that matter, and put in place the demand management that stops the saving leaking back."),
            ("Revenue and pricing",
             "Pricing studies, fee-structure redesign and product profitability analysis that identify where value is being given away. Combined with our marketing practice, this turns the revenue side of the ratio into a lever rather than a given."),
        ],
        "capabilities": [
            "Cost-to-income diagnostic", "Front-to-back Lean process redesign", "Strategic sourcing and procurement",
            "Third-party spend governance", "Pricing and product profitability", "Business case development and benefits tracking",
            "Capital and RWA optimisation", "Zero-based budgeting",
        ],
        "outcomes": [("$25M", "Cost savings realised in a single global bank engagement"), ("$1.1bn", "RWA reduction through redesigned credit processes"), ("$150M", "Capital released")],
        "cases": ["lean-optimisation", "hr-synergy"],
    },
    {
        "slug": "risk-esg",
        "num": "04",
        "icon": "shield",
        "name": "Risk, Control & ESG",
        "short": "Risk, Control<br>&amp; ESG",
        "photo": "svc-risk-esg",
        "photo_pos": "center",
        "summary": "Building robust governance frameworks and automated sustainability reporting to meet the GCC's rapidly evolving regulatory environment, from Basel III through to IFRS S1/S2.",
        "tags": ["ESG reporting (IFRS S1/S2)", "ESG national agenda framework", "AML / KYC remediation", "Basel III compliance", "Third-party risk management"],
        "intro": "The regulatory agenda in the GCC is moving faster than most control functions can absorb. We help risk, compliance and finance leaders meet it with frameworks that are robust, automated where they should be, and defensible in front of the regulator.",
        "body": [
            ("ESG and sustainability reporting",
             "IFRS S1 and S2 adoption, UAE Decree-Law No. 11 and national sustainability agendas have turned ESG from a communications exercise into a reporting obligation with audit-grade expectations. At a large UAE bank we replaced manual, spreadsheet-based data collection with automated real-time dashboards, cutting processing time by 70 percent and saving over 1,200 hours a year."),
            ("Financial crime remediation",
             "AML and KYC remediation programmes across the GCC, delivered by practitioners who have run financial crime operations. We fix the backlog, then fix the process that created it, so the remediation does not need to be repeated."),
            ("Prudential and operational resilience",
             "Basel III implementation, ICAAP and ILAAP uplift, operational resilience frameworks and third-party risk management protocols that satisfy SAMA, CBUAE and QCB expectations without paralysing the business."),
            ("Risk governance that works",
             "Three lines of defence redesigned around accountability rather than committees. Risk appetite that the front line can actually use. Board risk reporting that surfaces what matters."),
        ],
        "capabilities": [
            "IFRS S1/S2 and ESG reporting automation", "ESG framework and national agenda alignment", "AML and KYC remediation",
            "Basel III, ICAAP and ILAAP", "Operational resilience", "Third-party risk management",
            "Risk governance and three lines of defence", "Regulatory engagement and response",
        ],
        "outcomes": [("70%", "Reduction in ESG reporting processing time"), ("1,200+", "Hours saved annually at a large UAE bank"), ("Full", "IFRS S1/S2 and UAE Decree-Law No. 11 compliance")],
        "cases": ["automated-esg", "lean-optimisation"],
    },
    {
        "slug": "human-capital",
        "num": "05",
        "icon": "people",
        "name": "Human Capital & Change",
        "short": "Human Capital<br>&amp; Change",
        "photo": "svc-human-capital",
        "photo_pos": "center",
        "summary": "Managing the people dimension of transformation with the care it demands: workforce transitions, culture change, Saudization strategy and skills mapping that preserves capability while realising synergies.",
        "tags": ["Workforce transition", "Saudization strategy", "Culture change", "Skills gap analysis"],
        "intro": "Every transformation is ultimately a change in what people do on Monday morning. We treat the people workstream as the critical path it is, with the rigour of a synergy model and the care that institutions in this region rightly expect.",
        "body": [
            ("Workforce transition and synergy realisation",
             "For a non-bank financial institution merger we built a granular HR synergy model validating SAR 4.75 million of annual recurring savings across three scenarios, securing Board and SAMA approval with a six-to-twelve-month payback. Harmonisation logic, selection processes and retention of critical capability were designed together, not sequentially."),
            ("Saudization and nationalisation strategy",
             "Nitaqat targets and Emiratisation commitments are strategic constraints, not HR footnotes. We build workforce plans that meet them through capability building and role redesign, with the skills mapping and development pathways that make national talent a competitive advantage."),
            ("Culture and change leadership",
             "Culture change that starts with what leaders do differently, measured through behaviours rather than surveys. Change management embedded in the transformation office, so adoption is planned with the same discipline as delivery."),
            ("Organisation design",
             "Spans, layers, role clarity and decision rights redesigned around the target operating model, with the grading and reward implications worked through before announcement rather than after."),
        ],
        "capabilities": [
            "HR synergy modelling and realisation", "Workforce transition and selection", "Saudization and Emiratisation strategy",
            "Skills gap analysis and capability building", "Culture change", "Organisation design",
            "Change management and adoption", "Leadership alignment",
        ],
        "outcomes": [("SAR 4.75M", "Annual recurring HR synergies validated"), ("6 to 12", "Months to payback"), ("SAMA", "Regulatory approval secured")],
        "cases": ["hr-synergy", "multi-business-integration"],
    },
    {
        "slug": "marketing",
        "num": "06",
        "icon": "megaphone",
        "name": "Marketing & Growth",
        "short": "Marketing<br>&amp; Growth",
        "photo": "svc-marketing",
        "photo_pos": "center",
        "summary": "Proposition, pricing and go-to-market for financial institutions that need to win the next generation of GCC customers, grounded in commercial evidence rather than creative instinct alone.",
        "tags": ["Proposition design", "Pricing studies", "Customer acquisition", "Segment strategy"],
        "intro": "Growth in GCC financial services is now a proposition contest. Digital challengers, super-apps and regional expansion have raised the bar on what customers expect from a bank, an insurer or a broker. We help incumbents compete on evidence.",
        "body": [
            ("Proposition and segment strategy",
             "Which segments to win, what to offer them and how to be different from the bank next door. We combine customer research with product economics so the proposition is both desirable and profitable, and we have helped launch digital-only propositions that won the next generation of customers."),
            ("Pricing studies",
             "Fee structures, rate cards and bundling designed from customer value and competitor benchmarks. Pricing is the fastest revenue lever most institutions never pull deliberately."),
            ("Go-to-market and acquisition",
             "Channel economics, partnership models and acquisition funnels measured to the unit level. Marketing spend becomes an investment with a return, not a budget line."),
            ("Brand and communications for regulated businesses",
             "Positioning that senior stakeholders and regulators are comfortable with, delivered with the discipline financial services requires."),
        ],
        "capabilities": [
            "Segment and proposition strategy", "Pricing studies and fee redesign", "Go-to-market planning",
            "Customer acquisition economics", "Partnership and ecosystem models", "Customer journey design",
            "Brand positioning", "Marketing effectiveness measurement",
        ],
        "outcomes": [("Minutes", "Onboarding for a newly launched digital proposition"), ("Next-gen", "GCC customers won by a digital-only launch"), ("Evidence", "Pricing and proposition decisions grounded in data")],
        "cases": ["digital-banking-launch", "saudi-capital-markets"],
    },
]

# ---------------------------------------------------------------------------
# CASE STUDIES
# ---------------------------------------------------------------------------
CASES = [
    {
        "slug": "digital-banking-launch",
        "cat": "Digital transformation",
        "metric": "Minutes",
        "metric_sub": "Customer onboarding, down from days",
        "title": "Omnichannel strategy and digital banking launch",
        "client": "Local bank, GCC",
        "summary": "Enabled a local bank to launch a competitive digital-only proposition: cloud-native architecture, WhatsApp banking and instant onboarding.",
        "challenge": "A local bank was losing the next generation of customers to digital challengers and neighbouring incumbents. Onboarding took days, the branch-led model was expensive, and the technology estate could not support a modern proposition.",
        "did": "Designed the omnichannel strategy and digital-only proposition, selected and architected a cloud-native platform, launched WhatsApp banking and instant digital onboarding, and ran the programme through to launch with cost-to-income impact tracked from day one.",
        "outcome": "Onboarding in minutes rather than days, a dramatically reduced cost-to-income ratio for the digital proposition, and a customer base skewed to the younger segments the bank had been losing.",
        "services": ["digital", "marketing"],
    },
    {
        "slug": "lean-optimisation",
        "cat": "Cost optimisation",
        "metric": "$25M",
        "metric_sub": "Cost savings realised · $1.1bn RWA reduction",
        "title": "Front-to-back Lean optimisation",
        "client": "Global bank, London and New York",
        "summary": "Comprehensive Lean review of primary loans and credit processes, eliminating manual waste, optimising RWA allocation and releasing capital.",
        "challenge": "Primary loans and credit processes had accreted controls, hand-offs and rework over a decade. Cost was high, cycle times were long, and capital was being consumed by risk-weighted assets the process was not optimising.",
        "did": "Mapped the front-to-back process across both locations, removed non-value-adding activity, redesigned credit process steps to optimise RWA allocation, and embedded the new standard operating procedures with the teams that run them.",
        "outcome": "Twenty-five million dollars of cost savings realised, 1.1 billion dollars of RWA reduction and 150 million dollars of capital released.",
        "services": ["revenue-cost", "risk-esg"],
    },
    {
        "slug": "saudi-capital-markets",
        "cat": "Strategy execution",
        "metric": "Top 5",
        "metric_sub": "Market position in KSA · 6 initiatives ahead of schedule",
        "title": "TMO-led strategic execution for a Saudi capital-markets institution",
        "client": "Newly merged capital-markets institution, KSA",
        "summary": "Positioned a newly merged capital-markets institution for a Top 5 position in KSA by 2027, delivering six key initiatives ahead of Board-committed dates.",
        "challenge": "Two merged institutions, one Board-approved Vision 2027 strategy, and no delivery engine capable of turning it into results with the visibility the Board and regulator expected.",
        "did": "Established a transformation management office as the single source of truth for scope, benefits and risk, prioritised the initiative portfolio, and ran delivery with rigorous governance and executive-grade reporting.",
        "outcome": "Six key initiatives delivered ahead of Board-committed dates, full executive visibility of execution and risk, and the institution on track for its Top 5 ambition.",
        "services": ["transformation", "marketing"],
    },
    {
        "slug": "multi-business-integration",
        "cat": "M&amp;A integration",
        "metric": "Zero",
        "metric_sub": "Disruption · 200,000+ customers · $205M of businesses",
        "title": "Transformation PMO for a multi-business integration",
        "client": "Financial group, GCC",
        "summary": "PMO-led integration of asset management, retail brokerage, margin lending and wealth management with legal-day readiness and a seamless day-one customer experience.",
        "challenge": "Four businesses, 205 million dollars of value and more than 200,000 customers had to be integrated to a fixed legal day, with no tolerance for customer disruption or regulatory surprise.",
        "did": "Ran the integration PMO: legal-day readiness across every function, transparent governance to the steering committee and regulator, customer-migration planning and day-one command centre.",
        "outcome": "Zero customer disruption on day one, on-time legal completion, and a governance record the regulator commended.",
        "services": ["transformation", "human-capital"],
    },
    {
        "slug": "automated-esg",
        "cat": "Risk &amp; ESG",
        "metric": "70%",
        "metric_sub": "Reduction in processing time · 1,200+ hours saved",
        "title": "Automated ESG reporting and compliance",
        "client": "Large UAE bank",
        "summary": "Replaced manual Excel-based ESG collection with Alteryx-powered real-time dashboards, with full compliance to IFRS S1/S2, UAE Decree-Law No. 11 and global standards.",
        "challenge": "ESG data was collected by hand across dozens of business units into spreadsheets, consuming thousands of hours a year and producing numbers nobody could fully defend as IFRS S1/S2 reporting approached.",
        "did": "Designed the ESG data model and control framework, automated collection and calculation using Alteryx, and delivered real-time dashboards mapped to IFRS S1/S2, UAE Decree-Law No. 11 and global standards.",
        "outcome": "Seventy percent reduction in processing time, more than 1,200 hours saved annually, and audit-grade sustainability reporting.",
        "services": ["risk-esg", "digital"],
    },
    {
        "slug": "hr-synergy",
        "cat": "Human capital",
        "metric": "SAR 4.75M",
        "metric_sub": "Annual recurring HR synergies · 6 to 12 month payback",
        "title": "HR synergy realisation for an NBFI merger",
        "client": "Non-bank financial institution, KSA",
        "summary": "Granular HR synergy model validating SAR 4.75M in annual savings across three scenarios, securing Board and SAMA regulatory approval.",
        "challenge": "A merger business case depended on people synergies that had been estimated top-down. The Board and SAMA needed a defensible, bottom-up model before approval, and the institution needed to keep the capability that made the deal worth doing.",
        "did": "Built a role-by-role synergy model across three scenarios, designed the harmonisation and selection logic, and prepared the Board and regulatory submissions.",
        "outcome": "SAR 4.75 million of annual recurring savings validated, a six-to-twelve-month payback, and approval from both the Board and SAMA.",
        "services": ["human-capital", "revenue-cost"],
    },
]

# ---------------------------------------------------------------------------
# TEAM
# ---------------------------------------------------------------------------
TEAM = [
    ("William", "William Higgins", "Managing Partner", "leadership",
     "William has spent the last decade deeply embedded in the GCC financial sector, partnering with all of the major banks in the region on their most critical transformation journeys. This is built on a distinguished global career in senior C-suite roles at NatWest and ABN AMRO, where he managed multi-billion dollar P&amp;Ls and teams of over 15,000 people."),
    ("Colin", "Colin Macdonald", "Executive Chairman", "leadership",
     "Colin has been a leading figure in GCC and international banking, serving as Deputy CEO of a major GCC bank, Group CEO of a major investment bank and Regional Head of a major full-service international bank. His leadership has guided large institutions through complex transformations and strategic shifts. With deep governance, risk and execution experience, Colin brings board-level and operational perspectives to Aspiro's client work."),
    ("Punit", "Punit Khanna", "Partner", "leadership",
     "Punit has over 20 years of strategic and operational banking and consultancy experience at one of India's and the GCC's major banks and one of the GCC's leading management consultancies. He works across business and technology change with a focus on practical, outcome-oriented implementation."),
    ("Lasse", "Lasse Hall", "Partner", "leadership",
     "Lasse has over 25 years of strategic, operational and technical implementation experience in investment banking and wealth management at one of the leading Swiss banks and one of the major GCC banks. He specialises in front-to-back transformation, platform modernisation and delivery across complex product and client landscapes."),
    ("Chis", "Chris Renardson", "Partner", "leadership",
     "Chris has over 30 years of strategic and operational leadership experience at one of the GCC's major sovereign wealth funds and one of the GCC's leading listed corporations. He advises on enterprise performance, value creation and strategic change in large, complex organisations."),
    ("David", "David Goodyear", "Partner", "leadership",
     "David has over 25 years of strategic and operational banking and consultancy experience at one of South Africa's and the GCC's major banks and one of Europe's and the GCC's major management consultancies. He focuses on end-to-end transformation, capability uplift and operational performance in financial services."),
    ("Jack-Donaldson", "Jack Donaldson", "Head of Marketing &amp; Communications", "leadership",
     "Jack is a dynamic marketing and communications leader with a proven record of driving brand growth, elevating storytelling and delivering measurable results across global markets. His experience spans London, New York and Sydney, blending creative vision with commercial precision for the world's leading banks and fintechs."),
    ("Brett", "Brett Maclagan", "Principal", "principals",
     "Brett has over 25 years of global strategy and operational banking, telecoms and aviation experience at one of the world's leading management consultancies and one of the GCC's leading consulting firms. He brings deep expertise in operating model design, delivery acceleration and execution discipline."),
    ("Gaurav", "Gaurav Diwan", "Principal", "principals",
     "Gaurav has over 20 years of strategic and operational banking and consultancy experience at one of Europe's major banks and one of the GCC's leading management consultancies. His experience covers transformation, operating model enhancement and large-scale programme execution."),
    ("Ashish", "Ashish Malhotra", "Principal", "principals",
     "Ashish has over 20 years of strategic and operational banking and technology experience at one of India's major banks and one of the GCC's largest banks. He has delivered major initiatives in banking operations, systems and process transformation."),
    ("Sunil", "Sunil Arora", "Principal", "principals",
     "Sunil has over 20 years of strategic and operational banking and technology experience at one of India's major banks and one of the GCC's largest banks. He works at the intersection of business change and technology enablement for financial institutions."),
    ("Clark", "Clark Fisher", "Principal", "principals",
     "Clark has over 15 years of strategic and operational banking and technology experience at one of the GCC's largest independent consulting firms and one of the GCC's largest banks. He supports transformation design and delivery across critical banking workstreams."),
    ("Yusuf", "Yusuf Tarajia", "Senior Associate", "principals",
     "Yusuf has over 10 years of strategic and operational banking and technology experience at one of the GCC's largest independent consulting firms and one of the GCC's largest banks. His focus includes analysis, delivery management and execution support for transformation programmes."),
    ("Ayesha", "Ayesha Azhar", "Associate", "principals",
     "Ayesha has over 10 years of strategic and operational banking and consultancy experience at one of the GCC's major independent consulting firms and one of the GCC's largest banks. She supports strategy and implementation delivery with a strong focus on practical outcomes."),
]

# ---------------------------------------------------------------------------
# INSIGHTS
# ---------------------------------------------------------------------------
INSIGHTS = [
    {
        "slug": "strategy-execution-gap",
        "cat": "Transformation",
        "date": "2026-09-02",
        "read": 6,
        "photo": "ins-strategy-execution-gap", "pos": "center",
        "title": "Why strategy dies in the gap between the Board and the front line",
        "dek": "GCC banks do not lack ambition. They lack a delivery engine that survives the second quarter. Here is what separates the programmes that land from the ones that quietly stall.",
        "quote": "A strategy the organisation cannot execute is a wish with a budget attached.",
        "body": """
<p>Every bank in the region has a strategy. Most of them are good. They have been benchmarked, stress-tested by advisers and approved by a Board that understands the market. And yet, two years on, the same institutions are commissioning the same strategy again, because the first one was never really executed.</p>
<p>The failure is rarely in the thinking. It is in the gap between the document the Board approved and the organisation that has to deliver it. That gap has a predictable anatomy.</p>
<h2>Three ways strategy stalls</h2>
<p><strong>The initiative portfolio is a wish list.</strong> Forty initiatives, each with a sponsor, none with a sequence. Nobody has decided what must be true by the end of quarter two for quarter four to be possible. The result is dozens of workstreams competing for the same architects, the same data team and the same executive attention.</p>
<p><strong>Governance reports status rather than making decisions.</strong> The steering committee meets monthly, receives a rag-status pack and moves on. Decisions that should take a week take a quarter, because no forum owns them. By the time the dependency is escalated, the date has already slipped.</p>
<p><strong>Benefits are declared, not tracked.</strong> The business case promised a cost-to-income improvement. Twelve months later nobody can say which initiative delivered which basis point, so nothing is stopped, nothing is doubled down on, and the P&amp;L looks much as it did.</p>
<h2>What a transformation management office actually does</h2>
<p>The fix is not another PMO. A conventional programme office collects plans and reports variances. A transformation management office is a decision engine. It holds the single source of truth for scope, benefits, risks and dependencies, and it forces the trade-offs that a portfolio of forty initiatives requires.</p>
<p>On a recent Saudi capital-markets mandate the difference was visible within a quarter. Six strategic initiatives, each with a Board-committed date, were delivered ahead of schedule, not because the teams worked harder but because the office removed the decisions that had been blocking them. The chief executive could see, every week, exactly where execution risk sat.</p>
<h2>Three questions to ask on Monday</h2>
<p>If you sponsor a transformation, ask three things. Which five initiatives, if they slipped by a quarter, would put the strategy at risk? Which decision has been waiting longest for a forum to make it? And which benefit in the business case would you struggle to evidence today? The answers tell you whether you have a strategy or a delivery engine.</p>
<p>Strategy survives contact with reality when somebody stays in the room to make sure it does. That is the job.</p>
""",
        "related": ["post-merger-day-one", "cost-to-income-levers"],
    },
    {
        "slug": "lean-before-automation",
        "cat": "Smart Ops",
        "date": "2026-08-19",
        "read": 7,
        "photo": "ins-lean-before-automation", "pos": "center",
        "title": "Digitising the mess: why Lean has to come before automation",
        "dek": "Automation applied to a broken process gives you a faster broken process. The banks getting real returns from AI and RPA are doing something unglamorous first.",
        "quote": "Every bot you deploy on an unredesigned process is a permanent monument to the inefficiency you chose not to fix.",
        "body": """
<p>There is a particular kind of automation programme that every operations leader in the region will recognise. It starts with a vendor demonstration, a proof of concept in a friendly department and a business case that promises a headcount saving. Eighteen months later there are two hundred bots, a team of twelve maintaining them, and a process that is no better understood than it was at the start.</p>
<p>The programme did not fail because the technology was poor. It failed because the process it automated was never redesigned. Automation encoded the exceptions, the re-keying and the four-way reconciliation, and made them permanent.</p>
<h2>Build the digital twin first</h2>
<p>Our Smart Ops method begins with a digital twin of the operation: a structured, living model of every process, control and risk in scope. It is an enterprise process management tool rather than a Visio diagram, and it tells you where the value-destroying activity actually sits.</p>
<p>What it reveals is consistent. Between a third and a half of the effort in a typical GCC bank back office is rework, waiting, duplicate control or manual transfer between systems. None of that should be automated. It should be removed.</p>
<h2>Lean, then digitise</h2>
<p>Only when the process has been simplified do we apply automation, and at that point the economics change entirely. The automation footprint is smaller, the bots are simpler, and each one delivers a measurable return because it is doing work that has to be done rather than work that should never have existed.</p>
<p>In a global bank's credit operations this sequence took twenty-five million dollars of cost out of the process and released capital on the balance sheet, largely through redesign. The automation that followed was the easy part.</p>
<h2>Pods, not programmes</h2>
<p>The delivery model matters as much as the sequence. We run cross-functional pods of process engineers, developers and change agents against a single value stream, in sprints with measurable weekly outcomes. Quick fixes are deployed in weeks. The traditional twelve-month programme, with its design phase and its big-bang go-live, is the enemy of this kind of return.</p>
<p>The question to ask of any automation business case is simple: has the process been redesigned, and can I see the digital twin? If the answer is no, you are about to digitise the mess.</p>
""",
        "related": ["agentic-ai-bank-operations", "cost-to-income-levers"],
    },
    {
        "slug": "ifrs-s1-s2-gcc-banks",
        "cat": "Risk & ESG",
        "date": "2026-08-05",
        "read": 6,
        "photo": "ins-ifrs-s1-s2-gcc-banks", "pos": "center",
        "title": "IFRS S1 and S2 are here. Most GCC sustainability data is not ready.",
        "dek": "Sustainability reporting has moved from the communications team to the audit committee. The institutions that treat it as a data and control problem will be the ones that sleep at night.",
        "quote": "If your ESG number lives in a spreadsheet, it is an opinion, not a disclosure.",
        "body": """
<p>For most of the last decade, sustainability reporting in the Gulf was a narrative exercise. A glossy report, a set of commitments and some carefully chosen metrics, produced annually by a small team with a large spreadsheet. That era has ended.</p>
<p>IFRS S1 and S2 set the expectation that sustainability-related financial disclosures are prepared with the same rigour as the financial statements they sit beside. UAE Decree-Law No. 11 and national agendas in Saudi Arabia and Qatar reinforce the direction. Regulators, auditors and increasingly investors expect the numbers to be traceable, controlled and repeatable.</p>
<h2>The data problem underneath the reporting problem</h2>
<p>When we look inside a large regional bank's ESG process, the pattern is familiar. Dozens of business units submit data by email. A central team consolidates it manually. Definitions differ between submitters. Nobody can reproduce last year's number from first principles, and the audit trail is a folder of versions.</p>
<p>At one large UAE bank this consumed thousands of hours a year and produced disclosures that the finance function was uncomfortable signing. Replacing the manual collection with an automated pipeline and real-time dashboards, mapped to IFRS S1 and S2 and to Decree-Law No. 11, cut processing time by seventy percent and saved more than 1,200 hours annually. More importantly, every number now has a lineage.</p>
<h2>Treat it like financial reporting, because it is</h2>
<p>The institutions handling this well have done four things. They have appointed a data owner for every disclosed metric. They have written a control framework for the ESG close that mirrors the financial close. They have automated collection and calculation so that the annual scramble becomes a monthly routine. And they have run a dry-run audit before the real one.</p>
<h2>Financed emissions will be the hard part</h2>
<p>Scope 3, and in particular financed emissions across the lending and investment book, is where the data is thinnest and the methodology is still settling. Banks that start building counterparty-level data now will have a defensible number in two years. Those that wait will be estimating under pressure.</p>
<p>The practical advice is unfashionable: fix the data and the controls before worrying about the narrative. The report writes itself when the numbers are right.</p>
""",
        "related": ["operational-resilience-tprm", "lean-before-automation"],
    },
    {
        "slug": "post-merger-day-one",
        "cat": "M&A integration",
        "date": "2026-07-22",
        "read": 7,
        "photo": "ins-post-merger-day-one", "pos": "center",
        "title": "Day one is not the finish line: lessons from GCC bank integrations",
        "dek": "The region has seen a wave of consolidation. The integrations that created value shared a small number of habits, and they were all in place long before legal day.",
        "quote": "Legal day is a date. Integration is a decision you take every week for two years.",
        "body": """
<p>Consolidation in GCC financial services has accelerated: bank mergers in Saudi Arabia and the UAE, the combination of capital-markets businesses, and the folding of asset management, brokerage and wealth units into single groups. The announcements make headlines. The integrations decide whether the value in the announcement is ever realised.</p>
<p>Having led integrations of the Kingdom's largest lenders and a four-business consolidation with more than 200,000 customers and no day-one disruption, we have a clear view of what separates the successful ones.</p>
<h2>Decide the operating model before the deal closes</h2>
<p>The integrations that stall are the ones that treat the target operating model as a post-closing activity. By then, every function has a view, every system has an advocate and the synergy case is already being renegotiated. The successful ones decide the model, the leadership and the platform choices during the pre-closing window, so that day one is the start of execution rather than the start of debate.</p>
<h2>Run legal day like a launch</h2>
<p>Legal-day readiness is a function-by-function checklist, rehearsed. Customer migration is planned to the account. A command centre runs the weekend. Regulators are briefed before they ask. When one of our clients completed a 205-million-dollar multi-business integration with zero customer disruption, it was because every one of those things had been done twice before the real day.</p>
<h2>Track synergies like revenue</h2>
<p>People synergies are the most sensitive and the most frequently overstated. For a non-bank financial institution merger we built a role-by-role model across three scenarios that validated SAR 4.75 million of annual savings with a six-to-twelve-month payback. It secured Board and SAMA approval because it was bottom-up and it named the capability that would be retained, not just the cost that would go.</p>
<h2>Keep the customers you paid for</h2>
<p>Attrition in the twelve months after a merger is the silent synergy killer. The banks that protect their franchise over-invest in front-line communication, keep relationship managers stable through the transition and measure customer sentiment weekly. It is cheaper than winning the customers back.</p>
<p>Integration is a two-year discipline that starts before signature. Treat day one as the midpoint and the value case has a chance.</p>
""",
        "related": ["strategy-execution-gap", "saudization-workforce-transition"],
    },
    {
        "slug": "saudization-workforce-transition",
        "cat": "Human capital",
        "date": "2026-07-08",
        "read": 5,
        "photo": "ins-saudization-workforce-transition", "pos": "center",
        "title": "Saudization as strategy: building national capability that competes",
        "dek": "Nationalisation targets are treated as compliance in too many institutions. The leaders are using them to build a workforce advantage their competitors cannot buy.",
        "quote": "A nationalisation target met by relabelling roles is a liability. One met by building capability is a moat.",
        "body": """
<p>Nitaqat in Saudi Arabia, Emiratisation targets in the UAE and equivalent programmes across the Gulf have been part of the operating environment for years. Most financial institutions meet them. Far fewer treat them as the strategic lever they are.</p>
<p>The difference shows up in the numbers. Institutions that approach nationalisation as a quota fill roles and watch attrition erode the ratio. Those that approach it as capability building end up with a workforce that is younger, more digitally native and more committed than the expatriate-heavy model it replaced.</p>
<h2>Start from the skills the strategy needs</h2>
<p>The mistake is to start from the ratio. The better starting point is the target operating model: which capabilities does the bank need in three years, in data, risk, digital product and client coverage? A skills gap analysis against that model tells you where national talent can be developed, where it must be hired and where the role itself should be redesigned.</p>
<h2>Design the pathway, not just the hire</h2>
<p>A graduate programme that feeds people into roles with no progression is a retention problem waiting to happen. The institutions doing this well design multi-year pathways with rotations, certification and visible sponsorship from the executive committee. They measure time-to-competence, not just headcount.</p>
<h2>Handle transition with care</h2>
<p>Workforce transition in a merger or transformation is where nationalisation strategy meets its hardest test. Harmonisation logic, selection processes and the retention of critical expatriate knowledge during the handover have to be designed together. Done well, a transition accelerates the national talent agenda. Done badly, it costs capability the institution cannot replace.</p>
<h2>The measure that matters</h2>
<p>Track the share of leadership roles held by nationals who were developed internally. It is the only number that tells you whether the programme is building capability or counting heads.</p>
""",
        "related": ["post-merger-day-one", "strategy-execution-gap"],
    },
    {
        "slug": "agentic-ai-bank-operations",
        "cat": "AI & Digital",
        "date": "2026-06-24",
        "read": 8,
        "photo": "ins-agentic-ai-bank-operations", "pos": "center",
        "title": "Agentic AI in bank operations: where the value actually lands",
        "dek": "Beyond the demos, a small number of use cases are delivering hard returns in regional banks. They share three characteristics, and none of them is the sophistication of the model.",
        "quote": "The winning question is not what the agent can do. It is which process has a baseline, an owner and a regulator who will accept the answer.",
        "body": """
<p>Agentic AI, systems that can plan, act across tools and complete multi-step work with limited supervision, has moved from research into the operating plans of every major bank in the region. The demonstrations are impressive. The production results are more uneven, and the pattern of where they succeed is instructive.</p>
<h2>Where it is working</h2>
<p><strong>KYC refresh and onboarding.</strong> Document collection, extraction, screening and case assembly are high-volume, rule-heavy and already measured. Agents that assemble the case for a human decision are cutting cycle times from days to hours in banks that have redesigned the underlying process.</p>
<p><strong>Credit operations.</strong> Covenant monitoring, financial spreading and early-warning triage are natural fits. The work is repetitive, the data is structured and the value of speed is clear to the chief risk officer.</p>
<p><strong>Reconciliations and regulatory reporting.</strong> Break investigation and narrative drafting for returns are being handled by agents with a human sign-off, releasing analyst time that had been spent on assembly rather than judgement.</p>
<h2>Three conditions for a return</h2>
<p>First, a baseline. If the process has not been measured, the agent's impact cannot be evidenced and the programme will be judged on anecdote. Second, an owner. Somebody in the business, not in technology, has to own the outcome and the exceptions. Third, governance the regulator will accept. Model risk management, audit trails and explainability are not afterthoughts; SAMA, the CBUAE and the QCB will ask, and the answer has to exist.</p>
<h2>Where it is not working</h2>
<p>Agents deployed on processes that have never been redesigned. Agents in customer-facing roles where the tolerance for error is near zero and the brand risk is real. And programmes run by the technology function alone, without the operations leadership that knows where the exceptions live.</p>
<h2>A practical sequence</h2>
<p>Build the digital twin of the operation. Remove the waste. Pick the two processes with the clearest baseline and owner. Deploy agents with human-in-the-loop controls, measure weekly, and expand only when the return is banked. It is less exciting than the demo. It is also how the money gets made.</p>
""",
        "related": ["lean-before-automation", "open-finance-incumbents"],
    },
    {
        "slug": "cost-to-income-levers",
        "cat": "Cost optimisation",
        "date": "2026-06-10",
        "read": 6,
        "photo": "ins-cost-to-income-levers", "pos": "center",
        "title": "Cost-to-income: the five levers that actually move the ratio",
        "dek": "Regional banks announce cost programmes with a percentage target and a deadline. The ones that hit it work lever by lever, with an owner and a baseline for each.",
        "quote": "A cost target without a lever is a press release.",
        "body": """
<p>Cost-to-income has become the metric by which GCC bank management is judged, and the region's leaders now compete with the most efficient banks in the world. But the ratio is an outcome, not a lever, and programmes that target it directly tend to deliver a round of hiring freezes and travel bans followed by a quiet return to trend.</p>
<p>The banks that move the ratio durably decompose it. In our experience five levers account for most of the movement.</p>
<h2>1. Operations productivity</h2>
<p>Front-to-back process redesign in the highest-volume operations. In a global bank's credit process this was worth twenty-five million dollars, delivered through Lean redesign before any technology was applied. In most GCC banks the equivalent opportunity sits in onboarding, payments operations and credit administration.</p>
<h2>2. Technology run cost</h2>
<p>Application rationalisation, infrastructure consolidation and, above all, the renegotiation of the three or four contracts that dominate the technology bill. Cloud migration reduces cost only if the legacy estate is actually retired.</p>
<h2>3. Third-party spend</h2>
<p>Often the largest addressable pool and the least governed. Category strategies, demand management and disciplined renegotiation routinely yield ten to fifteen percent of addressable spend, and the saving sticks only if the governance stays.</p>
<h2>4. Distribution footprint</h2>
<p>Branch networks sized for a customer base that now transacts digitally. The lever is real but politically difficult, and it works best when paired with a digital proposition that gives customers a better alternative rather than simply removing the old one.</p>
<h2>5. The denominator</h2>
<p>Income. Pricing discipline, fee leakage, product profitability and the removal of unprofitable complexity move the ratio as surely as cost does, and they are frequently ignored because they belong to a different executive.</p>
<h2>Make each lever somebody's job</h2>
<p>Each lever needs an accountable owner, a baseline measured to the basis point and a monthly tracking cadence that reports to the executive committee. Capital matters too: redesigning credit processes released 150 million dollars of capital for one client through RWA optimisation, a benefit no cost programme would have found.</p>
""",
        "related": ["lean-before-automation", "pricing-fastest-revenue-lever"],
    },
    {
        "slug": "open-finance-incumbents",
        "cat": "AI & Digital",
        "date": "2026-05-27",
        "read": 6,
        "photo": "ins-open-finance-incumbents", "pos": "center",
        "title": "Open finance in the Gulf: compliance obligation or distribution strategy?",
        "dek": "SAMA's open banking framework and the CBUAE's open finance regulation give incumbents a choice. Most are choosing compliance. A few are choosing advantage.",
        "quote": "The API you expose to satisfy the regulator is the same API a competitor will use to reach your customers.",
        "body": """
<p>Open banking arrived in the Gulf later than in Europe, and it arrived with more ambition. SAMA's framework and the CBUAE's open finance regulation extend beyond payments and accounts into lending, insurance and investment data, and they set timelines that most institutions are now working to meet.</p>
<p>The prevailing response has been to treat the obligation as a technology project: expose the mandated APIs, pass the conformance tests, move on. That is a defensible minimum. It is also a strategic mistake.</p>
<h2>What incumbents actually have</h2>
<p>Regional banks hold something the challengers do not: deep, trusted relationships with customers who have complex needs, from family businesses to high-net-worth individuals to public-sector employees. Open finance lets those relationships be served through partners and platforms the bank does not own, at a cost of acquisition the branch model cannot match.</p>
<h2>Three strategic postures</h2>
<p><strong>Comply.</strong> Meet the regulation, protect the core, accept some erosion at the margins. Appropriate for institutions with other priorities, but it cedes the initiative.</p>
<p><strong>Distribute.</strong> Use open APIs to embed the bank's products in the platforms where customers already are: property portals, employer payroll, e-commerce and super-apps. This is where the most immediate revenue sits.</p>
<p><strong>Orchestrate.</strong> Become the platform that aggregates a customer's financial life across institutions. Ambitious, expensive and only realistic for a handful of institutions with the brand and the technology to carry it.</p>
<h2>The governance that makes it possible</h2>
<p>Whichever posture is chosen, the enablers are the same: a partner model with clear commercial terms, consent and data governance that satisfies the regulator and the customer, an API product function that treats developers as customers, and a risk framework for third parties that goes beyond the annual questionnaire.</p>
<p>The banks that win the next decade of GCC retail and SME banking will be the ones that decided, early, that open finance was a distribution strategy. The regulation simply removed the excuse not to.</p>
""",
        "related": ["agentic-ai-bank-operations", "operational-resilience-tprm"],
    },
    {
        "slug": "operational-resilience-tprm",
        "cat": "Risk & ESG",
        "date": "2026-05-13",
        "read": 6,
        "photo": "ins-operational-resilience-tprm", "pos": "center",
        "title": "Operational resilience and third-party risk: the questionnaire is not a control",
        "dek": "As GCC regulators sharpen their expectations on resilience and outsourcing, the annual vendor questionnaire looks increasingly like a ritual. What good looks like is more demanding and more useful.",
        "quote": "You cannot outsource a process to a vendor and outsource the accountability with it.",
        "body": """
<p>The dependence of regional banks on third parties has grown faster than the frameworks that govern it. Core banking in the cloud, payments processed by fintech partners, KYC run on external platforms and entire operations functions delivered by outsourcers. Regulators across the Gulf have noticed, and their expectations on operational resilience and third-party risk management now go well beyond a signed contract and an annual questionnaire.</p>
<h2>Start from the services that matter</h2>
<p>Operational resilience frameworks begin with the identification of important business services: the handful of things the bank does that, if disrupted, would harm customers, the market or the institution's safety. Payments, access to accounts, trade settlement. Each has an impact tolerance, and each is mapped end to end across people, processes, technology and third parties.</p>
<p>This mapping is where most institutions discover how concentrated their dependencies are. Three vendors underpin ten services. One data centre sits behind half of them. The map is uncomfortable, which is why it is valuable.</p>
<h2>Third-party risk as a lifecycle</h2>
<p>Effective third-party risk management runs across the lifecycle: risk-tiered due diligence before contracting, contractual rights to audit, data and exit, ongoing monitoring proportionate to the tier, scenario testing for the critical few and a tested exit plan for each of them. The questionnaire is one input to one stage. It is not the control.</p>
<h2>Test it, then test it again</h2>
<p>Severe-but-plausible scenario testing is the discipline that separates a framework on paper from resilience in practice. Simulate the loss of the payments processor for forty-eight hours. Walk through the exit from the cloud provider. The gaps found in a rehearsal are cheap; the same gaps found during an outage are not.</p>
<h2>Make it useful to the business</h2>
<p>Resilience done well is not only a regulatory response. The service map becomes the basis for investment decisions, the vendor tiering informs procurement, and the scenario tests surface simplification opportunities that reduce cost. A control function that produces business insight earns its seat at the table.</p>
""",
        "related": ["ifrs-s1-s2-gcc-banks", "open-finance-incumbents"],
    },
    {
        "slug": "pricing-fastest-revenue-lever",
        "cat": "Marketing & Growth",
        "date": "2026-04-15",
        "read": 5,
        "photo": "ins-pricing-fastest-revenue-lever", "pos": "center",
        "title": "Pricing is the fastest revenue lever most GCC banks never pull deliberately",
        "dek": "Fee structures set years ago, rate cards that follow the competitor and bundles nobody has costed. A disciplined pricing study routinely finds revenue that costs nothing to deliver.",
        "quote": "Every bank has a pricing strategy. Most of them are just unaware of what it is.",
        "body": """
<p>When management teams look for revenue, they reach for growth: new segments, new products, new markets. Each takes years and capital. Pricing takes a quarter and a decision, and in most regional financial institutions it has not been examined systematically in a decade.</p>
<h2>Where the value leaks</h2>
<p>Fee waivers granted by relationship managers and never reviewed. Legacy tariffs on products that have been superseded. Bundles priced on instinct rather than the cost to serve. Rate cards that track the largest competitor regardless of the bank's own cost of funds or risk appetite. Each is small. Together they are frequently worth several percent of non-interest income.</p>
<h2>What a pricing study does</h2>
<p>A disciplined study starts from customer value and willingness to pay, segment by segment, and sets it against the cost to serve and competitor benchmarks. It quantifies fee leakage. It tests price elasticity where the data allows. And it produces a redesigned tariff and a governance process for exceptions, so that the discipline survives the study.</p>
<h2>Proposition first, then price</h2>
<p>Pricing cannot be separated from proposition. A digital-only offering that onboards a customer in minutes can command a different fee structure from a branch-served account, and customers will accept it if the value is visible. When we helped a local bank launch its digital proposition, pricing and product were designed together, and the cost-to-income impact was tracked from launch.</p>
<h2>The governance that keeps the gain</h2>
<p>Pricing gains erode unless somebody owns them. A pricing committee, an exceptions policy with limits by role and a quarterly review of waivers are unglamorous but essential. The revenue recovered in the first year is the easy part. Keeping it is the discipline.</p>
""",
        "related": ["cost-to-income-levers", "open-finance-incumbents"],
    },
]

# ---------------------------------------------------------------------------
# WHITEPAPERS (gated PDFs in public/whitepapers/)
# ---------------------------------------------------------------------------
WHITEPAPERS = [
    {
        "slug": "closing-the-execution-gap",
        "photo": "svc-transformation", "pos": "center",
        "title": "Closing the <em>execution</em> gap",
        "plain": "Closing the execution gap",
        "series": "Point of view · 2026",
        "cat": "Transformation",
        "audience": "For chief executives",
        "dek": "Why execution certainty, not another strategy refresh, is the scarce asset on the GCC board agenda, and how a Transformation Management Office changes the physics of delivery.",
        "stat": ("Top 5", "Market positioning in KSA, six initiatives ahead of Board dates"),
        "pages": 4, "size": "1.8 MB",
        "insight": "strategy-execution-gap",
        "service": "transformation",
    },
    {
        "slug": "dont-digitise-the-mess",
        "photo": "svc-digital", "pos": "center",
        "title": "Don't digitise the <em>mess</em>",
        "plain": "Don't digitise the mess",
        "series": "Point of view · 2026",
        "cat": "Smart Ops",
        "audience": "For operations and technology leaders",
        "dek": "Why the sequencing of Lean and automation decides whether the digital budget compounds or evaporates, and a method that puts the process before the tool.",
        "stat": ("$25M", "Cost savings realised through front-to-back Lean before automation"),
        "pages": 4, "size": "1.9 MB",
        "insight": "lean-before-automation",
        "service": "digital",
    },
    {
        "slug": "disclosure-has-outgrown-the-spreadsheet",
        "photo": "svc-risk-esg", "pos": "center 40%",
        "title": "Disclosure has outgrown the <em>spreadsheet</em>",
        "plain": "Disclosure has outgrown the spreadsheet",
        "series": "Point of view · 2026",
        "cat": "Risk &amp; ESG",
        "audience": "For chief risk officers",
        "dek": "Why sustainability reporting now belongs to the risk function under IFRS S1/S2 and UAE Decree-Law No. 11, and the four phases to audit-ready disclosure.",
        "stat": ("70%", "Reduction in ESG processing time at a large UAE bank"),
        "pages": 4, "size": "1.7 MB",
        "insight": "ifrs-s1-s2-gcc-banks",
        "service": "risk-esg",
    },
    {
        "slug": "efficiency-is-the-new-margin",
        "photo": "svc-revenue-cost", "pos": "center 60%",
        "title": "Efficiency is the new <em>margin</em>",
        "plain": "Efficiency is the new margin",
        "series": "Point of view · Volume II · 2026",
        "cat": "Cost optimisation",
        "audience": "For finance and digital officers",
        "dek": "As GCC interest margins compress, the cost-to-income ratio becomes the margin you can control. Four levers on the ratio, with the evidence in numbers.",
        "stat": ("32.0%", "GCC average cost-to-income ratio, H1 2025"),
        "pages": 6, "size": "2.6 MB",
        "insight": "cost-to-income-levers",
        "service": "revenue-cost",
    },
    {
        "slug": "saudization-is-a-capability-strategy",
        "photo": "svc-human-capital", "pos": "center",
        "title": "Saudization is a <em>capability</em> strategy",
        "plain": "Saudization is a capability strategy",
        "series": "Point of view · Volume II · 2026",
        "cat": "Human capital",
        "audience": "For human capital leaders",
        "dek": "Why the institutions that treat nationalisation as workforce design will out-hire, out-retain and out-perform those that treat it as compliance.",
        "stat": ("SAR 4.75M", "Annual HR synergies validated by Board and SAMA"),
        "pages": 6, "size": "2.4 MB",
        "insight": "saudization-workforce-transition",
        "service": "human-capital",
    },
    {
        "slug": "the-first-hundred-days-decide-the-deal",
        "photo": "about-hero", "pos": "center",
        "title": "The first <em>hundred</em> days decide the deal",
        "plain": "The first hundred days decide the deal",
        "series": "Point of view · Volume II · 2026",
        "cat": "M&amp;A integration",
        "audience": "For chief executives and finance officers",
        "dek": "Why value is won or lost between signature and day one, what the integration record actually shows, and four disciplines of a clean integration.",
        "stat": ("Zero", "Customer disruption across a four-business, 200,000-customer integration"),
        "pages": 6, "size": "2.5 MB",
        "insight": "post-merger-day-one",
        "service": "transformation",
    },
]
