# ESMValTool support for RAW ACCESS outputs

ESMValTool only supports data that have been CMORised, which is crucial for ensuring standardized and high-quality input. CMORisation allows the tool to handle data consistently across different climate models, making it easier to process and enabling accurate comparisons. However, this requirement does come with a significant downside: the necessity to pre-process the data. This pre-processing step can be both time-consuming and computationally intensive, adding an additional overhead for researchers who need to prepare their datasets before they can utilize ESMValTool for their analyses.

A Live (or on-the-fly) CMORiser acts as an intermediary, modifying only the necessary data for comparison so ESMValTool sees it as CMORised. This saves users from having to pre-CMORise their entire dataset. The trade-off is potential additional computation, which might slow down the evaluation process. The key advantage is the reduction in upfront effort, focusing transformations only where needed.

Currently, ESMValTool supports raw data from ACCESS-ESM1.5 and can process the following variables:

| Variable | Long CMIP Name       |
|----------|----------------------|
| `clt`    | Total Cloud Cover    |
| `hus`    | Specific Humidity    |
| `pr`     | Precipitation        |
| `ps`     | Surface Pressure     |
| `psl`    | Sea Level Pressure   |
| `rlds`   | Longwave Downwelling Radiation at Surface |
| `rlus`   | Surface Upwelling Longwave Radiation |
| `rsus`   | Surface Upwelling Shortwave Radiation |
| `ta`     | Air Temperature      |
| `tas`    | Near-Surface Air Temperature |
| `ua`     | Eastward Wind        |
| `va`     | Northward Wind       |
| `zg`     | Geopotential Height  |

## Getting started on Gadi

### Pre-requisites

- `xp65` membership (request access [here](https://my.nci.org.au/mancini/project/xp65))

### Configure

Support of ACCESS-ESM1.5 is enable via the ESMValTool `ACCESS` project. Root path(s) to this project needs to be define in the `rootpaths` section of your `~/.esmvaltool/config-user.yml` file.

 By default, the ESMValTool-workflow deployed on Gadi supports raw data stored in the **ACCESS Model Output Archive (AOGCM)** (project `p73` on gdata).

 You should see a line that looks like this:

 ```yaml
 rootpaths:
   ...
   ...
   ACCESS: /g/data/p73/archive/non-CMIP
```

You might, for example, want to point to data stored in the **CMIP7 collaborative development and evaluation** (project `zv30`). This can be done by appending the path to the above:

 ```yaml
 rootpaths:
   ...
   ...
   ACCESS: [/g/data/p73/archive/non-CMIP, /g/data/zv30/CMIP7_Hackathon_sep2024]
```

The ESMValTool `ACCESS` project assumes the following directory structure under the rootpaths:

`'{dataset}/{sub_dataset}/{exp}/{modeling_realm}/netCDF'`

and the following filename format:

`'{sub_dataset}.{special_attr}-*.nc'`

An example of a valid path will be:

`/g/data/p73/archive/non-CMIP/ACCESS-ESM1-5/HI-CN-05/history/atm/netCDF/HI-CN-05.pe-191412_dai.nc`

Broken down into:

- rootpath: `/g/data/p73/archive/non-CMIP`
- dataset: `ACCESS-ESM1-5`
- sub_dataset: `HI-CN-05`
- exp: `history`
- modeling_realm: `atm`
- special_attr: `pe`

Advanced users can modify the `~/.esmvaltool/config-developer.yml` file to account for other directory structures. We recommend using the default:

```yaml
    ACCESS:
      cmor_strict: false
      input_dir:
        default:
        - '{dataset}/{sub_dataset}/{exp}/{modeling_realm}/netCDF'
      input_file:
        default: '{sub_dataset}.{special_attr}-*.nc'
      output_file: '{project}_{dataset}_{mip}_{exp}_{institute}_{sub_dataset}_{special_attr}_{short_name}'
      cmor_type: 'CMIP6'
      cmor_default_table_prefix: 'CMIP6_'
``` 

## Load the ESMValTool-workflow module

Support for ACCESS-ESM1-5 raw data is only available for the ESMValTool-workflow version 1.2 and above.

You can load the module as follow:

```bash
module use /g/data/xp65/public/modules
module load esmvaltool
```

## Use datasets in a recipe

ACCESS-ESM1-5 raw datasets can now be used directly in a recipe as follow:

```
    dataset:
    - {project: ACCESS, mip: Amon, dataset: ACCESS_ESM1_5, sub_dataset: HI-CN-05, 
      exp: history, modeling_realm: atm, special_attr: pa, start_year: 1986, end_year: 1986}
```

The different **facets** (`project`, `dataset`, `sub_dataset`, `exp`, `modeling_realm`, `special_attr`) need to be defined.

Here is a complete example for the `recipe_quantile_bias.yml`

```yml
# ESMValTool
# recipe_eady_growth_rate.yml
---
documentation:
  title: |
    Annual and seasonal means of the maximum Eady Growth Rate (EGR).

  description: |
    Recipe to compute the annual mean or the seasonal mean of the maximum Eady Growth Rate
    (EGR, Brian J Hoskins and Paul J Valdes. On the existence of storm-tracks.
    Journal of the atmospheric sciences, 47(15):1854–1864, 1990.).
    The output produces netcdf files for each model. In the case of the seasonal means, a plot is
    produced for each specified level showing the EGR values over the North-Atlantic region.


  authors:
    - sanchez-gomez_emilia
    - moreno-chamarro_eduardo

  maintainer:
    - loosveldt-tomas_saskia

  references:
    - morenochamarro2021

  projects:
    - primavera

datasets:s

  - {project: ACCESS, dataset: ACCESS-ESM1-5, mip: Amon, sub_dataset: HI-CN-05, exp: history, modeling_realm: atm, special_attr: pa, start_year: 2001, end_year: 2002}

preprocessors:
  summer:
    extract_season:
      season: 'JJA'
  winter:
    extract_season:
      season: 'DJF'

diagnostics:
  annual_egr:
    variables:
      ta:
      zg:
      ua:
    scripts:
      annual_eady_growth_rate:
        script: primavera/eady_growth_rate/eady_growth_rate.py
        time_statistic: 'annual_mean'


  summer_egr:
    variables:
      ta:
        preprocessor: summer
      zg:
        preprocessor: summer
      ua:
        preprocessor: summer
    scripts:
      summer_eady_growth_rate:
        script: primavera/eady_growth_rate/eady_growth_rate.py
        time_statistic: 'seasonal_mean'

  winter_egr:
    variables:
      ta:
        preprocessor: winter
      zg:
        preprocessor: winter
      ua:
        preprocessor: winter
    scripts:
      winter_eady_growth_rate:
        script: primavera/eady_growth_rate/eady_growth_rate.py
        time_statistic: 'seasonal_mean'
        plot_levels: [70000]
```