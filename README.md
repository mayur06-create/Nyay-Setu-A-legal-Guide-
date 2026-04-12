Every day, millions of Indians face situations where they desperately need legal help — a landlord illegally locking them out, a government office denying their rightful documents, a consumer being cheated, a worker not getting their dues.
But:

A lawyer costs ₹2,000–₹10,000 just for a consultation
Legal language is complex and intimidating
Most people don't know which law applies to their situation
Emergency helplines are scattered and hard to find
Hindi-speaking users are underserved by existing legal tools

NyaySetu bridges this gap. It's not a legal encyclopedia. It's a legal first-responder.

🚀 What is NyaySetu?
NyaySetu (न्यायसेतु — Bridge to Justice) is an AI-powered platform that gives everyday Indians the tools to understand their rights and take immediate, informed action — without needing to hire a lawyer first.
It combines AI case analysis, auto-generated legal documents, emergency resources, and bilingual support into a single, accessible interface.

✨ Key Features
🤖 AI Case Analysis
Describe your situation in plain language (Hindi or English). NyaySetu's AI identifies:

Which laws and rights apply to your case
What your immediate options are
What evidence you should collect
Whether your case has merit for escalation

📄 RTI Generator
Automatically drafts Right to Information (RTI) applications ready to file. Just answer a few questions about what information you need and from which government body — NyaySetu handles the legal formatting.
📬 Legal Notice Generator
Generate legally sound notices for common situations:

Consumer complaints
Landlord–tenant disputes
Employer dues and wrongful termination
Deficiency of services

🆘 Emergency Helplines
A curated, categorized directory of legal emergency contacts:

National Legal Services Authority (NALSA)
Women's helplines and domestic violence support
Consumer courts
Cybercrime reporting
Labour department contacts
State-wise legal aid numbers

🇮🇳 Hindi-First Design
Full support for Hindi input and output. Because justice shouldn't require you to think in a second language.

🏗️ Tech Stack
LayerTechnologyFrontendReact.js / Next.jsAI EngineClaude API (Anthropic)BackendNode.js / ExpressDatabasePostgreSQLDeploymentVercel / RailwayLanguage Supporti18n (Hindi + English)

nyaysetu/
├── client/                  # Frontend (React/Next.js)
│   ├── components/
│   │   ├── CaseAnalyzer/    # AI-powered case input & analysis
│   │   ├── RTIGenerator/    # RTI form and document output
│   │   ├── LegalNotice/     # Notice generation wizard
│   │   └── Helplines/       # Emergency contact directory
│   ├── pages/
│   └── locales/             # Hindi & English translations
├── server/                  # Backend (Node.js/Express)
│   ├── routes/
│   ├── services/
│   │   ├── aiAnalysis.js    # AI case analysis logic
│   │   ├── documentGen.js   # RTI & notice generation
│   │   └── helplines.js     # Helpline data service
│   └── prompts/             # Curated legal AI prompts
├── data/
│   ├── helplines.json       # Emergency contacts database
│   └── legal-templates/     # RTI & notice templates
└── docs/                    # Documentation
