# -*- coding: utf-8 -*-

from odoo import fields, models


class MyCustomItem(models.Model):
    _name = "my.custom.item"
    _description = "My Custom Item"

    name = fields.Char(required=True)
    description = fields.Text()
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("done", "Done"),
        ],
        default="draft",
        required=True,
    )

    def action_mark_done(self):
        for record in self:
            record.state = "done"
