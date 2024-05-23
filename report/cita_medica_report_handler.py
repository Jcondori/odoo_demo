from odoo import models, fields, api


class CitaMedicaCustomHandler(models.AbstractModel):
    _name = 'cita.medica.report.handler'
    _inherit = 'account.report.custom.handler'
    _description = 'Cita Medica Custom Handler'

    def _dynamic_lines_generator(self, report, options, all_column_groups_expression_totals):
        lines = [{
            'id': report._get_generic_line_id(None, None, markup='citas_medicas'),
            'name': 'Citas Medicas',
            'class': 'total',
            'columns': [
                {},
                {}
            ],
            'level': 1,
        }]

        return [(0, line) for line in lines]
