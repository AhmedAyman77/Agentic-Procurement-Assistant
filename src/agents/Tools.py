from fastapi import Request
from crewai.tools import tool
from .AgentOutputStructure.AllExtractedProducts import SingleExtractedProduct

class Tools():
    def __init__(self, request: Request) -> None:
        self.request = request
    
    @tool
    def search_engine_tool(self, query: str):
        """
        Useful for search-based queries.
        Use this to find current information about any query related pages using a search engine.
        """
        return self.request.app.search_client.search(query)
    
    @tool
    def web_scraping_tool(self, page_url: str):
        """
        An AI Tool to help an agent to scrape a web page

        Example:
        web_scraping_tool(
            page_url="https://www.noon.com/egypt-en/15-bar-fully-automatic-espresso-machine-1-8-l-1500"
        )
        """
        details = self.request.app.scrape_client.smartscraper(
            website_url=page_url,
            user_prompt="Extract ```json\n" + SingleExtractedProduct.schema_json() + "```\n From the web page"
        )

        return {
            "page_url": page_url,
            "details": details
        }
