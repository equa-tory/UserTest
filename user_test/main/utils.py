menus = [{'title': 'News', 'url_name': 'news', 'btn_ico': 'newspaper-outline'},
         {'title': 'Message', 'url_name': 'msg', 'btn_ico': 'mail-outline'},
         {'title': 'Profile', 'url_name': 'profile', 'btn_ico': 'person-outline'},
         {'title': 'Settings', 'url_name': 'settings', 'btn_ico': 'cog-outline'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menus'] = menus
        
        return context