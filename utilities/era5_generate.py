"""Generate PBS run scripts to run every recipe."""
import os
import subprocess
from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def generate_pbs_scripts():
    """Generate GitHub action scripts."""
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("launch_recipe_daily_era5_year.pbs")

    for year in range(1990, 2023):
        filename = f'launch_recipe_daily_era5_{year}.pbs'
        content = template.render(year=year)
        with open(f'./ERA5/{filename}', 'w', encoding='utf-8') as file:
            file.write(content)

def generate_recipes():
    """Generate GitHub action scripts."""
    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("recipe_daily_era5_year.yml")

    for year in range(1990, 2023):
        filename = f'recipe_daily_era5_{year}.yml'
        content = template.render(year=year)
        with open(f'./ERA5/{filename}', 'w', encoding='utf-8') as file:
            file.write(content)

def run_pbs():
    for year in range(1990, 2023):
        filename = f'launch_recipe_daily_era5_{year}.pbs'
        subprocess.run(["qsub", year])

if __name__ == '__main__':
    generate_pbs_scripts()
    generate_recipes()
    run_pbs()
