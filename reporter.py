from typing import List
from search import search_google
from extractor import extract_text_from_url
from summarizer import summarize_text, client

def generate_insights(query: str) -> List[str]:
    """
    Search, extract and summarize multiple sources into insight snippets.
    """
    urls = search_google(query)
    summaries = []
    for url in urls:
        text = extract_text_from_url(url)
        summary = summarize_text(text)
        summaries.append(summary)
    return summaries

def generate_report(insights: List[str], query: str) -> str:
    """
    Compile insights into a structured intelligence report in Markdown.
    """
    joined = "\n\n".join(insights)
    prompt = f"""
Based on the following insights extracted from online sources related to the query: \"{query}\", generate a strategic intelligence report.

The report should have the following structure:
1. Executive Summary
2. Market Trends
3. Key Competitors
4. Strategic Recommendations

Insights:
{joined}
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content