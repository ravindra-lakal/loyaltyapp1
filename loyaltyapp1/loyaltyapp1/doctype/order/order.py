# -*- coding: utf-8 -*-
# Copyright (c) 2015, New Indictrans Technologies PVT LTD and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _
class Order(Document):
	def validate(self):
		#frappe.errprint("Validate occured")
		amount=0
		# self.get is used to access child table values in python script
		for raw in self.get("product_details"):
			amount+=int(raw.total)
		self.amount=amount
		self.repeatitemcheck()


	#total amount is now updated only after order is saved
	def on_update(self):
		pass
	def before_submit(self):
		self.pointscheck()
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
		n1.points_gained=self.points_earned
		if self.checkmethod()==0:
			n1.points_consumed=0
		else:
			n1.points_consumed=self.checkmethod()

		customer.save()
	def repeatitemcheck(self):
		l=[]
		# print "****************"
		# print self.get('product_details')
		# print "****************"
		for item in self.get('product_details'):
			l.append(item.ean)
		#frappe.errprint(item.ean)
		uniquel=set(l)
		if len(l)!=len(uniquel) :
			frappe.throw(_("Same item has been entered multiple times."))
	def checkmethod(self):
		l1=[]
		for raw in self.get("payment_method"):
			l1.append(raw.method)
		if "Points" in l1:
			return int(raw.points)
		else:
			return 0
	def pointscheck(self):
		customer=frappe.get_doc("Customer",self.username)
		tpoint=customer.total_points
		#frappe.errprint(tpoint)
		for raw in self.get("payment_method"):
			if raw.method=="Points":
				# frappe.errprint(tpoint)
				if int(raw.points) > int(tpoint):
					#frappe.errprint("#####True######")

					frappe.throw(_("Customer doesn't have enough points for redumption reduce the points and try again"))
# @frappe.whitelist()
# 	def make_return(source_name,target_doc=None):
		
