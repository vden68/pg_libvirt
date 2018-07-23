# -*- coding: utf-8 -*-
__author__ = 'vden'
import os
import pytest
import time
from fixture.fixlib.lib import Lib_helper

class Image_helper:
    def __init__(self, app):
        self.app = app
        self.flib = Lib_helper(self)


    def clone_an_image(self, image=None, clone_name=None):

        conn_open_kvm = self.conn_open_kvm2()

        lib_domain = self.check_for_availability(conn_open_kvm, image)
        if lib_domain is None:
            print('Cannot find image %s to be clone.' %image ) # self.app.pgl_kvm.name_sourse_image)
            exit(0)

        #if the domain is enabled we finish work domain
        if lib_domain.ID() != -1:
            self.flib.domain_shutdown_name(conn=conn_open_kvm, lib_name=lib_domain.name())

        if clone_name is None:
            with pytest.allure.step('Формируем название новой виртуальной машины'):
                clone_name = self.flib.create_clone_name(pgl_kvm=self.app.pgl_kvm, conn=conn_open_kvm)

        with pytest.allure.step('Клонируем образ %s в новый клон %s' %(self.app.pgl_kvm.name_source_image, clone_name)):
            self.flib.clone_image(clone_name=clone_name, name_image=image , conn=conn_open_kvm)
            #self.app.pgl_kvm.name_sourse_image, conn=conn_open_kvm)

        conn_open_kvm.close()

        return clone_name

    def check_for_availability(self, conn_open_kvm, image):
        with pytest.allure.step('Проверяем на наличие образ %s' % image):
            lib_domain = self.flib.domain_check_for_availability(check_domain=image,
                                                                 # self.app.pgl_kvm.name_sourse_image,
                                                                 conn=conn_open_kvm)
        return lib_domain

    def conn_open_kvm2(self):
        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()
        return conn_open_kvm

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

        list_yes = self.get_list_yes(list_images)

        list_del=list_yes

        """
        list_del=[]
        split_equally=None
        for list_y in list_yes:
            split_yes=list_y.split('--')
            if split_yes[0]+split_yes[1]+split_yes[2]+split_yes[3]+split_yes[4]+split_yes[5]+split_yes[6] == split_equally:
                list_del.append(list_y)
            else:
                split_equally=split_yes[0]+split_yes[1]+split_yes[2]+split_yes[3]+split_yes[4]+split_yes[5]+split_yes[6]

        """
        print('list_del=', list_del)

        conn_open_kvm.close()

        return list_del

    def get_list_yes(self, list_images):
        print('\n')
        list_yes = []
        for list_image in list_images:
            #print(list_image.name())

            split_image = list_image.name().split('--')
            if len(split_image) > 7 and (split_image[0] == 'yes' or split_image[0] == 'mmts_node1'
                                         or split_image[0] == 'mmts_node2'or split_image[0] == 'mmts_node3'
                                         or split_image[0] == 'quick'):
                print('.....', list_image.name())
                #print(split_image[0])
                list_yes.append(list_image.name())
        #print('list_yes= \n', list_yes)
        list_yes.sort(reverse=True)
        print('list_yes= \n', list_yes)
        return list_yes

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


    def get_list_ready_images(self):
        with pytest.allure.step('Подключаемся к KVM'):
            conn_open_kvm = self.flib.connection_open()

        with pytest.allure.step('Получаем список images '):
            list_images = self.flib.get_list_images(conn=conn_open_kvm)

        list_yes=self.get_list_yes(list_images)
        list_yes.sort(reverse=False)
        #print(list_yes)

        list_ready_images = []

        sly0 = None
        sly1 = None
        sly2 = None
        sly3 = None
        sly4 = None
        sly5 = None
        sly6 = None

        for list_y in list_yes:
            split_list_y = list_y.split('--')
            if sly0 == None or (split_list_y[0] != sly0 or split_list_y[1] != sly1 or split_list_y[2] != sly2 or
                                 split_list_y[3] != sly3 or split_list_y[4] != sly4 or split_list_y[5] != sly5 or
                                 split_list_y[6] != sly6):

                sly0 = split_list_y[0]
                sly1 = split_list_y[1]
                sly2 = split_list_y[2]
                sly3 = split_list_y[3]
                sly4 = split_list_y[4]
                sly5 = split_list_y[5]
                sly6 = split_list_y[6]

                list_ready_images.append(sly1+'--'+sly2+'--'+sly3+'--'+sly4+'--'+sly5+'--'+sly6)

        #print('list_ready_images=', list_ready_images)

        return list_ready_images

    def creating_nodes(self, clone_name):

        mmts_node1 = 'mmts_node1--' + clone_name
        mmts_node2 = 'mmts_node2--' + clone_name
        mmts_node3 = 'mmts_node3--' + clone_name

        with pytest.allure.step('Переименовываем виртуальную машину %s в %s' % (clone_name, mmts_node1)):
            self.rename_image(name_image=clone_name, name_image_new=mmts_node1)

        time.sleep(2)
        with pytest.allure.step('Клонирование образа %s ' % mmts_node1):
            self.clone_an_image(image=mmts_node1, clone_name=mmts_node2)

        time.sleep(2)
        with pytest.allure.step('Клонирование образа %s ' % mmts_node1):
            self.clone_an_image(image=mmts_node1, clone_name=mmts_node3)










