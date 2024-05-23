from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CitaMedicaWizard(models.TransientModel):
    _name = 'cita.medica.wizard'
    _description = 'Cita Medica Wizard'

    name = fields.Char(string='Nombre')
    datetime = fields.Datetime(string='Fecha', required=True)
    cita_medica_ids = fields.Many2many('cita.medica')

    @api.model
    def default_get(self, default_fields):
        res = super().default_get(default_fields)
        if self.env.context.get('active_model') == 'cita.medica' and self.env.context.get('active_ids'):
            cita = self.env['cita.medica'].browse(self.env.context.get('active_ids'))
            if cita:
                res['name'] = cita[0].name
                res['datetime'] = cita[0].datetime
                res['cita_medica_ids'] = [(4, cita[0].id)]
        return res

    def create_invoices(self):
        for rec in self:
            val = {
                'ref': rec.name,
                'move_type': 'out_invoice'
            }
            if rec.datetime:
                val.update({'date': rec.datetime.date()})
            invoice = self.env['account.move'].create(val)
            if invoice:
                return {
                    'name': 'Factura Cita Medica',
                    'type': 'ir.actions.act_window',
                    'res_model': 'account.move',
                    'context': {'create': False},
                    'view_mode': 'form',
                    'res_id': invoice.id,
                }
            else:
                raise ValidationError('No se ha podido crear la factura')
