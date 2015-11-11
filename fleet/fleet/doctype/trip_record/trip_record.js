// see license.txt

unhide_field = function(n) {
	if(cur_frm) {
		if(n.substr) toggle_field(n, 0);
		else { for(var i in n) toggle_field(n[i], 0) }
	}
}

hide_field = function(n) {
	if(cur_frm) {
		if(n.substr) toggle_field(n, 1);
		else { for(var i in n) toggle_field(n[i], 1) }
	}
}

frappe.ui.form.on("Trip Record", {
	onload: function(frm) { 
		frappe.call({
        	method: "frappe.client.get",
        	args: {
        		doctype: "Fleet Settings"
        	},
        	callback: function (data) {
	        	distance_uom = data.message.distance;
				
        		if(distance_uom == "km"){
	        		unhide_field("departure_odometer_km");
	        		hide_field("departure_odometer_mile");
	        		unhide_field("arrival_odometer_km");
	        		hide_field("arrival_odometer_mile");
	        		unhide_field("distance_km");
	        		hide_field("distance_mile");
        		}

        		if(distance_uom == "mile"){
	        		unhide_field("departure_odometer_mile");
	        		hide_field("departure_odometer_km");
	        		unhide_field("arrival_odometer_mile");
	        		hide_field("arrival_odometer_km");
	        		unhide_field("distance_mile");
	        		hide_field("distance_km");
        		}
        	}
    	})
	}
});

cur_frm.set_query("party_type", function(doc) {
	return {
		"filters": {"name": ["in", ["Customer", "Supplier", "Employee"]]}
	};
});
