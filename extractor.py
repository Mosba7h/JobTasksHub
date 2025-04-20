import requests
from bs4 import BeautifulSoup

def extract_text_from_url(url: str) -> str:
    """
    Scrape and return main text paragraphs from a URL.
    """
    try:
        html = requests.get(url, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")
        paragraphs = soup.find_all("p")
        # Filter out very short paragraphs
        text = " ".join(p.get_text() for p in paragraphs if len(p.get_text()) > 50)
        return text.strip() if len(text) > 100 else ""
    except Exception:
        return ""
