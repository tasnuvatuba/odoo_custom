from odoo import fields, models, api


class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Training Session Model'

    name = fields.Char(string='Training Name', required=True)
    topic = fields.Char(string='Topic', required=True)
    trainer = fields.Many2one('res.partner', string='Trainer', required=True)
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    status = fields.Selection([
        ('planned', 'Planned'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ], string='Status', default='planned', required=True)
    participants = fields.Many2many('res.partner', string='Participants')
