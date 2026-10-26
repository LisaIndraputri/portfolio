#!/usr/bin/env python3
"""Write Lisa_Indraputri_CV.docx from the agreed portfolio copy."""

import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parents[1] / "Lisa_Indraputri_CV.docx"

BLOCKS = [
    ("name", "Lisa Indraputri"),
    ("role", "Senior Software Development Engineer"),
    ("meta", "Jakarta  ·  lisaindraputri98@gmail.com  ·  linkedin.com/in/lisa-indraputri"),
    ("h", "SUMMARY"),
    ("p", "Front-end engineer building mobile web for DANA, an Indonesian digital wallet. At DANA since 2019, from intern to Senior Software Development Engineer. Works in Vue, Nuxt, and React, and uses Web Vitals, product analytics, and AI-assisted tooling to keep critical flows reliable."),
    ("h", "EXPERIENCE"),
    ("job", "Senior Software Development Engineer"),
    ("when", "2025 – Present"),
    ("where", "DANA Indonesia, Jakarta  ·  Social and Account Recovery"),
    ("li", "Delivered Social features: the Feeds revamp, birthday feeds, and in-app chat with media, and wrote the system analysis for each release."),
    ("li", "Own Account Recovery end to end: change number with risk checks, account transfer, account merge, lost-phone recovery, and change number via link."),
    ("li", "Surfaced real native error codes on all 4 recovery flows, and traced a conversion drop to network errors on the eligibility check."),
    ("li", "Brought TypeScript to zero errors across the app and its tests, and kept a 1,500+ Vitest suite green."),
    ("li", "Implemented the design system on 4 web apps, with a visual-regression audit on each change."),
    ("li", "Improved Core Web Vitals on high-traffic recovery pages and set up a repeatable Lighthouse measurement."),
    ("li", "Introduced AI-assisted tooling for CI monitoring, ticket updates, QA test cases, and incident triage."),
    ("job", "Software Development Engineer"),
    ("when", "2022 – 2024"),
    ("where", "DANA Indonesia, Jakarta  ·  Deals, Promotions, and B2B  ·  promoted to Senior SDE"),
    ("li", "Built the front end for DANA Deals & Promotions and B2B web products."),
    ("li", "Delivered the Deals 2.0 redesign: voucher search, category pills, visual filters, recommendation sorting, and skeleton loading."),
    ("li", "Built Buy as Gift end to end, from custom themes and messages to birthday notifications and back-office gifting tools."),
    ("li", "Shipped growth integrations: a universal deeplink for search ads, audience-targeted click-to-claim deals, and Google Ads attribution."),
    ("li", "Made seasonal campaign assets configurable, so Ramadan, Chinese New Year, and 11.11 no longer needed a manual swap."),
    ("li", "Built B2B features: role-based menus, enterprise-wallet cash-out approval, and a QoS dashboard."),
    ("li", "Authored 25+ system analysis documents."),
    ("job", "Associate Software Development Engineer"),
    ("when", "Dec 2019 – 2021"),
    ("where", "DANA Indonesia, Jakarta"),
    ("li", "Built online-to-offline and financial-service features on a stable, maintainable codebase."),
    ("li", "Checked UI/UX designs for technical feasibility."),
    ("li", "Learned the product, improved performance, and fixed defects."),
    ("li", "Improved stability and the user experience, working with the rest of the team."),
    ("job", "Front-End Engineer Intern"),
    ("when", "2019"),
    ("where", "DANA Indonesia, Jakarta"),
    ("li", "Built a website from scratch in Vue and Laravel."),
    ("li", "Improved performance through SEO, and checked UI/UX designs for technical feasibility."),
    ("h", "SELECTED WORK"),
    ("job", "Trip Craft"),
    ("when", "trip-craft-phi.vercel.app"),
    ("where", "Shared trip planner  ·  Nuxt, Supabase, Gemini"),
    ("li", "People on one trip share dates, places, flights, stays, and an itinerary, and join by link."),
    ("li", "A day plan can be suggested by Gemini and saved on the trip."),
    ("job", "STTAA Admissions"),
    ("when", "admisi.sttaa.ac.id"),
    ("where", "Sekolah Tinggi Teologi Amanat Agung  ·  Vue"),
    ("li", "Live admissions site: open waves, registration forms, recommendations, application status, and the registration payment."),
    ("h", "EDUCATION"),
    ("job", "BINUS University"),
    ("when", "2016 – 2020"),
    ("where", "Computer Science  ·  IPK 3.95"),
    ("h", "SKILLS"),
    ("p", "Vue, Nuxt, React, TypeScript, Laravel, Tailwind, Web Vitals, Sentry, Mixpanel, Jira, Notion, AI-assisted tooling."),
]


