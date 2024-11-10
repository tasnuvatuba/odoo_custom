from odoo import models, fields, api

class Employee(models.Model):
    _inherit = 'hr.employee'

    father_name = fields.Char(string='Father Name')


