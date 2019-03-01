from jinja2 import Environment, PackageLoader

env = Environment(
    loader=PackageLoader('spark', 'templates')
)

template = env.get_template('mytemplate.html')

model = {
    'title': 'Welcome'
}

print(template.render(vars=model))
