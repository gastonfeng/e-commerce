# -*- coding: utf-8 -*-
# © 2015 Antiun Ingeniería, S.L. - Jairo Llopis
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.addons.website_sale.controllers.main import WebsiteSale

from odoo import http


class RequireLoginToCheckout(WebsiteSale):
    @http.route(auth="user")
    def checkout(self, **post):
        return super(RequireLoginToCheckout, self).checkout(**post)
