from ninja import ModelSchema
from ..models import FeedbackModel


class FeedbackSchema(ModelSchema):
    class Meta:
        model = FeedbackModel
        fields = "__all__"
        exclude = ["mentoring"]
