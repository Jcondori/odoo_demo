# -*- coding: utf-8 -*-
# from odoo import http


# class OdooDemo(http.Controller):
#     @http.route('/odoo_demo/odoo_demo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_demo/odoo_demo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_demo.listing', {
#             'root': '/odoo_demo/odoo_demo',
#             'objects': http.request.env['odoo_demo.odoo_demo'].search([]),
#         })

#     @http.route('/odoo_demo/odoo_demo/objects/<model("odoo_demo.odoo_demo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_demo.object', {
#             'object': obj
#         })
