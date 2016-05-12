# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2016 Comunitea All Rights Reserved
#    $Omar Castiñeira Saavedra <omar@comunitea.com>$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api


class ProductTemplate(models.Model):

    _inherit = "product.template"

    @api.one
    def _stock_conservative(self):
        self.virtual_stock_conservative = self.qty_available - \
            self.outgoing_qty

    virtual_stock_conservative = fields.Float(compute=_stock_conservative,
                                              string='Virtual Stock '
                                                     'Conservative',
                                              readonly=True)


class ProductProduct(models.Model):

    _inherit = "product.product"

    @api.one
    def _stock_conservative(self):
        self.virtual_stock_conservative = self.qty_available - \
            self.outgoing_qty

    virtual_stock_conservative = fields.Float(compute=_stock_conservative,
                                              string='Virtual Stock '
                                                     'Conservative',
                                              readonly=True)