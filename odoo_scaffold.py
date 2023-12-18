import os
import sys

# Get module name from command line arguments
if len(sys.argv) < 2:
    print("Usage: python create_odoo_module.py <module_name>")
    sys.exit(1)

module_name = sys.argv[1]

# Define the directory structure
directories = [
    f"{module_name}",
    f"{module_name}/controllers",
    f"{module_name}/models",
    f"{module_name}/security",
    f"{module_name}/views",
    f"{module_name}/data",
    f"{module_name}/demo",
]

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create __init__.py files for making the directories as Python packages
init_files = [
    f"{module_name}",
    f"{module_name}/controllers",
    f"{module_name}/models",
]

for init_file in init_files:
    with open(f"{init_file}/__init__.py", 'w') as file:
        file.write('# -*- coding: utf-8 -*-\n')

# Create a basic __manifest__.py file
with open(f"{module_name}/__manifest__.py", 'w') as file:
    file.write(f"""# -*- coding: utf-8 -*-
{{
    'name': '{module_name}',
    'version': '1.0',
    'summary': 'Module Summary',
    'sequence': -100,
    'description': \"\"\"Module Description\"\"\",
    'category': 'Category',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/template.xml',
    ],
    'demo': [
        # 'demo/demo.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}}
""")

print(f"Odoo module '{module_name}' has been scaffolded.")
