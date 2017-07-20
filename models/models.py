# -*- coding: utf-8 -*-

from odoo import models, fields, api

<<<<<<< HEAD
# class todo_app(models.Model):
#     _name = 'todo_app.todo_app'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
=======
class TodoTask(models.Model):
	_name="todo.task"
	_description = "To-Do Task"
	name = fields.Char('Description', required=True)
	is_done = fields.Boolean('Done?')
	active = fields.Boolean('Active?',default=True)

	@api.multi
	def do_toggle_done(self):
		for task in self:
			task.is_done = not task.is_done
		return True
		
	@api.model 
	def do_clear_done(self):
		dones = self.search([('is_done','=',True)])
		dones.write({'active': False})
		return True
>>>>>>> c7efeb3aa008d20d82f33b8f02a31a9ab9391f84
