from typing import List
from ninja import Router
from ninja.pagination import paginate, PageNumberPagination

from .schemas import FeedbackSchema
from .use_cases import list_feedbacks_by_id_use_case


router = Router(tags=["feedback"])


@router.get("/{id}", response=List[FeedbackSchema])
def list_feedbacks_by_id(request, id):
    response = list_feedbacks_by_id_use_case(id)
    return response
