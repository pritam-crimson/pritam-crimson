<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,50:0d1117,100:1f1f1f&height=220&section=header&text=PRITAM%20LASKAR&fontSize=64&fontColor=ffffff&fontAlignY=38&desc=Data%20%26%20Automation%20Engineer%20%E2%80%A2%20Crimson%20Education&descSize=18&descAlignY=60&descColor=9ca3af" />

<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=1200&color=E5E7EB&center=true&vCenter=true&width=700&lines=Humans+decide.+Machines+do+the+doing.;I+automate+the+boring+stuff.;Cron+jobs+don%27t+sleep.+Neither+do+my+pipelines.;If+you+can%27t+follow+it%2C+you+can%27t+trust+it." alt="Typing SVG" /></a>

<br/>

[![Portfolio](https://img.shields.io/badge/PORTFOLIO-pritamlaskar.github.io-000000?style=for-the-badge&logo=safari&logoColor=white)](https://pritamlaskar.github.io/)
[![Crimson](https://img.shields.io/badge/@-Crimson_Education-8B0000?style=for-the-badge)](https://github.com/crimson-education)
![Bangkok](https://img.shields.io/badge/BASED_IN-BANGKOK-111111?style=for-the-badge)
![Timezone](https://img.shields.io/badge/OVERLAP-US_%7C_UK_%7C_EU-111111?style=for-the-badge)

</div>

---

## ⚫ `whoami`

```bash
$ whoami
pritam  # data & automation engineer

$ cat about.txt
3+ years automating real operations, from a YC-backed startup to one of Ireland's biggest retailers.
UCD (Dublin) Master's on scholarship. Now building the data engine behind Crimson Education.
I don't replace people. I multiply them: kill the copy-paste, the chasing, the checking.

$ cat philosophy.txt
1. Humans decide. Machines do the doing.
2. Automate the boring. Keep the judgement calls.
3. Always explainable. Nothing gets written to production without a human saying yes.
```

---

## 🔥 What I build

<table>
<tr>
<td width="50%" valign="top">

### 🕸️ Monitors that never sleep
Scheduled pipelines that read official college and program websites, compare them with the source of truth, and surface only the differences.

### 🧠 AI with guardrails
LLMs extract facts, **fixed rules make the decision**. Confidence tiers, quote-on-page checks, majority-vote reads.

</td>
<td width="50%" valign="top">

### 🧑‍⚖️ Human-in-the-loop by design
Review queues, approval flags and write-only-after-yes. Automation does the legwork, a person owns the final call.

### 🛠️ Self-healing, observable
Hash-based change detection (skip unchanged pages, save AI calls), resumable state, Slack summaries, JSON run logs.

</td>
</tr>
</table>

---

## 🧪 Things I've shipped at Crimson

> Source is private (company code). Here's what they do.

| Project | What it does | Stack |
|---|---|---|
| ⏰ **Deadline Monitor** | Weekly GitHub Actions run checks first-year application deadlines on each college's own site, diffs them against the CMS, and sends mismatches to a review table. Approved rows are pushed live on a schedule, verified, and archived. Nothing is published without a human `TRUE`. | `Python` `GitHub Actions` `Contentful` `Baserow` `Gemini` `Scrapling` `Tavily` |
| 📝 **Test Score Monitor** | Weekly policy check of ~1,000 US colleges' SAT/ACT stance. LLM answers *facts*, a decision table assigns one of 5 labels, and diffs must pass a 2-of-3 vote with a verbatim quote before they're raised. | `Python` `GitHub Actions` `Contentful` `Baserow` `Google Sheets` `LLMs` |
| ☀️ **Summer Program Monitor** | Always-on worker checks every summer program for 2027 dates and tuition, then runs **extract → verify → auto-apply → validate** with HIGH / MEDIUM / LOW confidence routing. Review-only, never writes to the search index. | `Python` `Scrapling` `Algolia` `Gemini` `Slack` |
| 🗄️ **UMatch Database** | Data work for Crimson's UMatch product, in the company org. | `Data` |

---

## 🧰 Arsenal

<div align="center">

**AI & Automation**

![n8n](https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white)
![Claude](https://img.shields.io/badge/Claude_Code-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-1a1a1a?style=for-the-badge&logo=googlegemini&logoColor=8E75B2)
![Cursor](https://img.shields.io/badge/Cursor-000000?style=for-the-badge&logo=cursor&logoColor=white)
![Zapier](https://img.shields.io/badge/Zapier-FF4F00?style=for-the-badge&logo=zapier&logoColor=white)
![Make](https://img.shields.io/badge/Make-6D00CC?style=for-the-badge&logo=make&logoColor=white)
![Replit](https://img.shields.io/badge/Replit-F26207?style=for-the-badge&logo=replit&logoColor=white)

**Languages & Backend**

![Python](https://img.shields.io/badge/Python-1a1a1a?style=for-the-badge&logo=python&logoColor=3776AB)
![JavaScript](https://img.shields.io/badge/JavaScript-1a1a1a?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Node.js](https://img.shields.io/badge/Node.js-1a1a1a?style=for-the-badge&logo=nodedotjs&logoColor=5FA04E)
![Docker](https://img.shields.io/badge/Docker-1a1a1a?style=for-the-badge&logo=docker&logoColor=2496ED)
![Postman](https://img.shields.io/badge/Postman-1a1a1a?style=for-the-badge&logo=postman&logoColor=FF6C37)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-1a1a1a?style=for-the-badge&logo=githubactions&logoColor=2088FF)

**Data Engineering**

![SQL](https://img.shields.io/badge/SQL-1a1a1a?style=for-the-badge&logo=postgresql&logoColor=4169E1)
![Snowflake](https://img.shields.io/badge/Snowflake-1a1a1a?style=for-the-badge&logo=snowflake&logoColor=29B5E8)
![Databricks](https://img.shields.io/badge/Databricks-1a1a1a?style=for-the-badge&logo=databricks&logoColor=FF3621)
![PySpark](https://img.shields.io/badge/PySpark-1a1a1a?style=for-the-badge&logo=apachespark&logoColor=E25A1C)
![Airflow](https://img.shields.io/badge/Airflow-1a1a1a?style=for-the-badge&logo=apacheairflow&logoColor=017CEE)
![Supabase](https://img.shields.io/badge/Supabase-1a1a1a?style=for-the-badge&logo=supabase&logoColor=3FCF8E)
![Airtable](https://img.shields.io/badge/Airtable-1a1a1a?style=for-the-badge&logo=airtable&logoColor=18BFFF)
![Power BI](https://img.shields.io/badge/Power_BI-1a1a1a?style=for-the-badge&logo=powerbi&logoColor=F2C811)
![Tableau](https://img.shields.io/badge/Tableau-1a1a1a?style=for-the-badge&logo=tableau&logoColor=E97627)

**CMS, Search & Commerce**

![Contentful](https://img.shields.io/badge/Contentful-1a1a1a?style=for-the-badge&logo=contentful&logoColor=2478CC)
![Algolia](https://img.shields.io/badge/Algolia-1a1a1a?style=for-the-badge&logo=algolia&logoColor=5468FF)
![WordPress](https://img.shields.io/badge/WordPress-1a1a1a?style=for-the-badge&logo=wordpress&logoColor=21759B)
![Shopify](https://img.shields.io/badge/Shopify-1a1a1a?style=for-the-badge&logo=shopify&logoColor=7AB55C)
![Salesforce](https://img.shields.io/badge/Salesforce-1a1a1a?style=for-the-badge&logo=salesforce&logoColor=00A1E0)
![HubSpot](https://img.shields.io/badge/HubSpot-1a1a1a?style=for-the-badge&logo=hubspot&logoColor=FF7A59)

**Design & Creative**

![Figma](https://img.shields.io/badge/Figma-1a1a1a?style=for-the-badge&logo=figma&logoColor=F24E1E)
![Adobe](https://img.shields.io/badge/Adobe_CC-1a1a1a?style=for-the-badge&logo=adobecreativecloud&logoColor=DA1F26)
![ElevenLabs](https://img.shields.io/badge/ElevenLabs-1a1a1a?style=for-the-badge&logo=elevenlabs&logoColor=white)

</div>

---

## 🛣️ Experience

```text
JUL 2026 → NOW   Data & Automation Engineer          Crimson Education      Remote · Shanghai
JAN 2025 → JUL 26 Founder's Office, Data Operations   Weekday (YC W21)       Remote · San Francisco
DEC 2023 → DEC 24 Tech Support Specialist             Tesco Ireland          Dublin
SEP 2023 → NOV 23 Business Operations Specialist      Centra                 Dublin
JUN 2020 → FEB 21 Project Support, Data & Digital     United Nations Volunteers  Remote · Yaoundé
```

<details>
<summary><b>▸ The details</b></summary>

- **Crimson Education:** automated data workflows that collect, check and report; data-quality checks on operational data; requirements into repeatable processes and dashboards.
- **Weekday (YC W21):** worked directly with the founders on how data flows in, gets checked and gets reported. Quality rules, access control, backups, reporting standards.
- **Tesco Ireland:** reviewed large volumes of operational and inventory data against quality standards, worked with IT and ops to fix issues.
- **Centra:** regular reporting on stock, sales and operational issues for senior leadership.
- **United Nations Volunteers:** collected, cleaned and managed data for digital-strategy projects, wrote step-by-step data procedures.

</details>

---

## 🎓 Education & Certs

| | |
|---|---|
| 🇮🇪 **University College Dublin** | MSc Information Systems, **scholarship recipient** (2023–24) |
| 🇮🇳 **All India Management Association** | Associate's, Data Analytics (2022–23) |
| 🇮🇳 **Manipal University Jaipur** | Bachelor's, Business (2019–22) |
| 📊 **UC Davis** | Data Visualization with Tableau |
| 🧩 **BCG** | Strategy Consulting Virtual Experience |

**Side projects:** 2022 FIFA World Cup dashboard (Power BI) · Netflix product analytics (Tableau) · vegan meal planner app, UI/UX case study from onboarding to subscription.

---

## 📈 GitHub stats

<div align="center">

<img height="170" src="https://github-readme-stats.vercel.app/api?username=pritam-crimson&show_icons=true&theme=black-ice&hide_border=true&bg_color=000000&include_all_commits=true&count_private=true" />
<img height="170" src="https://github-readme-streak-stats.herokuapp.com/?user=pritam-crimson&theme=dark&hide_border=true&background=000000" />

<img src="https://github-readme-activity-graph.vercel.app/graph?username=pritam-crimson&bg_color=000000&color=9ca3af&line=ffffff&point=ffffff&area=true&hide_border=true" width="100%" />

</div>

---

## 🤝 Work with me

> *Not sure what to automate? Let's find out.* Free 30 minute call, no pitch, no pressure.

<div align="center">

[![Portfolio](https://img.shields.io/badge/PORTFOLIO-000000?style=for-the-badge&logo=safari&logoColor=white)](https://pritamlaskar.github.io/)

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=0:1f1f1f,50:0d1117,100:000000&height=120&section=footer" />

</div>
