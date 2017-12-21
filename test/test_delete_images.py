# -*- coding: utf-8 -*-
__author__ = 'vden'

import pytest


@pytest.allure.step('Удаление images')
def test_delete_images(app):

    with pytest.allure.step('получаем список на удаление '):
        list_del = app.img.get_list_delete()
