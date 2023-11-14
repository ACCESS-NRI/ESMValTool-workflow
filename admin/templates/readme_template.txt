{# templates/readme_template.txt #}


# ACCESS-NRI ESMValTool-Workflow

 ACCESS-NRI maintenance of ESMValTool for the Australian Community.

## What is ESMValTool? 

The Earth System Model Evaluation Tool (ESMValTool) is a tool developed for evaluation of Earth System Models in CMIP (Climate Model Intercomparison Projects). It allows for routine comparison of single or multiple models, either against predecessor versions or against observations. ESMValTool is a community-developed climate model diagnostics and evaluation software package, driven both by computational performance and scientific accuracy and reproducibility. It is open to both users and developers, encouraging open exchange of diagnostic source code and evaluation results from the Coupled Model Intercomparison Project CMIP ensemble. 

## What are we releasing? 

ACCESS-NRI is releasing an NCI configuration of ESMValTool under the name **ESMValTool-workflow**.  

ESMValTool-workflow is the ACCESS-NRI software and data infrastructure that enables the ESMValTool evaluation framework on NCI Gadi. It includes the **ESMValTool/ESMValCore Python packages**, the **ESMValTool collection of recipes and diagnostics** and some **observational datasets**. ESMValTool-workflow is configured to use the existing NCI supported CMIP data collections. 

<!--
![example workflow](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/sync_jasmin.yml/badge.svg)
![example workflow](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/sync_auxdata.yml/badge.svg)
-->

# Recipes current status

## Recipes without observation datasets

| Name     |      status   |
|----------|:-------------|{% for recipe in no_obs %} 
| [{{ recipe }}](https://docs.esmvaltool.org/en/latest/recipes/{{ recipe }}.html) | [![{{ recipe }}](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml) |{% endfor %}

## Tier 1 recipes

| Name     |      status   |
|----------|:-------------|{% for recipe in tier1 %} 
| [{{ recipe }}](https://docs.esmvaltool.org/en/latest/recipes/{{ recipe }}.html)  | [![{{ recipe }}](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml) |{% endfor %}

## Tier 2 recipes

| Name     |      status   |
|----------|:-------------|{% for recipe in tier2 %} 
| [{{ recipe }}](https://docs.esmvaltool.org/en/latest/recipes/{{ recipe }}.html)  | [![{{ recipe }}](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml) |{% endfor %}

## Tier 3 recipes

| Name     |      status   |
|----------|:-------------|{% for recipe in tier3 %} 
| [{{ recipe }}](https://docs.esmvaltool.org/en/latest/recipes/{{ recipe }}.html)  | [![{{ recipe }}](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/{{ recipe }}.yml) |{% endfor %}
