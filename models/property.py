from odoo import models, fields, api
from datetime import timedelta

class Property(models.Model):
    _name = "estate.property"
    _description = "Estate Property"


    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(default=fields.date.today() + timedelta(days=90))
    expected_price = fields.Float(required=True)
    best_price = fields.Float(compute="_compute_best_price", string="Best Offer")
    selling_price = fields.Float()
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(default=0)
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(default=0)
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', "East"), ('west', 'West')])

    total_area = fields.Float(compute="_compute_total_area")

    salesperson = fields.Many2one('res.users', string='Salesperson', index=True, tracking=True, default=lambda self: self.env.user)
    buyer = fields.Many2one('res.partner', copy=False, string="Buyer")
    property_type = fields.Many2one('estate.property.type', string="Property Type")
    tag_ids = fields.Many2many('estate.property.tag')
    offer_ids = fields.One2many('estate.property.offer', 'property_id')

    active = fields.Boolean(default=True)
    state  = fields.Selection([
        ('new', 'New'),
        ('offer_received', 'Offer Received'),
        ('offer_accepted', 'Offer Accepted'),
        ('sold', 'Sold'),
        ('cancelled', 'Cancelled')
    ], default='new')

    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area
    

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            best_price = 0
            for offer in record.offer_ids:
                if offer.price > best_price:
                    best_price = offer.price
            
            record.best_price = best_price
        

