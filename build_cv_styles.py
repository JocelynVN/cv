#!/usr/bin/env python3
"""Regenerate alternate CV styles with identical content to dinh-van-khoa-cv.html."""

from pathlib import Path

DIR = Path(__file__).parent

# ── Shared content (must match dinh-van-khoa-cv.html) ──────────────────────

NAME = "Đinh Văn Khoa"
ROLE = "Odoo Developer &amp; AI-Augmented Consultant"
ROLE_BR = "Odoo Developer &amp;<br>AI-Augmented Consultant"

CONTACT = [
    ("Email", "dinhvankhoa14091999@gmail.com", "mailto:dinhvankhoa14091999@gmail.com", "email"),
    ("Điện thoại", "0982 594 840", None, "phone"),
    ("Địa chỉ", "Tiên Minh, Hải Phòng", None, "location"),
    ("GitHub", "github.com/JocelynVN", "https://github.com/JocelynVN", "github"),
]

SKILLS_ODOO = [
    "Odoo 11–19", "Python", "PostgreSQL", "XML / QWeb", "OWL / JavaScript",
    "HTML / CSS", "Git / GitHub", "Bootstrap", "BigQuery", "Looker Studio", "Data Pipeline",
]
SKILLS_AI = [
    "MCP Server", "AI Skills", "AI Agent", "Knowledge Base",
    "Prompt Engineering", "Cursor / Codex",
]
SKILLS_SOFT = [
    "Đào tạo người dùng", "Phân tích nghiệp vụ", "Làm việc nhóm", "Tự học", "Hỗ trợ kỹ thuật",
]

EDU = {
    "degree": "Cử nhân Công nghệ Thông tin",
    "school": "Trường Đại học Hàng hải Việt Nam",
    "meta": "09/2018 – 06/2022 · GPA 3.2",
}

SUMMARY = (
    'Odoo Developer full-stack, <strong>4+ năm · Odoo 11–19</strong> — làm được cả hai: code sâu và đứng sát người dùng cuối. '
    'Tại Viindoo đã đi trọn vòng đời: triển khai ERP đa ngành, phát triển sản phẩm, vận hành SaaS nội bộ; '
    'hiện là Engineer chính tại Elasten VN — phát triển module, nâng cấp hệ thống và <strong>đào tạo trực tiếp nhân viên</strong>, '
    'nên hiểu nghiệp vụ từ pain point thực tế, không chỉ từ tài liệu yêu cầu. '
    'Điểm khác biệt: <strong>AI-augmented developer</strong> — xây dựng MCP Server, Skills và knowledge base Odoo cho agent, '
    'rút ngắn vòng lặp dev → review → triển khai mà vẫn giữ chất lượng đầu ra.'
)

JOBS = [
    {
        "title": "Odoo Software Engineer",
        "period": "03/2025 – Hiện tại · Toàn thời gian",
        "company": "Công ty TNHH Elasten Việt Nam",
        "bullets": [
            "Đào tạo và hỗ trợ nhân viên, người dùng nội bộ khai thác Odoo — xây dựng tài liệu hướng dẫn, FAQ nghiệp vụ, giảm ticket lặp lại.",
            "Phát triển và tùy chỉnh module theo quy trình bán hàng đa kênh; đảm bảo hệ thống đáp ứng nhu cầu vận hành thực tế.",
            "Bảo trì, nâng cấp và tối ưu hệ thống Odoo nội bộ; xử lý sự cố production, đảm bảo vận hành ổn định.",
            "Xây dựng CDP, Customer Engagement và Data Warehouse phục vụ phân tích dữ liệu chiến lược.",
        ],
    },
    {
        "title": "Internal System Developer (Part-time)",
        "period": "06/2025 – Hiện tại",
        "company": "Công ty Cổ phần Công nghệ Viindoo",
        "bullets": [
            "Quay lại làm part-time sau giai đoạn chuyển sang Elasten VN; hỗ trợ hệ thống nội bộ theo nhu cầu dự án.",
            "Cải tiến và tối ưu hệ thống nội bộ, nền tảng SaaS — đảm bảo ổn định, bảo mật và khả năng mở rộng.",
            "Nâng cấp và triển khai dự án khách hàng; thử nghiệm AI tooling nội bộ phục vụ dev và vận hành.",
        ],
    },
    {
        "title": "Product Developer → Project Developer",
        "period": "02/2022 – 01/2025",
        "company": "Công ty Cổ phần Công nghệ Viindoo",
        "bullets": [
            "Tham gia xuyên suốt triển khai và nâng cấp hệ thống cho khách hàng đa ngành — từ sản xuất, bán lẻ đến tư vấn xây dựng.",
            "Phân tích nhu cầu, đề xuất và thực hiện giải pháp phù hợp; đóng vai trò key member, giải quyết triệt để vấn đề khách hàng.",
            "Nghiên cứu, phát triển và tối ưu sản phẩm Odoo; tiếp xúc hầu hết nghiệp vụ trên nhiều phiên bản (11–19).",
            "Phối hợp team dự án cải tiến sản phẩm dựa trên phản hồi thực tế từ triển khai.",
        ],
    },
    {
        "title": "Odoo Developer (Freelance)",
        "period": "05/2024 – 02/2025",
        "company": "Dự án độc lập",
        "bullets": [
            "Xây dựng hệ thống HIS (Hospital Information System) và HMS (Hospital Management System) trên Odoo.",
            "Tham gia đội nghiên cứu Robot Y tế tích hợp với hệ thống Odoo.",
        ],
    },
]

AI_BULLETS = [
    'Thiết kế và vận hành <strong>MCP Server</strong> kết nối AI với codebase và tri thức Odoo.',
    'Xây dựng <strong>AI Skills &amp; Agent workflows</strong> (intake, code review, gap analysis, triển khai) — chuẩn hóa quy trình dev/consulting.',
    'Xây dựng <strong>knowledge base cho AI</strong>: rules, patterns, domain context giúp agent trả lời đúng nghiệp vụ Odoo, giảm hallucination.',
    'Áp dụng AI hỗ trợ <strong>đào tạo người dùng</strong> (FAQ, hướng dẫn nghiệp vụ) và tăng năng suất dev/review trong môi trường production.',
]

PROJECT_NOTE = "Một số dự án nổi bật — còn nhiều triển khai &amp; nâng cấp khác trong 4+ năm tại Viindoo chưa liệt kê hết tại đây."

PROJECTS = [
    ("Nâng cấp Viindoo 16.0 → 17.0", " · Viindoo · Developer · Odoo 17", [
        "Nâng cấp cụm module: Sản xuất, Kho vận, Ví điện tử, Affiliate, HRM và Kế toán — team 8 Developers, 4 Testers.",
        "Phân tích, cải tiến và migrate code đảm bảo tương thích phiên bản mới, ổn định sau nâng cấp.",
    ]),
    ("Triển khai ERP — Tư vấn Xây dựng Điện 3", " · TVXĐ3 · Developer · Odoo 17", [
        "Phát triển tính năng đặc thù ngành: kiểm soát chất lượng dự án, tạm hoãn HĐ nhân sự, khen thưởng/kỷ luật, hậu kiểm dự án.",
        "Phân tích yêu cầu từ dự án xây dựng điện, đề xuất và triển khai giải pháp ERP toàn diện (dự án, tài chính, nhân sự).",
    ]),
    ("Triển khai ERP — Zulo Holdings", " · MLM &amp; E-commerce · Developer · Odoo 16", [
        "Xây dựng sàn TMĐT, ví điện tử và hệ thống Affiliate — quản lý giao dịch, hoa hồng đa cấp, thanh toán trực tuyến.",
        "Phân tích mô hình bán hàng đa cấp, tùy chỉnh module đáp ứng quy trình kinh doanh đặc thù.",
    ]),
    ("Triển khai ERP — Công ty Cổ phần X20", " · Dệt may · Developer · Odoo 15", [
        "Custom manufacturing VN: kế toán sản xuất, tiêu hao định mức, thuê gia công, báo cáo giá thành, PLM/ECO.",
        "Phân tích quy trình sản xuất dệt may, đề xuất giải pháp phù hợp đặc thù ngành.",
    ]),
    ("Nâng cấp ERP 13.0 → 15.0 — BDO Việt Nam", " · Kiểm toán · Team Leader · Odoo 13–15", [
        "Lead team 2 Developers: phân tích hệ thống, migrate dữ liệu, nâng cấp module Kế toán, HRM, Quản lý dự án.",
        "Kiểm tra và khắc phục lỗi sau nâng cấp, đảm bảo hệ thống vận hành ổn định theo đặc thù ngành kiểm toán.",
    ]),
]

