{
    "name": "Library Management",
    "version": "1.0",
    "summary": "Manage books in library",
    "license": "LGPL-3",
    'sequence':'2',
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/book_views.xml",
    ],
    "installable": True,
    "auto_install": False,
    "application": True,
}