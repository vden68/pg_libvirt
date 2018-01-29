__author__ = 'vden'

import pytest

@pytest.allure.step('Список виртуальных машин с установленным Postgres')
def test_get_list_ready_images(app):

    with pytest.allure.step('Получаем список готовых виртуальных машин '):
        dict_ready_images = app.img.get_list_ready_images()

    with pytest.allure.step('Получаем список готовых виртуальных машин '):
        app.jsn.written_in_json_python_obj(python_obj=dict_ready_images)


