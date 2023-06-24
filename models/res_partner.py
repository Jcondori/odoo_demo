from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    is_doctor = fields.Boolean('Es Médico')
