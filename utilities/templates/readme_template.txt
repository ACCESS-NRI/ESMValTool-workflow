{# templates/readme_template.txt #}

# ACCESS-NRI MED ESMValTool Workflow

ACCESS-NRI maintenance of ESMValTool for the Australian Community.

![example workflow](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/sync_jasmin.yml/badge.svg)
![example workflow](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/sync_auxdata.yml/badge.svg)

| Name     |      status   |
|----------|:-------------|{% for recipe in recipes %} 
| {{ recipe }} | ![{{ recipe }}](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml/badge.svg) | {% endfor %}
