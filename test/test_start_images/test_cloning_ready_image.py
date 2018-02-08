__author__ = 'vden'

import pytest

@pytest.allure.step('Список виртуальных машин с установленным Postgres')
@pytest.mark.parametrize()
def test_cloning_ready_image(app):

    with pytest.allure.step('Считываем параметры из jenkins '):
        pass
        #list_ready_images = app.app.jnk.
