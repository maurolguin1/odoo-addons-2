# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import models, fields, api


class ProductUpload(models.Model):
    _description = "Log of product uploads"
    _name = 'log'

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
    data = fields.Binary(
        'File',
        required=True
    )
    name = fields.Char(
        'Filename',
        readonly=True
    )

    @api.model
    def create(self, values):
        log_create = super(ProductUpload, self).create(values)
        print 'creando importacion'
        return log_create
