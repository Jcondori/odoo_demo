from odoo import models, fields, api
from odoo.exceptions import ValidationError
import base64


class CitaMedicaDoctorReport(models.TransientModel):
    _name = 'cita.medica.doctor.report'
    _description = 'Cita Medica Doctor Report'

    # Parámetros
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Date End')

    # Resultado
    file = fields.Binary(string='File')
    file_name = fields.Char(string='File Name', compute='_compute_file_name')

    def _compute_file_name(self):
        for rec in self:
            rec.file_name = 'reporte_doctor.txt'

    def generate_report(self):
        content = ''

        # citas1 = self.env['cita.medica'].search([])
        # for cita in citas:
        #     cita.name

        # citas2 = self.env['cita.medica'].search_read([], ['name', 'partner_id'])
        # for cita in citas:
        #     cita.name

        # citas3 = self.env['cita.medica'].read_group([], ['partner_id'], ['partner_id'])
        # for cita in citas3:
        #     cita.name

        # sql2 = """
        #     select rp.name, count(*)
        #     from cita_medica cm
        #              inner join res_partner rp on cm.partner_id = rp.id
        #     group by rp.name
        # """
        # self.env.cr.execute(sql2)
        # result2 = self.env.cr.fetchall()

        sql = """
            select rp.name, count(*)
            from cita_medica cm
                     inner join res_partner rp on cm.partner_id = rp.id
            group by rp.name
        """
        self.env.cr.execute(sql)
        result = self.env.cr.dictfetchall()
        for line in result:
            text_line = '%s|%s' % (
                line['name'],
                line['count']
            )
            content += text_line + '\n'
        self.write({
            'file': base64.b64encode(content.encode('utf-8'))
        })
        return {
            'name': 'Doctor Resultado',
            'type': 'ir.actions.act_window',
            'res_model': self._name,
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'target': 'new'
        }
