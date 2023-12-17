from django.urls import path
from .views import *


urlpatterns = [
    path('',dashboard, name="adminDashboard"),
    # * Voters
    path('voters',voters, name="adminViewVoters"),
    path('voters/view',view_voter_by_id, name="viewVoter"),
    path('voters/delete',deleteVoter, name='deleteVoter'),
    path('voters/update',updateVoter, name="updateVoter"),

    # * Position
    path('position/view',view_position_by_id, name="viewPosition"),
    path('position/update',updatePosition, name="updatePosition"),
    path('position/delete',deletePosition, name='deletePosition'),
    path('positions/view',viewPositions, name='viewPositions'),

    # * Candidate
    path('candidate/',viewCandidates, name='viewCandidates'),
    path('candidate/update',updateCandidate, name="updateCandidate"),
    path('candidate/delete',deleteCandidate, name='deleteCandidate'),
    path('candidate/view',view_candidate_by_id, name='viewCandidate'),

    # * Settings (Ballot Position and Election Title)
    path("settings/ballot/position",ballot_position, name='ballot_position'),
    path("settings/ballot/title/",ballot_title, name='ballot_title'),
    path("settings/ballot/position/update/<int:position_id>/<str:up_or_down>/",
        update_ballot_position, name='update_ballot_position'),

    # * Votes
    path('votes/view',viewVotes, name='viewVotes'),
    path('votes/reset/',resetVote, name='resetVote'),
    path('votes/print/',PrintView, name='printResult'),




]
