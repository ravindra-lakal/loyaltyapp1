import frappe
import string
import random

@frappe.whitelist()
def otp():
    size=6
    chars=string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))
