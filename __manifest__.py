{
    'name': "Real Estate",

    'sequence': -101,  
    'application': True,
    'category': 'Estate',    

    'summary': "Real Estate Application",

    'description': "Real Estate Application",

    'author': "Mohammad Zohair",
    'website': "",

    'version': '0.1',

    'depends': ['base'],

    
    'data': [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_menus.xml",

    ],
    
    'demo': [],
}