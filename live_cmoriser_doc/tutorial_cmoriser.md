## Tutorial of ESMValTool Live-cmoriser for ACCESS-ESM Row Data

### What is live-cmoriser

Live-cmoriser(also known as on-the-fly-cmoriser) in ESMValTool is a tool to autimatically convert raw output of a model to a format which can be load by ESMValTool.

In this case, our live-cmoriser for ACCESS-ESM can read and convert ACCESS-ESM1_5 raw data, so that NCI users can evaluate ACCESS raw data by ESMValTool without any complicate cmorise as a pre-process.

### How to use live-cmoriser on Gadi

#### Pre-requisites

For ACCESS-ESM1_5 raw data, ACCESS users can use data in project `zv30`, or their own output from ACCESS model, just make sure those data been stored in the same directory structure as ACCESS model output.

For ESMValTool, you need to be a member of project `xp65`.

For basic usage of ESMValTool, we already provide a detailed documentation [here](https://access-hive.org.au/model_evaluation/model_evaluation_on_gadi/model_evaluation_on_gadi_esmvaltool/), if you are new to ESMValTool, we strongly suggest you to read the documentation, it will make things easier in the following step.

#### Supported variables list

This is the first version of ACCESS-ESM CMORizer for ESMValCore. Currently, 
  Supported variables: ``pr``, ``ps``, ``psl``, ``rlds``, ``tas``, ``ta``, ``va``,
  ``ua``, ``zg``, ``hus``, ``clt``, ``rsus``, ``rlus``.


#### Load module

We already have ESMValTool version 2.11 with live-cmoriser for ACCESS-ESM data be installed in a module on project `xp65`, to load it, execute the following commands:
```
    module use /g/data/xp65/public/modules
    module load esmvaltool
```


#### Add metadata to `config-user.yml` file

`config-user.yml` usually be in path `~/.esmvaltool`, for people want to use live-cmoriser, the root of ACCESS raw data should be add into `config-user.yml`.
```
    ACCESS: {ACCESS raw data root}
```


#### Add metadata to `config-developer.yml` file

`config-developer.yml` usually be in path `~/.esmvaltool` unless you have your own `config-developer.yml` file and you specify the root in `config-user.yml` file. In version 2.11 the default `config-developer.yml` already have ACCESS metadata, but in case you are using your own old version file, you need to add the following part to `config-developer.yml`.
```
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

This part is telling ESMValTool where to find the raw data and how to name the cmorised dataset file. we will explain those parameters in detail in following part.

#### How to invoke in recipe

There is an example of a dataset entries in recipe:
```
    dataset:
    - {project: ACCESS, mip: Amon, dataset: ACCESS_ESM1_5, sub_dataset: HI-CN-05, 
      exp: history, modeling_realm: atm, special_attr: pa, start_year: 1986, end_year: 1986}
```

`project` and `dataset` are used for ESMValTool to find the cmoriser, so it's mandatory to be `project: ACCESS` and `dataset: ACCESS_ESM1_5`.

`sub_dataset`, `exp`, `modeling_realm` are used to specify the path to ACCESS-ESM raw dataset.

`sub_dataset`, `special_attr` are components in raw dataset file name.

`project`, `dataset`, `mip`, `exp`, `institute`, `sub_dataset`, `special_attr`, `short_name` are components of output dataset file.

we also prepared an example recipe named `access-live-cmoriser-example.yml`, users can read and run the recipe to easily get start.

#### trigger the live-cmoriser

Once you have your datasets been set like above in a recipe and specify variables in above list then run it, ESmValTool will automatically trigger the corresponding live-cmoriser. 