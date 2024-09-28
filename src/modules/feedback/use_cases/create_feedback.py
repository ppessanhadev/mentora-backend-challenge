from django.shortcuts import get_object_or_404
from ..models import FeedbackModel
from ..schemas import CreateFeedbackInSchema
from src.modules.mentoring.models import MentoringModel


def create_feedback_use_case(body: CreateFeedbackInSchema):
    mentoring = get_object_or_404(MentoringModel, id=body.mentoring)
    body.mentoring = mentoring
    feedback = FeedbackModel.objects.create(**body.dict())
    return {"id": feedback.id}
