# -*- coding: utf-8 -*-
# Copyright (c) 2015, Revant Nandgaonkar and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document, _

class TripRecord(Document):
	def validate(self):
		self.validate_arrival_departure()
		self.calculate_distance()

	def calculate_distance(self):
		fleet_settings = frappe.get_single("Fleet Settings")

		if fleet_settings.distance == "km":
			self.arrival_odometer_mile = self.arrival_odometer_km * 0.6214
			self.departure_odometer_mile = self.departure_odometer_km * 0.6214
			self.distance_km = self.arrival_odometer_km - self.departure_odometer_km
			self.distance_mile = self.distance_km * 0.6214

		if fleet_settings.distance == "mile" and self.odometer_mile:
			self.arrival_odometer_km = self.arrival_odometer_mile * 1.6093
			self.departure_odometer_km = self.departure_odometer_mile * 1.6093
			self.distance_mile = self.arrival_odometer_mile - self.departure_odometer_mile
			self.distance_km = self.distance_km * 1.6093

	def validate_arrival_departure(self):
		if (self.arrival_odometer_mile and self.departure_odometer_mile) or (self.arrival_odometer_km and self.departure_odometer_km):
			if self.arrival_odometer_mile < self.departure_odometer_mile or self.arrival_odometer_km < self.departure_odometer_km:
				frappe.throw(_("Arrival Odometer Reading cannot be Greater than Departure Odometer"))
