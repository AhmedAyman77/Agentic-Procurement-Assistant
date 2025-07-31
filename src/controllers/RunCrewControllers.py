from agents.Crew import ProcurementCrew
from typing import List
from helpers import get_settings, Settings
from fastapi import Request

class RunCrewControllers():
    """
    this class is responsible for running the crew agent.
    """

    def __init__(
        self,
        request: Request,
        product_name: str,
        websites_list: List[str],
        country_name: str,
        no_keywords: int,
        language: str,
    ):
        self.product_name = product_name
        self.websites_list = websites_list
        self.country_name = country_name
        self.no_keywords = no_keywords
        self.language = language

        self.request = request
        self.settings: Settings = get_settings()
        self.crew = ProcurementCrew(request=request).prepare_crew()

    def crew_results(self):
        return self.crew.kickoff(
            inputs={
                "product_name": self.product_name,
                "websites_list": self.websites_list,
                "country_name": self.country_name,
                "no_keywords": self.no_keywords,
                "language": self.language,
                "score_th": self.settings.SCORE_THRESH,
                "top_recommendations_no": self.settings.TOP_RECOMMENDATIONS_NUM,
            }
        )