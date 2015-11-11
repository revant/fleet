# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Fleet": {
			"color": "#800000",
			"icon": "octicon octicon-dashboard",
			"type": "module",
			"label": _("Fleet")
		}
	}
