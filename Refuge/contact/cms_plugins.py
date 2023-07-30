from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import gettext_lazy as _

from .models import ContactForm
from .forms import ContactFormForm


@plugin_pool.register_plugin
class ContactFormPlugin(CMSPluginBase):
    model = ContactForm
    form = ContactFormForm
    name = _("Contact Form Plugin")
    render_template = "contact_form.html"

    cache = False

    def render(self, context, instance, placeholder):
        context = super().render(context, instance, placeholder)
        return context
