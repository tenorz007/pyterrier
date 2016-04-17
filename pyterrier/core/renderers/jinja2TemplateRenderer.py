from jinja2 import Environment, FileSystemLoader

class Jinja2TemplateRenderer:


    def __init__(self, template_dir):
        """ Create a new template renderer. By default pyterrier is using Jinja2"""

        self._loader = FileSystemLoader(template_dir)
        self._env = Environment(loader = self._loader)


    def get_template(self, name):
        """ Get and return the rendered template """

        template = self._env.get_template(name)
        return template.render()
