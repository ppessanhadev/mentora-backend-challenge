from typing import List
from ninja import Router
from ninja.pagination import paginate, PageNumberPagination

from .schemas import SimpleMentoringSchema, MentoringSchema
from .use_cases import list_all_mentories_use_cases, get_by_id_use_case


router = Router(tags=["mentoring"])


@router.get("", response=List[SimpleMentoringSchema])
@paginate(PageNumberPagination, page_size=16)
def list_all_mentories(request):
    response = list_all_mentories_use_cases()
    return response


@router.get("/{id}", response={200: MentoringSchema})
def get_by_id(request, id):
    response = get_by_id_use_case(id)
    return response
