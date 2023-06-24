# -*- coding: utf-8 -*-

from odoo.exceptions import ValidationError
from odoo import models, fields, api


class CitaMedica(models.Model):
    _name = 'cita.medica'
    _description = 'Cita Medica'

    name = fields.Char('Numero de cita', required=True)
    datetime = fields.Datetime(string='Fecha', required=True, default=lambda self: fields.Datetime.now())
    description = fields.Text('Diagnostico')
    partner_id = fields.Many2one('res.partner', string='Médico', ondelete='restrict')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancel', 'Cancelled')], string='Status',
                             required=True, readonly=True, copy=False, default='draft')
    line_ids = fields.One2many(comodel_name='medical.appointment.line', inverse_name='appointment_id')
    category_ids = fields.Many2many('res.partner.category', string='Tags')

    def action_confirm(self):
        for cita in self:
            if cita.state == 'draft':
                if not cita.partner_id:
                    raise ValidationError('El campo medico(a) no puede estar vacío.')
                if not cita.partner_id.is_doctor:
                    raise ValidationError('El medico(a) elegido no es valido.')
                if not cita.partner_id.active:
                    raise ValidationError('No puede usar un medico(a) archivado.')
                cita.state = 'done'

    def action_draft(self):
        for cita in self:
            cita.state = 'draft'

    def create_line(self):
        self.ensure_one()
        # product = self.env['product.product'].search([], limit=1)
        # vals = {
        #     'appointment_id': self.id,
        #     'product_id': product.id,
        #     'quantity': 1,
        # }
        # # stock = self.env['stock.quant'].search([('product_id', '=', product.id)])
        # # if sum(stock.mapped('quantity')) < 1:
        # #     raise ('El producto no tiene stock')
        # self.env['medical.appointment.line'].create(vals)

        # category = self.env['res.partner.category'].search([('name', 'like', 'i')], limit=1)
        # if category:
        #     vals = {'category_ids': [(4, x.id) for x in category]}
        #     self.write(vals)

        # if self.category_ids:
        #     vals = {'category_ids': [(3, self.category_ids[-1].id)]}
        #     self.write(vals)

        # self.write({'category_ids': [(5)]})

        # product = self.env['product.product'].search([], limit=1)
        vals = {
            'product_id': product.id,
            'quantity': 5,
        }
        self.write({'line_ids': [(0, 0, vals)]})

        # if self.line_ids:
        #     self.write({'line_ids': [(1, self.line_ids[0].id, {'quantity': 8})]})


    def write(self, vals):
        res = super().write(vals)
        return res


class MedicalAppointmentLine(models.Model):
    _name = 'medical.appointment.line'
    _description = 'Medical Appointment Line'

    appointment_id = fields.Many2one('cita.medica', required=True)
    product_id = fields.Many2one('product.product', required=True)
    quantity = fields.Float()
