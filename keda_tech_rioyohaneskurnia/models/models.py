# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

TYPE_SELECTION = [
    ('fabric', 'Fabric'),
    ('jeans', 'Jeans'),
    ('cotton', 'Cotton'),
]

class RegistrasiMaterial(models.Model):
    _name = 'registrasi.material'
    _description = 'Model Registrasi Material for client'

    name = fields.Char( required=True)
    code = fields.Char( required=True)
    type = fields.Selection(TYPE_SELECTION, required=True)
    supplier_id = fields.Many2one('res.partner', required=True)
    # currency_id = fields.Many2one("res.currency", string="Valuta")
    currency_id = fields.Many2one('res.currency', readonly=True)
    buy_price = fields.Monetary(required=True)

    @api.model
    def create(self, values):
        print(self)
        if values.buy_price <= 100:
            raise UserError("Buy Price Cant Value < 100")
        data_res = super(RegistrasiMaterial, self).create(values)
        return data_res

    def write(self, values):
        print(self)
        if 'buy_price' in values and values['buy_price'] <= 100:
            raise UserError("Buy Price Cant Value < 100")
        data_res = super(RegistrasiMaterial, self).write(values)
        return data_res

class ResPartnerInherit(models.Model):
    _inherit = 'res.partner'
    _description = 'Model Inherit From Res Partner'


#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
