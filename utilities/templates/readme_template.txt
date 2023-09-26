{# templates/readme_template.txt #}

# ACCESS-NRI MED ESMValTool Workflow

ACCESS-NRI maintenance of ESMValTool for the Australian Community.

![example workflow](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/sync_jasmin.yml/badge.svg)
![example workflow](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/sync_auxdata.yml/badge.svg)

## Recipe without observation datasets

| Name     |      status   |
|----------|:-------------|{% for recipe in no_obs %} 
| [{{ recipe }}](http://130.56.247.78/esmvaltool/{{ recipe }}/index.html) | [![{{ recipe }}](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml) |{% endfor %}

## Tier 1 recipes

| Name     |      status   |
|----------|:-------------|{% for recipe in tier1 %} 
| [{{ recipe }}](http://130.56.247.78/esmvaltool/{{ recipe }}/index.html) | [![{{ recipe }}](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml) |{% endfor %}

## Tier 2 recipes

| Name     |      status   |
|----------|:-------------|{% for recipe in tier2 %} 
| [{{ recipe }}](http://130.56.247.78/esmvaltool/{{ recipe }}/index.html) | [![{{ recipe }}](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml) |{% endfor %}

## Tier 3 recipes

| Name     |      status   |
|----------|:-------------|{% for recipe in tier3 %} 
| [{{ recipe }}](http://130.56.247.78/esmvaltool/{{ recipe }}/index.html) | [![{{ recipe }}](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml) |{% endfor %}
