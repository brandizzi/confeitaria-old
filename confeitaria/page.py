class Page(object):
    def fill_template(self, template, values=None, js_files=None, css_files=None):
        values = values if values else {}
        js_files = js_files if js_files else []
        css_files = css_files if css_files else []

        values['css_imports'] = self.get_css_imports(css_files)
        values['js_imports'] = self.get_js_imports(js_files)

        compiled_template = self.get_template(template)
