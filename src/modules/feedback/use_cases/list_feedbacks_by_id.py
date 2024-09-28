from django.shortcuts import get_object_or_404
from ..models import FeedbackModel
from ...mentoring.models.mentoring import MentoringModel


def list_feedbacks_by_id_use_case(id: int):
    mentoring = get_object_or_404(MentoringModel, id=id)
    feedbacks = FeedbackModel.objects.filter(mentoring=mentoring)
    return feedbacks