MORE_TAGS = ["POS — F&amp;B", "Nâng cấp Odoo", "HIS / HMS", "SaaS nội bộ", "Robot y tế", "Subscription", "CDP / DWH", "Đa ngành"]
MORE_TEXT = "Danh sách đầy đủ và mô tả chi tiết — sẵn sàng trình bày khi phỏng vấn hoặc theo yêu cầu."
MORE_CTA = "→ Hỏi thêm về domain / module cụ thể bạn quan tâm."

ICONS = {
    "email": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 7l10 7 10-7"/></svg>',
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12 12 0 0 0 8.09 9.91"/></svg>',
    "location": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "github": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>',
}


def bullets_html(items, indent=10):
    lis = "\n".join(f'{" "*indent}<li>{b}</li>' for b in items)
    return f'{" "*indent}<ul>\n{lis}\n{" "*indent}</ul>'


def jobs_html(indent=8):
    parts = []
    for j in JOBS:
        parts.append(f'''{" "*indent}<div class="job">
{" "*indent}  <div class="job-header">
{" "*indent}    <span class="job-title">{j["title"]}</span>
{" "*indent}    <span class="job-period">{j["period"]}</span>
{" "*indent}  </div>
{" "*indent}  <div class="job-company">{j["company"]}</div>
{bullets_html(j["bullets"], indent + 2)}
{" "*indent}</div>''')
    return "\n".join(parts)


def projects_html(indent=8):
    parts = []
    for title, meta, blts in PROJECTS:
        parts.append(f'''{" "*indent}<div class="project">
{" "*indent}  <div class="project-header">{title}<span class="project-meta">{meta}</span></div>
{bullets_html(blts, indent + 2)}
{" "*indent}</div>''')
    return "\n".join(parts)


def main_content(indent=6):
    return f'''{" "*indent}<section class="main-section">
{" "*indent}  <h2>Tóm tắt</h2>
{" "*indent}  <p class="summary">{SUMMARY}</p>
{" "*indent}</section>

{" "*indent}<section class="main-section">
{" "*indent}  <h2>Kinh nghiệm làm việc</h2>
{jobs_html(indent + 2)}
{" "*indent}</section>

{" "*indent}<section class="main-section ai-section">
{" "*indent}  <h2>Ứng dụng AI &amp; Tự động hóa quy trình</h2>
{" "*indent}  <div class="job">
{bullets_html(AI_BULLETS, indent + 4)}
{" "*indent}  </div>
{" "*indent}</section>

{" "*indent}<section class="main-section">
{" "*indent}  <h2>Dự án tiêu biểu</h2>
{" "*indent}  <p class="section-note">{PROJECT_NOTE}</p>
{projects_html(indent + 2)}
{" "*indent}  <div class="projects-more">
{" "*indent}    <span class="projects-more-label">Các dự án &amp; hạng mục khác đã tham gia:</span>
{" "*indent}    <div class="projects-tags">{"".join(f"<span>{t}</span>" for t in MORE_TAGS)}</div>
{" "*indent}    {MORE_TEXT}
{" "*indent}    <span class="projects-cta">{MORE_CTA}</span>
{" "*indent}  </div>
{" "*indent}</section>'''


def sidebar_skills(indent=6):
    def tags(items):
        return "".join(f'<span class="skill-tag">{s}</span>' for s in items)
    return f'''{" "*indent}<div class="sidebar-section"><h2>Kỹ năng Odoo / Dev</h2><div class="skill-tags">{tags(SKILLS_ODOO)}</div></div>
{" "*indent}<div class="sidebar-section"><h2>Ứng dụng AI</h2><div class="skill-tags">{tags(SKILLS_AI)}</div></div>
{" "*indent}<div class="sidebar-section"><h2>Kỹ năng mềm</h2><div class="skill-tags">{tags(SKILLS_SOFT)}</div></div>
{" "*indent}<div class="sidebar-section"><h2>Học vấn</h2>
{" "*indent}  <div class="edu-degree">{EDU["degree"]}</div>
{" "*indent}  <div class="edu-school">{EDU["school"]}</div>
{" "*indent}  <div class="edu-meta">{EDU["meta"]}</div>
{" "*indent}</div>'''


def contact_sidebar(indent=8):
    rows = []
    for label, text, href, icon in CONTACT:
        val = f'<a href="{href}">{text}</a>' if href else text
        rows.append(f'''{" "*indent}<li>
{" "*indent}  <span class="contact-icon" aria-hidden="true">{ICONS[icon]}</span>
{" "*indent}  <div class="contact-body"><span class="contact-label">{label}</span>{val}</div>
{" "*indent}</li>''')
    return "\n".join(rows)


SHARED_MAIN_CSS = '''
    .main-section { margin-bottom: 18px; }
    .main-section:last-child { margin-bottom: 0; }
    .section-note { font-size: 8.5pt; color: var(--muted); font-style: italic; margin-bottom: 12px; line-height: 1.4; }
    .summary { font-size: 10pt; text-align: justify; line-height: 1.5; }
    .summary strong { font-weight: 700; }
    .job { margin-bottom: 14px; break-inside: avoid; page-break-inside: avoid; }
    .job:last-child { margin-bottom: 0; }
    .job-header { display: flex; justify-content: space-between; align-items: baseline; flex-wrap: wrap; gap: 4px 12px; margin-bottom: 2px; }
    .job-title { font-weight: 700; font-size: 10.5pt; }
    .job-period { font-size: 9pt; color: var(--muted); white-space: nowrap; font-weight: 600; }
    .job-company { font-size: 9.5pt; color: var(--muted); font-style: italic; margin-bottom: 6px; }
    .job ul { padding-left: 16px; }
    .job li { font-size: 9.5pt; margin-bottom: 3px; line-height: 1.4; }
    .project { margin-bottom: 11px; break-inside: avoid; page-break-inside: avoid; }
    .project-header { font-size: 9.5pt; font-weight: 700; margin-bottom: 4px; line-height: 1.35; }
    .project-meta { font-weight: 400; color: var(--muted); font-size: 9pt; }
    .project ul { padding-left: 14px; }
    .project li { font-size: 9.5pt; margin-bottom: 2px; line-height: 1.4; }
    .projects-more { margin-top: 12px; font-size: 9pt; line-height: 1.45; color: var(--muted); }
    .projects-more-label { color: var(--text); font-weight: 400; }
    .projects-tags { display: flex; flex-wrap: wrap; gap: 4px; margin: 6px 0 8px; }
    .projects-tags span { font-size: 8pt; background: #fff; border: 1px solid var(--border); border-radius: 3px; padding: 2px 6px; color: var(--text); }
    .projects-cta { display: block; font-size: 8.5pt; color: var(--muted); font-style: italic; }
    .ai-section .job li strong { font-weight: 700; }
    @media print {
      body { background: #fff; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
      .cv, .cv-page { margin: 0; box-shadow: none; max-width: none; width: 100%; border-radius: 0; overflow: visible; }
      .profile, .chips, .projects-more, .summary { break-inside: avoid; page-break-inside: avoid; }
      .main-section > h2, .main h2 { break-after: avoid; page-break-after: avoid; }
      @page { size: A4; margin: 0; }
    }
'''


