# from django.urls import path

# from .apiviews import PollList, PollDetail

# urlpatterns = [
#     path("polls/", PollList.as_view(), name="polls_list"),
#     path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail")
# ]

# from .apiviews import *

# urlpatterns = [
#     path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
#     path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

# ]
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet, ChoiceViewSet, VoteViewSet


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
router.register('choice', ChoiceViewSet, base_name='choices')
router.register('vote', VoteViewSet, base_name='votes')




urlpatterns = [
    # ...
]

urlpatterns += router.urls