# -*- coding: utf-8 -*-

from odoo import fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    x_sale_order_id = fields.Many2one(
        "sale.order",
        string="Sales Order",
        copy=False,
    )

    def action_create_sale_order(self):
        self.ensure_one()
        if self.x_sale_order_id:
            return self._action_open_sale_order(self.x_sale_order_id)

        partner = self.partner_id or self.company_id.partner_id
        order_lines = []
        for line in self.lines:
            product = line.product_id
            if not product:
                continue
            order_lines.append(
                (
                    0,
                    0,
                    {
                        "product_id": product.id,
                        "name": line.full_product_name or product.display_name,
                        "product_uom_qty": line.qty,
                        "price_unit": line.price_unit,
                        "product_uom": (
                            line.product_uom_id.id if line.product_uom_id else product.uom_id.id
                        ),
                    },
                )
            )

        sale_order = self.env["sale.order"].create(
            {
                "partner_id": partner.id,
                "origin": self.name,
                "order_line": order_lines,
            }
        )
        self.x_sale_order_id = sale_order
        return self._action_open_sale_order(sale_order)

    def _action_open_sale_order(self, sale_order):
        action = self.env.ref("sale.action_orders").read()[0]
        action.update(
            {
                "res_id": sale_order.id,
                "views": [(self.env.ref("sale.view_order_form").id, "form")],
                "view_mode": "form",
                "target": "current",
            }
        )
        return action
