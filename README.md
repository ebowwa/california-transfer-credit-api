# California Higher Education Transfer Credit System

A comprehensive API system for facilitating credit transfers and academic planning within the California higher education system, specifically between California Community Colleges (CCC), California State Universities (CSU), and University of California (UC) institutions.

## 🎯 Problem Statement

Higher education advisors in California face challenges managing complex transfer requirements across 116 community colleges, 23 CSU campuses, and 10 UC campuses. Students often struggle to understand which courses will transfer and how to efficiently plan their academic pathway. This system automates access to transfer articulation data from [Assist.org](https://assist.org), California's official transfer information system.

## 🏗️ Architecture Overview

This repository consolidates three complementary projects that work together to provide a complete transfer credit information system:

```
py-ccc-csu-advisor/
├── core-fastapi-async/     # FastAPI app with async scrapers
├── flask-sync-scraper/     # Flask-based synchronous scraper
└── modular-fastapi-backend/   # Modular async API with foundation layer
```

## 📁 Project Components

### 1. `/core-fastapi-async` - Core FastAPI Application

**Purpose**: High-performance async API for querying transfer agreements

**Key Features:**
- Async/await architecture using `httpx` for concurrent requests
- Pydantic models for request/response validation
- PDF report generation for articulation agreements
- Rate-limited scraping with configurable delays

**Tech Stack:**
- FastAPI
- httpx (async HTTP client)
- Pydantic
- Python 3.8+

**Core Classes:**
- `AsyncScraper`: Base class for async web scraping
- `InstitutionFetcher`: Specialized institution data fetcher
- `AssistOrgAPI`: Main API wrapper with methods for:
  - Fetching institution agreements
  - Getting agreement categories
  - Retrieving articulation details
  - Downloading PDF reports

### 2. `/flask-sync-scraper` - Flask Scraper

**Purpose**: Simple synchronous API for basic Assist.org data access

**Key Features:**
- Lightweight Flask server
- Direct API mapping to Assist.org endpoints
- Synchronous requests using `requests` library
- Simple JSON responses

**Tech Stack:**
- Flask
- requests
- Python 3.x

**Functions:**
- `fetch_institution_agreements()`: Get agreements for an institution
- `fetch_agreements_categories()`: Retrieve categories between institutions
- `fetch_agreements()`: Get specific agreements with filters
- `fetch_articulation_agreements()`: Fetch detailed articulation data

### 3. `/modular-fastapi-backend` - Modular FastAPI Backend

**Purpose**: Production-ready API with modular architecture and separated business logic

**Key Features:**
- Modular foundation layer for business logic separation
- Comprehensive error handling with detailed HTTP exceptions
- Comprehensive data models for all agreement types
- Support for complex multi-step operations
- OpenAPI specification endpoint

**Architecture:**
```
modular-fastapi-backend/
├── api/
│   ├── index.py              # FastAPI app with all endpoints
│   └── _assist/
│       ├── async_scraper.py  # Base async scraper
│       ├── models.py         # Pydantic models
│       ├── scrapers.py       # Main API wrapper
│       └── foundation/       # Core business logic
│           ├── fetch_agreements.py
│           ├── get_agreements.py
│           ├── get_keys.py
│           └── get_pdfs.py
```

## 🚀 API Endpoints

All three projects provide similar endpoints with varying implementations:

### Common Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/institutions` | List all institutions | - |
| GET | `/institution-agreements/{id}` | Get agreements for institution | `institution_id` |
| GET | `/agreements-categories/` | Get agreement categories | `receiving_institution_id`, `sending_institution_id`, `academic_year_id` |
| GET | `/agreements/` | Get specific agreements | `receiving_institution_id`, `sending_institution_id`, `academic_year_id`, `category_code` |
| GET | `/articulation-agreements/{key}` | Get articulation details | `key` |
| POST | `/query-agreements/` | Custom agreement query | JSON body with query parameters |

### Example Requests

```bash
# Get all institutions
curl http://localhost:8000/institutions

# Get agreements for CSU Northridge (ID: 7)
curl http://localhost:8000/institution-agreements/7

# Get agreement categories between institutions
curl "http://localhost:8000/agreements-categories/?receiving_institution_id=7&sending_institution_id=119&academic_year_id=69"

# Get specific Computer Science agreements
curl "http://localhost:8000/agreements/?receiving_institution_id=7&sending_institution_id=119&academic_year_id=69&category_code=COMP_SCI"
```

## 📊 Data Models

### AgreementQuery
```python
{
  "receiving_institution_id": int,      # Target CSU/UC ID
  "sending_institution_id": int,        # Source CCC ID
  "academic_year_id": int,              # Academic year ID
  "category_code": str (optional),      # Major/category code
  "major": str,                         # Major name
  "major_code": str                     # Major abbreviation
}
```

### Institution
```python
{
  "id": int,
  "name": str
}
```

### ArticulationAgreement
Contains detailed course equivalency mappings between institutions

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip or poetry for dependency management
- (Optional) Virtual environment

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/ebowwa/py-ccc-csu-advisor
cd py-ccc-csu-advisor
```

2. **Set up virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

For core-fastapi-async:
```bash
cd core-fastapi-async
pip install fastapi uvicorn httpx pydantic
```

For flask-sync-scraper:
```bash
cd ../flask-sync-scraper
pip install flask requests
```

For modular-fastapi-backend:
```bash
cd ../enhanced-modular-api
pip install fastapi uvicorn httpx aiohttp pydantic
```

### Running the Applications

**Option 1: core-fastapi-async (Recommended)**
```bash
cd core-fastapi-async
uvicorn app:app --reload --port 8000
```

**Option 2: flask-sync-scraper**
```bash
cd flask-sync-scraper
python main.py  # Runs on port 5000
```

**Option 3: modular-fastapi-backend**
```bash
cd enhanced-modular-api
uvicorn api.index:app --reload --port 8000
```

## 💡 Use Cases

### For Students
- **Transfer Planning**: Check which community college courses satisfy requirements at target CSU/UC
- **Major Exploration**: Compare transfer requirements across different majors
- **Unit Optimization**: Identify the most efficient course combinations for transfer

### For Academic Advisors
- **Bulk Queries**: Process multiple student transfer scenarios efficiently
- **Real-time Updates**: Access the latest articulation agreements
- **Report Generation**: Download official PDF documentation

### For Developers
- **Integration Ready**: RESTful API design for easy integration
- **Extensible**: Modular architecture allows custom features
- **Well-Documented**: OpenAPI spec available at `/docs`

## 🔧 Configuration

### Environment Variables
```bash
# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Scraping Configuration
RATE_LIMIT_DELAY=1  # Seconds between requests
REQUEST_TIMEOUT=30  # Request timeout in seconds
```

### Rate Limiting
The system respects Assist.org rate limits with configurable delays between requests. Adjust the `delay` parameter in `AssistOrgAPI` initialization.

## 📈 Performance Considerations

- **Async Operations**: The FastAPI implementations use async/await for concurrent requests
- **Caching**: Consider implementing Redis caching for frequently accessed data
- **Rate Limiting**: Built-in delays prevent overwhelming the Assist.org API
- **Error Handling**: Comprehensive exception handling ensures graceful failures

## 🐛 Known Issues

1. **Missing Imports**: Some foundation modules in enhanced-modular-api need import fixes
2. **Directory Creation**: PDF download feature requires manual `agreements/` directory creation
3. **Error Messages**: Some error responses could be more descriptive

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source. Please check individual project directories for specific license information.

## 👤 Author

**Elijah Arbee**
- GitHub: [@ebowwa](https://github.com/ebowwa)

## ⚠️ Disclaimer

This system is designed to complement, not replace, official academic advising. Always verify transfer credits with your institution's official advisors. Data accuracy depends on Assist.org updates.

## 🔗 Resources

- [Assist.org](https://assist.org) - Official California transfer information
- [CSU System](https://www.calstate.edu) - California State University
- [UC System](https://www.universityofcalifornia.edu) - University of California
- [CCC System](https://www.cccco.edu) - California Community Colleges

---

*Empowering students to navigate their academic journey with confidence and clarity.*