import re

def main():
    css_content = """
        /* Dashboard Layout Styles */
        .dashboard-layout {
            display: flex;
            max-width: 1400px;
            margin: 0 auto;
            background-color: var(--bg-color);
            border-top: 1px solid var(--border-color);
        }
        .sidebar {
            width: 320px;
            background-color: #FFFFFF;
            border-right: 1px solid var(--border-color);
            padding: 2rem 0;
            min-height: calc(100vh - 90px);
            flex-shrink: 0;
        }
        .sidebar-title {
            display: flex;
            align-items: center;
            gap: 12px;
            padding: 0 24px;
            font-size: 1.1rem;
            font-family: var(--font-heading);
            color: var(--primary-accent);
            margin-bottom: 1.5rem;
        }
        .sidebar-nav {
            display: flex;
            flex-direction: column;
        }
        .sidebar-item {
            padding: 1.25rem 24px;
            display: flex;
            align-items: flex-start;
            gap: 16px;
            color: var(--text-secondary);
            border-bottom: 1px solid rgba(229, 224, 216, 0.4);
            transition: all 0.2s ease;
            cursor: pointer;
            text-decoration: none;
        }
        .sidebar-item:hover {
            background-color: rgba(97, 33, 43, 0.02);
        }
        .sidebar-item.active {
            background-color: #EBDAC2;
            border-left: 4px solid var(--primary-accent);
            color: var(--text-primary);
        }
        .sidebar-item-icon {
            margin-top: 2px;
            width: 20px;
            height: 20px;
            stroke-width: 1.5;
        }
        .sidebar-item.active .sidebar-item-icon {
            color: var(--primary-accent);
        }
        .sidebar-item-titles {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }
        .sidebar-item-name {
            font-family: var(--font-heading);
            font-size: 1.1rem;
            font-weight: 500;
        }
        .sidebar-item-sub {
            font-size: 0.7rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 600;
            line-height: 1.4;
            color: #9B8B88;
        }
        .sidebar-item.active .sidebar-item-sub {
            color: var(--primary-hover);
        }

        .main-content {
            flex-grow: 1;
            padding: 4rem 4rem 6rem;
            max-width: 900px;
        }
        .issue-header h1 {
            font-family: var(--font-heading);
            font-size: clamp(3rem, 4vw, 4.5rem);
            font-weight: 400;
            color: var(--text-primary);
            margin-bottom: 1rem;
            line-height: 1.1;
        }
        .issue-header p {
            font-size: 1.15rem;
            color: var(--text-secondary);
            margin-bottom: 3rem;
        }

        .tabs-container {
            margin-bottom: 3rem;
        }
        .tabs-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: #A09B96;
            margin-bottom: 1rem;
            font-weight: 600;
        }
        .tabs-row {
            display: flex;
            gap: 1rem;
            overflow-x: auto;
            padding-bottom: 10px;
            scrollbar-width: none;
        }
        .tabs-row::-webkit-scrollbar {
            display: none;
        }
        .tab-card {
            min-width: 180px;
            padding: 24px;
            border-radius: var(--border-radius-sm);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            gap: 2rem;
            cursor: pointer;
            transition: all 0.2s ease;
            border: 1px solid transparent;
        }
        .tab-card.active {
            background-color: #4B1E28;
            color: white;
        }
        .tab-card.inactive {
            background-color: transparent;
            color: #A09B96;
        }
        .tab-card-title {
            font-family: var(--font-heading);
            font-weight: 500;
            font-size: 1.25rem;
            line-height: 1.2;
        }
        .tab-card-action {
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .divider {
            height: 1px;
            background-color: var(--border-color);
            margin: 3rem 0;
        }

        .legal-grounding {
            background-color: #F1F6F2;
            border: 1px solid #D7E8DA;
            border-radius: var(--border-radius-sm);
            padding: 24px 32px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 3rem;
            gap: 1rem;
            flex-wrap: wrap;
        }
        .legal-grounding-left {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        .legal-grounding-icon {
            width: 48px;
            height: 48px;
            background-color: #557859;
            color: white;
            border-radius: var(--border-radius-sm);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
        }
        .legal-grounding-title {
            font-family: var(--font-heading);
            font-size: 1.5rem;
            color: #2F4131;
            margin-bottom: 4px;
        }
        .legal-grounding-sub {
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #466348;
        }
        .legal-verified-chip {
            background-color: white;
            border: 1px solid #D7E8DA;
            padding: 8px 16px;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #466348;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .legal-verified-chip::before {
            content: '';
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background-color: #557859;
        }

        .law-section-title {
            display: flex;
            align-items: center;
            gap: 12px;
            font-family: var(--font-heading);
            font-size: 2rem;
            color: var(--text-primary);
            margin-bottom: 2rem;
        }
        .law-section-title span {
            font-family: var(--font-body);
            font-size: 1.15rem;
            color: var(--text-secondary);
            font-style: italic;
            font-weight: 400;
        }
        .law-cards-grid {
            display: grid;
            grid-template-columns: 1fr;
            gap: 1rem;
            margin-bottom: 2rem;
        }
        @media (min-width: 600px) {
            .law-cards-grid {
                grid-template-columns: 1fr 1fr;
            }
        }
        .law-card {
            background-color: white;
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-sm);
            padding: 24px;
            display: flex;
            gap: 16px;
        }
        .law-card svg {
            color: var(--primary-accent);
            flex-shrink: 0;
            margin-top: 2px;
        }
        .law-card p {
            font-size: 1rem;
            color: var(--text-primary);
            line-height: 1.5;
            font-weight: 500;
        }
        .show-original-btn {
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--primary-accent);
            display: flex;
            align-items: center;
            gap: 8px;
            background: none;
            border: none;
            cursor: pointer;
            margin-bottom: 4rem;
        }

        .action-plan-container {
            background-color: #4B1E28;
            border-radius: var(--border-radius-sm);
            color: white;
            padding: 3rem 4rem;
            margin-bottom: 4rem;
        }
        .action-plan-header {
            display: flex;
            align-items: center;
            gap: 12px;
            font-family: var(--font-heading);
            font-size: 2.25rem;
            margin-bottom: 3rem;
        }
        .action-plan-header svg {
            color: rgba(255,255,255,0.4);
        }
        .timeline {
            position: relative;
            padding-left: 20px;
            margin-bottom: 3rem;
        }
        .timeline::before {
            content: '';
            position: absolute;
            left: 35px;
            top: 20px;
            bottom: 20px;
            width: 1px;
            background-color: rgba(255,255,255,0.2);
        }
        .timeline-item {
            display: flex;
            gap: 2rem;
            margin-bottom: 3rem;
            position: relative;
            align-items: flex-start;
        }
        .timeline-item:last-child {
            margin-bottom: 0;
        }
        .timeline-number {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            background-color: #2D1117;
            border: 1px solid rgba(255,255,255,0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.85rem;
            font-weight: 700;
            z-index: 1;
            flex-shrink: 0;
        }
        .timeline-content {
            padding-top: 4px;
        }
        .timeline-content h4 {
            font-family: var(--font-heading);
            font-size: 1.25rem;
            font-weight: 400;
            margin-bottom: 8px;
        }
        .timeline-content p {
            font-size: 0.85rem;
            color: rgba(255,255,255,0.6);
        }
        .timeline-content .action-link {
            display: inline-block;
            margin-top: 12px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: #EBDAC2;
        }

        .action-warning {
            background-color: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            padding: 24px;
            border-radius: var(--border-radius-sm);
            display: flex;
            gap: 16px;
            align-items: center;
            margin-bottom: 4rem;
        }
        .action-warning svg {
            color: rgba(255,255,255,0.6);
            flex-shrink: 0;
        }
        .action-warning p {
            font-family: var(--font-heading);
            font-style: italic;
            font-size: 1.15rem;
            color: rgba(255,255,255,0.9);
        }

        .action-stats {
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            gap: 2rem;
            margin-bottom: 1rem;
        }
        .stat-item {
            display: flex;
            flex-direction: column;
        }
        .stat-label {
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: rgba(255,255,255,0.6);
            margin-bottom: 12px;
        }
        .stat-value {
            font-family: var(--font-heading);
            font-size: 2.5rem;
            margin-bottom: 8px;
            line-height: 1;
        }
        .stat-value.medium {
            font-size: 1.5rem;
            margin-top: 15px;
        }
        .stat-sub {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: rgba(255,255,255,0.5);
            margin-top: 10px;
        }

        .ai-lawyer-box {
            background-color: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: var(--border-radius-sm);
            padding: 24px 32px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            margin-top: 3rem;
        }
        .ai-lawyer-text h5 {
            font-size: 1.05rem;
            font-weight: 700;
            margin-bottom: 8px;
        }
        .ai-lawyer-text p {
            font-size: 0.95rem;
            color: rgba(255,255,255,0.7);
            max-width: 400px;
            line-height: 1.5;
        }
        .ai-lawyer-btn {
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: rgba(255,255,255,0.9);
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .action-buttons-row {
            display: flex;
            gap: 16px;
            align-items: center;
            flex-wrap: wrap;
        }
        .btn-solid {
            background-color: #EBDAC2;
            color: #2D1117;
            padding: 12px 20px;
            border-radius: var(--border-radius-sm);
            font-size: 0.85rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .btn-solid::after {
            content: '';
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background-color: #200B0F;
        }
        .btn-border {
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            padding: 12px 20px;
            border-radius: var(--border-radius-sm);
            font-size: 0.85rem;
            font-weight: 700;
        }
        .btn-text {
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: rgba(255,255,255,0.7);
            margin-left: 1rem;
        }

        .evidence-section-title {
            font-family: var(--font-heading);
            font-size: 2.25rem;
            margin-bottom: 2rem;
            color: var(--text-primary);
        }
        .evidence-card {
            background-color: white;
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius-sm);
            padding: 32px;
            min-height: 200px; /* Placeholder */
        }

        @media (max-width: 1024px) {
            .dashboard-layout {
                flex-direction: column;
            }
            .sidebar {
                width: 100%;
                border-right: none;
                border-bottom: 1px solid var(--border-color);
                min-height: auto;
            }
            .action-plan-container {
                padding: 2rem;
            }
            .main-content {
                padding: 2rem 20px 4rem;
            }
            .action-stats {
                grid-template-columns: 1fr;
            }
            .ai-lawyer-box {
                flex-direction: column;
                align-items: flex-start;
                gap: 1rem;
            }
        }
"""

    html_content = """
    <div class="dashboard-layout">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-title">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                Your Situation
            </div>
            <nav class="sidebar-nav">
                <a href="#" class="sidebar-item active">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><circle cx="9" cy="21" r="1"></circle><circle cx="20" cy="21" r="1"></circle><path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Consumer Rights</span>
                        <span class="sidebar-item-sub">DEFECTIVE PRODUCT? REFUND DENIED?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Workplace & Employment</span>
                        <span class="sidebar-item-sub">SALARY UNPAID? WRONGFUL TERMINATION?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><rect x="8" y="11" width="8" height="6" rx="1"></rect><path d="M10 11V9a2 2 0 0 1 4 0v2"></path></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Police & FIR</span>
                        <span class="sidebar-item-sub">POLICE REFUSING TO HELP? NEED TO FILE FIR?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Property & Real Estate</span>
                        <span class="sidebar-item-sub">BUILDER DELAY? FRAUD?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Family & Matrimonial</span>
                        <span class="sidebar-item-sub">DIVORCE? DOMESTIC VIOLENCE?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Cyber Crime & Online Fraud</span>
                        <span class="sidebar-item-sub">ONLINE SCAM? IDENTITY THEFT?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Medical Negligence</span>
                        <span class="sidebar-item-sub">WRONG TREATMENT? OVERCHARGING?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="4" y="2" width="16" height="20" rx="2" ry="2"></rect><line x1="12" y1="18" x2="12" y2="22"></line><line x1="8" y1="6" x2="8" y2="6.01"></line><line x1="16" y1="6" x2="16" y2="6.01"></line></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Banking & Financial Fraud</span>
                        <span class="sidebar-item-sub">LOAN HARASSMENT? UNAUTHORIZED TX?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><line x1="12" y1="1" x2="12" y2="23"></line><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Government & Public Services</span>
                        <span class="sidebar-item-sub">PASSPORT DELAY? PENSION NOT RECEIVED?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><path d="M22 10v6M2 10l10-5 10 5-10 5z"></path><path d="M6 12v5c3 3 9 3 12 0v-5"></path></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Education & Student Rights</span>
                        <span class="sidebar-item-sub">FEE REFUND? ADMISSION FRAUD?</span>
                    </div>
                </a>
                <a href="#" class="sidebar-item">
                    <svg class="sidebar-item-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor"><rect x="2" y="10" width="20" height="8" rx="2" ry="2"></rect><path d="M4 10V6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v4"></path></svg>
                    <div class="sidebar-item-titles">
                        <span class="sidebar-item-name">Traffic & Motor Vehicle</span>
                        <span class="sidebar-item-sub">CHALLAN DISPUTES? ACCIDENT CLAIMS?</span>
                    </div>
                </a>
            </nav>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <header class="issue-header">
                <h1>Consumer Rights</h1>
                <p>Protect yourself against defective products and fraud.</p>
            </header>

            <div class="tabs-container">
                <div class="tabs-label">COMMON ISSUES IN THIS CATEGORY</div>
                <div class="tabs-row">
                    <div class="tab-card active">
                        <div class="tab-card-title">Defective product</div>
                        <div class="tab-card-action">VIEW DETAILS <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg></div>
                    </div>
                    <div class="tab-card inactive">
                        <div class="tab-card-title">Refund denied</div>
                        <div class="tab-card-action" style="color: #A09B96;">COMING SOON</div>
                    </div>
                    <div class="tab-card inactive">
                        <div class="tab-card-title">Misleading ads</div>
                        <div class="tab-card-action" style="color: #A09B96;">COMING SOON</div>
                    </div>
                    <div class="tab-card inactive">
                        <div class="tab-card-title">Service complaint</div>
                        <div class="tab-card-action" style="color: #A09B96;">COMING SOON</div>
                    </div>
                </div>
            </div>

            <div class="divider"></div>

            <div class="legal-grounding">
                <div class="legal-grounding-left">
                    <div class="legal-grounding-icon">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                    </div>
                    <div>
                        <div class="legal-grounding-title">Solid Legal Grounding</div>
                        <div class="legal-grounding-sub">YOU HAVE STRONG LEGAL RIGHTS IN THIS SITUATION</div>
                    </div>
                </div>
                <div class="legal-verified-chip">
                    VERIFIED BY AI LAWYER
                </div>
            </div>

            <h2 class="law-section-title">
                <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
                What the Law Says <span>— In Simple Words</span>
            </h2>

            <div class="law-cards-grid">
                <div class="law-card">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    <p>Sellers are legally bound to replace or refund defective goods.</p>
                </div>
                <div class="law-card">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    <p>'No Return/Refund' signs DO NOT override your statutory rights.</p>
                </div>
                <div class="law-card">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    <p>You can claim compensation for mental agony and legal costs.</p>
                </div>
                <div class="law-card">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    <p>E-commerce platforms are jointly liable for seller defaults.</p>
                </div>
            </div>

            <button class="show-original-btn">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg>
                SHOW ORIGINAL LAW TEXT
            </button>

            <!-- Action Plan -->
            <div class="action-plan-container">
                <div class="action-plan-header">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
                    Your Action Plan
                </div>
                
                <div class="timeline">
                    <div class="timeline-item">
                        <div class="timeline-number">1</div>
                        <div class="timeline-content">
                            <h4>Serve a written complaint/Legal Notice to the seller</h4>
                            <p>(deadline: 15 days to respond)</p>
                        </div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-number">2</div>
                        <div class="timeline-content">
                            <h4>File an online grievance via INGRAM (National Consumer Helpline)</h4>
                            <a href="#" class="action-link">NEXT MOVE: START NOW</a>
                        </div>
                    </div>
                    <div class="timeline-item">
                        <div class="timeline-number">3</div>
                        <div class="timeline-content">
                            <h4>File a consumer case at District Commission</h4>
                            <p>No lawyer required for claims under ₹5 Lakh.</p>
                        </div>
                    </div>
                </div>

                <div class="action-warning">
                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"></path><line x1="12" y1="9" x2="12" y2="13"></line><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
                    <p>"Consumer courts resolve 80% of defective product cases in favor of the consumer."</p>
                </div>

                <div class="divider" style="background-color: rgba(255,255,255,0.1); margin: 0 0 3rem 0;"></div>

                <div class="action-stats">
                    <div class="stat-item">
                        <div class="stat-label">SUCCESS ODDS</div>
                        <div class="stat-value">85%</div>
                        <div class="stat-label" style="color: #EBDAC2; margin-top: 0;">HIGH POTENTIAL</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">TIMELINE</div>
                        <div class="stat-value medium">3-6 months</div>
                    </div>
                    <div class="stat-item">
                        <div class="stat-label">EST. COST</div>
                        <div class="stat-value medium">₹0 - ₹200</div>
                    </div>
                </div>
                
                <div class="stat-sub">Based on E-Daakhil resolution statistics (2023)</div>

                <div class="ai-lawyer-box">
                    <div class="ai-lawyer-text">
                        <h5>Got a specific question?</h5>
                        <p>Our AI Lawyer can analyze your specific documents and situation instantly.</p>
                    </div>
                    <a href="#" class="ai-lawyer-btn" style="text-decoration: none;">
                        ASK OUR AI LAWYER 
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
                    </a>
                </div>

                <div class="action-buttons-row">
                    <button class="btn-solid">Generate Legal Notice</button>
                    <button class="btn-border">Consumer Complaint</button>
                    <a href="#" class="btn-text" style="text-decoration: none;">FIND LOCAL LAWYER →</a>
                </div>

            </div>

            <!-- Evidence Checklist -->
            <h2 class="evidence-section-title">Evidence Checklist</h2>
            <div class="evidence-card">
                <!-- Placeholder for now as it was cut off -->
                <p style="color: var(--text-secondary);">Your checklist items will appear here...</p>
            </div>
            
        </main>
    </div>
    """
    
    # Read the base template (we can use explore.html and rip out its <main>)
    with open('explore.html', 'r', encoding='utf-8') as f:
        full_html = f.read()

    # Change the title
    full_html = re.sub(r'<title>.*?</title>', '<title>Consumer Rights | Nyay Setu</title>', full_html)
    
    # Inject CSS
    full_html = full_html.replace('/* Floating Elements */', css_content + '\n        /* Floating Elements */')

    # Find the main body using regex again layout
    # from <!-- Explore Main --> up to <!-- Footer -->
    # WAIT, actually in explore.html we injected <!-- Hero Section -->...
    pattern = re.compile(r'<!-- Hero Section -->.*?<!-- Floating Elements -->', re.DOTALL)
    
    new_body_block = "<!-- Hero Section -->\n" + html_content + "\n    <!-- Floating Elements -->\n"
    
    full_html = pattern.sub(new_body_block, full_html)
    
    with open('consumer-rights.html', 'w', encoding='utf-8') as f:
        f.write(full_html)
        
    print("consumer-rights.html generated successfully!")

if __name__ == "__main__":
    main()
