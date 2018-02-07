{
  'name':'CA theme',
  'description': 'LESS to adapt Loftspace Theme and Beauty Theme applying CA Corporate style',
  'version':'1.1',
  'author':'Esteban Tapia',

  'data': [
  'views/assets.xml',
  'views/theme_loftspace_sale.products_categories.xml'
  ],

  'css': ['static/src/css/css.css'],
  'less': ['static/src/less/less.less'],

  'category': 'Generic Modules/Others',
  'depends': ['website','theme_loftspace','theme_beauty'],

  'installable': True,
  'application': False,
  'auto_install': False,
  'qweb': [],
}
