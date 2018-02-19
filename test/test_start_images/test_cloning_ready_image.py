__author__ = 'vden'

import pytest
import os.path

from model.test_data import Test_data


test_data = [
    (),
    (),
]




@pytest.allure.step('Список виртуальных машин с установленным Postgres')
@pytest.mark.parametrize()
def test_cloning_ready_image(app):

    with pytest.allure.step('Считываем параметры из jenkins '):
        pass
        #list_ready_images = app.app.jnk.
