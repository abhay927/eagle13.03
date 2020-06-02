# Part of Eagle. See LICENSE file for full copyright and licensing details.

from eagle import fields, models, api, _


class UomUom(models.Model):
    _inherit = 'uom.uom'

    l10n_cl_sii_code = fields.Char('SII Code')
