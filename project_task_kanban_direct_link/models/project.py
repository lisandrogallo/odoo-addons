# -*- coding: utf-8 -*-

from odoo import models, api


class Task(models.Model):
    _name = "project.task"
    _inherit = 'project.task'

    @api.multi
    @api.onchange('description')
    def _onchange_document_object(self):
        if self.description == u'<p><br></p>':
            self.description = ''
