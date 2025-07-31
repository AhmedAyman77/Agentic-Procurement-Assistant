import os
import yaml
from crewai import Agent
from fastapi import Request
from .Tools import Tools
from .AgentsEnum import AgentsEnum

class Agents():
    """
    This agent is responsible for recommending search queries based on user input.
    It uses a language model to generate relevant search queries that can be used
    in subsequent searches or analyses.
    """
    
    def __init__(self, request:Request) -> None:
        self.dirname = os.path.dirname(__file__)
        self.agents_config_path = os.path.join(self.dirname, AgentsEnum.AGENTS_CONFIG.value)
        with open(self.agents_config_path, 'r') as file:
            self.agents_config = yaml.safe_load(file)

        self.request = request
        
    def search_queries_recommendation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config[AgentsEnum.SEARCH_QUERIES_RECOMMENDATION_AGENT.value],
            llm=self.request.app.basic_llm,
            allow_delegation=True,
            max_rpm=3,
            reasoning=True,
            inject_date=True
        )
    

    def search_engine_agent(self) -> Agent:
        return Agent(
            config=self.agents_config[AgentsEnum.SEARCH_ENGINE_AGENT.value],
            llm=self.request.app.basic_llm,
            tools=[Tools(request=self.request).search_engine_tool],
            allow_delegation=True,
            max_rpm=3,
            reasoning=True,
            inject_date=True,
        )
    
    def scraping_agent(self) -> Agent:
        return Agent(
            config=self.agents_config[AgentsEnum.SCRAPING_AGENT.value],
            llm=self.request.app.basic_llm,
            tools=[Tools(request=self.request).web_scraping_tool],
            allow_delegation=True,
            max_rpm=3,
            reasoning=True,
            inject_date=True,
        )


    def procurement_report_author_agent(self) -> Agent:
        return Agent(
            config=self.agents_config[AgentsEnum.PROCUREMENT_REPORT_AUTHOR_AGENT.value],
            llm=self.request.app.basic_llm,
            allow_delegation=True,
            inject_date=True,
            max_iter=5,
            max_rpm=3
        )
