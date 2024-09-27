from ninja import Schema


class MentoringSchema(Schema):
    id: int
    title: str
    description: str
    price: float
