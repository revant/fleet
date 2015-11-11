# -*- coding: utf-8 -*-
# Copyright (c) 2015, Revant Nandgaonkar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Vehicle(Document):
	def validate(self):
		self.set_odometer()

	def set_odometer(self):
		fleet_settings = frappe.get_single("Fleet Settings")

		if fleet_settings.distance == "km" and self.odometer_km:
			self.odometer_mile = self.odometer_km * 0.6214

		if fleet_settings.distance == "mile" and self.odometer_mile:
			self.odometer_km = self.odometer_mile * 1.6093

