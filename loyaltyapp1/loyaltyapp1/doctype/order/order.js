frappe.ui.form.on("Order", "onload", function(frm) {
  console.log("Page loaded")

frm.set_value("cashier",frappe.user.name)
});
