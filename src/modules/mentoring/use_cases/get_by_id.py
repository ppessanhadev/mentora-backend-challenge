from django.shortcuts import get_object_or_404
from ..models import MentoringModel


def get_by_id_use_case(id: int):
    mentoring = get_object_or_404(MentoringModel, id=id)
    return mentoring
