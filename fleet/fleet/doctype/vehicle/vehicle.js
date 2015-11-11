// see license.txt

var distance_uom = "";
var fuel_item_group = "";

frappe.ui.form.on("Vehicle", {
	onload: function(frm) {
		frappe.call({
        	method: "frappe.client.get",
        	args: {
        		doctype: "Fleet Settings"
        	},
        	callback: function (data) {
	        	distance_uom = data.message.distance;
				fuel_item_group = data.message.fuel_item_group;
        		if(fuel_item_group === ""){
	        		msgprint (__("Set \"Fuel Item Group\" in Fleet Settings"));
        		}
        	}
    	});
    	frm.set_query("default_fuel", function() { 
			return {
				filters: {item_group:fuel_item_group}
			}
		})
	}
});
cur_frm.add_fetch("default_fuel", "stock_uom", "tank_capacity_uom");
