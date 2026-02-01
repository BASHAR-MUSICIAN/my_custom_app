# -*- coding: utf-8 -*-

from odoo import fields, models


class MyCustomItem(models.Model):
    _name = "my.custom.item"
    _description = "My Custom Item"

    name = fields.Char(required=True)
    description = fields.Text()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("in_progress", "In Progress"),
            ("done", "Done"),
        ],
        default="draft",
        required=True,
    )

    def action_mark_done(self):
        for record in self:
            record.state = "done"

    def action_reset_to_draft(self):
        for record in self:
            record.state = "draft"

    def action_start_progress(self):
        for record in self:
            record.state = "in_progress"

    def action_toggle_active(self):
        for record in self:
            record.active = not record.active
