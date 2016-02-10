# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies PVT LTD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class Customer(Document):
	def validate(self):
		#checks if the mobile number is unique
		a=frappe.db.get_value("Customer",{"username":self.username},"username")
		if a==self.username:
			frappe.throw(_("Username already used please enter diffrent one"))
		#counts total points on each update
		points_gained=0
		points_consumed=0
		total_points=0
		for raw in self.get("points_details"):
			points_gained+=int(raw.points_gained)
			points_consumed+=int(raw.points_consumed)
		self.total_points=points_gained - points_consumed
		self.pos_customer_id=self.name
	# def checkusername(self):
	# 	a=frappe.db.get_value("Customer",{"username":self.username},"username")
	# 	return
