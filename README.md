

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
    module load esmvaltool-workflow
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
