#!/bin/python
from pathlib import Path

import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

import fiona
from cartopy.io import shapereader
from shapely.geometry import Polygon
from esmvaltool.diag_scripts.shared import run_diagnostic
from esmvaltool.diag_scripts.shared._base import get_plot_filename

def rect_from_bound(xmin, xmax, ymin, ymax):
    """Returns list of (x,y)'s for a rectangle"""
    xs = [xmax, xmin, xmin, xmax, xmax]
    ys = [ymax, ymax, ymin, ymin, ymax]
    return [(x, y) for x, y in zip(xs, ys)]


def get_country_polygon(country):
    """Returns the polygon geometry object for the country specified from
    the natural earth admin shapefile"""
    resolution = '10m'
    category = 'cultural'
    name = 'admin_0_countries'

    shpfilename = shapereader.natural_earth(resolution, category, name)
    f = fiona.open(shpfilename)
    reader = shapereader.Reader(shpfilename)
    records = list(reader.records())

    for record in records:
        if record.attributes["ADMIN"] == "Australia":
            return [record.geometry]


def plot_australia(data, name, cmap):
    """Plot a countoured map over Australia, masking sea""" 
    poly = get_country_polygon("Australia")
    # Make the figure larger
    fig = plt.figure(figsize=(11,8.5))
    
    # Set the axes using the specified map projection
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.add_geometries(poly, crs=ccrs.PlateCarree(), facecolor='none', edgecolor='black')
    
    pad1 = 0.1  #padding, degrees unit
    exts = [poly[0].bounds[0] - pad1, poly[0].bounds[2] + pad1, poly[0].bounds[1] - pad1, poly[0].bounds[3] + pad1];
    exts = [110, 165, -45, -9]
    ax.set_extent(exts, crs=ccrs.PlateCarree())

    min_lon, max_lon, min_lat, max_lat = exts
    pad2 = 1 # padding, degrees unit
    data = data.sel(lat=slice(min_lat - pad2, max_lat + pad2), lon=slice(min_lon - pad2,max_lon + pad2))
    data = data.mean("time")

    # make a mask polygon by polygon's difference operation
    # base polygon is a rectangle, another polygon is simplified switzerland
    msk = Polygon(rect_from_bound(*exts)).difference( poly[0].simplify(0.01) )
    msk_stm  = ccrs.PlateCarree().project_geometry (msk, ccrs.PlateCarree())  # project geometry to the projection used by stamen
    
    # Make a filled contour plot
    cs=ax.contourf(data['lon'], data['lat'], data['tas'],
                transform = ccrs.PlateCarree(),cmap='coolwarm',extend='both')
                                         
    # plot the mask using semi-transparency (alpha=0.65) on the masked-out portion
    ax.add_geometries( msk_stm, ccrs.PlateCarree(), zorder=12, facecolor='white', edgecolor='none', alpha=1.0)
    
    # Add colorbar
    cbar = plt.colorbar(cs,shrink=0.7,orientation='vertical',label='Surface Air Temperature (K)')
    
    # Add title
    plt.title('Australia Temperature')

    return fig


def main(cfg):
    input_data = cfg['input_data'].values()

    for dataset in input_data:
        # Load the data
        input_file = dataset["filename"]
        name = dataset["variable_group"]
        data = xr.open_dataset(input_file)

        cmap = "coolwarm"
        fig = plot_australia(data, name, cmap)

        # Save output
        output_file = Path(input_file).stem.replace('tas', name)
        output_path = get_plot_filename(output_file, cfg)
        fig.savefig(output_path)



if __name__ == '__main__':

    with run_diagnostic() as config:
        main(config)