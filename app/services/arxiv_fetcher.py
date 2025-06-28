import arxiv

def search_arxiv(query: str, max_results: int = 3):
    search = arxiv.Search(query=query, max_results=max_results)
    return [
        {
            "title": result.title,
            "summary": result.summary,
            "pdf_url": result.pdf_url
        }
        for result in search.results()
    ]
