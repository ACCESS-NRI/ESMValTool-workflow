"""Generate PBS run scripts to run every recipe."""
import os
import subprocess
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def generate_pbs_scripts(variables):
    """Generate GitHub action scripts."""
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("launch_recipe_daily_era5_year.pbs")

    for var in variables:
        for year in range(1990, 2024):
            filename = f'launch_recipe_daily_era5_{var}_{year}.pbs'
            content = template.render(year=year, variable=var)
            with open(f'{filename}', 'w', encoding='utf-8') as file:
                file.write(content)

def generate_recipes(variables):
    """Generate GitHub action scripts."""
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("recipe_daily_era5_year.yml")

    for var in variables:
        for year in range(1990, 2024):
            filename = f'recipe_daily_era5_{var}_{year}.yml'
            content = template.render(year=year, variable=var)
            with open(f'{filename}', 'w', encoding='utf-8') as file:
                file.write(content)

def run_pbs(variables):
    for var in variables:
        for year in range(1990, 2023):
            filename = f'launch_recipe_daily_era5_{var}_{year}.pbs'
            subprocess.run(["qsub", filename])

if __name__ == '__main__':
    var = ["pr"]
    var = ["psl"]
    generate_pbs_scripts(variables=var)
    generate_recipes(variables=var)
    run_pbs(variables=var)
