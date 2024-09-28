from ninja.schema import Schema
from ..models.feedback import stars_choices


class FeedbackSchema(Schema):
    id: int
    name: str
    description: str
    stars: 1 | 2 | 3 | 4 | 5
