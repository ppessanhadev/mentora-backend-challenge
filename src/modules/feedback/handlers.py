from typing import List
from ninja import Router
from ninja.pagination import paginate, PageNumberPagination

from .schemas import FeedbackSchema, CreateFeedbackInSchema, CreateFeedbackOutSchema
from .use_cases import list_feedbacks_by_mentoring_id_use_case, create_feedback_use_case


router = Router(tags=["feedback"])


@router.post("", response={200: CreateFeedbackOutSchema})
def create(request, payload: CreateFeedbackInSchema):
    response = create_feedback_use_case(payload)
    return response


@router.get("/{id}", response=List[FeedbackSchema])
def list_feedbacks_by_id(request, id):
    response = list_feedbacks_by_mentoring_id_use_case(id)
    return response
