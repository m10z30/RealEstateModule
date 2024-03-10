from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import timedelta

class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "estate.property.offer"

    price = fields.Float()
    status = fields.Selection([('accepted','Accepted'), ('refused', 'Refused')], copy=False)

    validity = fields.Integer(default=7)
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_validity")

    partner_id = fields.Many2one('res.partner', required=True)
    property_id = fields.Many2one('estate.property', required=True)


    @api.depends('validity')
    def _compute_deadline(self):
        for record in self:
            if record.validity:
                record.date_deadline = fields.Date.today() + timedelta(days=record.validity)