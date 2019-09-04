import re
from copy import deepcopy
from builder.template import render_template
from plugin import Plugin, PluginHandler


class ChePlugin(Plugin):
    """
    A simple che image gallery plugin
    Usage: Place {{GALLERY}} shortcode in your [page] file, i.e. in your page's markdown code
    """
    def install(self):
        PluginHandler.install_template_path('plugins/che_gallery')

    def __init__(self):
        super().__init__()
        self.find_rule = re.compile('{{GALLERY}}')

    def before_load(self, raw_content):
        return deepcopy(raw_content)

    def after_load(self, loaded_contents):
        """
        Replace all occurrences of the shortcode {{GALLERY}} with a simple html image gallery
        """
        modified_contents = deepcopy(loaded_contents)

        # Render page
        html_in = render_template('che_gallery_template.html')

        if 'page' in loaded_contents:
            matches = self.find_rule.findall(loaded_contents['page']['loaded'])
            if len(matches):
                modified_contents['page']['loaded'] = re.sub(self.find_rule, html_in, modified_contents['page']['loaded'])
        return modified_contents
