from ..models import FeedbackModel


def list_feedbacks_by_id(id: int):
    feedbacks = FeedbackModel.objects.filter(id=id)
    return feedbacks
