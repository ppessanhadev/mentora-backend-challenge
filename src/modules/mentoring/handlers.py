from typing import List
from ninja import Router

from .schemas.mentoring import MentoringSchema
from .use_cases.list_all import list_all_mentories_use_cases


router = Router(tags=["mentoring"])


@router.get("", response={200: List[MentoringSchema]})
def list_all_mentories(request):
    response = list_all_mentories_use_cases()
    return 200, response
