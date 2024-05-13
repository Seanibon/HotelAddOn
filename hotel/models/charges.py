# -*- coding: utf-8 -*-
# charges.py

from odoo import models, fields, api


class charges(models.Model):
    _name = 'hotel.charges'
    _description = 'hotel charges master list'
    _order = 'title'

    title = fields.Char("Charge Title")
    description = fields.Char("Description")

