# -*- coding: utf-8 -*-
__author__ = 'vden'
import os
import pytest
from fixture.fixlib.lib import Lib_helper

class Image_helper:
    def __init__(self, app):
        self.app = app
        self.flib = Lib_helper(self)


    def clone_an_image(self):

        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()

        with pytest.allure.step('Проверяем на наличие образ %s' % self.app.pgl_kvm.name_sourse_image):
            lib_domain = self.flib.domain_check_for_availability(check_domain=self.app.pgl_kvm.name_sourse_image,
                                                                 conn=conn_open_kvm)
        if lib_domain is None:
            print('Cannot find image %s to be clone.' %self.app.pgl_kvm.name_sourse_image)
            exit(0)

        #if the domain is enabled we finish work domain
        if lib_domain.ID() != -1:
            self.flib.domain_shutdown_name(conn=conn_open_kvm, lib_name=lib_domain.name())

        with pytest.allure.step('Формируем название новой виртуальной машины'):
            clone_name = self.flib.create_clone_name(pgl_kvm=self.app.pgl_kvm, conn=conn_open_kvm)

        with pytest.allure.step('Клонируем образ %s в новый клон %s' %(self.app.pgl_kvm.name_sourse_image, clone_name)):
            self.flib.clone_image(clone_name=clone_name, name_image=self.app.pgl_kvm.name_sourse_image, conn=conn_open_kvm)

        conn_open_kvm.close()

        return clone_name


    def start_image(self, name_image):

        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()

        with pytest.allure.step('Проверяем на наличие образ %s' % name_image):
            lib_domain = self.flib.domain_check_for_availability(check_domain=name_image,
                                                             conn=conn_open_kvm)
        if lib_domain is None:
            print('Cannot find image %s to be clone.' % name_image)
            exit(0)

        with pytest.allure.step('Стартуем виртуальную машину %s' % name_image):
            lib_domain= self.flib.start_image(lib_domain=lib_domain, conn=conn_open_kvm)

        conn_open_kvm.close()

        return lib_domain


    def rename_image(self, name_image, name_image_new):

        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()

        with pytest.allure.step('Проверяем на наличие образ %s' % name_image):
            lib_domain = self.flib.domain_check_for_availability(check_domain=name_image,
                                                             conn=conn_open_kvm)

        if lib_domain is None:
            print('Cannot find image %s to be clone.' % name_image)
            exit(0)

        #if the domain is enabled we finish work domain
        if lib_domain.ID() != -1:
            self.flib.domain_shutdown_name(conn=conn_open_kvm, lib_name=lib_domain.name())

        with pytest.allure.step('Переименовываем виртуальную машину %s в %s' % (name_image, name_image_new)):
            self.flib.rename_image(name_image=name_image, name_image_new=name_image_new, conn=conn_open_kvm)

        conn_open_kvm.close()


    def get_list_delete(self):

        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()

        with pytest.allure.step('Получаем список images '):
            list_images = self.flib.get_list_images(conn=conn_open_kvm)

        print('\n')
        list_yes = []
        for list_image in list_images:
            print(list_image.name())


            split_image= list_image.name().split('--')
            if len(split_image)>7 and (split_image[0]=='yes'):
                print('.....', list_image.name())
                print(split_image[0])
                list_yes.append(list_image.name())

        print('list_yes= \n', list_yes)
        list_yes.sort(reverse=True)
        print('list_yes= \n', list_yes)

        list_del=[]
        split_equally=None
        for list_y in list_yes:
            split_yes=list_y.split('--')
            if split_yes[0]+split_yes[1]+split_yes[2]+split_yes[3]+split_yes[4]+split_yes[5]+split_yes[6] == split_equally:
                list_del.append(list_y)
            else:
                split_equally=split_yes[0]+split_yes[1]+split_yes[2]+split_yes[3]+split_yes[4]+split_yes[5]+split_yes[6]

        print('list_del=', list_del)

        conn_open_kvm.close()

        return list_del

    def delete_images(self, list_del):

        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()

        with pytest.allure.step('Удаляем '):
            for list_d in list_del:

                with pytest.allure.step('Получаем путь к файлу .img ВМ %s' %list_d):
                    path_img= self.flib.get_path_img(conn=conn_open_kvm, del_img=list_d)

                with pytest.allure.step('Удаляем %s' %list_d):
                    self.flib.del_img(conn=conn_open_kvm, del_img=list_d, path_img=path_img)



        conn_open_kvm.close()








