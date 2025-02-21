from django.utils.translation import gettext_lazy

from pretix_worldlinedirect import __compatibility__, __version__

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")


class PluginApp(PluginConfig):
    default = True
    name = "pretix_payonedirect"
    verbose_name = "PayOne Direct"

    class PretixPluginMeta:
        name = gettext_lazy("PayOne Direct")
        author = "pretix team"
        description = gettext_lazy("Accept payments through PayOne Direct")
        visible = True
        version = __version__
        category = "PAYMENT"
        picture = "pretix_payonedirect/logo.svg"
        compatibility = __compatibility__

    def ready(self):
        from . import signals  # NOQA
