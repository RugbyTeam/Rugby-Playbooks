import yaml
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('Vagrantfile.template')


project_base = ''
with open(project_base + '.rugby.yml', 'r') as config_file:
    vms = yaml.load(config_file)
    with open(project_base + 'Vagrantfile', 'w') as generated_vagrantfile:
        t = template.render(vms = vms)
        generated_vagrantfile.write(t)
