cur_frm.add_fetch("ean", "mrp", "mrp");
cur_frm.add_fetch("cashier", "store", "store_id");
  var amount=0
frappe.ui.form.on("Order", "onload", function(frm) {
//  console.log("Page loaded")

//  console.log(amount)

frm.set_value("cashier",frappe.user.name)

});
//used to set amount based on item prices
frappe.ui.form.on("Product Details","quantity",function(frm,cdt,cdn){
  var d=locals[cdt][cdn];

  d.total=d.mrp*d.quantity
  refresh_field("product_details")
  //amount=amount+d.total
//   //console.log(d.total)
//
//     frm.set_value("amount",amount)
//
});
frappe.ui.form.on("Product Details", "product_details_remove", function(frm) {

  var d=locals[cdt][cdn]
  //console.log(d)

  // console.log(amount)

//frm.set_value("cashier",frappe.user.name)

});
frappe.ui.form.on("Order", "purchase_date", function(frm) {
frm.set_value("purchase_date",frappe.datetime.now_datetime())
//console.log("Hi")



});
