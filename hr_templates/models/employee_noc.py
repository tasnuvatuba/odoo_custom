from odoo import models, fields, api
from odoo.exceptions import UserError

class EmployeeNOC(models.Model):
    _name = 'employee.noc'
    _description = 'NOC for Employees'

    reference_number = fields.Char(string="Reference Number", required=True, readonly=True, default=lambda self: self.env['ir.sequence'].next_by_code('employee.noc'))
    date = fields.Date(string="Date", required=True, default=fields.Date.context_today)
    employee_id = fields.Many2one('hr.employee', string="Employee", required=True)

    # Related fields to fetch data from the hr.employee model
    name = fields.Char(string="Employee Name", related='employee_id.name', store=True)
    passport_no = fields.Char(string="Passport No", related='employee_id.passport_id', store=True)  # assuming passport_id exists
    father_name = fields.Char(string="Father's Name", related='employee_id.father_name', store=True)
    date_joined = fields.Date(string="Date Joined", related='employee_id.first_contract_date', store=True)
    job_position = fields.Char(string="Job Position", related='employee_id.job_id.name', store=True)


    country = fields.Char(string="Country")
    hr_name = fields.Char(string="Name of HR", default=lambda self: self.env.user.name, required=True)
    email = fields.Char(string="E-mail", default=lambda self: self.env.user.email, required=True)
    phone = fields.Char(string="Phone", default=lambda self: self.env.user.phone, required=True)
