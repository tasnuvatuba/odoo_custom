# odoo_custom
Custom Module Development on Odoo 16

## Prerequisites
Ensure that the following are installed:
- **Python** (3.8 or higher)
- **PostgreSQL** (configured for Odoo)
- **Odoo 16** (since these modules are designed for Odoo 16)

## File Structure
The recommended file structure for setting up these custom modules is as follows:
```plaintext
odoo_16_dev/
├── conf/
│   └── odoo.conf          # Odoo configuration file with paths and settings
├── custom/                # Directory for custom Odoo modules
│   ├── hr_templates/      
│   ├── real_estate_ads/   
│   └── training_management/ 
├── odoo_16/               # Odoo 16 source code directory
└── venv/                  # Python virtual environment for Odoo dependencies
```


## odoo.conf Template
[options]

addons_path = /home/dsi/odoo-dev/odoo-dev-16/odoo-16.0/addons, /home/dsi/odoo-dev/odoo-dev-16/custom

db_user = <your-db-username>

db_password = <your-db-password>

db_host = <your-db-host>

db_port = <your-db-port>

default_productivity_apps = True

http_port = <port number>

