from odoo import fields, models, api


class Property(models.Model):
    # table in the database, use . instead of _
    _name = 'estate.property'
    _inherit = ['mail.thread', 'mail.activity.mixin'] #can't use website mixin
    _description = 'Estate Properties'

    # columns of the table
    name = fields.Char(string="Property Name", required=True)
    state = fields.Selection([('new', 'New'),
                              ('received', 'Offer Received'),
                              ('accepted', 'Offer Accepted'),
                              ('sold', 'Sold'),
                              ('cancel', 'Cancel')], default='new', string="Status")
    type_id = fields.Many2one('estate.property.type',
                              string="Property Type")  # convention is to use id at the end of Many2one rel
    tag_ids = fields.Many2many('estate.property.tag',
                               string="Property Tags")  # convention is to use ids at the end of Many2many rel
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    data_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price", tracking=True)
    best_offer = fields.Float(string="Best Offer", compute='_compute_best_price')
    selling_price = fields.Float(string="Selling Price", readonly="1")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Garden Orientation", default='north'
    )
    # automatic fields
    # id, create_date, created_uid, write_date, write_uid
    # if no access rights are specified, odoo determines that no user can access the data
    offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
    sales_id = fields.Many2one('res.users', string="Salesman")
    buyer_id = fields.Many2one('res.partner', string="Buyer", domain=[('is_company', '=', True)])
    phone = fields.Char(string="Phone", related='buyer_id.phone')

    # onchange works inside the form view only, computed works anywhere
    @api.onchange('living_area', 'garden_area')
    def _onchange_total_area(self):
        self.total_area = self.living_area + self.garden_area

    total_area = fields.Integer(string="Total Area")

    def action_sold(self):
        self.state = 'sold'

    def action_cancel(self):
        self.state = 'cancel'

    @api.depends('offer_ids')
    def _compute_offer_count(self):
        for rec in self:
            rec.offer_count = len(rec.offer_ids)

    offer_count = fields.Integer(string="Offer Count", compute=_compute_offer_count)

    @api.depends('offer_ids')
    def _compute_best_price(self):
        for rec in self:
            if rec.offer_ids:
                rec.best_offer = max(rec.offer_ids.mapped('price'))
            else:
                rec.best_offer = 0

    def action_client_action(self):
        return {
            'type': 'ir.actions.client',
            # 'tag': 'reload'
            # 'tag': 'apps'
            'tag': 'display_notification',
            'params': {
                'title': 'Testing Client',
                'type': 'success',
                'sticky': False

            }
        }

    def _get_report_base_filename(self):
        self.ensure_one()
        return 'Estate Property - %s' % self.name

class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Estate Property Type'

    name = fields.Char(string="Property Type Name", required=True)


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Estate Property Tag'

    name = fields.Char(string="Property Tag Name", required=True)
    color = fields.Integer(string="Color")
