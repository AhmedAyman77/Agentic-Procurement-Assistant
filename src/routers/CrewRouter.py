import os
import logging
from typing import List
from controllers import RunCrewControllers
from helpers.config import Settings, get_settings
from fastapi import APIRouter, Depends, Request, Form
from agents.AgentsEnum import AgentsEnum
from fastapi.responses import FileResponse

from agents.Tasks import Tasks

logger = logging.getLogger('uvicorn.error')
crew_router = APIRouter(
    prefix="/api",
    tags=["api_v1", "crew"],
)

@crew_router.post("/get_procurement_review")
async def get_procurement_review(
        request: Request,
        settings: Settings = Depends(get_settings),
        product_name: str = Form(...),
        websites_list: List[str] = Form(["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"]),
        country_name: str = Form("Egypt"),
        no_keywords: int = Form(5),
        language: str = Form("English"),
    ):

    _ = RunCrewControllers(
        request=request,
        product_name=product_name,
        websites_list=websites_list,
        country_name=country_name,
        no_keywords=no_keywords,
        language=language
    ).crew_results()

    dir_name = os.path.dirname(os.path.dirname(__file__))
    
    return FileResponse(
        path=os.path.join(dir_name, AgentsEnum.OUTPUT_FILE_PATH.value),
        media_type=AgentsEnum.MEDIA_TYPE.value,
        filename=AgentsEnum.PROCUREMENT_REPORT.value
    )
