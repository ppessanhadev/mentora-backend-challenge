from typing import List
from ninja import Router
from ninja.pagination import paginate, PageNumberPagination

from .schemas.mentoring import MentoringSchema
from .use_cases.list_all import list_all_mentories_use_cases, MentoringModel


router = Router(tags=["mentoring"])


@router.get("", response=List[MentoringSchema])
@paginate(PageNumberPagination, page_size=16)
def list_all_mentories(request):
    response = list_all_mentories_use_cases()
    return response
