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

## Using ESMValTool on Gadi

<i>ESMValTool</i> is provided through the `xp65` project on Gadi.

### Pre-requisites

To enable the  <i>ESMValTool-workflow</i>, you need to be a member of the `xp65` NCI projects:

Depending on your needs, you may want to also joined the following supported data collections:

- CMIP6: `fs38`, `oi10`
- CMIP5: `rr3`, `al33`
- ERA5 and ERA5-Land: `rt52`, `zz93`
- obs4MIPs: `qv56`

### Loading the ESMValTool-workflow modules
 <!-- #### Load the `access-med` conda environment -->

To load the the `esmvaltool` module, execute the following commands:
```
    module use /g/data/xp65/public/modules
    module load esmvaltool
```

ESMValTool is pre-configured to access CMIP and observation datasets available on Gadi.
By default, ESMValTool looks for the `config_user.yml` file in the home directory, inside the `.esmvaltool` folder.
You can get a copy by running:

```
esmvaltool config get_config_user --path=dest
```

To list which <i>ESMValTool</i> recipes are available on <i>Gadi</i>, run:
```
esmvaltool recipes list
```

To find out details of a specific `recipe_name.yml`, execute:
```
esmvaltool recipes show recipe_name.yml
```

To retrieve a recipe (and modify it), execute:
```
esmvaltool recipes get recipe_name.yml
```

To execute `recipe_name.yml` and automatically download the required climate data to the default directory, run:

```
esmvaltool run examples/recipe_python.yml --search_esgf=when_missing
```
The `--search_esgf=when_missing` option tells <i>ESMValTool</i> to search for and download the necessary climate data files from Earth System Grid Federation (ESGF), if they cannot be found locally.

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