MOBILE_STACK_CSS = '''
      body { background: #fff; font-size: 10pt; overflow-x: hidden; }
      .cv-page, .cv {
        margin: 0;
        width: 100%;
        max-width: 100%;
        min-width: 0;
        min-height: auto;
        box-shadow: none;
        border-radius: 0;
        display: block !important;
        grid-template-columns: none !important;
      }
      .sidebar, aside.sidebar {
        width: 100%;
        border-right: none !important;
        border-left: none !important;
        border-bottom: 2px solid var(--navy, var(--accent, var(--coral, var(--ocean, #1e3a5f))));
        padding: 20px 16px;
      }
      .main, main.main { padding: 20px 16px; width: 100%; }
      .body, .layout { display: block !important; }
      .body .sidebar, .body .main,
      .layout .sidebar, .layout .main {
        border-right: none !important;
        border-left: none !important;
      }
      .top, .banner, .head {
        display: block !important;
        grid-template-columns: none !important;
        text-align: center;
        padding: 20px 16px;
      }
      .top .avatar, .banner .avatar, .head .avatar {
        margin-left: auto;
        margin-right: auto;
      }
      .top-left { flex-direction: column; align-items: center; text-align: center; }
      .contact-row, .contact, .profile .contact { justify-content: center; }
      .cols, .skills-grid, .skills-row { grid-template-columns: 1fr !important; }
      .profile {
        flex-direction: column;
        align-items: center;
        text-align: center;
      }
      .chips { flex-direction: column; gap: 12px; }
      .chip-group p { max-width: none; }
      .wrap { padding: 16px; }
      .cv { padding-left: 0; padding-right: 0; }
      .job-header { flex-direction: column; align-items: flex-start; gap: 2px; }
      .job-period { white-space: normal; }
      .contact-list a, .contact-body { overflow-wrap: anywhere; word-break: normal; }
      .wave, .accent-bar { display: block; }
'''

def _embed_css(mobile_css):
    import re

    lines = []
    single_line = re.compile(r"^(.+?)\s*\{(.+)\}\s*$")
    for line in mobile_css.split("\n"):
        stripped = line.strip()
        if not stripped:
            lines.append(line)
            continue
        indent = line[: len(line) - len(line.lstrip())]
        match = single_line.match(stripped)
        if match and "{" not in match.group(1):
            parts = [p.strip() for p in match.group(1).split(",")]
            prefixed = ", ".join(
                p if p.startswith("html.cv-embed") else f"html.cv-embed {p}"
                for p in parts
            )
            lines.append(f"{indent}{prefixed} {{ {match.group(2).strip()} }}")
            continue
        if stripped.endswith("{"):
            selector = stripped[:-1].strip()
            parts = [p.strip() for p in selector.split(",")]
            prefixed = ", ".join(
                p if p.startswith("html.cv-embed") else f"html.cv-embed {p}"
                for p in parts
            )
            lines.append(f"{indent}{prefixed} {{")
        else:
            lines.append(line)
    return "\n".join(lines)


EMBED_STACK_CSS = _embed_css(MOBILE_STACK_CSS)

RESPONSIVE_CSS = f'''
    html {{ -webkit-text-size-adjust: 100%; }}
    @media screen {{
      body {{
        container-type: inline-size;
        container-name: cv-root;
        min-width: 0;
        overflow-x: hidden;
      }}
      .cv-page, .cv {{ width: 100%; min-width: 0; }}
      @container cv-root (max-width: 600px) {{
{MOBILE_STACK_CSS}
      }}
    }}
    @media screen and (max-width: 600px) {{
{MOBILE_STACK_CSS}
    }}
{EMBED_STACK_CSS}
'''

EMBED_SCRIPT = '''
  <script>
    (function () {
      if (new URLSearchParams(location.search).get("embed") === "1") {
        document.documentElement.classList.add("cv-embed");
      }
    })();
  </script>
'''


def wrap(title, css, body):
    return f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
{css}{RESPONSIVE_CSS}
  </style>
