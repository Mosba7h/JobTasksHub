
```markdown
# 🧠 Autonomous Industry Intelligence Report Generator

A system designed to autonomously generate strategic business intelligence reports by scraping, summarizing, and organizing insights from online sources.

---

## ⚙️ System Architecture

The system follows a **modular architecture** with the following key components:

```
          +----------------+        +------------------+
          |   User Query   | -----> |   Search Module   |
          +----------------+        +------------------+
                                             |
                                             v
                                   +--------------------+
                                   |  Scraping Module   |
                                   +--------------------+
                                             |
                                             v
                                   +--------------------+
                                   | Summarizer Module  |
                                   +--------------------+
                                             |
                                             v
                                   +--------------------+
                                   | Report Generator   |
                                   +--------------------+
                                             |
                                             v
                                 +------------------------+
                                 | Markdown & PDF Output  |
                                 +------------------------+
```

---

## 🧩 Modular Approach

Each functionality is encapsulated into a standalone module to ensure maintainability and scalability.

### 1. **Search Module** – `search.py`
- Uses **SerpAPI** to search Google based on the user query.
- Returns a list of top relevant URLs.
- ✅ Decoupled from scraping logic.

```python
from serpapi import GoogleSearch
```

---

### 2. **Scraping Module** – `extractor.py`
- Extracts readable paragraphs from the fetched URLs using **BeautifulSoup**.
- Filters out short/irrelevant content.

```python
from bs4 import BeautifulSoup
```

---

### 3. **Summarization Module** – `summarizer.py`
- Uses **OpenAI GPT** to summarize the scraped text.
- Truncates long content to avoid API limits.

```python
client.chat.completions.create(...)
```

---

### 4. **Report Builder Module** – `reporter.py`
- Combines all insights into a structured report format:
  - Executive Summary
  - Market Trends
  - Key Competitors
  - Strategic Recommendations

---

### 5. **PDF Generator** – `pdf_generator.py`
- Converts the Markdown report into a clean, well-formatted PDF using `FPDF`.

---

### 6. **Main Script** – `main.py`
- CLI interface that:
  - Accepts a business query
  - Triggers the full pipeline
  - Outputs both `.md` and `.pdf` versions of the report

```bash
python main.py "AI startups in healthcare"
```

---

## 🔁 Workflow

1. **Input**: User provides a business-level query.
2. **Search**: Top 5 relevant URLs are fetched using SerpAPI.
3. **Scrape**: Main content extracted from each URL.
4. **Summarize**: GPT model summarizes each article.
5. **Report**: Summaries are compiled into a final report.
6. **Export**: Report saved as both `.md` and `.pdf`.

---

## 🔐 Environment Variables

Configured in `.env`:

```env
SERPAPI_API_KEY=your_api_key_here
OPENAI_API_KEY=your_api_key_here
```

---

## 🛠 Dependencies

- `requests`, `beautifulsoup4`
- `fpdf`, `markdown2`
- `openai`, `python-dotenv`
- `serpapi`
