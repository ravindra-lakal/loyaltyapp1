import frappe
import string
import random
from erpnext.setup.doctype.sms_settings.sms_settings import send_sms

@frappe.whitelist()
def otp(number):
    size=6
    chars=string.ascii_uppercase + string.digits + string.ascii_lowercase
    code=''.join(random.choice(chars) for _ in range(size))
    text="Your otp is %s"%code
    a=[]
    a.append(number)
    # send_sms(a,text)
    return code
