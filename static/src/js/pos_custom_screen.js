/** @odoo-module **/

import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { registry } from "@web/core/registry";

class MyCustomMainScreen extends ProductScreen {
    static template = "my_custom_app.MyCustomMainScreen";
    static components = ProductScreen.components;

    get categories() {
        const pos = this.env.pos;
        const categoryById = (pos.db && pos.db.category_by_id) || {};
        const rootId = pos.db && pos.db.get_root_category_id ? pos.db.get_root_category_id() : pos.root_category_id;
        return Object.values(categoryById)
            .filter((category) => {
                const parentId = Array.isArray(category.parent_id)
                    ? category.parent_id[0]
                    : category.parent_id;
                return parentId === rootId;
            })
            .sort((a, b) => (a.sequence || 0) - (b.sequence || 0));
    }

    get quickButtons() {
        return [
            { key: "lunch", label: "Lunch", action: "category", category: "Lunch" },
            { key: "drinks", label: "Drinks", action: "category", category: "Drinks" },
            { key: "favorites", label: "Favorites", action: "category", category: "Favorites" },
            { key: "takeaway", label: "Takeaway", action: "toggle_takeaway" },
        ];
    }

    selectCategory(categoryId) {
        if (!categoryId) {
            return;
        }
        if (this.env.pos.setSelectedCategoryId) {
            this.env.pos.setSelectedCategoryId(categoryId);
        } else {
            this.env.pos.selectedCategoryId = categoryId;
        }
    }

    handleQuickButton(button) {
        if (button.action === "category") {
            const category = this._findCategoryByName(button.category);
            if (!category) {
                this._notify(`Category "${button.category}" not found.`);
                return;
            }
            this.selectCategory(category.id);
            return;
        }

        if (button.action === "toggle_takeaway") {
            const order = this.env.pos.get_order();
            if (!order) {
                return;
            }
            order.is_takeaway = !order.is_takeaway;
            this._notify(order.is_takeaway ? "Takeaway enabled." : "Takeaway disabled.");
        }
    }

    _findCategoryByName(name) {
        const categoryById = (this.env.pos.db && this.env.pos.db.category_by_id) || {};
        return Object.values(categoryById).find((category) => category.name === name);
    }

    _notify(message) {
        if (this.env.services && this.env.services.notification) {
            this.env.services.notification.add(message, { type: "info" });
        }
    }
}

registry.category("pos_screens").add("ProductScreen", MyCustomMainScreen, { force: true });
