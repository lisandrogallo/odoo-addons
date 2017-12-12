# -*- coding: utf-8 -*-

{
    'name': 'Project Task Kanban Direct Link',
    'version': '10.0.1.0.0',
    'category': 'Project',
    'author': u'Lisandro Gallo',
    'license': 'AGPL-3',
    'sequence': 10,
    'summary': 'Projects, Tasks',
    'depends': ['project'],
    'description': """
        Odoo addon for open tasks in kanban view using a direct link when \
        task description is set.
    """,
    'data': [
        'views/project_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
