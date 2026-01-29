# -*- coding: utf-8 -*-
# from odoo import http


# class MyCustomApp(http.Controller):
#     @http.route('/my_custom_app/my_custom_app', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_custom_app/my_custom_app/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_custom_app.listing', {
#             'root': '/my_custom_app/my_custom_app',
#             'objects': http.request.env['my_custom_app.my_custom_app'].search([]),
#         })

#     @http.route('/my_custom_app/my_custom_app/objects/<model("my_custom_app.my_custom_app"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_custom_app.object', {
#             'object': obj
#         })

