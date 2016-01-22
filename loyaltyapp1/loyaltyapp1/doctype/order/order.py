# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies PVT LTD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Order(Document):
	def before_submit(self):

		a=frappe.get_all("Rule Engine", fields=["rule_type","amount","points ","points_multiplication_factor"], filters={"status":"Active"})
		for i in a:
			if i.get('rule_type')=="Loyalty Points":
					minamount=int(i.get('amount'))
					pointsawarded=int(i.get('points'))
					factor=int(i.get('points_multiplication_factor'))
					amount=int(self.amount)
					frappe.errprint([a,factor])
					points=(amount*pointsawarded)/minamount
					a=factor*points
					self.amount=amount
					self.points_earned=a
