# -*- coding: utf-8 -*-
from openerp import http

# class NewAsset(http.Controller):
#     @http.route('/new_asset/new_asset/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/new_asset/new_asset/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('new_asset.listing', {
#             'root': '/new_asset/new_asset',
#             'objects': http.request.env['new_asset.new_asset'].search([]),
#         })

#     @http.route('/new_asset/new_asset/objects/<model("new_asset.new_asset"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('new_asset.object', {
#             'object': obj
#         })