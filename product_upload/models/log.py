# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import models, fields, api, _
import openpyxl


class Log(models.Model):
    _description = "Log of product uploads"
    _name = 'product_upload.log'

    updated_products = fields.Integer(
    )
    created_products = fields.Integer(
    )
    errors = fields.Integer(
    )
    error_ids = fields.One2many(
        comodel_name="error",
        inverse_name="log_id",
        string="Errors",
        readonly=True
    )
    state = fields.Selection(
        [('load', 'Load'),  # load spreadsheet
         ('error', 'Error')],  # show errors
        default="load"
    )

    @api.multi
    def name_get(self):
        ret = []
        for rec in self:
            name = _(u'Uploaded for {} on {}').format(rec.create_uid.name,
                                                      rec.create_date)
            ret.append((rec.id, name))
        return ret

    @api.multi
    def import_worksheet(self):
        for rec in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Import Worksheet',
                'res_model': 'product_upload.import_worksheet',
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new',
                'context': {'fp_name': ''}
            }

    def add_error(self, text):
        pass

    def process_data(self, fp_name):
        product_obj = self.env['product.product']
        partner_obj = self.env['res.partner']

        # open worksheet
        wb = openpyxl.load_workbook(filename=fp_name,
                                    read_only=True,
                                    data_only=True)

        # cada hoja de la planilla es un vendor
        for vendor in wb.sheetnames:
            partner = partner_obj.search([('ref', '=', vendor)])
            if not partner:
                self.add_error(_('Vendor %s not found.') % vendor)
                break
            # leer toda la hoja en una estructura
            data = self.read_data(wb[vendor])
            # chequear la estructura
            if self.check_data(data, vendor):
                # aplicar la estructura
                self.process_data(data, vendor)
            else:
                return
