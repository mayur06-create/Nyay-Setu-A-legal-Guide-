import re

with open('news.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update title
content = content.replace('<title>Legal Guide | Nyay Setu</title>', '<title>News | Nyay Setu</title>')

# Update navbar
nav_old = """                <div class="nav-links">
                    <a href="#">Explore Issues</a>
                    <a href="#" class="active">Guide</a>
                    <a href="#">Directory</a>
                    <a href="#">News</a>
                    <a href="#">RTI Generator</a>
                    <a href="#">AI Analysis</a>
                </div>"""
nav_new = """                <div class="nav-links">
                    <a href="#">Explore Issues</a>
                    <a href="index.html">Guide</a>
                    <a href="directory.html">Directory</a>
                    <a href="news.html" class="active">News</a>
                    <a href="#">RTI Generator</a>
                    <a href="#">AI Analysis</a>
                </div>"""
content = content.replace(nav_old, nav_new)

# Add new styles
style_insertion = """        /* News Specific Styles */
        .news-header {
            text-align: center;
            padding: 5rem 20px 2rem;
            animation: fadeIn 0.8s ease-out;
        }
        .news-header h1 {
            font-family: var(--font-heading);
            font-size: clamp(2.5rem, 5vw, 4rem);
            font-weight: 400;
            color: var(--text-primary);
            margin-bottom: 1rem;
            line-height: 1.1;
            letter-spacing: -0.02em;
        }
        .news-header p {
            color: var(--text-secondary);
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }
        .news-last-updated {
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-top: 2rem;
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 0.5rem;
        }
        .news-cards-top {
            display: grid;
            grid-template-columns: 1fr;
            gap: 24px;
            margin: 3rem 0;
        }
        @media (min-width: 768px) {
            .news-cards-top {
                grid-template-columns: repeat(3, 1fr);
            }
        }
        .news-card-simple {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            padding: 24px;
            display: flex;
            flex-direction: column;
        }
        .news-card-simple .meta {
            font-size: 0.7rem;
            font-weight: 700;
            color: var(--primary-accent);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }
        .news-card-simple h3 {
            font-family: var(--font-heading);
            font-size: 1.15rem;
            font-weight: 500;
            color: var(--text-primary);
            margin-bottom: 2rem;
            line-height: 1.4;
            flex-grow: 1;
        }
        .news-card-simple .footer {
            font-size: 0.7rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .scam-section {
            margin-bottom: 3rem;
            padding-top: 1rem;
        }
        .scam-title {
            font-size: 0.85rem;
            font-weight: 600;
            color: #8C6A5D;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 1.5rem;
        }
        .scam-banner {
            background-color: var(--primary-hover);
            padding: 1.5rem 2rem;
            margin-bottom: 1rem;
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        @media (min-width: 768px) {
            .scam-banner {
                flex-direction: row;
                justify-content: space-between;
                align-items: center;
            }
        }
        .scam-banner-content {
            flex-grow: 1;
        }
        .scam-banner-content h3 {
            font-family: var(--font-heading);
            font-size: 1.25rem;
            font-weight: 500;
            color: #2C2A29;
            margin-bottom: 0.5rem;
        }
        .scam-banner-content p {
            font-size: 0.95rem;
            color: #2C2A29;
            opacity: 0.8;
            font-weight: 500;
        }
        .scam-banner-btn {
            background-color: var(--btn-cream);
            color: #4B1E26;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            padding: 0.75rem 1.5rem;
            border-radius: 2px;
            white-space: nowrap;
        }
        .scam-banner-btn:hover {
            background-color: #DBC3A4;
        }

        .news-tabs {
            display: flex;
            justify-content: center;
            gap: 2rem;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 3rem;
            flex-wrap: wrap;
        }
        .news-tab {
            padding: 1rem 0;
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            border-bottom: 2px solid transparent;
            cursor: pointer;
            transition: color 0.2s, border-color 0.2s;
        }
        .news-tab:hover, .news-tab.active {
            color: var(--primary-accent);
            border-bottom-color: var(--primary-accent);
        }

        .news-list {
            margin-bottom: 4rem;
        }
        .news-list-item {
            border-bottom: 1px solid var(--border-color);
            padding: 2.5rem 0;
            display: flex;
            flex-direction: column;
        }
        .news-list-meta {
            display: flex;
            justify-content: space-between;
            font-size: 0.75rem;
            font-weight: 700;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }
        .news-list-meta .category {
            color: var(--primary-accent);
        }
        .news-list-title {
            font-family: var(--font-heading);
            font-size: 1.5rem;
            font-weight: 500;
            color: var(--text-primary);
            margin-bottom: 1rem;
            max-width: 800px;
        }
        .news-list-desc {
            color: var(--text-primary);
            font-size: 1rem;
            margin-bottom: 2.5rem;
            max-width: 800px;
        }
        .news-list-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 0.8rem;
            font-weight: 600;
            color: var(--text-secondary);
            border-top: 1px dashed var(--border-color);
            padding-top: 1rem;
        }
        .news-list-source span {
            color: var(--primary-accent);
            font-weight: 700;
        }
        .news-list-link {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--primary-accent);
            text-transform: uppercase;
            letter-spacing: 0.1em;
            transition: transform 0.2s;
        }
        .news-list-link:hover {
            transform: translateX(4px);
        }
        .news-list-link svg {
            width: 20px;
            height: 20px;
            stroke-width: 2.5;
        }
    </style>"""

content = content.replace('    </style>', style_insertion)

main_content = """    <!-- Main News Section -->
    <main class="container" style="padding-bottom: 6rem;">
        
        <!-- Header -->
        <header class="news-header">
            <h1>Legal News & Alerts</h1>
            <p>Stay aware. Scam alerts, landmark cases, policy changes, and what they mean for you.</p>
            <div class="news-last-updated">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
                LAST UPDATED: 10:36:04 PM
            </div>
        </header>

        <!-- Top Cards -->
        <div class="news-cards-top">
            <div class="news-card-simple">
                <div class="meta">SCAM ALERTS</div>
                <h3>Why your UPI payments will feel different from April 2026 - ET Edge Insights</h3>
                <div class="footer">NEWS SOURCE • MARCH 31, 2026</div>
            </div>
            <div class="news-card-simple">
                <div class="meta">SCAM ALERTS</div>
                <h3>UPI fraud is surging. Here's how fintechs and regulators are fighting back - MSN</h3>
                <div class="footer">NEWS SOURCE • MARCH 28, 2026</div>
            </div>
            <div class="news-card-simple">
                <div class="meta">SCAM ALERTS</div>
                <h3>LPG Cylinder Scam India 2026: Fake Bharat Gas, Indane, HP Gas Links, APK Malware & UPI Fraud | TraceX...</h3>
                <div class="footer">NEWS SOURCE • MARCH 21, 2026</div>
            </div>
        </div>

        <!-- Scam Banners -->
        <div class="scam-section">
            <div class="scam-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                ACTIVE SCAM ALERTS
            </div>
            
            <div class="scam-banner">
                <div class="scam-banner-content">
                    <h3>Why your UPI payments will feel different from April 2026 - ET Edge Insights</h3>
                    <p>Why your UPI payments will feel different from April 2026 ET Edge Insights</p>
                </div>
                <button class="scam-banner-btn">READ ADVISORY</button>
            </div>
            <div class="scam-banner">
                <div class="scam-banner-content">
                    <h3>UPI fraud is surging. Here's how fintechs and regulators are fighting back - MSN</h3>
                    <p>UPI fraud is surging. Here's how fintechs and regulators are fighting back MSN</p>
                </div>
                <button class="scam-banner-btn">READ ADVISORY</button>
            </div>
            <div class="scam-banner">
                <div class="scam-banner-content">
                    <h3>LPG Cylinder Scam India 2026: Fake Bharat Gas, Indane, HP Gas Links, APK Malware & UPI Fraud | TraceX Labs - First India</h3>
                    <p>LPG Cylinder Scam India 2026: Fake Bharat Gas, Indane, HP Gas Links, APK Malware & UPI Fraud | TraceX Labs First India</p>
                </div>
                <button class="scam-banner-btn">READ ADVISORY</button>
            </div>
        </div>

        <!-- Tabs -->
        <div class="news-tabs">
            <div class="news-tab active">ALL</div>
            <div class="news-tab">SCAM ALERTS</div>
            <div class="news-tab">COURT DECISIONS</div>
            <div class="news-tab">POLICY CHANGES</div>
            <div class="news-tab">CONSUMER WARNINGS</div>
            <div class="news-tab">AWARENESS</div>
            <div class="news-tab">CRIME & SAFETY</div>
        </div>

        <!-- List -->
        <div class="news-list">
            <div class="news-list-item">
                <div class="news-list-meta">
                    <span class="category">SCAM ALERTS</span>
                    <span>MARCH 31, 2026</span>
                </div>
                <h3 class="news-list-title">Why your UPI payments will feel different from April 2026 - ET Edge Insights</h3>
                <p class="news-list-desc">Why your UPI payments will feel different from April 2026 ET Edge Insights</p>
                <div class="news-list-footer">
                    <div class="news-list-source">Source: <span>News Source</span></div>
                    <a href="#" class="news-list-link">
                        ORIGINAL ARTICLE 
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                    </a>
                </div>
            </div>
            
            <div class="news-list-item">
                <div class="news-list-meta">
                    <span class="category">SCAM ALERTS</span>
                    <span>MARCH 28, 2026</span>
                </div>
                <h3 class="news-list-title">UPI fraud is surging. Here's how fintechs and regulators are fighting back - MSN</h3>
                <p class="news-list-desc">UPI fraud is surging. Here's how fintechs and regulators are fighting back MSN</p>
                <div class="news-list-footer">
                    <div class="news-list-source">Source: <span>News Source</span></div>
                    <a href="#" class="news-list-link">
                        ORIGINAL ARTICLE 
                        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
                    </a>
                </div>
            </div>
        </div>

    </main>
"""

# Extract the body from index.html that needs to be replaced.
# It starts at `<header class="hero">` and ends at `<div class="load-more-section"> ... </div>` inclusive.
start_idx = content.find('<!-- Hero Section -->')
end_idx = content.find('<!-- Newsletter Section -->')

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + main_content + content[end_idx:]
else:
    print("Could not find replacement bounds")

# Update script to not throw errors for missing elements
script_old = "renderFeatured();"
script_new = "// renderFeatured();"
content = content.replace(script_old, script_new)
content = content.replace("renderGrid();", "// renderGrid();")
content = content.replace("setupScrollAnimations();", "setTimeout(() => { if(document.querySelector('.article-card')) setupScrollAnimations(); }, 50);")

with open('news.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("success")
