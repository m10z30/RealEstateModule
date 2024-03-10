from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate.property.offer"

    price = fields.Float()
    status = fields.Selection([('accepted','Accepted'), ('refused', 'Refused')], copy=False)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_deadline")

    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)


    @api.depends('validity')
    def _compute_deadline(self):
        for record in self:
            if record.validity:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)
    

    def action_accept(self):
        for record in self:
            if record.property_id.selling_price > 0 or record.status == "accepted":
                raise UserError('The property already sold')
            elif record.status == "refused":
                raise UserError('The offer is already refused')
            else:
                record.status = "accepted"
                record.property_id.selling_price = record.price
                record.property_id.buyer = record.partner_id
    
    def action_refuse(self):
        for record in self:
            if record.status == "accepted":
                raise UserError('The offer has been accepted before')
            elif record.status == "refused":
                raise UserError('The offer is already refused')
            else:
                record.status = "refused"
    