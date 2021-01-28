import json
from odoo import http
from odoo.http import request
from odoo import models, fields, api, _


class WebinarBooking(http.Controller):

    @http.route('/page/webinar', csrf=False, type="http", methods=['POST', 'GET'], auth="public", website=True)
    def webinar_details(self, **kwargs):
        print('webinar_details',kwargs)
        name=kwargs.get('name')
        email=kwargs.get('email')
        if kwargs.get('email')!='':email= kwargs.get('email')
        else:email=0
        if kwargs.get('phone')!='':phone= kwargs.get('phone')
        else:phone=True
        if len(kwargs)>0:
            partner_obj_email=request.env['res.partner'].search([('email','=',email)])
            partner_obj_mobile=request.env['res.partner'].search([('phone','=',phone)])
            lead_obj_email=request.env['crm.lead'].search([('email_from','=',email)])
            lead_obj_phone=request.env['crm.lead'].search([('mobile','=',phone)])
            print(partner_obj_email,partner_obj_mobile,lead_obj_email,lead_obj_phone)
            if partner_obj_email:
                partner_obj_email.sudo().write({'name':name,'phone':phone})
            elif partner_obj_mobile:
                partner_obj_email.sudo().write({'name': name, 'email': email})
            elif lead_obj_email:
                lead_obj_email.sudo().write({'name':name,'phone':phone})
            elif lead_obj_phone:
                lead_obj_email.sudo().write({'name': name, 'email_to': email})
            else:request.env['res.partner'].sudo().create({'name':name,'email':email,'phone':phone,'company_type':'person'})
        return request.render('task_webinar.webinar_page_template')


