__author__ = 'vden'

import pytest

@pytest.allure.step('Список виртуальных машин с установленным Postgres')
def test_get_list_ready_images(app):

    with pytest.allure.step('Получаем список виртуальных машин '):
        list_ready_images = app.img.get_list_ready_images()

