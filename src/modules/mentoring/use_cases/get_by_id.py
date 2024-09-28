from ..models import MentoringModel


def get_by_id_use_case(id: int):
    mentoring = MentoringModel.objects.get(id=id)
    return mentoring
