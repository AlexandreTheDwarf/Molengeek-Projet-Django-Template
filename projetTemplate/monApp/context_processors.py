def footer_data(request):
    return {
        'footer_email': 'hello@businessperfect.com',
        'footer_phone': '+1-541-754-3010',
        'footer_fax': '+1-541-754-3010',
        'footer_address': {
            'name': 'BusinessPerfect',
            'street': '848 My Street',
            'city_state_zip': 'CA 94544',
        },
        'footer_links': [
            {'name': 'About Us', 'url': 'blog'},
            {'name': 'Portfolio', 'url': 'portfolio'},
            {'name': 'Contact', 'url': 'contact'},
        ],
        'footer_copyright': '© 2017 BusinessPerfect | Made by Milan Savov',
        'footer_made_by_url': 'http://milansavov.com/',
    }