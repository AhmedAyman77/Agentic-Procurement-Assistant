from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Application configuration settings.
    """
    AGENTOPS_API_KEY: str
    COHERE_API_KEY: str
    TAVILY_API_KEY: str
    SCRAPEGRAPH_API_KEY: str
    
    SCORE_THRESH: float
    TOP_RECOMMENDATIONS_NUM: int
    LLM: str


    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
