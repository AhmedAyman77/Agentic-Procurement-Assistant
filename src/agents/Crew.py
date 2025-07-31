from .Tasks import Tasks
from .Agents import Agents
from fastapi import Request
from crewai import Crew, Process


class ProcurementCrew():
    """
    A Crew class that represents a group of agents working together on tasks.
    """

    def __init__(self, request: Request):
        self.request = request
        self.agents = Agents(request=request)
        self.task = Tasks(request=request)
    
    def prepare_crew(self) -> Crew:
        return Crew(
            agents=[
                self.agents.search_queries_recommendation_agent(),
                self.agents.search_engine_agent(),
                self.agents.scraping_agent(),
                self.agents.procurement_report_author_agent(),
            ],
            tasks=[
                self.task.search_queries_recommendation_task(),
                self.task.search_engine_task(),
                self.task.scraping_task(),
                self.task.procurement_report_author_task(),
            ],
            process=Process.sequential,
            verbose=True,
            planning=True,
            planning_llm=self.request.app.basic_llm,
            max_rpm=3,
            knowledge_sources=[self.request.app.company_context]
        )