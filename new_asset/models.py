# -*- coding: utf-8 -*-

from openerp import models, fields, api
from account_asset import account_asset_depreciation_line

 #class new_asset_test1(models.Model):
 #    _name = 'new_asset.new_asset'
 #    name = fields.Char()
 #    test1 = account_asset_depreciation_line.asset_id
 
class new_asset_test2(models.Model):
    _inherit = 'account_asset.account_asset_depreciation_line'
    _columns = {
        'asset_date_test2_id': depreciation_date,
    }
