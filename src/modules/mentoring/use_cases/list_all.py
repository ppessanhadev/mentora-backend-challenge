from ..models import MentoringModel


def list_all_mentories_use_cases():
    mentoring = MentoringModel.objects.all()
    return mentoring
