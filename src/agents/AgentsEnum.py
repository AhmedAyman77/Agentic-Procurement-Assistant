from enum import Enum

class AgentsEnum(Enum):
    ABOUT_COMPANY = "Rankyx is a company that provides AI solutions to help websites refine their search and recommendation systems."
    
    AGENTS_CONFIG = "config/agents.yaml"
    TASKS_CONFIG = "config/tasks.yaml"
    
    SEARCH_QUERIES_RECOMMENDATION_AGENT = "search_queries_recommendation_agent"
    SEARCH_ENGINE_AGENT = "search_engine_agent"
    SCRAPING_AGENT = "scraping_agent"
    PROCUREMENT_REPORT_AUTHOR_AGENT = "procurement_report_author_agent"


    SEARCH_QUERIES_RECOMMENDATION_TASK = "search_queries_recommendation_task"
    SEARCH_ENGINE_TASK = "search_engine_task"
    SCRAPING_TASK = "scraping_task"
    PROCUREMENT_REPORT_AUTHOR_TASK = "procurement_report_author_task"

    SUGGESTED_SEARCH_QUERIES = "suggested_search_queries.json"
    SEARCH_RESULTS = "search_results.json"
    EXTRACTED_PRODUCTS = "extracted_products.json"
    PROCUREMENT_REPORT = "procurement_report.html"

    MEDIA_TYPE="text/html"

    OUTPUT_FILE_PATH = "agent_output/procurement_report.html"
