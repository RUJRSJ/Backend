from flask import Blueprint

from service.admin import *
from flask_login import login_required
from .utils.response import HTTPResponse, HTTPError
from .utils.request import Request
from .utils.auth_required import auth_required, AuthLevel
from service.admin import Admin, NonedataError

__all__ = ['adminApp_api']

adminApp_api = Blueprint('adminApp_api', __name__)

@adminApp_api.route('/user_management', methods=['GET'])
@login_required
@auth_required(AuthLevel.ADMIN)
@Request.args('Identity')
def user_management(Identity):
    try:
        users = Admin.user_management(Identity)
    except:
        return HTTPError('unknown error', 406)
    return HTTPResponse('ok', data=users)


@adminApp_api.route('/change_auth', methods=['PUT'])
@login_required
@auth_required(AuthLevel.ADMIN)
@Request.json('user: str', 'userlevel: str')
def change_auth(user, userlevel):
    try:
        Admin.change_auth(user, userlevel)
    except:
        return HTTPError('unknown error', 406)
    return HTTPResponse('ok')


@adminApp_api.route('/auth', methods=['GET'])
@login_required
@auth_required(AuthLevel.ADMIN)
@Request.args('auth')
def search_by_auth(auth):
    try:
        surveys = Admin.search_by_auth(auth)
    except:
        return HTTPError('unknown error', 406)
    return HTTPResponse('ok', data=surveys)


@adminApp_api.route('/month', methods=['GET'])
@login_required
@auth_required(AuthLevel.ADMIN)
@Request.args('month')
def search_by_month(month):
    try:
        surveys = Admin.search_by_month(month)
    except:
        return HTTPError('unknown error', 406)
    return HTTPResponse('ok', data=surveys)


@adminApp_api.route('/wave', methods=['GET'])
@login_required
@auth_required(AuthLevel.ADMIN)
@Request.args('wave')
def search_by_wave(wave):
    try:
        surveys = Admin.search_by_wave(wave)
    except:
        return HTTPError('unknown error', 406)
    return HTTPResponse('ok', data=surveys)


@adminApp_api.route('/type', methods=['GET'])
@login_required
@auth_required(AuthLevel.ADMIN)
@Request.args('type')
def search_by_type(type):
    try:
        surveys = Admin.search_by_type(type)
    except:
        return HTTPError('unknown error', 406)
    return HTTPResponse('ok', data=surveys)


@adminApp_api.route('/keyword', methods=['GET'])
@login_required
@auth_required(AuthLevel.ADMIN)
@Request.args('keyword')
def search_by_keyword(keyword):
    try:
        surveys = Admin.search_by_keyword(keyword)
    except:
        return HTTPError('unknown error', 406)
    return HTTPResponse('ok', data=surveys)

@adminApp_api.route('/release', methods=['PUT'])
@login_required
@auth_required(AuthLevel.ADMIN)
@Request.json('DataId: int', 'Release: int')
def release(DataId, Release):
    try:
        Admin.release_survey(DataId, Release)
    except NonedataError:
        return HTTPError('None Data', 404)
    except:
        return HTTPError('unknown error', 406)
    return HTTPResponse('ok')