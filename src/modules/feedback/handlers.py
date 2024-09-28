from typing import List
from ninja import Router
from ninja.pagination import paginate, PageNumberPagination

from .schemas import FeedbackSchema
from .use_cases import list_feedbacks_by_id


router = Router(tags=["feedback"])


@router.get("/{id}", response=List[FeedbackSchema])
@paginate(PageNumberPagination, page_size=10)
def list_feedbacks_by_id(request, id):
    response = list_feedbacks_by_id(id)
    return response
