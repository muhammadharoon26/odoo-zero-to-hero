from odoo import models, fields

class Book(models.Model):
    _name='library.book'
    _description = 'Library Book'
    
    name= fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    publication_date = fields.Date(string='Publication Date')
    isbn = fields.Char(string='ISBN')