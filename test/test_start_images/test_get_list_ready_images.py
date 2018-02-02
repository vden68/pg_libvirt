__author__ = 'vden'

import pytest

@pytest.allure.step('Список виртуальных машин с установленным Postgres')
def test_get_list_ready_images(app):

    with pytest.allure.step('Получаем список готовых виртуальных машин '):
        list_ready_images = app.img.get_list_ready_images()

    with pytest.allure.step('Получаем список готовых виртуальных машин '):
        app.jnk.written_in_property_file_list_ready_images(list_property = list_ready_images,
                                                           name_file= 'ready_images.txt', property_key= 'images')


