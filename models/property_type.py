from odoo import models, fields


class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "estate.property.type"

    name = fields.Char("Property Type Name")
    