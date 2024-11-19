

# ACCESS-NRI ESMValTool-workflow

[![DOI](https://zenodo.org/badge/642656227.svg)](https://doi.org/10.5281/zenodo.14183930)


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
|----------|:-------------| 
| [recipe_combined_indices](https://docs.esmvaltool.org/en/latest/recipes/recipe_combined_indices.html) | [![recipe_combined_indices](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_combined_indices.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_combined_indices.yml) | 
| [recipe_modes_of_variability](https://docs.esmvaltool.org/en/latest/recipes/recipe_modes_of_variability.html) | [![recipe_modes_of_variability](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_modes_of_variability.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_modes_of_variability.yml) | 
| [recipe_li17natcc](https://docs.esmvaltool.org/en/latest/recipes/recipe_li17natcc.html) | [![recipe_li17natcc](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_li17natcc.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_li17natcc.yml) | 
| [recipe_extreme_index](https://docs.esmvaltool.org/en/latest/recipes/recipe_extreme_index.html) | [![recipe_extreme_index](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_extreme_index.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_extreme_index.yml) | 
| [recipe_multimodel_products](https://docs.esmvaltool.org/en/latest/recipes/recipe_multimodel_products.html) | [![recipe_multimodel_products](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_multimodel_products.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_multimodel_products.yml) | 
| [recipe_seaice_feedback](https://docs.esmvaltool.org/en/latest/recipes/recipe_seaice_feedback.html) | [![recipe_seaice_feedback](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_seaice_feedback.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_seaice_feedback.yml) | 
| [recipe_hyint_extreme_events](https://docs.esmvaltool.org/en/latest/recipes/recipe_hyint_extreme_events.html) | [![recipe_hyint_extreme_events](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_hyint_extreme_events.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_hyint_extreme_events.yml) | 
| [recipe_capacity_factor](https://docs.esmvaltool.org/en/latest/recipes/recipe_capacity_factor.html) | [![recipe_capacity_factor](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_capacity_factor.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_capacity_factor.yml) | 
| [recipe_ocean_scalar_fields](https://docs.esmvaltool.org/en/latest/recipes/recipe_ocean_scalar_fields.html) | [![recipe_ocean_scalar_fields](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_scalar_fields.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_scalar_fields.yml) | 
| [recipe_tebaldi21esd](https://docs.esmvaltool.org/en/latest/recipes/recipe_tebaldi21esd.html) | [![recipe_tebaldi21esd](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_tebaldi21esd.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_tebaldi21esd.yml) | 
| [recipe_psyplot](https://docs.esmvaltool.org/en/latest/recipes/recipe_psyplot.html) | [![recipe_psyplot](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_psyplot.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_psyplot.yml) | 
| [recipe_climate_change_hotspot](https://docs.esmvaltool.org/en/latest/recipes/recipe_climate_change_hotspot.html) | [![recipe_climate_change_hotspot](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climate_change_hotspot.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climate_change_hotspot.yml) | 
| [recipe_ocean_amoc](https://docs.esmvaltool.org/en/latest/recipes/recipe_ocean_amoc.html) | [![recipe_ocean_amoc](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_amoc.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_amoc.yml) | 
| [recipe_russell18jgr](https://docs.esmvaltool.org/en/latest/recipes/recipe_russell18jgr.html) | [![recipe_russell18jgr](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_russell18jgr.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_russell18jgr.yml) | 
| [recipe_diurnal_temperature_index](https://docs.esmvaltool.org/en/latest/recipes/recipe_diurnal_temperature_index.html) | [![recipe_diurnal_temperature_index](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_diurnal_temperature_index.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_diurnal_temperature_index.yml) | 
| [recipe_seaborn](https://docs.esmvaltool.org/en/latest/recipes/recipe_seaborn.html) | [![recipe_seaborn](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_seaborn.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_seaborn.yml) | 
| [recipe_ensclus](https://docs.esmvaltool.org/en/latest/recipes/recipe_ensclus.html) | [![recipe_ensclus](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ensclus.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ensclus.yml) | 
| [recipe_zmnam](https://docs.esmvaltool.org/en/latest/recipes/recipe_zmnam.html) | [![recipe_zmnam](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_zmnam.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_zmnam.yml) | 
| [recipe_cvdp](https://docs.esmvaltool.org/en/latest/recipes/recipe_cvdp.html) | [![recipe_cvdp](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_cvdp.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_cvdp.yml) | 
| [recipe_consecdrydays](https://docs.esmvaltool.org/en/latest/recipes/recipe_consecdrydays.html) | [![recipe_consecdrydays](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_consecdrydays.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_consecdrydays.yml) | 
| [recipe_kcs](https://docs.esmvaltool.org/en/latest/recipes/recipe_kcs.html) | [![recipe_kcs](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_kcs.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_kcs.yml) | 
| [recipe_autoassess_landsurface_permafrost](https://docs.esmvaltool.org/en/latest/recipes/recipe_autoassess_landsurface_permafrost.html) | [![recipe_autoassess_landsurface_permafrost](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_autoassess_landsurface_permafrost.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_autoassess_landsurface_permafrost.yml) | 
| [recipe_carvalhais14nat](https://docs.esmvaltool.org/en/latest/recipes/recipe_carvalhais14nat.html) | [![recipe_carvalhais14nat](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_carvalhais14nat.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_carvalhais14nat.yml) | 
| [recipe_rainfarm](https://docs.esmvaltool.org/en/latest/recipes/recipe_rainfarm.html) | [![recipe_rainfarm](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_rainfarm.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_rainfarm.yml) | 
| [recipe_eady_growth_rate](https://docs.esmvaltool.org/en/latest/recipes/recipe_eady_growth_rate.html) | [![recipe_eady_growth_rate](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_eady_growth_rate.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_eady_growth_rate.yml) | 
| [recipe_toymodel](https://docs.esmvaltool.org/en/latest/recipes/recipe_toymodel.html) | [![recipe_toymodel](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_toymodel.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_toymodel.yml) | 
| [recipe_williams09climdyn_CREM](https://docs.esmvaltool.org/en/latest/recipes/recipe_williams09climdyn_CREM.html) | [![recipe_williams09climdyn_CREM](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_williams09climdyn_CREM.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_williams09climdyn_CREM.yml) | 
| [recipe_heatwaves_coldwaves](https://docs.esmvaltool.org/en/latest/recipes/recipe_heatwaves_coldwaves.html) | [![recipe_heatwaves_coldwaves](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_heatwaves_coldwaves.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_heatwaves_coldwaves.yml) | 
| [recipe_thermodyn_diagtool](https://docs.esmvaltool.org/en/latest/recipes/recipe_thermodyn_diagtool.html) | [![recipe_thermodyn_diagtool](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_thermodyn_diagtool.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_thermodyn_diagtool.yml) | 
| [recipe_ecs](https://docs.esmvaltool.org/en/latest/recipes/recipe_ecs.html) | [![recipe_ecs](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ecs.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ecs.yml) | 
| [recipe_runoff_et](https://docs.esmvaltool.org/en/latest/recipes/recipe_runoff_et.html) | [![recipe_runoff_et](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_runoff_et.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_runoff_et.yml) | 
| [recipe_tcr](https://docs.esmvaltool.org/en/latest/recipes/recipe_tcr.html) | [![recipe_tcr](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_tcr.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_tcr.yml) | 
| [recipe_hyint](https://docs.esmvaltool.org/en/latest/recipes/recipe_hyint.html) | [![recipe_hyint](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_hyint.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_hyint.yml) | 
| [recipe_ocean_ice_extent](https://docs.esmvaltool.org/en/latest/recipes/recipe_ocean_ice_extent.html) | [![recipe_ocean_ice_extent](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_ice_extent.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_ice_extent.yml) | 
| [recipe_ocean_example](https://docs.esmvaltool.org/en/latest/recipes/recipe_ocean_example.html) | [![recipe_ocean_example](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_example.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_example.yml) | 
| [recipe_meehl20sciadv](https://docs.esmvaltool.org/en/latest/recipes/recipe_meehl20sciadv.html) | [![recipe_meehl20sciadv](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_meehl20sciadv.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_meehl20sciadv.yml) | 
| [recipe_deangelis15nat_fig1_fast](https://docs.esmvaltool.org/en/latest/recipes/recipe_deangelis15nat_fig1_fast.html) | [![recipe_deangelis15nat_fig1_fast](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_deangelis15nat_fig1_fast.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_deangelis15nat_fig1_fast.yml) | 
| [recipe_python_for_CI](https://docs.esmvaltool.org/en/latest/recipes/recipe_python_for_CI.html) | [![recipe_python_for_CI](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_python_for_CI.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_python_for_CI.yml) | 
| [recipe_flato13ipcc_figure_942](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figure_942.html) | [![recipe_flato13ipcc_figure_942](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_942.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_942.yml) | 
| [recipe_monitor](https://docs.esmvaltool.org/en/latest/recipes/recipe_monitor.html) | [![recipe_monitor](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_monitor.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_monitor.yml) | 
| [recipe_monitor_with_refs](https://docs.esmvaltool.org/en/latest/recipes/recipe_monitor_with_refs.html) | [![recipe_monitor_with_refs](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_monitor_with_refs.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_monitor_with_refs.yml) | 
| [recipe_preprocessor_derive_test](https://docs.esmvaltool.org/en/latest/recipes/recipe_preprocessor_derive_test.html) | [![recipe_preprocessor_derive_test](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_preprocessor_derive_test.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_preprocessor_derive_test.yml) | 
| [recipe_python](https://docs.esmvaltool.org/en/latest/recipes/recipe_python.html) | [![recipe_python](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_python.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_python.yml) | 
| [recipe_preprocessor_test](https://docs.esmvaltool.org/en/latest/recipes/recipe_preprocessor_test.html) | [![recipe_preprocessor_test](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_preprocessor_test.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_preprocessor_test.yml) | 
| [recipe_my_personal_diagnostic](https://docs.esmvaltool.org/en/latest/recipes/recipe_my_personal_diagnostic.html) | [![recipe_my_personal_diagnostic](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_my_personal_diagnostic.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_my_personal_diagnostic.yml) | 
| [recipe_extract_shape](https://docs.esmvaltool.org/en/latest/recipes/recipe_extract_shape.html) | [![recipe_extract_shape](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_extract_shape.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_extract_shape.yml) | 
| [recipe_julia](https://docs.esmvaltool.org/en/latest/recipes/recipe_julia.html) | [![recipe_julia](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_julia.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_julia.yml) | 
| [recipe_r](https://docs.esmvaltool.org/en/latest/recipes/recipe_r.html) | [![recipe_r](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_r.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_r.yml) | 
| [recipe_ncl](https://docs.esmvaltool.org/en/latest/recipes/recipe_ncl.html) | [![recipe_ncl](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ncl.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ncl.yml) |

## Tier 1 recipes

| Name     |      status   |
|----------|:-------------| 
| [recipe_validation](https://docs.esmvaltool.org/en/latest/recipes/recipe_validation.html)  | [![recipe_validation](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_validation.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_validation.yml) | 
| [recipe_autoassess_landsurface_surfrad](https://docs.esmvaltool.org/en/latest/recipes/recipe_autoassess_landsurface_surfrad.html)  | [![recipe_autoassess_landsurface_surfrad](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_autoassess_landsurface_surfrad.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_autoassess_landsurface_surfrad.yml) | 
| [recipe_ocean_quadmap](https://docs.esmvaltool.org/en/latest/recipes/recipe_ocean_quadmap.html)  | [![recipe_ocean_quadmap](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_quadmap.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_quadmap.yml) | 
| [recipe_radiation_budget](https://docs.esmvaltool.org/en/latest/recipes/recipe_radiation_budget.html)  | [![recipe_radiation_budget](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_radiation_budget.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_radiation_budget.yml) | 
| [recipe_quantilebias](https://docs.esmvaltool.org/en/latest/recipes/recipe_quantilebias.html)  | [![recipe_quantilebias](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_quantilebias.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_quantilebias.yml) | 
| [recipe_clouds_ipcc](https://docs.esmvaltool.org/en/latest/recipes/recipe_clouds_ipcc.html)  | [![recipe_clouds_ipcc](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_clouds_ipcc.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_clouds_ipcc.yml) | 
| [recipe_bock20jgr_fig_8-10](https://docs.esmvaltool.org/en/latest/recipes/recipe_bock20jgr_fig_8-10.html)  | [![recipe_bock20jgr_fig_8-10](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_bock20jgr_fig_8-10.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_bock20jgr_fig_8-10.yml) |

## Tier 2 recipes

| Name     |      status   |
|----------|:-------------| 
| [recipe_seaice](https://docs.esmvaltool.org/en/latest/recipes/recipe_seaice.html)  | [![recipe_seaice](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_seaice.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_seaice.yml) | 
| [recipe_ocean_bgc](https://docs.esmvaltool.org/en/latest/recipes/recipe_ocean_bgc.html)  | [![recipe_ocean_bgc](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_bgc.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_bgc.yml) | 
| [recipe_landcover](https://docs.esmvaltool.org/en/latest/recipes/recipe_landcover.html)  | [![recipe_landcover](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_landcover.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_landcover.yml) | 
| [recipe_sea_surface_salinity](https://docs.esmvaltool.org/en/latest/recipes/recipe_sea_surface_salinity.html)  | [![recipe_sea_surface_salinity](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_sea_surface_salinity.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_sea_surface_salinity.yml) | 
| [recipe_arctic_ocean](https://docs.esmvaltool.org/en/latest/recipes/recipe_arctic_ocean.html)  | [![recipe_arctic_ocean](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_arctic_ocean.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_arctic_ocean.yml) | 
| [recipe_cox18nature](https://docs.esmvaltool.org/en/latest/recipes/recipe_cox18nature.html)  | [![recipe_cox18nature](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_cox18nature.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_cox18nature.yml) | 
| [recipe_wenzel16nat](https://docs.esmvaltool.org/en/latest/recipes/recipe_wenzel16nat.html)  | [![recipe_wenzel16nat](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_wenzel16nat.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_wenzel16nat.yml) | 
| [recipe_collins13ipcc](https://docs.esmvaltool.org/en/latest/recipes/recipe_collins13ipcc.html)  | [![recipe_collins13ipcc](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_collins13ipcc.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_collins13ipcc.yml) | 
| [recipe_albedolandcover](https://docs.esmvaltool.org/en/latest/recipes/recipe_albedolandcover.html)  | [![recipe_albedolandcover](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_albedolandcover.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_albedolandcover.yml) | 
| [recipe_autoassess_landsurface_soilmoisture](https://docs.esmvaltool.org/en/latest/recipes/recipe_autoassess_landsurface_soilmoisture.html)  | [![recipe_autoassess_landsurface_soilmoisture](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_autoassess_landsurface_soilmoisture.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_autoassess_landsurface_soilmoisture.yml) | 
| [recipe_ocean_Landschuetzer2016](https://docs.esmvaltool.org/en/latest/recipes/recipe_ocean_Landschuetzer2016.html)  | [![recipe_ocean_Landschuetzer2016](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_Landschuetzer2016.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_Landschuetzer2016.yml) | 
| [recipe_wenzel14jgr](https://docs.esmvaltool.org/en/latest/recipes/recipe_wenzel14jgr.html)  | [![recipe_wenzel14jgr](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_wenzel14jgr.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_wenzel14jgr.yml) | 
| [recipe_ocean_multimap](https://docs.esmvaltool.org/en/latest/recipes/recipe_ocean_multimap.html)  | [![recipe_ocean_multimap](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_multimap.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ocean_multimap.yml) | 
| [recipe_esacci_oc](https://docs.esmvaltool.org/en/latest/recipes/recipe_esacci_oc.html)  | [![recipe_esacci_oc](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_esacci_oc.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_esacci_oc.yml) | 
| [recipe_esacci_lst](https://docs.esmvaltool.org/en/latest/recipes/recipe_esacci_lst.html)  | [![recipe_esacci_lst](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_esacci_lst.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_esacci_lst.yml) | 
| [recipe_flato13ipcc_figure_98](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figure_98.html)  | [![recipe_flato13ipcc_figure_98](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_98.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_98.yml) | 
| [recipe_flato13ipcc_figure_914](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figure_914.html)  | [![recipe_flato13ipcc_figure_914](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_914.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_914.yml) | 
| [recipe_flato13ipcc_figure_924](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figure_924.html)  | [![recipe_flato13ipcc_figure_924](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_924.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_924.yml) | 
| [recipe_ipccwg1ar6ch3_fig_3_9](https://docs.esmvaltool.org/en/latest/recipes/recipe_ipccwg1ar6ch3_fig_3_9.html)  | [![recipe_ipccwg1ar6ch3_fig_3_9](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_9.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_9.yml) | 
| [recipe_lauer22jclim_fig9-11c_pdf](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig9-11c_pdf.html)  | [![recipe_lauer22jclim_fig9-11c_pdf](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig9-11c_pdf.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig9-11c_pdf.yml) | 
| [recipe_lauer22jclim_fig9-11ab_scatter](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig9-11ab_scatter.html)  | [![recipe_lauer22jclim_fig9-11ab_scatter](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig9-11ab_scatter.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig9-11ab_scatter.yml) |

## Tier 3 recipes

| Name     |      status   |
|----------|:-------------| 
| [recipe_martin18grl](https://docs.esmvaltool.org/en/latest/recipes/recipe_martin18grl.html)  | [![recipe_martin18grl](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_martin18grl.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_martin18grl.yml) | 
| [recipe_seaice_drift](https://docs.esmvaltool.org/en/latest/recipes/recipe_seaice_drift.html)  | [![recipe_seaice_drift](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_seaice_drift.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_seaice_drift.yml) | 
| [recipe_smpi_4cds](https://docs.esmvaltool.org/en/latest/recipes/recipe_smpi_4cds.html)  | [![recipe_smpi_4cds](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_smpi_4cds.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_smpi_4cds.yml) | 
| [recipe_miles_eof](https://docs.esmvaltool.org/en/latest/recipes/recipe_miles_eof.html)  | [![recipe_miles_eof](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_miles_eof.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_miles_eof.yml) | 
| [recipe_ecs_constraints](https://docs.esmvaltool.org/en/latest/recipes/recipe_ecs_constraints.html)  | [![recipe_ecs_constraints](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ecs_constraints.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ecs_constraints.yml) | 
| [recipe_impact](https://docs.esmvaltool.org/en/latest/recipes/recipe_impact.html)  | [![recipe_impact](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_impact.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_impact.yml) | 
| [recipe_shapeselect](https://docs.esmvaltool.org/en/latest/recipes/recipe_shapeselect.html)  | [![recipe_shapeselect](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_shapeselect.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_shapeselect.yml) | 
| [recipe_perfmetrics_CMIP5_4cds](https://docs.esmvaltool.org/en/latest/recipes/recipe_perfmetrics_CMIP5_4cds.html)  | [![recipe_perfmetrics_CMIP5_4cds](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_perfmetrics_CMIP5_4cds.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_perfmetrics_CMIP5_4cds.yml) | 
| [recipe_autoassess_stratosphere](https://docs.esmvaltool.org/en/latest/recipes/recipe_autoassess_stratosphere.html)  | [![recipe_autoassess_stratosphere](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_autoassess_stratosphere.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_autoassess_stratosphere.yml) | 
| [recipe_miles_block](https://docs.esmvaltool.org/en/latest/recipes/recipe_miles_block.html)  | [![recipe_miles_block](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_miles_block.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_miles_block.yml) | 
| [recipe_miles_regimes](https://docs.esmvaltool.org/en/latest/recipes/recipe_miles_regimes.html)  | [![recipe_miles_regimes](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_miles_regimes.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_miles_regimes.yml) | 
| [recipe_climwip_brunner2019_med](https://docs.esmvaltool.org/en/latest/recipes/recipe_climwip_brunner2019_med.html)  | [![recipe_climwip_brunner2019_med](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climwip_brunner2019_med.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climwip_brunner2019_med.yml) | 
| [recipe_perfmetrics_CMIP5](https://docs.esmvaltool.org/en/latest/recipes/recipe_perfmetrics_CMIP5.html)  | [![recipe_perfmetrics_CMIP5](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_perfmetrics_CMIP5.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_perfmetrics_CMIP5.yml) | 
| [recipe_climwip_test_basic](https://docs.esmvaltool.org/en/latest/recipes/recipe_climwip_test_basic.html)  | [![recipe_climwip_test_basic](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climwip_test_basic.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climwip_test_basic.yml) | 
| [recipe_climwip_brunner20esd](https://docs.esmvaltool.org/en/latest/recipes/recipe_climwip_brunner20esd.html)  | [![recipe_climwip_brunner20esd](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climwip_brunner20esd.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climwip_brunner20esd.yml) | 
| [recipe_wenzel16jclim](https://docs.esmvaltool.org/en/latest/recipes/recipe_wenzel16jclim.html)  | [![recipe_wenzel16jclim](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_wenzel16jclim.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_wenzel16jclim.yml) | 
| [recipe_snowalbedo](https://docs.esmvaltool.org/en/latest/recipes/recipe_snowalbedo.html)  | [![recipe_snowalbedo](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_snowalbedo.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_snowalbedo.yml) | 
| [recipe_extreme_events](https://docs.esmvaltool.org/en/latest/recipes/recipe_extreme_events.html)  | [![recipe_extreme_events](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_extreme_events.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_extreme_events.yml) | 
| [recipe_galytska23jgr](https://docs.esmvaltool.org/en/latest/recipes/recipe_galytska23jgr.html)  | [![recipe_galytska23jgr](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_galytska23jgr.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_galytska23jgr.yml) | 
| [recipe_gier2020bg](https://docs.esmvaltool.org/en/latest/recipes/recipe_gier2020bg.html)  | [![recipe_gier2020bg](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_gier2020bg.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_gier2020bg.yml) | 
| [recipe_eyring06jgr](https://docs.esmvaltool.org/en/latest/recipes/recipe_eyring06jgr.html)  | [![recipe_eyring06jgr](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_eyring06jgr.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_eyring06jgr.yml) | 
| [recipe_schlund20esd](https://docs.esmvaltool.org/en/latest/recipes/recipe_schlund20esd.html)  | [![recipe_schlund20esd](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_schlund20esd.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_schlund20esd.yml) | 
| [recipe_deangelis15nat](https://docs.esmvaltool.org/en/latest/recipes/recipe_deangelis15nat.html)  | [![recipe_deangelis15nat](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_deangelis15nat.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_deangelis15nat.yml) | 
| [recipe_spei](https://docs.esmvaltool.org/en/latest/recipes/recipe_spei.html)  | [![recipe_spei](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_spei.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_spei.yml) | 
| [recipe_climwip_test_performance_sigma](https://docs.esmvaltool.org/en/latest/recipes/recipe_climwip_test_performance_sigma.html)  | [![recipe_climwip_test_performance_sigma](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climwip_test_performance_sigma.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_climwip_test_performance_sigma.yml) | 
| [recipe_smpi](https://docs.esmvaltool.org/en/latest/recipes/recipe_smpi.html)  | [![recipe_smpi](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_smpi.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_smpi.yml) | 
| [recipe_ecs_scatter](https://docs.esmvaltool.org/en/latest/recipes/recipe_ecs_scatter.html)  | [![recipe_ecs_scatter](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ecs_scatter.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ecs_scatter.yml) | 
| [recipe_validation_CMIP6](https://docs.esmvaltool.org/en/latest/recipes/recipe_validation_CMIP6.html)  | [![recipe_validation_CMIP6](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_validation_CMIP6.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_validation_CMIP6.yml) | 
| [recipe_cmug_h2o](https://docs.esmvaltool.org/en/latest/recipes/recipe_cmug_h2o.html)  | [![recipe_cmug_h2o](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_cmug_h2o.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_cmug_h2o.yml) | 
| [recipe_perfmetrics_land_CMIP5](https://docs.esmvaltool.org/en/latest/recipes/recipe_perfmetrics_land_CMIP5.html)  | [![recipe_perfmetrics_land_CMIP5](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_perfmetrics_land_CMIP5.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_perfmetrics_land_CMIP5.yml) | 
| [recipe_pv_capacity_factor](https://docs.esmvaltool.org/en/latest/recipes/recipe_pv_capacity_factor.html)  | [![recipe_pv_capacity_factor](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_pv_capacity_factor.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_pv_capacity_factor.yml) | 
| [recipe_anav13jclim](https://docs.esmvaltool.org/en/latest/recipes/recipe_anav13jclim.html)  | [![recipe_anav13jclim](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_anav13jclim.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_anav13jclim.yml) | 
| [recipe_eyring13jgr_12](https://docs.esmvaltool.org/en/latest/recipes/recipe_eyring13jgr_12.html)  | [![recipe_eyring13jgr_12](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_eyring13jgr_12.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_eyring13jgr_12.yml) | 
| [recipe_flato13ipcc_figures_926_927](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figures_926_927.html)  | [![recipe_flato13ipcc_figures_926_927](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figures_926_927.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figures_926_927.yml) | 
| [recipe_flato13ipcc_figures_938_941_cmip6](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figures_938_941_cmip6.html)  | [![recipe_flato13ipcc_figures_938_941_cmip6](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figures_938_941_cmip6.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figures_938_941_cmip6.yml) | 
| [recipe_flato13ipcc_figure_945a](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figure_945a.html)  | [![recipe_flato13ipcc_figure_945a](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_945a.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_945a.yml) | 
| [recipe_flato13ipcc_figures_938_941_cmip3](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figures_938_941_cmip3.html)  | [![recipe_flato13ipcc_figures_938_941_cmip3](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figures_938_941_cmip3.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figures_938_941_cmip3.yml) | 
| [recipe_flato13ipcc_figures_92_95](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figures_92_95.html)  | [![recipe_flato13ipcc_figures_92_95](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figures_92_95.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figures_92_95.yml) | 
| [recipe_weigel21gmd_figures_13_16](https://docs.esmvaltool.org/en/latest/recipes/recipe_weigel21gmd_figures_13_16.html)  | [![recipe_weigel21gmd_figures_13_16](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_weigel21gmd_figures_13_16.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_weigel21gmd_figures_13_16.yml) | 
| [recipe_flato13ipcc_figure_96](https://docs.esmvaltool.org/en/latest/recipes/recipe_flato13ipcc_figure_96.html)  | [![recipe_flato13ipcc_figure_96](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_96.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_flato13ipcc_figure_96.yml) | 
| [recipe_ipccwg1ar6ch3_atmosphere](https://docs.esmvaltool.org/en/latest/recipes/recipe_ipccwg1ar6ch3_atmosphere.html)  | [![recipe_ipccwg1ar6ch3_atmosphere](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_atmosphere.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_atmosphere.yml) | 
| [recipe_ipccwg1ar6ch3_fig_3_42_a](https://docs.esmvaltool.org/en/latest/recipes/recipe_ipccwg1ar6ch3_fig_3_42_a.html)  | [![recipe_ipccwg1ar6ch3_fig_3_42_a](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_42_a.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_42_a.yml) | 
| [recipe_ipccwg1ar6ch3_fig_3_19](https://docs.esmvaltool.org/en/latest/recipes/recipe_ipccwg1ar6ch3_fig_3_19.html)  | [![recipe_ipccwg1ar6ch3_fig_3_19](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_19.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_19.yml) | 
| [recipe_ipccwg1ar6ch3_fig_3_43](https://docs.esmvaltool.org/en/latest/recipes/recipe_ipccwg1ar6ch3_fig_3_43.html)  | [![recipe_ipccwg1ar6ch3_fig_3_43](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_43.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_43.yml) | 
| [recipe_ipccwg1ar6ch3_fig_3_42_b](https://docs.esmvaltool.org/en/latest/recipes/recipe_ipccwg1ar6ch3_fig_3_42_b.html)  | [![recipe_ipccwg1ar6ch3_fig_3_42_b](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_42_b.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_ipccwg1ar6ch3_fig_3_42_b.yml) | 
| [recipe_mpqb_xch4](https://docs.esmvaltool.org/en/latest/recipes/recipe_mpqb_xch4.html)  | [![recipe_mpqb_xch4](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_mpqb_xch4.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_mpqb_xch4.yml) | 
| [recipe_lauer22jclim_fig2_taylor_amip](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig2_taylor_amip.html)  | [![recipe_lauer22jclim_fig2_taylor_amip](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig2_taylor_amip.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig2_taylor_amip.yml) | 
| [recipe_lauer22jclim_fig6_interannual](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig6_interannual.html)  | [![recipe_lauer22jclim_fig6_interannual](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig6_interannual.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig6_interannual.yml) | 
| [recipe_lauer22jclim_fig1_clim](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig1_clim.html)  | [![recipe_lauer22jclim_fig1_clim](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig1_clim.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig1_clim.yml) | 
| [recipe_lauer22jclim_fig2_taylor](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig2_taylor.html)  | [![recipe_lauer22jclim_fig2_taylor](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig2_taylor.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig2_taylor.yml) | 
| [recipe_lauer22jclim_fig5_lifrac](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig5_lifrac.html)  | [![recipe_lauer22jclim_fig5_lifrac](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig5_lifrac.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig5_lifrac.yml) | 
| [recipe_clouds_bias](https://docs.esmvaltool.org/en/latest/recipes/recipe_clouds_bias.html)  | [![recipe_clouds_bias](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_clouds_bias.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_clouds_bias.yml) | 
| [recipe_lauer22jclim_fig3-4_zonal](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig3-4_zonal.html)  | [![recipe_lauer22jclim_fig3-4_zonal](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig3-4_zonal.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig3-4_zonal.yml) | 
| [recipe_lauer22jclim_fig7_seas](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig7_seas.html)  | [![recipe_lauer22jclim_fig7_seas](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig7_seas.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig7_seas.yml) | 
| [recipe_lauer22jclim_fig8_dyn](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig8_dyn.html)  | [![recipe_lauer22jclim_fig8_dyn](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig8_dyn.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig8_dyn.yml) | 
| [recipe_lauer22jclim_fig1_clim_amip](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer22jclim_fig1_clim_amip.html)  | [![recipe_lauer22jclim_fig1_clim_amip](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig1_clim_amip.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer22jclim_fig1_clim_amip.yml) | 
| [recipe_lauer13jclim](https://docs.esmvaltool.org/en/latest/recipes/recipe_lauer13jclim.html)  | [![recipe_lauer13jclim](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer13jclim.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lauer13jclim.yml) | 
| [recipe_daily_era5](https://docs.esmvaltool.org/en/latest/recipes/recipe_daily_era5.html)  | [![recipe_daily_era5](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_daily_era5.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_daily_era5.yml) | 
| [recipe_era5-land](https://docs.esmvaltool.org/en/latest/recipes/recipe_era5-land.html)  | [![recipe_era5-land](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_era5-land.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_era5-land.yml) | 
| [recipe_bock20jgr_fig_6-7](https://docs.esmvaltool.org/en/latest/recipes/recipe_bock20jgr_fig_6-7.html)  | [![recipe_bock20jgr_fig_6-7](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_bock20jgr_fig_6-7.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_bock20jgr_fig_6-7.yml) | 
| [recipe_bock20jgr_fig_1-4](https://docs.esmvaltool.org/en/latest/recipes/recipe_bock20jgr_fig_1-4.html)  | [![recipe_bock20jgr_fig_1-4](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_bock20jgr_fig_1-4.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_bock20jgr_fig_1-4.yml) | 
| [recipe_lisflood](https://docs.esmvaltool.org/en/latest/recipes/recipe_lisflood.html)  | [![recipe_lisflood](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lisflood.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_lisflood.yml) | 
| [recipe_hype](https://docs.esmvaltool.org/en/latest/recipes/recipe_hype.html)  | [![recipe_hype](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_hype.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_hype.yml) | 
| [recipe_marrmot](https://docs.esmvaltool.org/en/latest/recipes/recipe_marrmot.html)  | [![recipe_marrmot](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_marrmot.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_marrmot.yml) | 
| [recipe_wflow](https://docs.esmvaltool.org/en/latest/recipes/recipe_wflow.html)  | [![recipe_wflow](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_wflow.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_wflow.yml) | 
| [recipe_pcrglobwb](https://docs.esmvaltool.org/en/latest/recipes/recipe_pcrglobwb.html)  | [![recipe_pcrglobwb](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_pcrglobwb.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_pcrglobwb.yml) | 
| [recipe_hydro_forcing](https://docs.esmvaltool.org/en/latest/recipes/recipe_hydro_forcing.html)  | [![recipe_hydro_forcing](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_hydro_forcing.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_hydro_forcing.yml) | 
| [recipe_globwat](https://docs.esmvaltool.org/en/latest/recipes/recipe_globwat.html)  | [![recipe_globwat](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_globwat.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_globwat.yml) | 
| [recipe_concatenate_exps](https://docs.esmvaltool.org/en/latest/recipes/recipe_concatenate_exps.html)  | [![recipe_concatenate_exps](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_concatenate_exps.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_concatenate_exps.yml) | 
| [recipe_check_obs](https://docs.esmvaltool.org/en/latest/recipes/recipe_check_obs.html)  | [![recipe_check_obs](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_check_obs.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_check_obs.yml) | 
| [recipe_variable_groups](https://docs.esmvaltool.org/en/latest/recipes/recipe_variable_groups.html)  | [![recipe_variable_groups](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_variable_groups.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_variable_groups.yml) | 
| [recipe_correlation](https://docs.esmvaltool.org/en/latest/recipes/recipe_correlation.html)  | [![recipe_correlation](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_correlation.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_correlation.yml) | 
| [recipe_decadal](https://docs.esmvaltool.org/en/latest/recipes/recipe_decadal.html)  | [![recipe_decadal](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_decadal.yml/badge.svg)](https://github.com/ACCESS-NRI/ESMValTool-workflow/actions/workflows/recipe_decadal.yml) |


## Observation and reanalyses data products available

You can request access to the ACCESS-NRI collection.
Data is stored in /g/data/ct11 on GADI.

We welcome contributions and feedback through the ACCESS-Hive forum. You can also request help through support.

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>long_name</th>
      <th>datasets</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Total Alkalinity</td>
      <td><a target="_blank" href="https://www.glodap.info/index.php/mapped-data-product/">GLODAP</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>talk</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Surface pH</td>
      <td><a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>phos</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Surface Downward Mass Flux of Carbon as CO2 [kgC m-2 s-1]</td>
      <td><a target="_blank" href="https://www.icos-cp.eu/GCP/2018">GCP2018</a>, <a target="_blank" href="https://www.icos-cp.eu/GCP/2020">GCP2020</a>, <a target="_blank" href="https://www.nodc.noaa.gov/archive/arc0105/0160558/3.3/data/0-data/">Landschuetzer2016</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>fgco2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Total Column Ozone</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/ozone/data/">ESACCI-OZONE</a></td>
      <td>toz</td>
    </tr>
    <tr>
      <th>4</th>
      <td>TOA Outgoing Longwave Radiation</td>
      <td><a target="_blank" href="https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA41Selection.jsp">CERES-EBAF</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="https://esgf.nccs.nasa.gov/thredds/fileServer/CREATE-IP/reanalysis/JMA/JRA-25/JRA-25/">JRA-25</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a>, <a target="_blank" href="ftp.cdc.noaa.gov/Projects/20thC_ReanV2/Monthlies/">NOAA-CIRES-20CR</a></td>
      <td>rlut</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Surface Dissolved Inorganic Carbon Concentration</td>
      <td><a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>dissicos</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Surface Upwelling Shortwave Radiation</td>
      <td><a target="_blank" href="">CERES-EBAF</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a></td>
      <td>rsus</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Primary Organic Carbon Production by All Types of Phytoplankton</td>
      <td><a target="_blank" href="http://orca.science.oregonstate.edu/data/1x2/monthly/eppley.r2018.m.chl.m.sst/hdf">Eppley-VGPM-MODIS</a></td>
      <td>intpp</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Grid-Cell Area for Ocean Variables</td>
      <td><a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>areacello</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Air Temperature</td>
      <td><a target="_blank" href="http://disc.sci.gsfc.nasa.gov/AIRS/documentation [Link-jpl](http://airs.jpl.nasa.gov/documents/documents_toc/">AIRS</a>, <a target="_blank" href="https://airs.jpl.nasa.gov">AIRS-2-1</a>, <a target="_blank" href="http://berkeleyearth.org/data/">BerkeleyEarth</a>, <a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a>, <a target="_blank" href="https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.02/cruts.1811131722.v4.02/">CRU</a>, <a target="_blank" href="https://www-users.york.ac.uk/~kdc3/papers/coverage2013/series.html">CowtanWay</a>, <a target="_blank" href="http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles">E-OBS</a>, <a target="_blank" href="https://www.esrl.noaa.gov/psd/data/gridded/data.ghcncams.html">GHCN-CAMS</a>, <a target="_blank" href="https://data.giss.nasa.gov/gistemp/ [data](https://data.giss.nasa.gov/pub/gistemp/gistemp250_GHCNv4.nc.gz">GISTEMP</a>, <a target="_blank" href="https://www.glodap.info/index.php/mapped-data-product/">GLODAP</a>, <a target="_blank" href="http://www.metoffice.gov.uk/hadobs/hadcrut3/data/download.html">HadCRUT3</a>, <a target="_blank" href="https://crudata.uea.ac.uk/cru/data/temperature/">HadCRUT4</a>, <a target="_blank" href="https://crudata.uea.ac.uk/cru/data/temperature">HadCRUT5</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="http://users.met.fu-berlin.de/~ChristopherKadow/">Kadow2020</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html">NCEP-DOE-R2</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/noaa-global-surface-temperature/v5/access/">NOAAGlobalTemp</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a>, <a target="_blank" href="http://psc.apl.washington.edu/nonwp_projects/PHC/Data3.html">PHC</a>, <a target="_blank" href="https://doi.org/10.24381/cds.20d54e34">WFDE5</a>, <a target="_blank" href="https://data.nodc.noaa.gov/woa/WOA18/DATA/">WOA</a></td>
      <td>ta</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Convective Cloud Area Percentage</td>
      <td><a target="_blank" href="doi:10.1029/2009JD012251">CALIOP</a>, <a target="_blank" href="ftp://ftp.climserv.ipsl.polytechnique.fr/">CALIPSO-GOCCP</a></td>
      <td>clc</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Near-Surface Air Temperature</td>
      <td><a target="_blank" href="http://berkeleyearth.org/data/">BerkeleyEarth</a>, <a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a>, <a target="_blank" href="https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.02/cruts.1811131722.v4.02/">CRU</a>, <a target="_blank" href="https://www-users.york.ac.uk/~kdc3/papers/coverage2013/series.html">CowtanWay</a>, <a target="_blank" href="http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles">E-OBS</a>, <a target="_blank" href="https://www.esrl.noaa.gov/psd/data/gridded/data.ghcncams.html">GHCN-CAMS</a>, <a target="_blank" href="https://data.giss.nasa.gov/gistemp/ [data](https://data.giss.nasa.gov/pub/gistemp/gistemp250_GHCNv4.nc.gz">GISTEMP</a>, <a target="_blank" href="http://www.metoffice.gov.uk/hadobs/hadcrut3/data/download.html">HadCRUT3</a>, <a target="_blank" href="https://crudata.uea.ac.uk/cru/data/temperature/">HadCRUT4</a>, <a target="_blank" href="https://crudata.uea.ac.uk/cru/data/temperature">HadCRUT5</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="http://users.met.fu-berlin.de/~ChristopherKadow/">Kadow2020</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/noaa-global-surface-temperature/v5/access/">NOAAGlobalTemp</a>, <a target="_blank" href="https://doi.org/10.24381/cds.20d54e34">WFDE5</a></td>
      <td>tas</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Specific Humidity</td>
      <td><a target="_blank" href="http://disc.sci.gsfc.nasa.gov/AIRS/documentation [Link-jpl](http://airs.jpl.nasa.gov/documents/documents_toc/">AIRS</a>, <a target="_blank" href="https://airs.jpl.nasa.gov">AIRS-2-1</a>, <a target="_blank" href="doi:10.5194/acp-5-2797-2005">HALOE</a>, <a target="_blank" href="https://esgf.nccs.nasa.gov/thredds/fileServer/CREATE-IP/reanalysis/JMA/JRA-25/JRA-25/">JRA-25</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a>, <a target="_blank" href="ftp.cdc.noaa.gov/Projects/20thC_ReanV2/Monthlies/">NOAA-CIRES-20CR</a></td>
      <td>hus</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Daily Maximum Near-Surface Air Temperature</td>
      <td><a target="_blank" href="http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles">E-OBS</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>tasmax</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Percentage of the Grid Cell Occupied by Land (Including Lakes)</td>
      <td><a target="_blank" href="http://berkeleyearth.org/data/">BerkeleyEarth</a></td>
      <td>sftlf</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Total Cloud Cover Percentage</td>
      <td><a target="_blank" href="doi:10.1029/2009JD012251">CALIOP</a>, <a target="_blank" href="doi:10.1029/2009JD012006">CloudSat</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="http://climserv.ipsl.polytechnique.fr/cfmip-obs/">ISCCP</a>, <a target="_blank" href="https://esgf.nccs.nasa.gov/thredds/fileServer/CREATE-IP/reanalysis/JMA/JRA-25/JRA-25/">JRA-25</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a>, <a target="_blank" href="https://ladsweb.modaps.eosdis.nasa.gov/search/order">MODIS</a>, <a target="_blank" href="">MODIS-1-0</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html">NCEP-DOE-R2</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a>, <a target="_blank" href="ftp.cdc.noaa.gov/Projects/20thC_ReanV2/Monthlies/">NOAA-CIRES-20CR</a>, <a target="_blank" href="https://www.ncdc.noaa.gov/cdr/atmospheric/avhrr-cloud-properties-patmos-x">PATMOS-x</a></td>
      <td>clt</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Sea Surface Salinity</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/sea_surface_salinity/data">ESACCI-SEA-SURFACE-SALINITY</a>, <a target="_blank" href="https://data.nodc.noaa.gov/woa/WOA18/DATA/">WOA</a></td>
      <td>sos</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Surface Downwelling Longwave Radiation</td>
      <td><a target="_blank" href="">CERES-EBAF</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a></td>
      <td>rlds</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Mole Fraction of CH4</td>
      <td><a target="_blank" href="http://www.esa-ghg-cci.org/">ESACCI-GHG</a>, <a target="_blank" href="https://zenodo.org/record/7293740">TCOM-CH4</a></td>
      <td>ch4</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Liquid Water Path</td>
      <td><a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="https://ladsweb.modaps.eosdis.nasa.gov/search/order">MODIS</a></td>
      <td>lwp</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Atmosphere CO2</td>
      <td><a target="_blank" href="https://www.esrl.noaa.gov/gmd/ccgg/carbontracker/index.php">CT2019</a>, <a target="_blank" href="http://www.esrl.noaa.gov/gmd/dv/data/index.php">ESRL</a>, <a target="_blank" href="https://scrippsco2.ucsd.edu/data/atmospheric_co2/kum.html">Scripps-CO2-KUM</a></td>
      <td>co2s</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Surface Downwelling Shortwave Radiation</td>
      <td><a target="_blank" href="">CERES-EBAF</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a></td>
      <td>rsds</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Ambient Aerosol Absorption Optical Thickness at 550nm</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/aerosol/data/">ESACCI-AEROSOL</a></td>
      <td>abs550aer</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Northward Near-Surface Wind</td>
      <td><a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a></td>
      <td>vas</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Near-Surface Relative Humidity</td>
      <td><a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>hurs</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Sea Surface Temperature</td>
      <td><a target="_blank" href="DOI: 10.1016/j.rse.2010.11.020">ATSR</a>, <a target="_blank" href="http://www.metoffice.gov.uk/hadobs/hadisst/data/download.html">HadISST</a>, <a target="_blank" href="https://data.nodc.noaa.gov/woa/WOA18/DATA/">WOA</a></td>
      <td>tos</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Sea Water Potential Temperature</td>
      <td><a target="_blank" href="http://psc.apl.washington.edu/nonwp_projects/PHC/Data3.html">PHC</a>, <a target="_blank" href="https://data.nodc.noaa.gov/woa/WOA18/DATA/">WOA</a></td>
      <td>thetao</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Ambient Aerosol Optical Thickness at 550nm</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/aerosol/data/">ESACCI-AEROSOL</a>, <a target="_blank" href="https://ladsweb.modaps.eosdis.nasa.gov/search/order">MODIS</a></td>
      <td>od550aer</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Ambient Aerosol Optical Depth at 870nm</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/aerosol/data/">ESACCI-AEROSOL</a></td>
      <td>od870aer</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Northward Wind</td>
      <td><a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>va</td>
    </tr>
    <tr>
      <th>30</th>
      <td>Sea Water Salinity</td>
      <td><a target="_blank" href="ftp://ftp.climserv.ipsl.polytechnique.fr/">CALIPSO-GOCCP</a>, <a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/land_cover/data/land_cover_maps/">ESACCI-LANDCOVER</a>, <a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/sea_surface_salinity/data">ESACCI-SEA-SURFACE-SALINITY</a>, <a target="_blank" href="http://psc.apl.washington.edu/nonwp_projects/PHC/Data3.html">PHC</a>, <a target="_blank" href="https://data.nodc.noaa.gov/woa/WOA18/DATA/">WOA</a></td>
      <td>so</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Tree Cover Percentage</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/land_cover/data/land_cover_maps/">ESACCI-LANDCOVER</a></td>
      <td>treeFrac</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Ice Water Path</td>
      <td><a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a></td>
      <td>clivi</td>
    </tr>
    <tr>
      <th>33</th>
      <td>Precipitation</td>
      <td><a target="_blank" href="https://crudata.uea.ac.uk/cru/data/hrg/cru_ts_4.02/cruts.1811131722.v4.02/">CRU</a>, <a target="_blank" href="http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles">E-OBS</a>, <a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/ozone/data/">ESACCI-OZONE</a>, <a target="_blank" href="https://www.esrl.noaa.gov/psd/data/gridded/data.ghcngridded.html">GHCN</a>, <a target="_blank" href="https://opendata.dwd.de/climate_environment/GPCC/html/fulldata-monthly_v2018_doi_download.html">GPCC</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.gpcp.html">GPCP-SG</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="https://esgf.nccs.nasa.gov/thredds/fileServer/CREATE-IP/reanalysis/JMA/JRA-25/JRA-25/">JRA-25</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html">NCEP-DOE-R2</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a>, <a target="_blank" href="ftp.cdc.noaa.gov/Projects/20thC_ReanV2/Monthlies/">NOAA-CIRES-20CR</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/precipitation-persiann/access/">PERSIANN-CDR</a>, <a target="_blank" href="https://researchdata.ands.org.au/rainfall-estimates-gridded-v1-2019/1408744">REGEN</a>, <a target="_blank" href="http://www.remss.com/measurements/atmospheric-water-vapor/tpw-1-deg-product">SSMI</a>, <a target="_blank" href="www.globvapour.info">SSMI-MERIS</a>, <a target="_blank" href="http://science.nasa.gov/missions/trmm/">TRMM-L3</a>, <a target="_blank" href="https://doi.org/10.24381/cds.20d54e34">WFDE5</a></td>
      <td>pr</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Surface Downwelling Clear-Sky Longwave Radiation</td>
      <td><a target="_blank" href="">CERES-EBAF</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a></td>
      <td>rldscs</td>
    </tr>
    <tr>
      <th>35</th>
      <td>Surface Downwelling Clear-Sky Shortwave Radiation</td>
      <td><a target="_blank" href="">CERES-EBAF</a></td>
      <td>rsdscs</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Delta CO2 Partial Pressure</td>
      <td><a target="_blank" href="https://www.nodc.noaa.gov/archive/arc0105/0160558/3.3/data/0-data/">Landschuetzer2016</a></td>
      <td>dpco2</td>
    </tr>
    <tr>
      <th>37</th>
      <td>TOA Outgoing Clear-Sky Shortwave Radiation</td>
      <td><a target="_blank" href="https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA41Selection.jsp">CERES-EBAF</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="https://esgf.nccs.nasa.gov/thredds/fileServer/CREATE-IP/reanalysis/JMA/JRA-25/JRA-25/">JRA-25</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>rsutcs</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Sea Level Pressure</td>
      <td><a target="_blank" href="http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles">E-OBS</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>psl</td>
    </tr>
    <tr>
      <th>39</th>
      <td>CALIPSO Percentage Cloud Cover</td>
      <td><a target="_blank" href="ftp://ftp.climserv.ipsl.polytechnique.fr/">CALIPSO-GOCCP</a></td>
      <td>clcalipso</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Surface Aqueous Partial Pressure of CO2</td>
      <td><a target="_blank" href="https://www.nodc.noaa.gov/archive/arc0105/0160558/3.3/data/0-data/">Landschuetzer2016</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0209633/">Landschuetzer2020</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>spco2</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Surface Upwelling Clear-Sky Shortwave Radiation</td>
      <td><a target="_blank" href="">CERES-EBAF</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a></td>
      <td>rsuscs</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Dissolved Inorganic Carbon Concentration</td>
      <td><a target="_blank" href="https://www.glodap.info/index.php/mapped-data-product/">GLODAP</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0221526/">MOBO-DIC_MPIM</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>dissic</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Mole Fraction of N2O</td>
      <td><a target="_blank" href="https://zenodo.org/record/7386001">TCOM-N2O</a></td>
      <td>n2o</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Percentage Cloud Cover</td>
      <td><a target="_blank" href="doi:10.1029/2009JD012251">CALIOP</a>, <a target="_blank" href="ftp://ftp.climserv.ipsl.polytechnique.fr/">CALIPSO-GOCCP</a>, <a target="_blank" href="doi:10.1029/2009JD012006">CloudSat</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="http://climserv.ipsl.polytechnique.fr/cfmip-obs/">ISCCP</a>, <a target="_blank" href="https://esgf.nccs.nasa.gov/thredds/fileServer/CREATE-IP/reanalysis/JMA/JRA-25/JRA-25/">JRA-25</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a>, <a target="_blank" href="https://ladsweb.modaps.eosdis.nasa.gov/search/order">MODIS</a>, <a target="_blank" href="">MODIS-1-0</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html">NCEP-DOE-R2</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a>, <a target="_blank" href="ftp.cdc.noaa.gov/Projects/20thC_ReanV2/Monthlies/">NOAA-CIRES-20CR</a>, <a target="_blank" href="https://www.ncdc.noaa.gov/cdr/atmospheric/avhrr-cloud-properties-patmos-x">PATMOS-x</a></td>
      <td>cl</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Surface Upwelling Longwave Radiation</td>
      <td><a target="_blank" href="">CERES-EBAF</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a></td>
      <td>rlus</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Carbon Mass Flux out of Atmosphere Due to Net Biospheric Production on Land [kgC m-2 s-1]</td>
      <td><a target="_blank" href="https://www.icos-cp.eu/GCP/2018">GCP2018</a>, <a target="_blank" href="https://www.icos-cp.eu/GCP/2020">GCP2020</a></td>
      <td>nbp</td>
    </tr>
    <tr>
      <th>47</th>
      <td>Total Dissolved Inorganic Phosphorus Concentration</td>
      <td><a target="_blank" href="https://data.nodc.noaa.gov/woa/WOA18/DATA/">WOA</a></td>
      <td>po4</td>
    </tr>
    <tr>
      <th>48</th>
      <td>TOA Incident Shortwave Radiation</td>
      <td><a target="_blank" href="">CERES-EBAF</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a></td>
      <td>rsdt</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Omega (=dp/dt)</td>
      <td><a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>wap</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Dissolved Oxygen Concentration</td>
      <td><a target="_blank" href="https://www.esrl.noaa.gov/gmd/ccgg/carbontracker/index.php">CT2019</a>, <a target="_blank" href="http://www.esa-ghg-cci.org/">ESACCI-GHG</a>, <a target="_blank" href="http://www.esrl.noaa.gov/gmd/dv/data/index.php">ESRL</a>, <a target="_blank" href="https://www.icos-cp.eu/GCP/2018">GCP2018</a>, <a target="_blank" href="https://www.icos-cp.eu/GCP/2020">GCP2020</a>, <a target="_blank" href="https://www.nodc.noaa.gov/archive/arc0105/0160558/3.3/data/0-data/">Landschuetzer2016</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0209633/">Landschuetzer2020</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a>, <a target="_blank" href="https://scrippsco2.ucsd.edu/data/atmospheric_co2/kum.html">Scripps-CO2-KUM</a>, <a target="_blank" href="https://data.nodc.noaa.gov/woa/WOA18/DATA/">WOA</a></td>
      <td>o2</td>
    </tr>
    <tr>
      <th>51</th>
      <td>Percentage Crop Cover</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/land_cover/data/land_cover_maps/">ESACCI-LANDCOVER</a></td>
      <td>cropFrac</td>
    </tr>
    <tr>
      <th>52</th>
      <td>Water Vapor Path</td>
      <td><a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="https://esgf.nccs.nasa.gov/thredds/fileServer/CREATE-IP/reanalysis/JMA/JRA-25/JRA-25/">JRA-25</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html">NCEP-DOE-R2</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a>, <a target="_blank" href="ftp.cdc.noaa.gov/Projects/20thC_ReanV2/Monthlies/">NOAA-CIRES-20CR</a>, <a target="_blank" href="http://www.remss.com/measurements/atmospheric-water-vapor/tpw-1-deg-product">SSMI</a>, <a target="_blank" href="www.globvapour.info">SSMI-MERIS</a></td>
      <td>prw</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Geopotential Height</td>
      <td><a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>zg</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Ambient Fine Aerosol Optical Depth at 550nm</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/aerosol/data/">ESACCI-AEROSOL</a></td>
      <td>od550lt1aer</td>
    </tr>
    <tr>
      <th>55</th>
      <td>Eastward Wind</td>
      <td><a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>ua</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Total Dissolved Inorganic Silicon Concentration</td>
      <td><a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a>, <a target="_blank" href="https://www.glodap.info/index.php/mapped-data-product/">GLODAP</a>, <a target="_blank" href="http://www.metoffice.gov.uk/hadobs/hadisst/data/download.html">HadISST</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0221526/">MOBO-DIC_MPIM</a>, <a target="_blank" href="http://osisaf.met.no/p/ice/">OSI-450-nh</a>, <a target="_blank" href="http://osisaf.met.no/p/ice/">OSI-450-sh</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a>, <a target="_blank" href="http://psc.apl.uw.edu/research/projects/arctic-sea-ice-volume-anomaly/data/model_grid">PIOMAS</a>, <a target="_blank" href="https://data.nodc.noaa.gov/woa/WOA18/DATA/">WOA</a></td>
      <td>si</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Mass Concentration of Total Phytoplankton Expressed as Chlorophyll in Sea Water</td>
      <td><a target="_blank" href="ftp://oceancolour.org/occci-v5.0/geographic/netcdf/monthly/chlor_a/">ESACCI-OC</a></td>
      <td>chl</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Natural Grass Area Percentage</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/land_cover/data/land_cover_maps/">ESACCI-LANDCOVER</a></td>
      <td>grassFrac</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Daily Minimum Near-Surface Air Temperature</td>
      <td><a target="_blank" href="http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles">E-OBS</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>tasmin</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Condensed Water Path</td>
      <td><a target="_blank" href="https://ladsweb.modaps.eosdis.nasa.gov/search/order">MODIS</a>, <a target="_blank" href="ftp.cdc.noaa.gov/Projects/20thC_ReanV2/Monthlies/">NOAA-CIRES-20CR</a></td>
      <td>clwvi</td>
    </tr>
    <tr>
      <th>61</th>
      <td>TOA Outgoing Clear-Sky Longwave Radiation</td>
      <td><a target="_blank" href="https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA41Selection.jsp">CERES-EBAF</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="https://esgf.nccs.nasa.gov/thredds/fileServer/CREATE-IP/reanalysis/JMA/JRA-25/JRA-25/">JRA-25</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>rlutcs</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Bare Soil Percentage Area Coverage</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/land_cover/data/land_cover_maps/">ESACCI-LANDCOVER</a></td>
      <td>baresoilFrac</td>
    </tr>
    <tr>
      <th>63</th>
      <td>pH</td>
      <td><a target="_blank" href="https://www.glodap.info/index.php/mapped-data-product/">GLODAP</a>, <a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>ph</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Surface Carbonate Ion Concentration</td>
      <td><a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>co3os</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Surface Air Pressure</td>
      <td><a target="_blank" href="ftp://ftp.climserv.ipsl.polytechnique.fr/">CALIPSO-GOCCP</a>, <a target="_blank" href="http://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles">E-OBS</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>ps</td>
    </tr>
    <tr>
      <th>66</th>
      <td>Relative Humidity</td>
      <td><a target="_blank" href="http://disc.sci.gsfc.nasa.gov/AIRS/documentation">AIRS-2-0</a>, <a target="_blank" href="https://airs.jpl.nasa.gov">AIRS-2-1</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis2.html">NCEP-DOE-R2</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>hur</td>
    </tr>
    <tr>
      <th>67</th>
      <td>Surface Temperature</td>
      <td><a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a>, <a target="_blank" href="On CEDA-JASMIN">ESACCI-LST</a>, <a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/sst/data/">ESACCI-SST</a>, <a target="_blank" href="http://www.metoffice.gov.uk/hadobs/hadisst/data/download.html">HadISST</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>ts</td>
    </tr>
    <tr>
      <th>68</th>
      <td>Eastward Near-Surface Wind</td>
      <td><a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a></td>
      <td>uas</td>
    </tr>
    <tr>
      <th>69</th>
      <td>TOA Outgoing Shortwave Radiation</td>
      <td><a target="_blank" href="https://ceres-tool.larc.nasa.gov/ord-tool/jsp/EBAFTOA41Selection.jsp">CERES-EBAF</a>, <a target="_blank" href="https://public.satproj.klima.dwd.de/data/ESA_Cloud_CCI/CLD_PRODUCTS/v3.0/">ESACCI-CLOUD</a>, <a target="_blank" href="https://isccp.giss.nasa.gov/pub/flux-fh/tar-nc4_MPF/">ISCCP-FH</a>, <a target="_blank" href="https://esgf.nccs.nasa.gov/thredds/fileServer/CREATE-IP/reanalysis/JMA/JRA-25/JRA-25/">JRA-25</a>, <a target="_blank" href="http://www.jma.go.jp/jma/indexe.html">JRA-55</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a>, <a target="_blank" href="ftp.cdc.noaa.gov/Projects/20thC_ReanV2/Monthlies/">NOAA-CIRES-20CR</a></td>
      <td>rsut</td>
    </tr>
    <tr>
      <th>70</th>
      <td>Daily-Mean Near-Surface Wind Speed</td>
      <td><a target="_blank" href="http://cfs.ncep.noaa.gov">CFSR</a>, <a target="_blank" href="https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html">NCEP-NCAR-R1</a></td>
      <td>sfcWind</td>
    </tr>
    <tr>
      <th>71</th>
      <td>Surface Total Alkalinity</td>
      <td><a target="_blank" href="https://www.ncei.noaa.gov/data/oceans/ncei/ocads/data/0220059/">OceanSODA-ETHZ</a></td>
      <td>talkos</td>
    </tr>
    <tr>
      <th>72</th>
      <td>Percentage Cover by Shrub</td>
      <td><a target="_blank" href="ftp://anon-ftp.ceda.ac.uk/neodc/esacci/land_cover/data/land_cover_maps/">ESACCI-LANDCOVER</a></td>
      <td>shrubFrac</td>
    </tr>
  </tbody>
</table>
