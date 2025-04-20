from serpapi import GoogleSearch
from config import SERPAPI_API_KEY

def search_google(query: str, num_results: int = 5) -> list:
    """
    Perform a Google search via SerpAPI and return list of result URLs.
    """
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": num_results
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    return [res["link"] for res in results.get("organic_results", [])]