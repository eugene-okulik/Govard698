import allure
import pytest

Test_create_data = [
    {
        'name': 'ivan test create posts',
        'data': {'group': 'groups ivan andriyanov test'}
    }
]

Test_data_change = [
    {
        'name': 'ivan test create posts put request',
        'data': {'group': 'groups ivan andriyanov test put request'}
    }
]


@allure.feature('get post')
@allure.story('Получаем посты')
def test_get_all_post(fixt_get_all_posts):
    fixt_get_all_posts.req_get_all_post()
    with allure.step("Проверяем успешность получения постов"):
        fixt_get_all_posts.check_status_code_is_200()


@allure.feature('create post')
@allure.story('Создаем посты')
@pytest.mark.parametrize('data', Test_create_data)
@pytest.mark.medium
def test_create_new_post(fixt_create_new_post, fixt_delete_post, data):
    fixt_create_new_post.req_create_new_post(payload=data)
    post_id = fixt_create_new_post.post_id

    with allure.step("Проверяем создание"):
        fixt_create_new_post.check_status_code_is_200()
        assert fixt_create_new_post.json['name'] == data['name']

    with allure.step("Удаляем пост"):
        fixt_delete_post.full_req_delete_post(post_id)
        fixt_delete_post.check_status_code_is_200()


@allure.feature('delete post')
@allure.story('Удаляем посты')
@pytest.mark.critical
def test_delete_post(fixt_delete_post, fixt_post_id):
    fixt_delete_post.full_req_delete_post(fixt_post_id)
    with allure.step("Проверяем успешность удаления поста"):
        fixt_delete_post.check_status_code_is_200()


@allure.feature('change put post')
@allure.story('Изменяем посты путом')
@pytest.mark.parametrize('test_data_put', Test_data_change)
def test_update_put_post(fixt_update_put_post, fixt_post_id, test_data_put):
    fixt_update_put_post.full_req_update_put_post(
        fixt_post_id,
        payload=test_data_put
    )
    with allure.step("Проверяем успешность обновления и имя в ответе"):
        fixt_update_put_post.check_status_code_is_200()
        assert fixt_update_put_post.json['name'] == test_data_put['name']


@allure.story('Изменяем посты патчем')
@allure.feature('change patch post')
@pytest.mark.parametrize('test_data_change', Test_data_change)
def test_update_patch_post(fixt_update_patch_post, fixt_post_id,
                           test_data_change):
    fixt_update_patch_post.full_req_patch_post(
        fixt_post_id,
        payload=test_data_change
    )
    with allure.step("Проверяем успешность обновления и имя в ответе"):
        fixt_update_patch_post.check_status_code_is_200()
        assert fixt_update_patch_post.json['name'] == test_data_change['name']