</head>
<body>
{body}
{EMBED_SCRIPT}
</body>
</html>
'''


def gen_modern():
    css = '''
    :root { --accent: #0d9488; --accent-dark: #0f766e; --text: #1e293b; --muted: #64748b; --border: #e2e8f0; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #f1f5f9; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; box-shadow: 0 8px 30px rgba(0,0,0,.08); }
    .top { display: grid; grid-template-columns: 110px 1fr; gap: 24px; padding: 28px 32px; background: linear-gradient(135deg, #f0fdfa, #fff 60%); border-bottom: 3px solid var(--accent); }
    .avatar { width: 110px; height: 110px; border-radius: 16px; object-fit: cover; object-position: center 15%; }
    .top h1 { font-size: 22pt; font-weight: 700; color: var(--text); }
    .top .role { font-size: 10pt; color: var(--accent-dark); font-weight: 600; margin: 4px 0 12px; }
    .contact-row { display: flex; flex-wrap: wrap; gap: 6px 18px; font-size: 9pt; color: var(--muted); }
    .contact-row a { color: var(--accent-dark); text-decoration: none; }
    .contact-item { display: flex; align-items: center; gap: 5px; }
    .contact-item svg { width: 13px; height: 13px; color: var(--accent); }
    .body { display: grid; grid-template-columns: 32% 68%; }
    .sidebar { padding: 22px 18px 24px 24px; border-right: 1px solid var(--border); }
    .main { padding: 22px 24px 24px 18px; }
    .sidebar-section { margin-bottom: 16px; }
    .sidebar-section h2 { font-size: 8pt; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--accent); border-bottom: 1px solid var(--border); padding-bottom: 4px; margin-bottom: 8px; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 5px; }
    .skill-tag { font-size: 8.5pt; background: #f0fdfa; color: var(--accent-dark); border-radius: 20px; padding: 3px 8px; }
    .edu-degree { font-weight: 600; font-size: 9.5pt; }
    .edu-school, .edu-meta { font-size: 9pt; color: var(--muted); }
    .main h2 { font-size: 11pt; font-weight: 700; color: var(--accent-dark); border-bottom: 1px solid var(--border); padding-bottom: 4px; margin-bottom: 8px; }
    .job-title { color: var(--accent-dark); }
''' + SHARED_MAIN_CSS.replace('var(--text)', 'var(--text)').replace('var(--muted)', 'var(--muted)').replace('var(--border)', 'var(--border)')

    contact = "".join(
        f'<span class="contact-item">{ICONS[icon]}'
        + (f'<a href="{href}">{text}</a>' if href else text)
        + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <header class="top">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div><h1>{NAME}</h1><div class="role">{ROLE}</div><div class="contact-row">{contact}</div></div>
  </header>
  <div class="body">
    <aside class="sidebar">
      {sidebar_skills(6)}
    </aside>
    <main class="main">
      {main_content(6)}
    </main>
  </div>
</div>'''
    return wrap(f"CV Modern — {NAME}", css, body)


def gen_dark():
    css = '''
    :root { --dark: #1a1f2e; --dark2: #252b3b; --gold: #c9a227; --text: #2d3748; --muted: #718096; --border: #e2e8f0; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #cbd5e0; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; display: grid; grid-template-columns: 30% 70%; background: #fff; box-shadow: 0 6px 28px rgba(0,0,0,.18); }
    .sidebar { background: var(--dark); color: #e2e8f0; padding: 26px 18px; }
    .avatar { width: 100px; height: 100px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 3px solid var(--gold); display: block; margin: 0 auto 14px; }
    .sidebar h1 { font-size: 15pt; text-align: center; color: #fff; margin-bottom: 4px; }
    .sidebar .role { text-align: center; font-size: 8.5pt; color: var(--gold); font-weight: 600; margin-bottom: 20px; line-height: 1.35; padding-bottom: 16px; border-bottom: 1px solid var(--dark2); }
    .sidebar-section { margin-bottom: 18px; }
    .sidebar-section h2 { font-size: 7.5pt; text-transform: uppercase; letter-spacing: .14em; color: var(--gold); margin-bottom: 8px; font-weight: 700; }
    .contact-list { list-style: none; }
    .contact-list li { display: flex; gap: 8px; margin-bottom: 9px; font-size: 8.5pt; color: #a0aec0; }
    .contact-icon svg { width: 13px; height: 13px; color: var(--gold); flex-shrink: 0; margin-top: 2px; }
    .contact-list a { color: #cbd5e0; text-decoration: none; }
    .contact-label { display: block; font-size: 6.5pt; text-transform: uppercase; letter-spacing: .06em; color: var(--gold); }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 7px; background: var(--dark2); color: #e2e8f0; border-radius: 3px; border: 1px solid #3d4663; }
    .edu-degree { font-weight: 700; font-size: 9pt; color: #fff; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: #a0aec0; }
    .main { padding: 26px 26px 22px 22px; }
    .main h2 { font-size: 11pt; color: var(--dark); border-bottom: 2px solid var(--gold); padding-bottom: 3px; margin-bottom: 8px; }
    .summary strong { color: var(--dark); }
    .job-title { color: var(--dark); }
    .job li::marker { color: var(--gold); }
    .project-header { color: var(--dark); }
    .ai-section .job li strong { color: var(--dark); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <aside class="sidebar">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1>{NAME}</h1>
    <div class="role">{ROLE_BR}</div>
    <div class="sidebar-section"><h2>Liên hệ</h2><ul class="contact-list">
      {contact_sidebar(6)}
    </ul></div>
    {sidebar_skills(4)}
  </aside>
  <main class="main">
    {main_content(4)}
  </main>
</div>'''
    return wrap(f"CV Dark — {NAME}", css, body)


def gen_minimal():
    css = '''
    :root { --black: #111; --gray: #555; --light: #999; --rule: #ddd; --text: #111; --muted: #555; --border: #ddd; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: 'Segoe UI', system-ui, sans-serif; font-size: 10pt; line-height: 1.5; color: var(--black); background: #f5f5f5; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; padding: 36px 40px; box-shadow: 0 2px 12px rgba(0,0,0,.06); }
    .header { display: flex; gap: 28px; align-items: center; padding-bottom: 20px; border-bottom: 1px solid var(--black); margin-bottom: 20px; }
    .avatar { width: 88px; height: 88px; border-radius: 4px; object-fit: cover; object-position: center 15%; }
    .header h1 { font-size: 20pt; font-weight: 600; }
    .header .role { font-size: 9.5pt; color: var(--gray); margin: 3px 0 10px; }
    .contact { display: flex; flex-wrap: wrap; gap: 4px 16px; font-size: 8.5pt; color: var(--gray); }
    .contact a { color: var(--black); text-decoration: none; border-bottom: 1px solid var(--rule); }
    .ci { display: inline-flex; align-items: center; gap: 4px; }
    .ci svg { width: 11px; height: 11px; }
    .skills-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--rule); }
    .skills-grid h3 { font-size: 7pt; text-transform: uppercase; letter-spacing: .1em; color: var(--light); margin-bottom: 6px; }
    .skills-grid p { font-size: 8.5pt; color: var(--gray); line-height: 1.6; }
    h2 { font-size: 11pt; font-weight: 600; margin-bottom: 8px; margin-top: 18px; }
    .summary strong { color: var(--black); font-weight: 600; }
    .job-title { color: var(--black); }
''' + SHARED_MAIN_CSS

    contact = "".join(
        f'<span class="ci">{ICONS[icon]}' + (f'<a href="{href}">{text}</a>' if href else text) + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <header class="header">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div>
      <h1>{NAME}</h1>
      <div class="role">{ROLE}</div>
      <div class="contact">{contact}</div>
    </div>
  </header>
  <div class="skills-grid">
    <div><h3>Kỹ năng Odoo / Dev</h3><p>{" · ".join(SKILLS_ODOO)}</p></div>
    <div><h3>Ứng dụng AI</h3><p>{" · ".join(SKILLS_AI)}</p></div>
    <div><h3>Học vấn</h3><p>{EDU["degree"]}<br>{EDU["school"]}<br>{EDU["meta"]}</p></div>
  </div>
  {main_content(2)}
</div>'''
    return wrap(f"CV Minimal — {NAME}", css, body)


def gen_elegant():
    css = '''
    :root { --wine: #6b2737; --wine-l: #8b3a4a; --paper: #faf8f5; --text: #3d3d3d; --muted: #7a7a7a; --border: #d4cfc8; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: Georgia, serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #e8e4df; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: var(--paper); padding: 32px 36px; box-shadow: 0 4px 20px rgba(0,0,0,.1); }
    .head { text-align: center; padding-bottom: 18px; border-bottom: 1px solid var(--border); margin-bottom: 20px; }
    .avatar { width: 96px; height: 96px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 2px solid var(--wine); margin-bottom: 12px; }
    h1.name { font-size: 26pt; font-weight: 700; color: var(--wine); letter-spacing: .04em; }
    .role { font-size: 10pt; color: var(--wine-l); font-style: italic; margin: 4px 0 14px; }
    .contact { display: flex; flex-wrap: wrap; justify-content: center; gap: 6px 20px; font-size: 8.5pt; color: var(--muted); }
    .contact a { color: var(--wine-l); text-decoration: none; }
    .ci { display: inline-flex; align-items: center; gap: 4px; }
    .ci svg { width: 11px; height: 11px; color: var(--wine); }
    .cols { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-bottom: 18px; }
    .cols h3 { font-size: 12pt; color: var(--wine); border-bottom: 1px solid var(--border); padding-bottom: 3px; margin-bottom: 8px; }
    .skill-line { font-size: 9pt; color: var(--muted); line-height: 1.65; font-family: system-ui, sans-serif; }
    h2 { font-size: 14pt; color: var(--wine); margin: 16px 0 8px; }
    .summary strong { color: var(--wine); }
    .job-title { color: var(--text); }
    .job-company { color: var(--wine-l); }
''' + SHARED_MAIN_CSS

    contact = "".join(
        f'<span class="ci">{ICONS[icon]}' + (f'<a href="{href}">{text}</a>' if href else text) + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <header class="head">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1 class="name">{NAME.upper()}</h1>
    <div class="role">{ROLE}</div>
    <div class="contact">{contact}</div>
  </header>
  <div class="cols">
    <div><h3>Kỹ năng Odoo / Dev</h3><div class="skill-line">{" · ".join(SKILLS_ODOO)}</div></div>
    <div><h3>Ứng dụng AI &amp; Kỹ năng mềm</h3><div class="skill-line">{" · ".join(SKILLS_AI)}<br><br>{" · ".join(SKILLS_SOFT)}</div></div>
  </div>
  <div class="cols" style="margin-bottom:0"><div><h3>Học vấn</h3><div class="skill-line"><strong>{EDU["degree"]}</strong><br>{EDU["school"]}<br>{EDU["meta"]}</div></div></div>
  {main_content(2)}
</div>'''
    return wrap(f"CV Elegant — {NAME}", css, body)


def gen_corporate():
    css = '''
    :root { --blue: #1565c0; --blue-d: #0d47a1; --text: #212121; --muted: #616161; --border: #e0e0e0; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #eceff1; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,.1); }
    .banner { background: var(--blue); color: #fff; padding: 24px 32px; display: grid; grid-template-columns: 90px 1fr auto; gap: 20px; align-items: center; }
    .avatar { width: 90px; height: 90px; border-radius: 8px; object-fit: cover; object-position: center 15%; border: 2px solid rgba(255,255,255,.4); }
    .banner h1 { font-size: 20pt; font-weight: 700; }
    .banner .role { font-size: 9.5pt; opacity: .9; margin-top: 3px; }
    .banner-contact { font-size: 8.5pt; line-height: 1.7; text-align: right; }
    .banner-contact a { color: #fff; text-decoration: none; }
    .layout { display: grid; grid-template-columns: 32% 68%; }
    .sidebar { padding: 20px 18px 24px 24px; border-right: 1px solid var(--border); background: #fafafa; }
    .main { padding: 20px 24px 24px 18px; }
    .sidebar-section { margin-bottom: 16px; }
    .sidebar-section h2 { font-size: 8pt; font-weight: 700; text-transform: uppercase; letter-spacing: .1em; color: var(--blue); border-bottom: 1px solid var(--border); padding-bottom: 4px; margin-bottom: 8px; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 5px; }
    .skill-tag { font-size: 8.5pt; background: #fff; border: 1px solid var(--border); border-radius: 3px; padding: 3px 7px; }
    .edu-degree { font-weight: 600; font-size: 9.5pt; }
    .edu-school, .edu-meta { font-size: 9pt; color: var(--muted); }
    .main h2 { font-size: 11pt; color: var(--blue); border-left: 4px solid var(--blue); padding-left: 10px; margin-bottom: 10px; }
    .summary strong { color: var(--text); }
    .job-title { color: var(--blue-d); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <header class="banner">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div><h1>{NAME}</h1><div class="role">{ROLE}</div></div>
    <div class="banner-contact">
      dinhvankhoa14091999@gmail.com<br>0982 594 840<br>Tiên Minh, Hải Phòng<br>
      <a href="https://github.com/JocelynVN">github.com/JocelynVN</a>
    </div>
  </header>
  <div class="layout">
    <aside class="sidebar">
      <div class="sidebar-section"><h2>Liên hệ</h2>
        <div class="edu-school">dinhvankhoa14091999@gmail.com<br>0982 594 840<br>Tiên Minh, Hải Phòng<br>github.com/JocelynVN</div>
      </div>
      {sidebar_skills(6)}
    </aside>
    <main class="main">{main_content(6)}</main>
  </div>
</div>'''
    return wrap(f"CV Corporate — {NAME}", css, body)


def gen_creative():
    css = '''
    :root { --coral: #e85d4c; --coral-d: #c44335; --cream: #fffbf7; --char: #2c2c2c; --muted: #666; --text: #2c2c2c; --border: #f0e0dc; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--char); background: #f0ebe6; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; display: grid; grid-template-columns: 32% 68%; background: var(--cream); box-shadow: 0 6px 24px rgba(0,0,0,.1); }
    .sidebar { background: var(--coral); color: #fff; padding: 28px 20px; }
    .avatar { width: 110px; height: 110px; border-radius: 20px; object-fit: cover; object-position: center 15%; margin-bottom: 16px; }
    .sidebar h1 { font-size: 17pt; line-height: 1.2; margin-bottom: 6px; }
    .sidebar .role { font-size: 9pt; opacity: .92; margin-bottom: 22px; line-height: 1.4; padding-bottom: 18px; border-bottom: 1px solid rgba(255,255,255,.25); }
    .sidebar-section { margin-bottom: 18px; }
    .sidebar-section h2 { font-size: 7.5pt; text-transform: uppercase; letter-spacing: .12em; opacity: .75; margin-bottom: 8px; }
    .contact-list { list-style: none; }
    .contact-list li { display: flex; gap: 7px; margin-bottom: 9px; font-size: 8.5pt; }
    .contact-icon svg { width: 13px; height: 13px; flex-shrink: 0; margin-top: 2px; }
    .contact-list a { color: #fff; text-decoration: none; }
    .contact-label { display: block; font-size: 6.5pt; text-transform: uppercase; opacity: .75; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 8px; background: rgba(255,255,255,.18); border-radius: 12px; }
    .edu-degree { font-weight: 700; font-size: 9pt; }
    .edu-school, .edu-meta { font-size: 8.5pt; opacity: .9; }
    .main { padding: 26px 22px 22px; }
    .main h2 { font-size: 13pt; color: var(--coral); margin-bottom: 8px; margin-top: 14px; }
    .main h2:first-child { margin-top: 0; }
    .summary strong { color: var(--coral-d); }
    .job-period { color: var(--coral); }
    .job li::marker { color: var(--coral); }
    .project-header { color: var(--coral-d); }
    .ai-section .job li strong { color: var(--coral-d); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <aside class="sidebar">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1>{NAME}</h1>
    <div class="role">{ROLE_BR}</div>
    <div class="sidebar-section"><h2>Liên hệ</h2><ul class="contact-list">{contact_sidebar(6)}</ul></div>
    {sidebar_skills(4)}
  </aside>
  <main class="main">{main_content(4)}</main>
</div>'''
    return wrap(f"CV Creative — {NAME}", css, body)


def gen_tech():
    css = '''
    :root { --slate: #1e293b; --green: #22c55e; --green-d: #16a34a; --text: #1e293b; --muted: #64748b; --border: #e2e8f0; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #0f172a; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; box-shadow: 0 8px 32px rgba(0,0,0,.3); }
    .top { background: var(--slate); color: #e2e8f0; padding: 20px 28px; display: flex; gap: 20px; align-items: center; position: relative; }
    .top::after { content: '// cv.json'; position: absolute; top: 8px; right: 28px; font-family: monospace; font-size: 7pt; color: var(--green); opacity: .6; }
    .avatar { width: 72px; height: 72px; border-radius: 6px; object-fit: cover; object-position: center 15%; border: 2px solid var(--green); }
    .top h1 { font-size: 16pt; font-weight: 700; }
    .top h1 span { color: var(--green); font-family: monospace; font-size: 10pt; font-weight: 400; }
    .top .role { font-size: 9pt; color: #94a3b8; margin-top: 2px; }
    .top .contact { margin-left: auto; text-align: right; font-family: monospace; font-size: 7.5pt; line-height: 1.8; color: #94a3b8; }
    .top .contact a { color: var(--green); text-decoration: none; }
    .layout { display: grid; grid-template-columns: 32% 68%; }
    .sidebar { padding: 18px 16px 22px 22px; border-right: 1px solid var(--border); background: #f8fafc; }
    .main { padding: 18px 22px 22px 16px; }
    .sidebar-section { margin-bottom: 14px; }
    .sidebar-section h2 { font-family: monospace; font-size: 7pt; text-transform: uppercase; letter-spacing: .08em; color: var(--green-d); margin-bottom: 6px; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 8pt; padding: 3px 7px; background: #fff; border: 1px solid var(--border); border-radius: 3px; font-family: monospace; }
    .edu-degree { font-weight: 600; font-size: 9pt; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: var(--muted); }
    .main h2 { font-family: monospace; font-size: 9pt; margin-bottom: 8px; margin-top: 14px; }
    .main h2::before { content: '## '; color: var(--green-d); }
    .main h2:first-child { margin-top: 0; }
    .summary { padding: 10px 12px; background: #f8fafc; border-left: 3px solid var(--green); border-radius: 0 6px 6px 0; }
    .summary strong { color: var(--slate); }
    .job-period { font-family: monospace; font-size: 8pt; color: var(--green-d); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <header class="top">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div><h1>{NAME} <span>{{ odoo_dev }}</span></h1><div class="role">{ROLE}</div></div>
    <div class="contact">
      <a href="mailto:dinhvankhoa14091999@gmail.com">dinhvankhoa14091999@gmail.com</a><br>
      0982 594 840 · Hải Phòng<br>
      <a href="https://github.com/JocelynVN">github.com/JocelynVN</a>
    </div>
  </header>
  <div class="layout">
    <aside class="sidebar">{sidebar_skills(6)}</aside>
    <main class="main">{main_content(6)}</main>
  </div>
</div>'''
    return wrap(f"CV Tech — {NAME}", css, body)


def gen_nordic():
    css = '''
    :root { --ink: #2e3440; --muted: #4c566a; --frost: #eceff4; --accent: #5e81ac; --border: #d8dee9; --text: #2e3440; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.5; color: var(--ink); background: var(--frost); print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; padding: 40px 44px; box-shadow: 0 2px 16px rgba(46,52,64,.08); }
    .head { display: flex; gap: 24px; align-items: center; margin-bottom: 28px; padding-bottom: 24px; border-bottom: 1px solid var(--border); }
    .avatar { width: 92px; height: 92px; border-radius: 50%; object-fit: cover; object-position: center 15%; }
    .head h1 { font-size: 21pt; font-weight: 300; letter-spacing: -.02em; color: var(--ink); }
    .head .role { font-size: 9.5pt; color: var(--accent); margin-top: 4px; font-weight: 500; }
    .contact { margin-top: 10px; display: flex; flex-wrap: wrap; gap: 4px 18px; font-size: 8.5pt; color: var(--muted); }
    .contact a { color: var(--accent); text-decoration: none; }
    .ci { display: inline-flex; align-items: center; gap: 5px; }
    .ci svg { width: 12px; height: 12px; color: var(--accent); }
    .layout { display: grid; grid-template-columns: 28% 72%; gap: 32px; }
    .sidebar-section { margin-bottom: 20px; }
    .sidebar-section h2 { font-size: 7pt; font-weight: 600; text-transform: uppercase; letter-spacing: .14em; color: var(--muted); margin-bottom: 8px; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 8pt; color: var(--ink); padding: 2px 0; border-bottom: 1px solid var(--border); width: 100%; }
    .edu-degree { font-weight: 600; font-size: 9pt; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: var(--muted); }
    .main h2 { font-size: 8pt; font-weight: 600; text-transform: uppercase; letter-spacing: .12em; color: var(--muted); margin-bottom: 10px; margin-top: 20px; }
    .main h2:first-child { margin-top: 0; }
    .summary { font-size: 10pt; color: var(--muted); text-align: justify; }
    .summary strong { color: var(--ink); }
    .job { padding-left: 14px; border-left: 2px solid var(--border); }
    .job-title { color: var(--ink); font-weight: 600; }
    .job-period { color: var(--accent); }
    .project { padding-left: 14px; border-left: 2px solid var(--frost); }
''' + SHARED_MAIN_CSS

    contact = "".join(
        f'<span class="ci">{ICONS[icon]}' + (f'<a href="{href}">{text}</a>' if href else text) + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <header class="head">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <div><h1>{NAME}</h1><div class="role">{ROLE}</div><div class="contact">{contact}</div></div>
  </header>
  <div class="layout">
    <aside>{sidebar_skills(4)}</aside>
    <main class="main">{main_content(4)}</main>
  </div>
</div>'''
    return wrap(f"CV Nordic — {NAME}", css, body)


def gen_forest():
    css = '''
    :root { --forest: #1b4332; --forest-l: #2d6a4f; --sage: #d8f3dc; --text: #1b4332; --muted: #52796f; --border: #b7e4c7; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: Georgia, serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #e9f5e9; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; display: grid; grid-template-columns: 34% 66%; background: #fff; box-shadow: 0 4px 20px rgba(27,67,50,.12); }
    .sidebar { background: var(--forest); color: #fff; padding: 28px 20px; }
    .avatar { width: 105px; height: 105px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 3px solid var(--sage); display: block; margin: 0 auto 16px; }
    .sidebar h1 { font-size: 16pt; text-align: center; margin-bottom: 4px; }
    .sidebar .role { text-align: center; font-size: 8.5pt; color: var(--sage); margin-bottom: 22px; line-height: 1.35; padding-bottom: 16px; border-bottom: 1px solid var(--forest-l); }
    .sidebar-section { margin-bottom: 18px; }
    .sidebar-section h2 { font-size: 7.5pt; text-transform: uppercase; letter-spacing: .12em; color: var(--sage); margin-bottom: 8px; }
    .contact-list { list-style: none; }
    .contact-list li { display: flex; gap: 8px; margin-bottom: 9px; font-size: 8.5pt; color: #d8f3dc; }
    .contact-icon svg { width: 13px; height: 13px; color: var(--sage); flex-shrink: 0; margin-top: 2px; }
    .contact-list a { color: #fff; text-decoration: none; }
    .contact-label { display: block; font-size: 6.5pt; text-transform: uppercase; color: var(--sage); }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 8px; background: var(--forest-l); border-radius: 4px; }
    .edu-degree { font-weight: 700; font-size: 9pt; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: #b7e4c7; }
    .main { padding: 26px 24px 22px; font-family: system-ui, sans-serif; }
    .main h2 { font-size: 11pt; color: var(--forest); border-bottom: 2px solid var(--sage); padding-bottom: 4px; margin-bottom: 10px; }
    .summary strong { color: var(--forest); }
    .job-title { color: var(--forest); }
    .job-period { color: var(--forest-l); }
    .job li::marker { color: var(--forest-l); }
    .project-header { color: var(--forest); }
    .ai-section .job li strong { color: var(--forest); }
''' + SHARED_MAIN_CSS.replace('var(--border)', 'var(--border)')

    body = f'''<div class="cv">
  <aside class="sidebar">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1>{NAME}</h1>
    <div class="role">{ROLE_BR}</div>
    <div class="sidebar-section"><h2>Liên hệ</h2><ul class="contact-list">{contact_sidebar(6)}</ul></div>
    {sidebar_skills(4)}
  </aside>
  <main class="main">{main_content(4)}</main>
</div>'''
    return wrap(f"CV Forest — {NAME}", css, body)


def gen_indigo():
    css = '''
    :root { --indigo: #4338ca; --indigo-l: #6366f1; --lavender: #eef2ff; --text: #1e1b4b; --muted: #64748b; --border: #c7d2fe; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #e0e7ff; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; display: grid; grid-template-columns: 68% 32%; background: #fff; box-shadow: 0 6px 24px rgba(67,56,202,.15); }
    .main { padding: 28px 24px 24px 28px; }
    .sidebar { background: var(--lavender); padding: 28px 18px; border-left: 1px solid var(--border); }
    .sb-top { text-align: center; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--border); }
    .avatar { width: 100px; height: 100px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 3px solid var(--indigo-l); margin-bottom: 12px; }
    .sidebar h1 { font-size: 14pt; color: var(--indigo); margin-bottom: 4px; }
    .sidebar .role { font-size: 8.5pt; color: var(--indigo-l); font-weight: 600; line-height: 1.35; }
    .sidebar-section { margin-bottom: 16px; }
    .sidebar-section h2 { font-size: 7.5pt; text-transform: uppercase; letter-spacing: .1em; color: var(--indigo); margin-bottom: 8px; font-weight: 700; }
    .contact-list { list-style: none; }
    .contact-list li { margin-bottom: 8px; font-size: 8pt; color: var(--muted); }
    .contact-list a { color: var(--indigo); text-decoration: none; }
    .contact-label { display: block; font-size: 6.5pt; text-transform: uppercase; color: var(--indigo-l); font-weight: 600; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 7px; background: #fff; border: 1px solid var(--border); border-radius: 4px; color: var(--text); }
    .edu-degree { font-weight: 600; font-size: 9pt; color: var(--text); }
    .edu-school, .edu-meta { font-size: 8.5pt; color: var(--muted); }
    .main h2 { font-size: 11pt; color: var(--indigo); margin-bottom: 8px; display: flex; align-items: center; gap: 8px; }
    .main h2::after { content: ''; flex: 1; height: 1px; background: var(--border); }
    .summary strong { color: var(--indigo); }
    .job-title { color: var(--indigo); }
    .job-period { color: var(--indigo-l); }
    .project-header { color: var(--indigo); }
    .ai-section .job li strong { color: var(--indigo); }
''' + SHARED_MAIN_CSS

    contact_simple = "".join(
        f'<li><span class="contact-label">{label}</span>'
        + (f'<a href="{href}">{text}</a>' if href else text)
        + '</li>'
        for label, text, href, _ in CONTACT
    )

    body = f'''<div class="cv">
  <main class="main">{main_content(4)}</main>
  <aside class="sidebar">
    <div class="sb-top">
      <img class="avatar" src="avatar.png" alt="{NAME}">
      <h1>{NAME}</h1>
      <div class="role">{ROLE_BR}</div>
    </div>
    <div class="sidebar-section"><h2>Liên hệ</h2><ul class="contact-list">{contact_simple}</ul></div>
    {sidebar_skills(4)}
  </aside>
</div>'''
    return wrap(f"CV Indigo — {NAME}", css, body)


def gen_newspaper():
    css = '''
    :root { --black: #1a1a1a; --gray: #555; --rule: #ccc; --text: #1a1a1a; --muted: #555; --border: #ccc; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: Georgia, 'Times New Roman', serif; font-size: 10.5pt; line-height: 1.45; color: var(--black); background: #f0f0f0; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; padding: 32px 36px; box-shadow: 0 2px 10px rgba(0,0,0,.1); }
    .masthead { text-align: center; border-top: 4px double var(--black); border-bottom: 4px double var(--black); padding: 16px 0; margin-bottom: 16px; }
    .masthead h1 { font-size: 24pt; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; }
    .masthead .role { font-size: 10pt; font-style: italic; color: var(--gray); margin: 4px 0 10px; }
    .masthead .contact { font-size: 8.5pt; color: var(--gray); display: flex; justify-content: center; flex-wrap: wrap; gap: 4px 16px; font-family: system-ui, sans-serif; }
    .masthead a { color: var(--black); }
    .masthead .avatar { width: 80px; height: 80px; border-radius: 4px; object-fit: cover; object-position: center 15%; float: left; margin: 0 16px 8px 0; border: 1px solid var(--rule); }
    .skills-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; padding: 12px 0; border-bottom: 1px solid var(--rule); margin-bottom: 14px; font-family: system-ui, sans-serif; }
    .skills-row h3 { font-size: 7pt; text-transform: uppercase; letter-spacing: .1em; border-bottom: 1px solid var(--black); padding-bottom: 2px; margin-bottom: 5px; }
    .skills-row p { font-size: 8.5pt; color: var(--gray); line-height: 1.55; }
    h2 { font-size: 11pt; font-variant: small-caps; letter-spacing: .08em; border-bottom: 1px solid var(--black); padding-bottom: 3px; margin: 14px 0 8px; }
    .summary { font-size: 10pt; text-align: justify; column-count: 1; }
    .summary strong { font-weight: 700; }
    .two-col { column-count: 2; column-gap: 24px; }
    .job { break-inside: avoid; margin-bottom: 10px; }
    .job-title { font-weight: 700; font-size: 10pt; }
    .job-period { font-size: 8.5pt; color: var(--gray); font-style: italic; }
    .job-company { font-size: 9pt; font-style: italic; }
    .job ul { padding-left: 14px; font-family: system-ui, sans-serif; font-size: 9pt; }
    .project { break-inside: avoid; margin-bottom: 8px; font-size: 9.5pt; }
    .project-header { font-weight: 700; }
    .project-meta { font-weight: 400; color: var(--gray); font-size: 9pt; }
    .project ul { font-family: system-ui, sans-serif; font-size: 9pt; padding-left: 14px; }
''' + SHARED_MAIN_CSS

    contact = " · ".join(
        f'<a href="{href}">{text}</a>' if href else text for _, text, href, _ in CONTACT
    )

    body = f'''<div class="cv">
  <header class="masthead">
    <img class="avatar" src="avatar.png" alt="{NAME}">
    <h1>{NAME}</h1>
    <div class="role">{ROLE}</div>
    <div class="contact">{contact}</div>
  </header>
  <div class="skills-row">
    <div><h3>Odoo / Dev</h3><p>{" · ".join(SKILLS_ODOO)}</p></div>
    <div><h3>Ứng dụng AI</h3><p>{" · ".join(SKILLS_AI)}</p></div>
    <div><h3>Học vấn</h3><p>{EDU["degree"]}<br>{EDU["school"]}<br>{EDU["meta"]}</p></div>
  </div>
  <h2>Tóm tắt</h2>
  <p class="summary">{SUMMARY}</p>
  <h2>Kinh nghiệm làm việc</h2>
  <div class="two-col">{jobs_html(2)}</div>
  <h2>Ứng dụng AI &amp; Tự động hóa quy trình</h2>
  <div class="job"><ul>{"".join(f"<li>{b}</li>" for b in AI_BULLETS)}</ul></div>
  <h2>Dự án tiêu biểu</h2>
  <p class="section-note">{PROJECT_NOTE}</p>
  <div class="two-col">{projects_html(2)}
  <div class="projects-more" style="column-span:all">
    <span class="projects-more-label">Các dự án &amp; hạng mục khác đã tham gia:</span>
    <div class="projects-tags">{"".join(f"<span>{t}</span>" for t in MORE_TAGS)}</div>
    {MORE_TEXT}
    <span class="projects-cta">{MORE_CTA}</span>
  </div></div>
</div>'''
    return wrap(f"CV Newspaper — {NAME}", css, body)


def gen_geometric():
    css = '''
    :root { --orange: #ea580c; --orange-l: #fb923c; --dark: #1c1917; --text: #292524; --muted: #78716c; --border: #e7e5e4; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #fafaf9; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; box-shadow: 0 4px 24px rgba(0,0,0,.08); overflow: hidden; }
    .accent-bar { height: 8px; background: linear-gradient(90deg, var(--orange), var(--orange-l), var(--dark)); }
    .top { padding: 24px 28px; display: grid; grid-template-columns: 1fr auto; gap: 20px; align-items: start; }
    .top-left { display: flex; gap: 20px; align-items: center; }
    .avatar { width: 88px; height: 88px; clip-path: polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%); object-fit: cover; object-position: center 15%; }
    .top h1 { font-size: 20pt; font-weight: 800; color: var(--dark); letter-spacing: -.03em; }
    .top .role { font-size: 9.5pt; color: var(--orange); font-weight: 600; margin-top: 3px; }
    .contact-block { font-size: 8pt; color: var(--muted); line-height: 1.7; text-align: right; }
    .contact-block a { color: var(--orange); text-decoration: none; font-weight: 500; }
    .body { display: grid; grid-template-columns: 30% 70%; }
    .sidebar { background: var(--dark); color: #fafaf9; padding: 22px 18px; }
    .sidebar-section { margin-bottom: 16px; }
    .sidebar-section h2 { font-size: 7pt; text-transform: uppercase; letter-spacing: .14em; color: var(--orange-l); margin-bottom: 8px; font-weight: 700; }
    .skill-tags { display: flex; flex-wrap: wrap; gap: 4px; }
    .skill-tag { font-size: 7.5pt; padding: 3px 7px; background: #292524; border-left: 2px solid var(--orange); color: #e7e5e4; }
    .edu-degree { font-weight: 700; font-size: 9pt; color: #fff; }
    .edu-school, .edu-meta { font-size: 8.5pt; color: #a8a29e; }
    .main { padding: 22px 24px 24px 20px; }
    .main h2 { font-size: 10pt; font-weight: 800; text-transform: uppercase; letter-spacing: .06em; color: var(--dark); margin-bottom: 8px; margin-top: 14px; display: inline-block; border-bottom: 3px solid var(--orange); padding-bottom: 2px; }
    .main h2:first-child { margin-top: 0; }
    .summary strong { color: var(--orange); }
    .job-title { color: var(--dark); font-weight: 700; }
    .job-period { color: var(--orange); font-weight: 600; }
    .job li::marker { color: var(--orange); }
    .project-header { color: var(--dark); }
    .ai-section .job li strong { color: var(--orange); }
''' + SHARED_MAIN_CSS

    body = f'''<div class="cv">
  <div class="accent-bar"></div>
  <header class="top">
    <div class="top-left">
      <img class="avatar" src="avatar.png" alt="{NAME}">
      <div><h1>{NAME}</h1><div class="role">{ROLE}</div></div>
    </div>
    <div class="contact-block">
      <a href="mailto:dinhvankhoa14091999@gmail.com">dinhvankhoa14091999@gmail.com</a><br>
      0982 594 840<br>Tiên Minh, Hải Phòng<br>
      <a href="https://github.com/JocelynVN">github.com/JocelynVN</a>
    </div>
  </header>
  <div class="body">
    <aside class="sidebar">{sidebar_skills(4)}</aside>
    <main class="main">{main_content(4)}</main>
  </div>
</div>'''
    return wrap(f"CV Geometric — {NAME}", css, body)


def gen_ocean():
    css = '''
    :root { --ocean: #0369a1; --ocean-l: #0ea5e9; --sky: #f0f9ff; --text: #0c4a6e; --muted: #64748b; --border: #bae6fd; }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: system-ui, sans-serif; font-size: 10.5pt; line-height: 1.45; color: var(--text); background: #e0f2fe; print-color-adjust: exact; }
    .cv { max-width: 210mm; margin: 16px auto; background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 8px 30px rgba(3,105,161,.15); }
    .wave { height: 6px; background: repeating-linear-gradient(90deg, var(--ocean), var(--ocean-l) 20px, var(--ocean) 40px); }
    .wrap { padding: 26px 28px 24px; }
    .profile { display: flex; gap: 22px; background: var(--sky); border-radius: 12px; padding: 20px; margin-bottom: 20px; }
    .avatar { width: 96px; height: 96px; border-radius: 50%; object-fit: cover; object-position: center 15%; border: 4px solid #fff; box-shadow: 0 2px 12px rgba(3,105,161,.2); flex-shrink: 0; }
    .profile h1 { font-size: 19pt; font-weight: 700; color: var(--ocean); }
    .profile .role { font-size: 9.5pt; color: var(--ocean-l); font-weight: 600; margin: 3px 0 10px; }
    .profile .contact { font-size: 8.5pt; color: var(--muted); display: flex; flex-wrap: wrap; gap: 4px 14px; }
    .profile a { color: var(--ocean); text-decoration: none; }
    .ci { display: inline-flex; align-items: center; gap: 4px; }
    .ci svg { width: 11px; height: 11px; color: var(--ocean-l); }
    .chips { display: flex; flex-wrap: wrap; gap: 16px; margin-bottom: 18px; padding-bottom: 16px; border-bottom: 1px dashed var(--border); }
    .chip-group h3 { font-size: 7pt; text-transform: uppercase; letter-spacing: .1em; color: var(--ocean-l); margin-bottom: 5px; }
    .chip-group p { font-size: 8.5pt; color: var(--muted); line-height: 1.6; max-width: 200px; }
    .main h2 { font-size: 10pt; color: var(--ocean); background: var(--sky); display: inline-block; padding: 4px 12px; border-radius: 4px; margin-bottom: 10px; margin-top: 14px; }
    .main h2:first-child { margin-top: 0; }
    .summary { background: var(--sky); padding: 12px 14px; border-radius: 8px; font-size: 10pt; text-align: justify; }
    .summary strong { color: var(--ocean); }
    .job { background: #fff; border: 1px solid var(--border); border-radius: 6px; padding: 10px 12px; }
    .job-title { color: var(--ocean); }
    .job-period { color: var(--ocean-l); }
    .project { border: 1px solid var(--border); border-radius: 6px; padding: 8px 10px; background: #fafcff; }
    .project-header { color: var(--ocean); }
    .ai-section .job li strong { color: var(--ocean); }
''' + SHARED_MAIN_CSS.replace('.job { margin-bottom: 14px; }', '.job { margin-bottom: 10px; }')

    contact = "".join(
        f'<span class="ci">{ICONS[icon]}' + (f'<a href="{href}">{text}</a>' if href else text) + '</span>'
        for _, text, href, icon in CONTACT
    )

    body = f'''<div class="cv">
  <div class="wave"></div>
  <div class="wrap">
    <div class="profile">
      <img class="avatar" src="avatar.png" alt="{NAME}">
      <div>
        <h1>{NAME}</h1>
        <div class="role">{ROLE}</div>
        <div class="contact">{contact}</div>
      </div>
    </div>
    <div class="chips">
      <div class="chip-group"><h3>Odoo / Dev</h3><p>{" · ".join(SKILLS_ODOO)}</p></div>
      <div class="chip-group"><h3>Ứng dụng AI</h3><p>{" · ".join(SKILLS_AI)}</p></div>
      <div class="chip-group"><h3>Kỹ năng mềm</h3><p>{" · ".join(SKILLS_SOFT)}</p></div>
      <div class="chip-group"><h3>Học vấn</h3><p>{EDU["degree"]}<br>{EDU["school"]}<br>{EDU["meta"]}</p></div>
    </div>
    <main class="main">{main_content(4)}</main>
  </div>
</div>'''
    return wrap(f"CV Ocean — {NAME}", css, body)


STYLES = {
    "dinh-van-khoa-cv-modern.html": gen_modern,
    "dinh-van-khoa-cv-dark.html": gen_dark,
    "dinh-van-khoa-cv-minimal.html": gen_minimal,
    "dinh-van-khoa-cv-elegant.html": gen_elegant,
    "dinh-van-khoa-cv-corporate.html": gen_corporate,
    "dinh-van-khoa-cv-creative.html": gen_creative,
    "dinh-van-khoa-cv-tech.html": gen_tech,
    "dinh-van-khoa-cv-nordic.html": gen_nordic,
    "dinh-van-khoa-cv-forest.html": gen_forest,
    "dinh-van-khoa-cv-indigo.html": gen_indigo,
    "dinh-van-khoa-cv-newspaper.html": gen_newspaper,
    "dinh-van-khoa-cv-geometric.html": gen_geometric,
    "dinh-van-khoa-cv-ocean.html": gen_ocean,
}


ALL_CV_HTML = ["dinh-van-khoa-cv.html", *STYLES.keys()]

PDF_EXPORT_CSS = """
    /* PDF export overrides */
    @page { size: A4; margin: 0; }
    html, body {
      margin: 0 !important;
      padding: 0 !important;
      background: #fff !important;
      container-type: normal !important;
      -webkit-print-color-adjust: exact;
      print-color-adjust: exact;
    }
    .cv-page, .cv {
      margin: 0 !important;
      box-shadow: none !important;
      max-width: none !important;
      width: 100% !important;
      min-height: auto !important;
      border-radius: 0 !important;
      overflow: visible !important;
    }
    .cv-page {
      display: grid !important;
      grid-template-columns: 32% 68% !important;
    }
    .cv {
      display: grid !important;
    }
    .sidebar, aside.sidebar {
      width: auto !important;
      border-bottom: none !important;
    }
    .body, .layout {
      display: grid !important;
    }
    .job-header {
      flex-direction: row !important;
      align-items: baseline !important;
    }
    .job-period {
      white-space: nowrap !important;
    }
    .job, .project, .profile, .chips, .projects-more, .summary {
      break-inside: avoid !important;
      page-break-inside: avoid !important;
    }
    .main-section > h2, .main h2 {
      break-after: avoid !important;
      page-break-after: avoid !important;
    }
"""


def _avatar_data_uri():
    import base64

    avatar_path = DIR / "avatar.png"
    if not avatar_path.exists():
        return None
    data = avatar_path.read_bytes()
    if data[:3] == b"\xff\xd8\xff":
        mime = "image/jpeg"
    elif data[:8] == b"\x89PNG\r\n\x1a\n":
        mime = "image/png"
    else:
        mime = "image/png"
    encoded = base64.b64encode(data).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def _prepare_pdf_html(html_path):
    import re

    content = html_path.read_text(encoding="utf-8")
    if "/* PDF export overrides */" not in content:
        content = content.replace("</style>", PDF_EXPORT_CSS + "\n  </style>", 1)
    avatar_src = _avatar_data_uri()
    if avatar_src:
        content = content.replace('src="avatar.png"', f'src="{avatar_src}"')
        content = re.sub(
            r'src="(?:file://[^"]*avatar\.png|data:image/[^;]+;base64,[^"]+)"',
            f'src="{avatar_src}"',
            content,
        )
    tmp_dir = DIR / ".pdf-tmp"
    tmp_dir.mkdir(exist_ok=True)
    tmp_path = tmp_dir / html_path.name
    tmp_path.write_text(content, encoding="utf-8")
    return tmp_path


def _find_chrome():
    import shutil

    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        path = shutil.which(name)
        if path:
            return path
    return None


def export_pdfs():
    import shutil
    import subprocess

    pdf_dir = DIR / "pdf"
    pdf_dir.mkdir(exist_ok=True)
    chrome = _find_chrome()
    wkhtml_bin = shutil.which("wkhtmltopdf")
    if not chrome and not wkhtml_bin:
        print("✗ Không tìm thấy Chrome hay wkhtmltopdf — bỏ qua xuất PDF")
        return

    engine = "Chrome headless" if chrome else "wkhtmltopdf"
    print(f"PDF engine: {engine}")

    for html_name in ALL_CV_HTML:
        html_path = DIR / html_name
        if not html_path.exists():
            print(f"✗ Bỏ qua (không có file): {html_name}")
            continue
        pdf_name = html_name.replace(".html", ".pdf")
        pdf_path = pdf_dir / pdf_name
        pdf_html_path = _prepare_pdf_html(html_path)
        if chrome:
            cmd = [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--allow-file-access-from-files",
                "--run-all-compositor-stages-before-draw",
                "--virtual-time-budget=10000",
                "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}",
                pdf_html_path.resolve().as_uri(),
            ]
        else:
            cmd = [
                wkhtml_bin,
                "--quiet",
                "--page-size", "A4",
                "--margin-top", "0",
                "--margin-bottom", "0",
                "--margin-left", "0",
                "--margin-right", "0",
                "--encoding", "UTF-8",
                "--disable-smart-shrinking",
                "--enable-local-file-access",
                str(pdf_html_path),
                str(pdf_path),
            ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if result.returncode == 0 and pdf_path.exists():
            print(f"✓ pdf/{pdf_name}")
        else:
            err = result.stderr.strip() or result.stdout.strip() or "lỗi không xác định"
            print(f"✗ pdf/{pdf_name}: {err}")


def main(export_pdf=True):
    for filename, generator in STYLES.items():
        path = DIR / filename
        path.write_text(generator(), encoding="utf-8")
        print(f"✓ {filename}")
    if export_pdf:
        print("— Xuất PDF —")
        export_pdfs()


if __name__ == "__main__":
    import sys
    pdf_only = "--pdf-only" in sys.argv
    if pdf_only:
        export_pdfs()
    else:
        main(export_pdf=True)
