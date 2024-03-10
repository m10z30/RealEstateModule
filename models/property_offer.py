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

    # def _inverse_deadline(self):
    #     for record in self:
    #         if record.date_deadline:
    #             today = fields.Date.today()
    #             today_date = fields.Date.from_string(today)  # Convert datetime.datetime to datetime.date
    #             delta = (record.date_deadline - today_date).days
    #             record.validity = delta if delta > 0 else 0
    #         else:
    #             raise UserError('Date Deadline cannot be empty!')


    # @api.depends('validity')
    # def _compute_deadline(self):
    #     for record in self:
    #         if record.create_date:
    #             record.date_deadline = record.create_date + timedelta(days=record.validity)
    #         else:
    #             record.date_deadline = fields.Date.today() + timedelta(days=record.validity)
    
    
            
    
    # def _calculate_validity(self):
    #     for record in self:
    #         # if record.date_deadline:
    #             today = record.create_date
    #             today_date = fields.Date.from_string(today)  # Convert datetime.datetime to datetime.date
    #             delta = (record.date_deadline - today_date).days
    #             record.validity = delta if delta > 0 else 0
            