# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase


class TestTodo(TransactionCase):
	"Create a Simple Todo"
	Todo = self.env['todo.task']
	task = Todo.create({'name' : 'Test Task'})
	self.assertEqual(task.is_done, False)
	