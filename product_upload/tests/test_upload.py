# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp.tests import common
import os
import openpyxl

#    Forma de correr el test
#    -----------------------
#
#   Definir un subpackage tests que será inspeccionado automáticamente por
#   modulos de test los modulos de test deben enpezar con test_ y estar
#   declarados en el __init__.py, como en cualquier package.
#
#   Hay que crear una base de datos no importa el nombre (por ejemplo act_test)
#   vacia y con el modulo que se va a testear instalado (por ejemplo business).
#
#   El usuario admin tiene que tener password admin, Language English, Country
#   United States.
#
#   oe -Q product_upload -c iomaq -d iomaq_test_product_upload
#

DECKER_0 = [{
    'default_code': 'D25811K-AR-DECKER',
    'cost': 9490.76,
    'currency': u'ARS',
    'margin': 0.42,
    'name': u'17 MM HEX DEDICATED CHIPPING HAMMER',
    'purchase_tax': 0.105,
    'sale_tax': 0.105,
    'barcode': 885911484848L,
    'meli': u'MELICODE123',
    'meshop': None
}]

EINHELL_0 = [{
    'default_code': '4513859-EINHELL',
    'cost': 9490.76,
    'currency': u'ARS',
    'margin': 0.42,
    'name': u'17 MM HEX DEDICATED CHIPPING HAMMER',
    'purchase_tax': 0.105,
    'sale_tax': 0.105,
    'barcode': 885911484848L,
    'meli': False,
    'meshop': False
}]


class TestProductUploadProduct(common.TransactionCase):
    """ Cada metodo de test corre en su propia transacción y se hace rollback
        despues de cada uno.
    """

    def setUp(self):
        super(TestProductUploadProduct, self).setUp()
        self.wizard_obj = self.env['product_upload.import_worksheet']

        log_obj = self.env['product_upload.log']
        self.wizard_obj.log = log_obj.create({})

    @staticmethod
    def get_filename(nro):
        path = os.path.dirname(os.path.realpath(__file__))
        return path + '/products_{}.xlsx'.format(nro)

    def get_ws(self, nro):
        return openpyxl.load_workbook(filename=self.get_filename(nro),
                                      read_only=True,
                                      data_only=True)

    def test_01_(self):
        data = self.wizard_obj.read_data(self.get_ws(0)['B&D'])
        self.assertEqual(data[0]['default_code'], DECKER_0[0]['default_code'])
        self.assertEqual(data[0]['barcode'], DECKER_0[0]['barcode'])
        self.assertEqual(data[0]['cost'], DECKER_0[0]['cost'])
        self.assertEqual(data[0]['currency'], DECKER_0[0]['currency'])
        self.assertEqual(data[0]['margin'], DECKER_0[0]['margin'])
        self.assertEqual(data[0]['meli'], DECKER_0[0]['meli'])
        self.assertEqual(data[0]['name'], DECKER_0[0]['name'])
        self.assertEqual(data[0]['purchase_tax'], DECKER_0[0]['purchase_tax'])
        self.assertEqual(data[0]['sale_tax'], DECKER_0[0]['sale_tax'])

    def test_02_(self):
        data = self.wizard_obj.read_data(self.get_ws(0)['B&D'])
        self.wizard_obj.check_data(data,'B&D')


    def test_02_(self):
        self.wizard_obj.process_tmp_file(self.get_filename(0))
        self.assertEqual(self.wizard_obj.log.state, 'done')
