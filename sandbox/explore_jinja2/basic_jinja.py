
"""
>>> from jinja2 import Template
>>> tpl = Template(u'Greetings, {{ name }}! I am from {{ location }}.')
>>> tpl.render(name='Mr. Arda', location='Amsterdam')
'Greetings, Mr. Arda! I am from Amsterdam.'

Template variables could also be passed as a dictionary.
>>> tpl.render({'name': 'Arthur', 'location':'Stockholm'})
'Greetings, Arthur! I am from Stockholm.'

One could use FileSystemLoader, supplying search path.
>>> from os import path
>>> from jinja2 import Environment, FileSystemLoader
>>> env = Environment(loader = FileSystemLoader('{}/tpl/templates'.format(path.dirname(__file__))))
>>> tpl = env.get_template('greetings.html')
>>> tpl.render(name = 'Mr. Basar')
'Greetings, Mr. Basar!'

One could use PackageLoader. You need to supply package name and directory inside the package.
>>> from jinja2 import Environment, PackageLoader
>>> env = Environment(loader = PackageLoader('tpl', 'templates'))
>>> tpl = env.get_template('greetings.html')
>>> tpl.render(name = 'Mr. Basar')
'Greetings, Mr. Basar!'

>>> v = { 'name': 'Arda' }

Template could be included.
>>> tpl = env.get_template('with_include.html')
>>> tpl.render(v)
'Greetings, Arda!'

Using {% raw %}:
>>> tpl = Template('{% raw %}<li>{{ item }}</li>{% endraw %}')
>>> tpl.render(v)
'<li>{{ item }}</li>'
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()
