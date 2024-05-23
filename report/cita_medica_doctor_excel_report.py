import io
import base64

from odoo import models, fields, api
from odoo.tools.misc import xlsxwriter


class CitaMedicaDoctorReport(models.TransientModel):
    _name = 'cita.medica.doctor.excel.report'
    _description = 'Cita Medica Doctor Excel Report'

    # Parámetros
    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Date End')

    # Resultado
    file = fields.Binary(string='File')
    file_name = fields.Char(string='File Name', compute='_compute_file_name')

    def _compute_file_name(self):
        for rec in self:
            rec.file_name = 'reporte_doctor.xlsx'

    def generate_report(self):
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()

        # Formatos de celda
        header = workbook.add_format({'bold': True, 'border': 1, 'align': 'center'})
        border = workbook.add_format({'border': 1})

        # Cabeceras
        worksheet.merge_range(1, 1, 1, 2, 'Cant. Citas', header)  # B2:C2
        worksheet.write_string(2, 1, 'Doctor', header)  # B3
        worksheet.write_string(2, 2, 'Cantidad', header)  # C3

        # Ancho de las columnas
        worksheet.set_column('B:B', 11)

        # Data
        sql = """
            select rp.name, count(*)
            from cita_medica cm
                     inner join res_partner rp on cm.partner_id = rp.id
            group by rp.name
        """
        self.env.cr.execute(sql)
        result = self.env.cr.fetchall()

        # Logica
        row = 3
        total = 0
        first_row = row
        for line in result:
            worksheet.write_string(row, 1, line[0], border)  # ROW | B
            worksheet.write_number(row, 2, line[1], border)  # ROW | C
            total += line[1]
            row += 1

        # Total
        worksheet.write_string(row, 1, 'Total:', border)
        worksheet.write_number(row, 2, total, border)
        worksheet.write_formula(row, 3, f'SUM(C{first_row + 1}:C{row})', border)

        workbook.close()
        output.seek(6)
        self.write({
            'file': base64.b64encode(output.getvalue()),
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
