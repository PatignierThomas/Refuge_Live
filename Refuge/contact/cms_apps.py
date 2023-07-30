from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


@apphook_pool.register  # register the application
class ContactApp(CMSApp):
    app_name = "contact"
    name = "Contact Form Application"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["contact.urls"]
