import pytest

from test_project_api_aivan.endpoints.create_new_post import CreateNewPost
from test_project_api_aivan.endpoints.get_all_posts import GetAllPost
from test_project_api_aivan.endpoints.post_delete import DeletePost
from test_project_api_aivan.endpoints.update_patch_post import UpdatePatchPost
from test_project_api_aivan.endpoints.update_put_post import UpdatePostPut


@pytest.fixture()
def fixt_get_all_posts():
    return GetAllPost()


@pytest.fixture()
def fixt_create_new_post():
    return CreateNewPost()


@pytest.fixture()
def fixt_post_id(fixt_create_new_post):
    payload = {
        'name': 'ivan test get post id',
        'data': {'group': 'groups ivan andriyanov test post id'}
    }
    fixt_create_new_post.req_create_new_post(payload=payload)
    yield fixt_create_new_post.post_id


@pytest.fixture()
def fixt_delete_post():
    return DeletePost()


@pytest.fixture()
def fixt_update_put_post():
    return UpdatePostPut()


@pytest.fixture()
def fixt_update_patch_post():
    return UpdatePatchPost()
