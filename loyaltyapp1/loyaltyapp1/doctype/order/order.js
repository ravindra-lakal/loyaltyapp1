cur_frm.add_fetch("ean", "mrp", "mrp");
var amount=0
frappe.ui.form.on("Order", "onload", function(frm) {
  console.log("Page loaded")

frm.set_value("cashier",frappe.user.name)
});

frappe.ui.form.on("Product Details","quantity",function(frm,cdt,cdn){
  console.log("Hello")
  var d=locals[cdt][cdn];
  
  d.total=d.mrp*d.quantity
  refresh_field("product_details")
  amount=amount+d.total
    console.log(amount)
    frm.set_value("amount",amount)

});
