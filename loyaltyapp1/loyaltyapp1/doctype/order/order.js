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
// frappe.ui.form.on("Product Details", "product_details_remove", function(frm) {
//
//   var d=locals[cdt][cdn]
  //console.log(d)

  // console.log(amount)

//frm.set_value("cashier",frappe.user.name)

//});
frappe.ui.form.on("Order", "purchase_date", function(frm) {
frm.set_value("purchase_date",frappe.datetime.now_datetime())
//console.log("Hi")



});
frappe.ui.form.on("Payment Method", "generate_otp", function(frm,cdt,cdn) {
//gets the customerid and username from server side
return frappe.call({
  method:"loyaltyapp1.api.otp",
  args:{number:frm.doc.username,

  },
  callback:function(r)
  {
    d=locals[cdt][cdn];
    d.confirm_otp=r.message
    refresh_field("payment_method")
    console.log(r.message)
  },
})

 });
 frappe.ui.form.on("Payment Method", "otp", function(frm,cdt,cdn) {
   //console.log("hi");
     d=locals[cdt][cdn];
     //console.log(d.otp);
     //console.log(d.otp);
 if (d.otp!=d.confirm_otp)
 {
   //console.log("Incorrect OTP")
   frappe.model.set_value(cdt,cdn,"otp","")
frappe.msgprint(__("Please enter correct otp"))
 }
  });
  //  frappe.ui.form.on("Payment Method", "points", function(frm,cdt,cdn) {
  //     d=locals[cdt][cdn];
  //    if (!d.otp)
  //    {
  //      frappe.model.set_value(cdt,cdn,"points","")
  //   frappe.msgprint(__("Please enter otp"))
   //
  //    }
   //
  //  });


// frappe.ui.form.on("Order", "refresh", function(frm) {
// //  console.log("Page loaded")
// cur_frm.add_custom_button(__('Return'), make_return).addClass("btn-primary");
// });
// make_return = function() {
//   frappe.model.open_mapped_doc({
//     method: "loyaltyapp1.order.doctype.order.order.make_return",
//     frm: cur_frm
//   })
// }
