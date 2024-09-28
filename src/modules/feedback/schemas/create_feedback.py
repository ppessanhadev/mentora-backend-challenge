from ninja import ModelSchema
from ..models import FeedbackModel


class CreateFeedbackInSchema(ModelSchema):
    class Meta:
        model = FeedbackModel
        fields = "__all__"
        exclude = ["created_at", "id"]


class CreateFeedbackOutSchema(ModelSchema):
    class Meta:
        model = FeedbackModel
        fields = ["id"]
