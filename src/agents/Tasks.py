import os
import yaml
from crewai import Task
from .Agents import Agents
from fastapi import Request
from .AgentsEnum import AgentsEnum
from .AgentOutputStructure.AllSearchResults import AllSearchResults
from .AgentOutputStructure.AllExtractedProducts import AllExtractedProducts
from .AgentOutputStructure.SearchQueriesRecommendationAgent import SuggestedSearchQueries

class Tasks():
    """
    This class is used to create tasks for the CrewAI framework.
    It defines various tasks that can be executed by agents, such as generating search queries,
    scraping data, and generating procurement reports.
    """

    def __init__(self, request: Request) -> None:
        self.dirname = os.path.dirname(__file__)
        self.AGENT_OUTPUT_FILE_PATH = "./agent_output" # os.path.join(self.dirname, 'agent_output')
        
        self.tasks_config_path = os.path.join(self.dirname, AgentsEnum.TASKS_CONFIG.value)
        with open(self.tasks_config_path, 'r') as file:
            self.tasks_config = yaml.safe_load(file)
    
        self.request = request
    
    def search_queries_recommendation_task(self):
        return Task(
            **self.tasks_config[AgentsEnum.SEARCH_QUERIES_RECOMMENDATION_TASK.value],
            output_json=SuggestedSearchQueries,
            output_file=os.path.join(self.AGENT_OUTPUT_FILE_PATH, AgentsEnum.SUGGESTED_SEARCH_QUERIES.value),
            agent=Agents(request=self.request).search_queries_recommendation_agent()
        )
    
    def search_engine_task(self):
        return Task(
            **self.tasks_config[AgentsEnum.SEARCH_ENGINE_TASK.value],
            output_json=AllSearchResults,
            output_file=os.path.join(self.AGENT_OUTPUT_FILE_PATH, AgentsEnum.SEARCH_RESULTS.value),
            agent=Agents(request=self.request).search_engine_agent()
        )
    
    def scraping_task(self):
        return Task(
            **self.tasks_config[AgentsEnum.SCRAPING_TASK.value],
            output_json=AllExtractedProducts,
            output_file=os.path.join(self.AGENT_OUTPUT_FILE_PATH, AgentsEnum.EXTRACTED_PRODUCTS.value),
            agent=Agents(request=self.request).scraping_agent()
        )

    def procurement_report_author_task(self):
        return Task(
            **self.tasks_config[AgentsEnum.PROCUREMENT_REPORT_AUTHOR_TASK.value],
            output_file=os.path.join(self.AGENT_OUTPUT_FILE_PATH, AgentsEnum.PROCUREMENT_REPORT.value),
            agent=Agents(request=self.request).procurement_report_author_agent(),
        )
