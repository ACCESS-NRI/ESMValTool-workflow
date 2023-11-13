#!/bin/python

# This script is used to concatenate monthly ERA5 data stored at 
# NCI. ESMValTool expect one file per year while NCI currently stores
# data into monthly files.


import iris
from iris.util import equalise_attributes

var = "tp"

for year in range(1959, 2023):
    print(f"Doing year {year} for variable {var}")
    cubes = iris.load(f"*_{year}*")
    equalise_attributes(cubes)
    cube = cubes.concatenate()
    iris.save(cube, f"{var}_era5_moda_sfc_{year}_monthly.nc")
