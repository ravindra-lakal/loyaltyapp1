# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies PVT LTD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Order(Document):
	#total amount is now updated only after order is saved
	def on_update(self):
		amount=0
		# self.get is used to access child table values in python script
		for raw in self.get("product_details"):
			amount+=int(raw.total)
		self.amount=amount



	def before_submit(self):

		a=frappe.get_all("Rule Engine", fields=["rule_type","amount","points ","points_multiplication_factor"], filters={"status":"Active","docstatus":1})
		# docstatus is 1 when document is submitted
		for i in a:
			if i.get('rule_type')=="Loyalty Points":
					minamount=int(i.get('amount'))
					pointsawarded=int(i.get('points'))
					factor=int(i.get('points_multiplication_factor'))
					amount=int(self.amount)
					points=(amount*pointsawarded)/minamount
					a=factor*points
					self.amount=amount
					self.points_earned=a
					self.doc_no=self.name
	def on_submit(self):
		now=0
		customer=frappe.get_doc("Customer",self.username)


		 #customer.set('Points Details',[])
		n1 = customer.append('points_details', {})
		n1.purchase_date=self.purchase_date
		n1.poins_gained=self.points_earned
		#customer.total_points=self.points_earned
		customer.save()
		for raw in customer.get("points_details"):
			frappe.errprint(raw.purchase_date)
			# now+=int(raw.points_gained)
		customer.total_points=now
#points_gained is used just for experimental purpose actually a coloum called total points will be added in place of points_gained
