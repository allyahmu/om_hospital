# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital',
    'version': '12.0.1.0.0',
    'category': 'Extra Tools',
    'summary': 'Module for Hacking Project',
    'sequence': 10,
    'author': 'Hmu',
    'website': 'hospital.com',

    'depends': ['portal', 'sale'],
    'demo': [],

    'data': [

        'views/patient.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',

        'views/appointment.xml',
        'data/sequence1.xml',
        'reports/report.xml',
        'reports/Patient_card.xml',
        'views/doctor.xml',

    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
