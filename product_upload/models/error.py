# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from openerp import models, fields, api


class Error(models.Model):
    _description = "Errors from product uploads"
    _name = 'error'

    log_id = fields.Integer(
    )
