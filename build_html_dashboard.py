import json
import os

def generate_html():
    json_path = os.path.join(os.path.dirname(__file__), "sih_2026_problem_statements_ascending.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Convert data to compact JSON string for embedding
    json_embedded = json.dumps(data, ensure_ascii=False)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SIH 2026 Problem Statement Explorer & Slot Tracker</title>
  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <style>
    :root {{
      --bg-dark: #080C14;
      --bg-card: #111827;
      --bg-card-hover: #172033;
      --bg-input: #1F293D;
      --border-color: rgba(255, 255, 255, 0.08);
      --border-focus: #3B82F6;
      
      --text-main: #F3F4F6;
      --text-muted: #9CA3AF;
      --text-dim: #64748B;
      
      --primary: #3B82F6;
      --primary-hover: #2563EB;
      --primary-glow: rgba(59, 130, 246, 0.2);
      
      --success: #10B981;
      --success-bg: rgba(16, 185, 129, 0.12);
      --warning: #F59E0B;
      --warning-bg: rgba(245, 158, 11, 0.12);
      --danger: #EF4444;
      --danger-bg: rgba(239, 68, 68, 0.12);
      --software: #06B6D4;
      --software-bg: rgba(6, 182, 212, 0.12);
      --hardware: #F97316;
      --hardware-bg: rgba(249, 115, 22, 0.12);
      --purple: #8B5CF6;
      
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
      --radius-full: 9999px;
      
      --shadow-sm: 0 2px 4px rgba(0,0,0,0.3);
      --shadow-md: 0 4px 12px rgba(0,0,0,0.4);
      --shadow-lg: 0 10px 30px rgba(0,0,0,0.6);
      --transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      min-height: 100vh;
      overflow-x: hidden;
      line-height: 1.5;
      background-image: 
        radial-gradient(ellipse 80% 50% at 50% -20%, rgba(59, 130, 246, 0.15), transparent),
        radial-gradient(ellipse 50% 30% at 85% 20%, rgba(139, 92, 246, 0.08), transparent);
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 8px;
      height: 8px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0B111E;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #25334E;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #3B82F6;
    }}

    .container {{
      max-width: 1440px;
      margin: 0 auto;
      padding: 1.5rem 2rem 4rem;
    }}

    /* Header */
    header {{
      padding: 1.5rem 0 2rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }}

    .header-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      flex-wrap: wrap;
      gap: 1.5rem;
    }}

    .brand-tag {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--primary);
      background: rgba(59, 130, 246, 0.1);
      border: 1px solid rgba(59, 130, 246, 0.25);
      padding: 0.35rem 0.85rem;
      border-radius: var(--radius-full);
      margin-bottom: 0.75rem;
    }}

    .live-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--success);
      box-shadow: 0 0 8px var(--success);
      animation: pulse 2s infinite;
    }}

    @keyframes pulse {{
      0% {{ transform: scale(0.95); opacity: 0.8; }}
      50% {{ transform: scale(1.2); opacity: 1; }}
      100% {{ transform: scale(0.95); opacity: 0.8; }}
    }}

    h1 {{
      font-family: 'Outfit', sans-serif;
      font-size: 2.35rem;
      font-weight: 800;
      letter-spacing: -0.025em;
      background: linear-gradient(135deg, #FFFFFF 20%, #93C5FD 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      margin-bottom: 0.4rem;
    }}

    .subtitle {{
      color: var(--text-muted);
      font-size: 0.95rem;
      max-width: 680px;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.65rem 1.1rem;
      font-size: 0.85rem;
      font-weight: 600;
      border-radius: var(--radius-md);
      cursor: pointer;
      transition: var(--transition);
      border: 1px solid transparent;
      font-family: inherit;
      text-decoration: none;
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #3B82F6, #2563EB);
      color: white;
      box-shadow: 0 4px 14px var(--primary-glow);
    }}
    .btn-primary:hover {{
      background: linear-gradient(135deg, #2563EB, #1D4ED8);
      transform: translateY(-1px);
    }}

    .btn-secondary {{
      background: #1E293B;
      color: var(--text-main);
      border-color: var(--border-color);
    }}
    .btn-secondary:hover {{
      background: #334155;
      border-color: rgba(255, 255, 255, 0.2);
    }}

    .btn-icon {{
      padding: 0.65rem;
    }}

    /* Metrics Ribbon */
    .metrics-ribbon {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 1rem;
      margin-top: 0.5rem;
    }}

    .metric-card {{
      background: linear-gradient(180deg, rgba(26, 36, 56, 0.6) 0%, rgba(17, 24, 39, 0.6) 100%);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.1rem 1.25rem;
      backdrop-filter: blur(10px);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      gap: 0.3rem;
    }}

    .metric-card::before {{
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: var(--card-accent, #3B82F6);
      opacity: 0.7;
    }}

    .metric-label {{
      font-size: 0.75rem;
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.05em;
      color: var(--text-dim);
    }}

    .metric-val {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.85rem;
      font-weight: 700;
      color: #FFF;
      line-height: 1.1;
    }}

    .metric-sub {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    /* Search & Filter Toolbar */
    .toolbar {{
      background: rgba(17, 24, 39, 0.85);
      backdrop-filter: blur(12px);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.25rem;
      margin: 1.75rem 0 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      box-shadow: var(--shadow-md);
      position: sticky;
      top: 1rem;
      z-index: 100;
    }}

    .search-row {{
      display: flex;
      gap: 1rem;
      align-items: center;
      flex-wrap: wrap;
    }}

    .search-box {{
      flex: 1;
      min-width: 280px;
      position: relative;
      display: flex;
      align-items: center;
    }}

    .search-icon {{
      position: absolute;
      left: 1rem;
      color: var(--text-dim);
      pointer-events: none;
    }}

    .search-input {{
      width: 100%;
      padding: 0.75rem 1rem 0.75rem 2.85rem;
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      color: #FFF;
      font-size: 0.95rem;
      font-family: inherit;
      transition: var(--transition);
    }}

    .search-input:focus {{
      outline: none;
      border-color: var(--border-focus);
      box-shadow: 0 0 0 3px var(--primary-glow);
    }}

    .search-clear {{
      position: absolute;
      right: 0.85rem;
      background: transparent;
      border: none;
      color: var(--text-dim);
      cursor: pointer;
      display: none;
      padding: 0.25rem;
    }}
    .search-clear:hover {{
      color: #FFF;
    }}

    .filter-row {{
      display: flex;
      gap: 0.75rem;
      align-items: center;
      flex-wrap: wrap;
      justify-content: space-between;
    }}

    .filter-group {{
      display: flex;
      gap: 0.6rem;
      align-items: center;
      flex-wrap: wrap;
    }}

    .select-wrap {{
      position: relative;
    }}

    .custom-select {{
      background: var(--bg-input);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.6rem 2.2rem 0.6rem 0.85rem;
      border-radius: var(--radius-md);
      font-size: 0.85rem;
      font-family: inherit;
      cursor: pointer;
      appearance: none;
      outline: none;
      transition: var(--transition);
      max-width: 200px;
      white-space: nowrap;
      text-overflow: ellipsis;
      overflow: hidden;
    }}

    .custom-select:focus {{
      border-color: var(--border-focus);
    }}

    .select-arrow {{
      position: absolute;
      right: 0.85rem;
      top: 50%;
      transform: translateY(-50%);
      pointer-events: none;
      color: var(--text-dim);
    }}

    /* Chip pills for status */
    .chip-pills {{
      display: flex;
      gap: 0.4rem;
      background: rgba(0, 0, 0, 0.25);
      padding: 0.3rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
    }}

    .chip-btn {{
      padding: 0.45rem 0.85rem;
      font-size: 0.8rem;
      font-weight: 600;
      border-radius: var(--radius-sm);
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }}

    .chip-btn:hover {{
      color: #FFF;
    }}

    .chip-btn.active {{
      background: #25334E;
      color: #FFF;
      box-shadow: var(--shadow-sm);
    }}

    .chip-btn.active.open-chip {{
      background: var(--success-bg);
      color: var(--success);
      border: 1px solid rgba(16, 185, 129, 0.3);
    }}

    .chip-btn.active.frozen-chip {{
      background: var(--danger-bg);
      color: var(--danger);
      border: 1px solid rgba(239, 68, 68, 0.3);
    }}

    .view-toggle {{
      display: flex;
      background: rgba(0, 0, 0, 0.25);
      padding: 0.3rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
    }}

    .view-btn {{
      padding: 0.45rem 0.65rem;
      background: transparent;
      border: none;
      color: var(--text-muted);
      border-radius: var(--radius-sm);
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .view-btn.active {{
      background: var(--primary);
      color: #FFF;
    }}

    /* Active filter count banner */
    .results-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.25rem;
      font-size: 0.85rem;
      color: var(--text-dim);
    }}

    .results-count b {{
      color: var(--text-main);
    }}

    /* Cards Grid View */
    .cards-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(420px, 1fr));
      gap: 1.25rem;
    }}

    .ps-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.35rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
      transition: var(--transition);
      position: relative;
      overflow: hidden;
      cursor: pointer;
    }}

    .ps-card:hover {{
      background: var(--bg-card-hover);
      border-color: rgba(255, 255, 255, 0.18);
      transform: translateY(-3px);
      box-shadow: var(--shadow-lg);
    }}

    .ps-card.is-frozen {{
      border-left: 4px solid var(--danger);
    }}
    .ps-card.is-open {{
      border-left: 4px solid var(--success);
    }}
    .ps-card.is-fast {{
      border-left: 4px solid var(--warning);
    }}

    .card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.75rem;
    }}

    .card-id-wrap {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .ps-badge-id {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 700;
      color: #60A5FA;
      background: rgba(59, 130, 246, 0.12);
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(59, 130, 246, 0.25);
    }}

    .ps-category-badge {{
      font-size: 0.75rem;
      font-weight: 600;
      padding: 0.25rem 0.6rem;
      border-radius: var(--radius-sm);
    }}

    .badge-software {{
      background: var(--software-bg);
      color: var(--software);
      border: 1px solid rgba(6, 182, 212, 0.3);
    }}

    .badge-hardware {{
      background: var(--hardware-bg);
      color: var(--hardware);
      border: 1px solid rgba(249, 115, 22, 0.3);
    }}

    .status-tag {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-full);
    }}

    .status-tag.open {{
      background: var(--success-bg);
      color: var(--success);
      border: 1px solid rgba(16, 185, 129, 0.25);
    }}

    .status-tag.fast {{
      background: var(--warning-bg);
      color: var(--warning);
      border: 1px solid rgba(245, 158, 11, 0.25);
    }}

    .status-tag.frozen {{
      background: var(--danger-bg);
      color: var(--danger);
      border: 1px solid rgba(239, 68, 68, 0.25);
    }}

    .ps-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.15rem;
      font-weight: 700;
      color: #FFF;
      line-height: 1.35;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .ps-org {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.8rem;
      color: var(--text-muted);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}

    .theme-pill {{
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 500;
      color: #A78BFA;
      background: rgba(139, 92, 246, 0.1);
      border: 1px solid rgba(139, 92, 246, 0.2);
      padding: 0.2rem 0.55rem;
      border-radius: var(--radius-sm);
      max-width: fit-content;
    }}

    /* Progress Slot Tracker Bar */
    .slot-tracker {{
      background: rgba(0, 0, 0, 0.3);
      padding: 0.85rem;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.05);
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }}

    .slot-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.8rem;
    }}

    .slot-count {{
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: #FFF;
    }}

    .slot-left {{
      color: var(--text-dim);
      font-size: 0.75rem;
    }}

    .slot-left b {{
      color: var(--success);
    }}

    .progress-bar-bg {{
      width: 100%;
      height: 7px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: var(--radius-full);
      overflow: hidden;
    }}

    .progress-bar-fill {{
      height: 100%;
      border-radius: var(--radius-full);
      transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    .card-snippet {{
      font-size: 0.85rem;
      color: var(--text-dim);
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
      line-height: 1.45;
    }}

    .card-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 0.75rem;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      margin-top: auto;
    }}

    .btn-details {{
      background: transparent;
      color: #60A5FA;
      font-size: 0.82rem;
      font-weight: 600;
      border: none;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.35rem 0.5rem;
      border-radius: var(--radius-sm);
    }}
    .btn-details:hover {{
      background: rgba(59, 130, 246, 0.15);
      color: #93C5FD;
    }}

    /* Table View */
    .table-view-wrap {{
      display: none;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: var(--shadow-md);
    }}

    .table-responsive {{
      overflow-x: auto;
      width: 100%;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.85rem;
    }}

    th {{
      background: #172033;
      padding: 0.9rem 1rem;
      color: var(--text-muted);
      font-weight: 600;
      text-transform: uppercase;
      font-size: 0.75rem;
      letter-spacing: 0.05em;
      border-bottom: 1px solid var(--border-color);
      white-space: nowrap;
    }}

    td {{
      padding: 0.95rem 1rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      vertical-align: middle;
    }}

    tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
      cursor: pointer;
    }}

    .td-title {{
      font-weight: 600;
      color: #FFF;
      max-width: 360px;
    }}

    /* Empty state */
    .empty-state {{
      display: none;
      text-align: center;
      padding: 4rem 2rem;
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      border: 1px dashed var(--border-color);
      margin-top: 1.5rem;
    }}

    .empty-state h3 {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.35rem;
      color: #FFF;
      margin-bottom: 0.5rem;
    }}

    /* Modal Dialog */
    .modal-overlay {{
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(4, 7, 15, 0.75);
      backdrop-filter: blur(8px);
      z-index: 1000;
      justify-content: center;
      align-items: center;
      padding: 1.5rem;
      animation: fadeIn 0.2s ease-out;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}

    .modal-card {{
      background: #0F172A;
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: var(--radius-lg);
      max-width: 900px;
      width: 100%;
      max-height: 90vh;
      display: flex;
      flex-direction: column;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.8);
      position: relative;
      overflow: hidden;
    }}

    .modal-header {{
      padding: 1.5rem 1.75rem;
      border-bottom: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 1.25rem;
      background: rgba(30, 41, 59, 0.5);
    }}

    .modal-title-area {{
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }}

    .modal-title {{
      font-family: 'Outfit', sans-serif;
      font-size: 1.45rem;
      font-weight: 700;
      color: #FFF;
      line-height: 1.3;
    }}

    .modal-close {{
      background: rgba(255, 255, 255, 0.08);
      border: none;
      color: var(--text-muted);
      width: 36px;
      height: 36px;
      border-radius: 50%;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition);
      flex-shrink: 0;
    }}
    .modal-close:hover {{
      background: rgba(255, 255, 255, 0.2);
      color: #FFF;
    }}

    .modal-body {{
      padding: 1.75rem;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }}

    .modal-grid-meta {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1rem;
      background: rgba(15, 23, 42, 0.8);
      padding: 1.25rem;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.06);
    }}

    .meta-box {{
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }}

    .meta-box-label {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
    }}

    .meta-box-value {{
      font-size: 0.9rem;
      font-weight: 600;
      color: #FFF;
    }}

    .modal-description-box {{
      line-height: 1.65;
      font-size: 0.92rem;
      color: #E2E8F0;
      white-space: pre-line;
      background: rgba(0, 0, 0, 0.2);
      padding: 1.25rem;
      border-radius: var(--radius-md);
      border: 1px solid rgba(255, 255, 255, 0.05);
      font-family: inherit;
    }}

    .modal-footer {{
      padding: 1.25rem 1.75rem;
      border-top: 1px solid var(--border-color);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(30, 41, 59, 0.5);
    }}

    /* Toast notification */
    .toast {{
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: #10B981;
      color: white;
      padding: 0.75rem 1.25rem;
      border-radius: var(--radius-md);
      font-weight: 600;
      font-size: 0.85rem;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
      z-index: 2000;
      opacity: 0;
      transform: translateY(20px);
      transition: var(--transition);
      pointer-events: none;
    }}

    .toast.show {{
      opacity: 1;
      transform: translateY(0);
    }}

    @media (max-width: 768px) {{
      .container {{ padding: 1rem; }}
      h1 {{ font-size: 1.75rem; }}
      .cards-grid {{ grid-template-columns: 1fr; }}
      .toolbar {{ position: static; }}
    }}
  </style>
