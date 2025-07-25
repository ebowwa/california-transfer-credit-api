# California Transfer Credit API Collection

> **Note**: This is an archive repository containing three separate, independent projects that were previously individual GitHub repositories. They have been consolidated here for historical reference and to clean up the GitHub profile. These are NOT a unified system but rather three different approaches to solving similar problems.

## 📦 Repository Structure

This repository contains three distinct projects that were exploring California higher education transfer credit systems:

```
california-transfer-credit-api/
├── 000-core-fastapi-async/      # Original: py-ccc-csu-advisor
├── 001-flask-sync-scraper/      # Original: assist.org_scrape  
└── 002-modular-fastapi-backend/ # Original: student_advisor
```

## 🗂️ Project Origins

These projects were developed at different times as separate explorations into accessing and processing transfer credit data from [Assist.org](https://assist.org), California's official transfer information system. They represent iterative attempts at solving the challenge of programmatically accessing transfer articulation agreements between California Community Colleges (CCC), California State Universities (CSU), and University of California (UC) institutions.

## 📁 Individual Projects

### `000-core-fastapi-async/` (Original: py-ccc-csu-advisor)

**What it is**: A FastAPI application with async scrapers for Assist.org data

**Key Features:**
- Async/await architecture using `httpx`
- Basic API endpoints for institutions and agreements
- PDF report generation capability
- Rate-limited scraping

**Tech Stack:** Python, FastAPI, httpx, Pydantic

### `001-flask-sync-scraper/` (Original: assist.org_scrape)

**What it is**: A simple Flask-based synchronous web scraper

**Key Features:**
- Lightweight Flask server
- Direct API mapping to Assist.org endpoints
- Synchronous requests
- Minimal dependencies

**Tech Stack:** Python, Flask, requests

### `002-modular-fastapi-backend/` (Original: student_advisor)

**What it is**: A more structured attempt with modular architecture

**Key Features:**
- Modular foundation layer
- Separated business logic
- More comprehensive error handling
- Includes some Next.js frontend files

**Tech Stack:** Python, FastAPI, aiohttp, (partial Next.js frontend)

## ⚠️ Important Notes

1. **These are separate projects**: Each subdirectory is a standalone project with its own dependencies and approaches
2. **Not production-ready**: These were experimental/educational projects exploring the problem space
3. **May have issues**: Import errors and other issues may exist as these were consolidated from separate repos
4. **Historical archive**: Maintained for reference rather than active development

## 🎯 Original Problem Statement

All three projects attempted to address the same core challenge: California higher education advisors and students need better tools to understand transfer credit compatibility between community colleges and four-year institutions. The manual process of checking Assist.org is time-consuming and error-prone.

## 🛠️ Running Individual Projects

Each project can be run independently. Navigate to the specific project directory and follow its setup:

```bash
# For 000-core-fastapi-async
cd 000-core-fastapi-async
pip install -r requirements.txt
uvicorn app:app --reload

# For 001-flask-sync-scraper
cd 001-flask-sync-scraper
pip install -r requirements.txt
python main.py

# For 002-modular-fastapi-backend
cd 002-modular-fastapi-backend
pip install -r requirements.txt
uvicorn api.index:app --reload
```

## 📚 Learning Value

These projects demonstrate:
- Evolution of approaches to the same problem
- Different Python web frameworks (Flask vs FastAPI)
- Sync vs async programming patterns
- Various levels of code organization and architecture

## 🤝 Contributing

This is an archival repository. For new projects addressing California transfer credits, consider starting fresh with lessons learned from these implementations.

## 📄 License

Various - check individual project directories.

## 👤 Author

**Elijah Arbee**
- GitHub: [@ebowwa](https://github.com/ebowwa)

---

*These projects were consolidated from separate repositories as part of GitHub profile cleanup. They represent early explorations into automating access to California higher education transfer credit data.*