def paragraph(kind, text):
    text = escape(text)
    if kind == "name":
        style, size, bold, after = "Name", "32", True, "40"
    elif kind == "role":
        style, size, bold, after = "Role", "22", False, "40"
    elif kind == "meta":
        style, size, bold, after = "Meta", "18", False, "160"
    elif kind == "h":
        style, size, bold, after = "Heading", "20", True, "60"
    elif kind == "job":
        style, size, bold, after = "Job", "22", True, "0"
    elif kind == "when":
        style, size, bold, after = "When", "18", False, "0"
    elif kind == "where":
        style, size, bold, after = "Where", "18", False, "40"
    elif kind == "li":
        style, size, bold, after = "Bullet", "20", False, "40"
    else:
        style, size, bold, after = "Body", "20", False, "80"
    bold_xml = "<w:b/>" if bold else ""
    bullet = '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>' if kind == "li" else ""
    return (
        f'<w:p><w:pPr><w:pStyle w:val="{style}"/>{bullet}'
        f'<w:spacing w:after="{after}" w:line="240" w:lineRule="auto"/></w:pPr>'
        f'<w:r><w:rPr>{bold_xml}<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
        f'<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri"/></w:rPr>'
        f"<w:t xml:space=\"preserve\">{text}</w:t></w:r></w:p>"
    )


DOCUMENT = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {''.join(paragraph(kind, text) for kind, text in BLOCKS)}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="864" w:right="864" w:bottom="864" w:left="864"/>
    </w:sectPr>
  </w:body>
</w:document>
"""

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>
"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>
"""

NUMBERING = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:abstractNum w:abstractNumId="0">
    <w:multiLevelType w:val="hybridMultilevel"/>
    <w:lvl w:ilvl="0">
      <w:start w:val="1"/>
      <w:numFmt w:val="bullet"/>
      <w:lvlText w:val="•"/>
      <w:lvlJc w:val="left"/>
      <w:pPr><w:ind w:left="420" w:hanging="240"/></w:pPr>
    </w:lvl>
  </w:abstractNum>
  <w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>
"""

STYLES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:style w:type="paragraph" w:default="1" w:styleId="Body">
    <w:name w:val="Body"/><w:qFormat/>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Name"><w:name w:val="Name"/></w:style>
  <w:style w:type="paragraph" w:styleId="Role"><w:name w:val="Role"/></w:style>
  <w:style w:type="paragraph" w:styleId="Meta"><w:name w:val="Meta"/></w:style>
  <w:style w:type="paragraph" w:styleId="Heading"><w:name w:val="Heading"/></w:style>
  <w:style w:type="paragraph" w:styleId="Job"><w:name w:val="Job"/></w:style>
  <w:style w:type="paragraph" w:styleId="When"><w:name w:val="When"/></w:style>
  <w:style w:type="paragraph" w:styleId="Where"><w:name w:val="Where"/></w:style>
  <w:style w:type="paragraph" w:styleId="Bullet"><w:name w:val="Bullet"/></w:style>
</w:styles>
"""


def main():
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", CONTENT_TYPES)
        docx.writestr("_rels/.rels", RELS)
        docx.writestr("word/document.xml", DOCUMENT)
        docx.writestr("word/_rels/document.xml.rels", DOC_RELS)
        docx.writestr("word/numbering.xml", NUMBERING)
        docx.writestr("word/styles.xml", STYLES)
    print(OUT)


if __name__ == "__main__":
    main()