</head>
<body>

  <div class="container">
    <!-- Header -->
    <header>
      <div class="header-top">
        <div>
          <div class="brand-tag">
            <span class="live-dot"></span>
            SIH 2026 Strategic Intelligence
          </div>
          <h1>SIH 2026 Problem Statement & Slot Explorer</h1>
          <p class="subtitle">
            Curated list of all 240 problem statements sorted in <b>ascending order of submissions</b> (fewest submissions / maximum open slots first out of 500).
          </p>
        </div>

        <div class="header-actions">
          <button class="btn btn-secondary" id="exportJsonBtn">
            <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path><polyline points="7 10 12 15 17 10"></polyline><line x1="12" y1="15" x2="12" y2="3"></line></svg>
            Export Filtered JSON
          </button>
          <button class="btn btn-secondary" id="exportCsvBtn">
            <svg width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line></svg>
            Export CSV
          </button>
        </div>
      </div>

      <!-- Real-time metrics ribbon -->
      <div class="metrics-ribbon">
        <div class="metric-card" style="--card-accent: #3B82F6;">
          <span class="metric-label">Total Challenges</span>
          <span class="metric-val" id="metricTotal">240</span>
          <span class="metric-sub">Official SIH 2026 problems</span>
        </div>
        <div class="metric-card" style="--card-accent: #10B981;">
          <span class="metric-label">Open for Submission</span>
          <span class="metric-val" id="metricOpen" style="color: #34D399;">215</span>
          <span class="metric-sub">Active slots remaining (&lt; 500)</span>
        </div>
        <div class="metric-card" style="--card-accent: #EF4444;">
          <span class="metric-label">Frozen (Capped)</span>
          <span class="metric-val" id="metricFrozen" style="color: #F87171;">25</span>
          <span class="metric-sub">Reached max 500 cap</span>
        </div>
        <div class="metric-card" style="--card-accent: #06B6D4;">
          <span class="metric-label">Lowest Competition</span>
          <span class="metric-val" id="metricLowest" style="color: #38BDF8;">21</span>
          <span class="metric-sub">Fewest submitted ideas</span>
        </div>
        <div class="metric-card" style="--card-accent: #8B5CF6;">
          <span class="metric-label">Total Idea Submissions</span>
          <span class="metric-val" id="metricSubmissions" style="color: #C084FC;">38,471</span>
          <span class="metric-sub">Across all organizations</span>
        </div>
      </div>
    </header>

    <!-- Interactive Filter Toolbar -->
    <div class="toolbar">
      <div class="search-row">
        <div class="search-box">
          <svg class="search-icon" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="searchInput" class="search-input" placeholder="Search by ID (e.g. SIH26116), title, keyword, ministry, theme...">
          <button id="searchClear" class="search-clear">&times;</button>
        </div>

        <!-- Status Filter Chips -->
        <div class="chip-pills">
          <button class="chip-btn active" data-status="ALL">All Status</button>
          <button class="chip-btn open-chip" data-status="OPEN">🟢 Open (&lt;500)</button>
          <button class="chip-btn" data-status="FAST" style="color: #FBBF24;">🟡 Filling Fast (&gt;80%)</button>
          <button class="chip-btn frozen-chip" data-status="FROZEN">🔴 Frozen (500)</button>
        </div>

        <!-- View Toggle -->
        <div class="view-toggle">
          <button class="view-btn active" id="viewGridBtn" title="Grid View">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
          </button>
          <button class="view-btn" id="viewTableBtn" title="Table View">
            <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><line x1="8" y1="6" x2="21" y2="6"></line><line x1="8" y1="12" x2="21" y2="12"></line><line x1="8" y1="18" x2="21" y2="18"></line><line x1="3" y1="6" x2="3.01" y2="6"></line><line x1="3" y1="12" x2="3.01" y2="12"></line><line x1="3" y1="18" x2="3.01" y2="18"></line></svg>
          </button>
        </div>
      </div>

      <div class="filter-row">
        <div class="filter-group">
          <!-- Category Select -->
          <div class="select-wrap">
            <select id="categorySelect" class="custom-select">
              <option value="ALL">All Categories</option>
              <option value="Software">Software</option>
              <option value="Hardware">Hardware</option>
            </select>
            <span class="select-arrow">▼</span>
          </div>

          <!-- Theme Select -->
          <div class="select-wrap">
            <select id="themeSelect" class="custom-select">
              <option value="ALL">All Themes (17)</option>
            </select>
            <span class="select-arrow">▼</span>
          </div>

          <!-- Ministry / Organization Select -->
          <div class="select-wrap">
            <select id="orgSelect" class="custom-select">
              <option value="ALL">All Organizations (35)</option>
            </select>
            <span class="select-arrow">▼</span>
          </div>
        </div>

        <div class="filter-group">
          <span style="font-size: 0.8rem; color: var(--text-dim);">Sort By:</span>
          <div class="select-wrap">
            <select id="sortSelect" class="custom-select">
              <option value="asc-count">Submissions: Low to High (Ascending)</option>
              <option value="desc-count">Submissions: High to Low (Descending)</option>
              <option value="avail-slots">Remaining Slots: Most First</option>
              <option value="id-asc">Problem ID (SIH26001...)</option>
              <option value="title-asc">Title: A to Z</option>
            </select>
            <span class="select-arrow">▼</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Results bar -->
    <div class="results-bar">
      <div class="results-count" id="resultsCount">
        Showing <b>240</b> of <b>240</b> problem statements
      </div>
      <div>
        Click any card for complete problem background & solution guidelines
      </div>
    </div>

    <!-- Cards Grid -->
    <div class="cards-grid" id="cardsGrid"></div>

    <!-- Table View -->
    <div class="table-view-wrap" id="tableView">
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th>PS ID</th>
              <th>Category</th>
              <th>Theme</th>
              <th>Title</th>
              <th>Organization</th>
              <th>Submissions</th>
              <th>Slots Left</th>
              <th>Status</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody id="tableBody"></tbody>
        </table>
      </div>
    </div>

    <!-- Empty State -->
    <div class="empty-state" id="emptyState">
      <h3>No Problem Statements Match Your Filter</h3>
      <p style="color: var(--text-dim); margin-bottom: 1.25rem;">Try clearing your search keyword or resetting the status and theme filters.</p>
      <button class="btn btn-primary" id="resetFiltersBtn">Reset All Filters</button>
    </div>
  </div>

  <!-- Detail Modal -->
  <div class="modal-overlay" id="detailModal">
    <div class="modal-card">
      <div class="modal-header">
        <div class="modal-title-area">
          <div style="display: flex; gap: 0.5rem; align-items: center;">
            <span class="ps-badge-id" id="modalId">SIH26001</span>
            <span class="ps-category-badge" id="modalCategory">Software</span>
            <span class="status-tag" id="modalStatus">Open</span>
          </div>
          <h2 class="modal-title" id="modalTitle">Problem Title</h2>
        </div>
        <button class="modal-close" id="modalCloseBtn" title="Close (Esc)">&times;</button>
      </div>

      <div class="modal-body">
        <!-- Metadata Grid -->
        <div class="modal-grid-meta">
          <div class="meta-box">
            <span class="meta-box-label">Organization</span>
            <span class="meta-box-value" id="modalOrg">-</span>
          </div>
          <div class="meta-box">
            <span class="meta-box-label">Department / Ministry</span>
            <span class="meta-box-value" id="modalDept">-</span>
          </div>
          <div class="meta-box">
            <span class="meta-box-label">Theme</span>
            <span class="meta-box-value" id="modalTheme">-</span>
          </div>
          <div class="meta-box">
            <span class="meta-box-label">Submissions Slot Status</span>
            <span class="meta-box-value" id="modalSlots">-</span>
          </div>
        </div>

        <div>
          <h3 style="font-family: 'Outfit', sans-serif; font-size: 1.1rem; margin-bottom: 0.75rem; color: #93C5FD;">Detailed Problem Description & Scope</h3>
          <div class="modal-description-box" id="modalDescription"></div>
        </div>
      </div>

      <div class="modal-footer">
        <div style="font-size: 0.8rem; color: var(--text-dim);" id="modalDeadline">
          Deadline: 30 September 2026
        </div>
        <div style="display: flex; gap: 0.5rem;">
          <button class="btn btn-secondary" id="copyIdBtn">Copy PS ID</button>
          <button class="btn btn-primary" id="copyJsonBtn">Copy Full JSON</button>
        </div>
      </div>
    </div>
  </div>

  <!-- Toast -->
  <div class="toast" id="toast">Copied to clipboard!</div>

  <script>
    // Embedded ascending dataset
    const RAW_DATA = {json_embedded};

    // State
    let currentFilter = {{
      search: "",
      status: "ALL",
      category: "ALL",
      theme: "ALL",
      org: "ALL",
      sort: "asc-count",
      view: "grid"
    }};

    let activeModalItem = null;

    // Elements
    const cardsGrid = document.getElementById("cardsGrid");
    const tableView = document.getElementById("tableView");
    const tableBody = document.getElementById("tableBody");
    const emptyState = document.getElementById("emptyState");
    const searchInput = document.getElementById("searchInput");
    const searchClear = document.getElementById("searchClear");
    const categorySelect = document.getElementById("categorySelect");
    const themeSelect = document.getElementById("themeSelect");
    const orgSelect = document.getElementById("orgSelect");
    const sortSelect = document.getElementById("sortSelect");
    const resultsCount = document.getElementById("resultsCount");
    const detailModal = document.getElementById("detailModal");
    const modalCloseBtn = document.getElementById("modalCloseBtn");
    const toast = document.getElementById("toast");

    // Populate dropdown filters
    function initFilters() {{
      const themes = [...new Set(RAW_DATA.map(d => d.theme).filter(Boolean))].sort();
      themes.forEach(t => {{
        const opt = document.createElement("option");
        opt.value = t;
        opt.textContent = t;
        themeSelect.appendChild(opt);
      }});

      const orgs = [...new Set(RAW_DATA.map(d => d.organization).filter(Boolean))].sort();
      orgs.forEach(o => {{
        const opt = document.createElement("option");
        opt.value = o;
        opt.textContent = o;
        orgSelect.appendChild(opt);
      }});
    }}

    // Filter & Sort
    function getFilteredData() {{
      return RAW_DATA.filter(item => {{
        // Search filter
        if (currentFilter.search) {{
          const term = currentFilter.search.toLowerCase();
          const matchId = (item.id || "").toLowerCase().includes(term);
          const matchTitle = (item.title || "").toLowerCase().includes(term);
          const matchOrg = (item.organization || "").toLowerCase().includes(term);
          const matchTheme = (item.theme || "").toLowerCase().includes(term);
          const matchDesc = (item.description || "").toLowerCase().includes(term);
          if (!matchId && !matchTitle && !matchOrg && !matchTheme && !matchDesc) return false;
        }}

        // Status filter
        if (currentFilter.status === "OPEN" && item.current_submissions_count >= 500) return false;
        if (currentFilter.status === "FAST" && (item.fill_percentage < 80 || item.current_submissions_count >= 500)) return false;
        if (currentFilter.status === "FROZEN" && item.current_submissions_count < 500) return false;

        // Category filter
        if (currentFilter.category !== "ALL" && item.category !== currentFilter.category) return false;

        // Theme filter
        if (currentFilter.theme !== "ALL" && item.theme !== currentFilter.theme) return false;

        // Organization filter
        if (currentFilter.org !== "ALL" && item.organization !== currentFilter.org) return false;

        return true;
      }}).sort((a, b) => {{
        switch (currentFilter.sort) {{
          case "asc-count":
            return (a.current_submissions_count - b.current_submissions_count) || a.id.localeCompare(b.id);
          case "desc-count":
            return (b.current_submissions_count - a.current_submissions_count) || a.id.localeCompare(b.id);
          case "avail-slots":
            return (b.remaining_slots - a.remaining_slots) || (a.current_submissions_count - b.current_submissions_count);
          case "id-asc":
            return a.id.localeCompare(b.id, undefined, {{ numeric: true }});
          case "title-asc":
            return a.title.localeCompare(b.title);
          default:
            return 0;
        }}
      }});
    }}

    function getProgressColor(count, cap) {{
      const ratio = count / cap;
      if (ratio >= 1) return "#EF4444"; // Red (Frozen)
      if (ratio >= 0.8) return "#F59E0B"; // Amber
      if (ratio >= 0.4) return "#06B6D4"; // Cyan
      return "#10B981"; // Emerald green (Low competition)
    }}

    function render() {{
      const filtered = getFilteredData();
      resultsCount.innerHTML = `Showing <b>${{filtered.length}}</b> of <b>${{RAW_DATA.length}}</b> problem statements`;

      if (filtered.length === 0) {{
        cardsGrid.style.display = "none";
        tableView.style.display = "none";
        emptyState.style.display = "block";
        return;
      }}

      emptyState.style.display = "none";

      if (currentFilter.view === "grid") {{
        cardsGrid.style.display = "grid";
        tableView.style.display = "none";
        renderCards(filtered);
      }} else {{
        cardsGrid.style.display = "none";
        tableView.style.display = "block";
        renderTable(filtered);
      }}
    }}

    function renderCards(items) {{
      cardsGrid.innerHTML = items.map(item => {{
        const isFrozen = item.current_submissions_count >= item.max_slots_cap;
        const isFast = !isFrozen && item.fill_percentage >= 80;
        const statusClass = isFrozen ? "frozen" : (isFast ? "fast" : "open");
        const statusBorder = isFrozen ? "is-frozen" : (isFast ? "is-fast" : "is-open");
        const statusText = isFrozen ? "Frozen (500)" : (isFast ? "Filling Fast" : "Open");
        const barColor = getProgressColor(item.current_submissions_count, item.max_slots_cap);
        const catBadgeClass = item.category === "Hardware" ? "badge-hardware" : "badge-software";

        return `
          <div class="ps-card ${{statusBorder}}" onclick="openModal('${{item.id}}')">
            <div class="card-header">
              <div class="card-id-wrap">
                <span class="ps-badge-id">${{item.id}}</span>
                <span class="ps-category-badge ${{catBadgeClass}}">${{item.category || "Software"}}</span>
              </div>
              <span class="status-tag ${{statusClass}}">${{statusText}}</span>
            </div>

            <h3 class="ps-title" title="${{escapeHtml(item.title)}}">${{escapeHtml(item.title)}}</h3>

            <div class="ps-org" title="${{escapeHtml(item.organization)}}">
              <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M3 21h18M3 7v14M21 7v14M6 10h.01M6 14h.01M6 18h.01M18 10h.01M18 14h.01M18 18h.01M9 7h6M12 3v4"></path></svg>
              ${{escapeHtml(item.organization)}}
            </div>

            <div class="theme-pill">${{escapeHtml(item.theme || "General")}}</div>

            <!-- Slot Tracker -->
            <div class="slot-tracker">
              <div class="slot-meta">
                <span class="slot-count">${{item.current_submissions_count}} <span style="color:var(--text-dim);font-weight:normal;">/ ${{item.max_slots_cap}} ideas</span></span>
                <span class="slot-left"><b>${{item.remaining_slots}}</b> slots left (${{item.fill_percentage}}%)</span>
              </div>
              <div class="progress-bar-bg">
                <div class="progress-bar-fill" style="width: ${{Math.min(100, item.fill_percentage)}}%; background: ${{barColor}};"></div>
              </div>
            </div>

            <p class="card-snippet">${{escapeHtml(item.description || "No detailed description provided.")}}</p>

            <div class="card-footer">
              <button class="btn-details" onclick="event.stopPropagation(); openModal('${{item.id}}')">
                View Full Brief & Solution Scope
                <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"></path></svg>
              </button>
              <button class="btn btn-secondary btn-icon" style="padding: 0.4rem;" onclick="event.stopPropagation(); copyText('${{item.id}}', 'Copied PS ID!')" title="Copy ID">
                <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
              </button>
            </div>
          </div>
        `;
      }}).join("");
    }}

    function renderTable(items) {{
      tableBody.innerHTML = items.map(item => {{
        const isFrozen = item.current_submissions_count >= item.max_slots_cap;
        const statusClass = isFrozen ? "frozen" : (item.fill_percentage >= 80 ? "fast" : "open");
        const statusText = isFrozen ? "Frozen (500)" : (item.fill_percentage >= 80 ? "Filling Fast" : "Open");
        const catBadgeClass = item.category === "Hardware" ? "badge-hardware" : "badge-software";

        return `
          <tr onclick="openModal('${{item.id}}')">
            <td><span class="ps-badge-id">${{item.id}}</span></td>
            <td><span class="ps-category-badge ${{catBadgeClass}}">${{item.category}}</span></td>
            <td><span class="theme-pill">${{escapeHtml(item.theme)}}</span></td>
            <td class="td-title" title="${{escapeHtml(item.title)}}">${{escapeHtml(item.title)}}</td>
            <td style="color:var(--text-muted);">${{escapeHtml(item.organization)}}</td>
            <td><b style="font-family:'JetBrains Mono'">${{item.current_submissions_count}}</b> / 500</td>
            <td><span style="color:var(--success);font-weight:600;">${{item.remaining_slots}}</span> left</td>
            <td><span class="status-tag ${{statusClass}}">${{statusText}}</span></td>
            <td>
              <button class="btn btn-secondary" style="padding: 0.35rem 0.65rem; font-size: 0.75rem;" onclick="event.stopPropagation(); openModal('${{item.id}}')">
                View
              </button>
            </td>
          </tr>
        `;
      }}).join("");
    }}

    function escapeHtml(str) {{
      if (!str) return "";
      return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }}

    function openModal(id) {{
      const item = RAW_DATA.find(d => d.id === id);
      if (!item) return;
      activeModalItem = item;

      document.getElementById("modalId").textContent = item.id;
      document.getElementById("modalCategory").textContent = item.category || "Software";
      document.getElementById("modalTitle").textContent = item.title;
      document.getElementById("modalOrg").textContent = item.organization || "-";
      document.getElementById("modalDept").textContent = item.ministry_or_department || item.organization || "-";
      document.getElementById("modalTheme").textContent = item.theme || "General";
      document.getElementById("modalSlots").textContent = `${{item.current_submissions_count}} / ${{item.max_slots_cap}} (${{item.remaining_slots}} slots left, ${{item.fill_percentage}}% filled)`;
      document.getElementById("modalDeadline").textContent = `Deadline: ${{item.deadline || "30 September 2026"}}`;
      document.getElementById("modalDescription").textContent = item.description || "No detailed description provided.";

      const statusTag = document.getElementById("modalStatus");
      const isFrozen = item.current_submissions_count >= item.max_slots_cap;
      statusTag.className = `status-tag ${{isFrozen ? "frozen" : (item.fill_percentage >= 80 ? "fast" : "open")}}`;
      statusTag.textContent = isFrozen ? "Frozen (500/500)" : (item.fill_percentage >= 80 ? "Filling Fast" : "Open");

      detailModal.style.display = "flex";
      document.body.style.overflow = "hidden";
    }}

    function closeModal() {{
      detailModal.style.display = "none";
      document.body.style.overflow = "auto";
      activeModalItem = null;
    }}

    function showToast(text) {{
      toast.textContent = text;
      toast.classList.add("show");
      setTimeout(() => toast.classList.remove("show"), 2500);
    }}

    function copyText(str, successMsg) {{
      navigator.clipboard.writeText(str).then(() => {{
        showToast(successMsg || "Copied to clipboard!");
      }}).catch(() => {{
        showToast("Error copying");
      }});
    }}

    // Export Handlers
    document.getElementById("exportJsonBtn").addEventListener("click", () => {{
      const filtered = getFilteredData();
      const blob = new Blob([JSON.stringify(filtered, null, 2)], {{ type: "application/json" }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `sih_2026_filtered_${{filtered.length}}_statements.json`;
      a.click();
      URL.revokeObjectURL(url);
      showToast(`Exported ${{filtered.length}} statements as JSON!`);
    }});

    document.getElementById("exportCsvBtn").addEventListener("click", () => {{
      const filtered = getFilteredData();
      const headers = ["ID", "Category", "Theme", "Organization", "Submissions", "Max Cap", "Remaining Slots", "Status", "Title"];
      const rows = filtered.map(item => [
        `"${{item.id}}"`,
        `"${{item.category}}"`,
        `"${{(item.theme || "").replace(/"/g, '""')}}"`,
        `"${{(item.organization || "").replace(/"/g, '""')}}"`,
        item.current_submissions_count,
        item.max_slots_cap,
        item.remaining_slots,
        `"${{item.status}}"`,
        `"${{(item.title || "").replace(/"/g, '""')}}"`
      ]);

      const csvContent = [headers.join(","), ...rows.map(r => r.join(","))].join("\\n");
      const blob = new Blob([csvContent], {{ type: "text/csv;charset=utf-8;" }});
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `sih_2026_filtered_${{filtered.length}}_statements.csv`;
      a.click();
      URL.revokeObjectURL(url);
      showToast(`Exported ${{filtered.length}} statements as CSV!`);
    }});

    // Modal Copy Buttons
    document.getElementById("copyIdBtn").addEventListener("click", () => {{
      if (activeModalItem) copyText(activeModalItem.id, `Copied ${{activeModalItem.id}}`);
    }});

    document.getElementById("copyJsonBtn").addEventListener("click", () => {{
      if (activeModalItem) copyText(JSON.stringify(activeModalItem, null, 2), `Copied full JSON for ${{activeModalItem.id}}!`);
    }});

    modalCloseBtn.addEventListener("click", closeModal);
    detailModal.addEventListener("click", (e) => {{
      if (e.target === detailModal) closeModal();
    }});

    window.addEventListener("keydown", (e) => {{
      if (e.key === "Escape") closeModal();
      if (e.key === "/" && document.activeElement !== searchInput) {{
        e.preventDefault();
        searchInput.focus();
      }}
    }});

    // Event Listeners
    searchInput.addEventListener("input", (e) => {{
      currentFilter.search = e.target.value.trim();
      searchClear.style.display = currentFilter.search ? "block" : "none";
      render();
    }});

    searchClear.addEventListener("click", () => {{
      searchInput.value = "";
      currentFilter.search = "";
      searchClear.style.display = "none";
      render();
    }});

    document.querySelectorAll(".chip-btn").forEach(btn => {{
      btn.addEventListener("click", (e) => {{
        document.querySelectorAll(".chip-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        currentFilter.status = btn.dataset.status;
        render();
      }});
    }});

    categorySelect.addEventListener("change", (e) => {{
      currentFilter.category = e.target.value;
      render();
    }});

    themeSelect.addEventListener("change", (e) => {{
      currentFilter.theme = e.target.value;
      render();
    }});

    orgSelect.addEventListener("change", (e) => {{
      currentFilter.org = e.target.value;
      render();
    }});

    sortSelect.addEventListener("change", (e) => {{
      currentFilter.sort = e.target.value;
      render();
    }});

    document.getElementById("viewGridBtn").addEventListener("click", function() {{
      currentFilter.view = "grid";
      this.classList.add("active");
      document.getElementById("viewTableBtn").classList.remove("active");
      render();
    }});

    document.getElementById("viewTableBtn").addEventListener("click", function() {{
      currentFilter.view = "table";
      this.classList.add("active");
      document.getElementById("viewGridBtn").classList.remove("active");
      render();
    }});

    document.getElementById("resetFiltersBtn").addEventListener("click", () => {{
      searchInput.value = "";
      currentFilter.search = "";
      currentFilter.status = "ALL";
      currentFilter.category = "ALL";
      currentFilter.theme = "ALL";
      currentFilter.org = "ALL";
      currentFilter.sort = "asc-count";
      searchClear.style.display = "none";

      document.querySelectorAll(".chip-btn").forEach(b => b.classList.remove("active"));
      document.querySelector('.chip-btn[data-status="ALL"]').classList.add("active");
      categorySelect.value = "ALL";
      themeSelect.value = "ALL";
      orgSelect.value = "ALL";
      sortSelect.value = "asc-count";
      render();
    }});

    // Initialize
    initFilters();
    render();
  </script>
</body>
</html>"""

    output_path = os.path.join(os.path.dirname(__file__), "sih_problem_statements_explorer.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated explorer at: {output_path}")

    # Also make a copy as index.html in the root for quick browser launching
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated root index at: {index_path}")

if __name__ == "__main__":
    generate_html()
