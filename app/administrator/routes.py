"""
    Administrator View
"""

from flask import render_template, request

from app.administrator import blueprint

from app.administrator.modules.user_services import UserServices
from app.administrator.modules.election_services import ElectionServices
from app.administrator.modules.candidate_services import CandidateServices
from app.administrator.modules.vote_services import VoteResultServices

# import forms
from app.forms import *

"""
    USERS
"""
@blueprint.route('/users')
#@login_required
def users():
    users = UserServices().show_all()
    return render_template('users.html', users=users,
                           form=CreateAccountForm())

@blueprint.route('/api/users', methods=["POST"])
def api_user():
    response = UserServices().add(request.form)
    return response

@blueprint.route('/api/users/<string:user_id>', methods=["GET", "PUT", "DELETE"])
def api_user_info(user_id):
    if request.method == "GET":
        response = UserServices(user_id).info()
    elif request.method == "DELETE":
        response = UserServices(user_id).remove()
    elif request.method == "PUT":
        response = UserServices(user_id).update(request.form)
    return response


"""
    CANDIDATES
"""
@blueprint.route('<string:election_id>/candidates', methods=["GET"])
#@login_required
def candidates(election_id):
    candidates = CandidateServices(election_id=election_id).show_all()
    print(candidates)
    return render_template('candidates.html', candidates=candidates,
                            form=CreateCandidateForm(), form2=EnrollCandidateForm())

@blueprint.route('/api/<string:election_id>/candidates', methods=["POST"])
#@login_required
def api_candidate(election_id):
    response = CandidateServices(election_id=election_id).add(request.form)
    return response

@blueprint.route('/api/<string:user_id>/enroll/<string:candidate_id>', methods=["POST"])
#@login_required
def api_enroll_candidate(user_id, candidate_id):
    response = UserServices(user_id=user_id).enroll(candidate_id)
    return response

@blueprint.route('/api/<string:election_id>/candidates/<string:candidate_id>', methods=["GET", "PUT", "DELETE"])
def api_candidate_info(election_id, candidate_id):
    if request.method == "GET":
        response = CandidateServices(candidate_id, election_id).info()
    elif request.method == "DELETE":
        response = CandidateServices(candidate_id, election_id).remove()
    elif request.method == "PUT":
        response = CandidateServices(candidate_id, election_id).update(request.form)
    return response

"""
    ELECTIONS
"""
@blueprint.route('/elections')
#@login_required
def elections():
    elections = ElectionServices().show_all()
    return render_template('elections.html', elections=elections,
                           form=CreateElectionForm())

@blueprint.route('/api/elections', methods=["POST"])
def api_election():
    response = ElectionServices().add(request.form)
    return response

@blueprint.route('/api/elections/<string:election_id>', methods=["GET", "PUT", "DELETE"])
def api_election_info(election_id):
    if request.method == "GET":
        response = ElectionServices(election_id).info()
    elif request.method == "DELETE":
        response = ElectionServices(election_id).remove()
    elif request.method == "PUT":
        response = ElectionServices(election_id).update(request.form)
    return response

"""
    VOTES
"""
@blueprint.route('/votes')
#@login_required
def votes():
    votes = VoteResultServices().show_all()
    return render_template('votes.html', votes=votes)
