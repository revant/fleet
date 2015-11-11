# -*- coding: utf-8 -*-
# Copyright (c) 2015, Revant Nandgaonkar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document, _

class FillUpRecord(Document):
	def validate(self):
		self.validate_distance_settings()
		self.validate_last_fillup()
		self.calculate_total_cost()

	def calculate_total_cost(self):
		self.total_cost = self.fuel_price * self.fillup_vol

	def validate_last_fillup(self):
		last_fillup = frappe.get_list("Fill Up Record",
			fields=["odometer_km","odometer_mile"],
			filters = {
				"vehicle": self.vehicle,
				"docstatus": 1
			})
		
		fleet_settings = frappe.get_single("Fleet Settings")

		if fleet_settings.distance == "km":
			if last_fillup and last_fillup[0].odometer_km > self.odometer_km:
				frappe.throw(_("Odometer was showing higher number in previous transaction"))

		if fleet_settings.distance == "mile":
			if last_fillup and last_fillup[0].odometer_mile > self.odometer_mile:
				frappe.throw(_("Odometer was showing higher number in previous transaction"))

	def validate_distance_settings(self):
		fleet_settings = frappe.get_single("Fleet Settings")

		if fleet_settings.distance == "km" and self.odometer_km:
			self.odometer_mile = self.odometer_km * 0.6214

		if fleet_settings.distance == "mile" and self.odometer_mile:
			self.odometer_km = self.odometer_mile * 1.6093
