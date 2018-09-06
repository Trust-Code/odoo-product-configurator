
from odoo import models


class ProductConfigurator(models.TransientModel):
    _inherit = 'product.configurator'

    def _extra_line_values(self, so, product, new=True):
        vals = super(ProductConfigurator, self)._extra_line_values(
            so, product, new=new)

        if self.env.context['active_model'] == 'stock.picking':
            vals['location_id'] = so.location_id.id
            vals['location_dest_id'] = \
                so.picking_type_id.default_location_dest_id.id

        return vals
