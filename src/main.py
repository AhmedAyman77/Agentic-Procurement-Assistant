import os
from crewai import LLM
from routers import CrewRouter
from fastapi import FastAPI
from tavily import TavilyClient
from scrapegraph_py import Client
from helpers.config import get_settings
from agents import AgentsEnum
from crewai.knowledge.source.string_knowledge_source import StringKnowledgeSource

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """
    Startup event to initialize resources.
    """
    env_settings = get_settings()

    # Huggingface cache directories
    os.environ["HF_HOME"] = "/home/user/.cache/huggingface"
    os.environ["HF_DATASETS_CACHE"] = "/home/user/.cache/huggingface/datasets"
    os.environ["TRANSFORMERS_CACHE"] = "/home/user/.cache/huggingface/transformers"
    os.environ["XDG_CACHE_HOME"] = "/home/user/.cache"
    os.environ["XDG_CONFIG_HOME"] = "/home/user/.config"
    os.environ["HOME"] = "/home/user"
    
    os.environ["COHERE_API_KEY"] = env_settings.COHERE_API_KEY

    app.basic_llm = LLM(model=env_settings.LLM, temperature=0)
    app.search_client = TavilyClient(api_key=env_settings.TAVILY_API_KEY)
    app.scrape_client = Client(api_key=env_settings.SCRAPEGRAPH_API_KEY)

    app.company_context = StringKnowledgeSource(
        content=AgentsEnum.ABOUT_COMPANY.value
    )

app.include_router(CrewRouter.crew_router)