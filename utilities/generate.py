"""Generate PBS run scripts to run every recipe."""
import os
import subprocess
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Name of the conda environment in which esmvaltool is installed
env = 'conda/access-med-0.1'
# Mail notifications when a submitted job fails or finishes
mail = False
submit = False
# Name of the NCI account in which the job will be billed
account = 'iq82'  # Select a compute project to be billed
# Name of the directory in which the job outputs files) are saved.
# The outputs will be saved in /home/user/<outputs>
outputs = '/g/data/kj13/admin/ESMValTool/logs'
# Default Levante computing partition used
nci_queue = 'copyq'
# Default amount of memory used
memory = '64GB'
# Default walltime
walltime = '04:00:00'
# Full path to config_file
# If none, ~/.esmvaltool/config-user.yml is used
config_file = '/g/data/kj13/admin/ESMValTool/.esmvaltool/config-user.yml'

# List of recipes that require non-default SLURM options set above
SPECIAL_RECIPES = {
    'recipe_anav13jclim': {
        'partition': '#SBATCH --partition=compute \n',
        'time': '#SBATCH --time=08:00:00 \n',
    },
    'recipe_bock20jgr_fig_6-7': {
        'partition': '#SBATCH --partition=shared \n',
        'time': '#SBATCH --time=48:00:00 \n',
        'memory': '#SBATCH --mem=50G \n',
    },
    'recipe_bock20jgr_fig_8-10': {
        'partition': '#SBATCH --partition=shared \n',
        'time': '#SBATCH --time=48:00:00 \n',
        'memory': '#SBATCH --mem=50G \n',
    },
    'recipe_check_obs': {
        'partition': '#SBATCH --partition=compute \n',
        'memory': '#SBATCH --constraint=512G \n',
    },
    'recipe_climate_change_hotspot': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_collins13ipcc': {
        'partition': '#SBATCH --partition=compute \n',
        'time': '#SBATCH --time=08:00:00 \n',
        'memory': '#SBATCH --constraint=512G \n',
    },
    'recipe_eady_growth_rate': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_ecs': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_ecs_constraints': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_extreme_index': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_eyring06jgr': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_eyring13jgr_12': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_flato13ipcc_figures_938_941_cmip6': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_ipccwg1ar6ch3_atmosphere': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_ipccwg1ar6ch3_fig_3_9': {
        'partition': '#SBATCH --partition=shared \n',
        'time': '#SBATCH --time=15:00:00 \n',
        'memory': '#SBATCH --mem=150G \n',
    },
    'recipe_ipccwg1ar6ch3_fig_3_19': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_ipccwg1ar6ch3_fig_3_42_a': {
        'partition': '#SBATCH --partition=compute \n',
        'time': '#SBATCH --time=08:00:00 \n',
        'memory': '#SBATCH --constraint=512G \n',
    },
    'recipe_ipccwg1ar6ch3_fig_3_42_b': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_ipccwg1ar6ch3_fig_3_43': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_lauer22jclim_fig3-4_zonal': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_lauer22jclim_fig5_lifrac': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_meehl20sciadv': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_mpqb_xch4': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_perfmetrics_CMIP5': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_perfmetrics_CMIP5_4cds': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_perfmetrics_land_CMIP5': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_russell18jgr': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_schlund20esd': {
        'partition': '#SBATCH --partition=compute \n',
        'time': '#SBATCH --time=08:00:00 \n',
        'memory': '#SBATCH --constraint=512G \n',
    },
    'recipe_schlund20jgr_gpp_abs_rcp85': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_schlund20jgr_gpp_change_1pct': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_schlund20jgr_gpp_change_rcp85': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_smpi': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_smpi_4cds': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_tebaldi21esd': {
        'partition': '#SBATCH --partition=compute \n',
        'time': '#SBATCH --time=08:00:00 \n',
    },
    'recipe_wenzel16jclim': {
        'partition': '#SBATCH --partition=compute \n',
    },
    'recipe_wenzel16nat': {
        'partition': '#SBATCH --partition=compute \n',
    },
}

# These recipes either use CMIP3 input data
# (see https://github.com/ESMValGroup/ESMValCore/issues/430)
# and recipes where tasks require the full compute node memory.
ONE_TASK_RECIPES = [
    'recipe_bock20jgr_fig_1-4',
    'recipe_bock20jgr_fig_6-7',
    'recipe_bock20jgr_fig_8-10',
    'recipe_flato13ipcc_figure_96',
    'recipe_flato13ipcc_figures_938_941_cmip3',
    'recipe_ipccwg1ar6ch3_fig_3_9',
    'recipe_ipccwg1ar6ch3_fig_3_42_a',
    'recipe_ipccwg1ar6ch3_fig_3_43',
    'recipe_check_obs',
    'recipe_collins13ipcc',
    'recipe_lauer22jclim_fig3-4_zonal',
    'recipe_lauer22jclim_fig5_lifrac',
    'recipe_smpi',
    'recipe_smpi_4cds',
    'recipe_wenzel14jgr',
    ]

    
# Fill the list with the names of the recipes to be excluded
# This includes recipes containing missing datasets
exclude = ['recipe_schlund20jgr_gpp_abs_rcp85',
           'recipe_schlund20jgr_gpp_change_1pct',
           'recipe_schlund20jgr_gpp_change_rcp85']

def generate_submit():
    """Generate and submit scripts."""
    home = os.path.expanduser('~')
    dir_recipes = Path('/g/data/kj13/admin/ESMValTool/recipes')

    for recipe in Path(dir_recipes).rglob('*.yml'):
        filename = f'launch_{recipe.stem}.pbs'
        if recipe.stem in exclude:
            continue
        with open(f'{filename}', 'w', encoding='utf-8') as file:
            file.write('#!/bin/bash -l \n')
            file.write('#PBS -S /bin/bash\n')
            file.write(f'#PBS -P {account}\n')
            file.write('#PBS -l storage=gdata/kj13+gdata/fs38+gdata/oi10+gdata/rr3+gdata/xp65+gdata/al33\n')
            file.write(f'#PBS -N {recipe.stem}\n')
            file.write('#PBS -W block=true\n')
            file.write('#PBS -W umask=037\n')
            file.write('#PBS -l wd\n')
            file.write(
                f'#PBS -o {outputs}\n'
            )
            file.write(
                f'#PBS -e {outputs}\n'
            )
            if not SPECIAL_RECIPES.get(recipe.stem, None):
                # continue
                file.write(f'#PBS -q {nci_queue}\n')
                file.write(f'#PBS -l walltime={walltime}\n')
                file.write(f'#PBS -l mem={memory}\n')
                file.write('#PBS -l ncpus=1\n')
            #else:
            #    file.write(SPECIAL_RECIPES[recipe.stem]['partition'])
            #    # Time requirements
            #    # Special time requirements
            #    if 'walltime' in SPECIAL_RECIPES[recipe.stem]:
            #        file.write(SPECIAL_RECIPES[recipe.stem]['walltime'])
            #    # Default
            #    else:
            #        file.write(f'#PBS -l walltime={walltime}\n')
            #    # Memory requirements
            #    # Full node memory (compute partition)
            #    if 'compute' in SPECIAL_RECIPES[recipe.stem]['partition']:
            #        mem_req_levante = '#SBATCH --mem=0\n'
            #        file.write(mem_req_levante)
            #        if 'memory' in SPECIAL_RECIPES[recipe.stem]:
            #            file.write(SPECIAL_RECIPES[recipe.stem]['memory'])
            #    # Shared nodes (other partitions)
            #    else:
            #        # Special memory requirements
            #        if 'memory' in SPECIAL_RECIPES[recipe.stem]:
            #            file.write(SPECIAL_RECIPES[recipe.stem]['memory'])
            #        # Default
            #        else:
            #            file.write(f'#SBATCH --mem={memory}\n')
            if mail:
                file.write('#PBS -m e \n')
                file.write('#PBS -M romain.beucher@anu.edu.au \n')
            file.write('\n')
            file.write('module purge \n')
            file.write('module load pbs \n')
            file.write('\n')
            file.write(f'export ESMVAL_USER_CONFIG={config_file}\n')
            file.write('module use /g/data/xp65/public/modules\n')
            file.write(f'module load {env}\n')
            file.write('\n')
            if not config_file:
                file.write(f'esmvaltool run {str(recipe)}')
            else:
                file.write(f'esmvaltool run --config_file '
                           f'{str(config_file)} {str(recipe)}')
            if recipe.stem in ONE_TASK_RECIPES:
                file.write(' --max_parallel_tasks=1')

        if submit:
            subprocess.check_call(['qsub', filename])


def generate_actions():
    """Generate GitHub action scripts."""
    home = os.path.expanduser('~')
    dir_recipes = Path('/g/data/kj13/admin/ESMValTool/recipes')

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("recipe_template.txt")

    for recipe in Path(dir_recipes).rglob('*.yml'):
        filename = f'{recipe.stem}.yml'
        if recipe.stem in exclude:
            continue
        content = template.render(
            recipe=recipe.stem,
        )
        with open(f'./actions/{filename}', 'w', encoding='utf-8') as file:
            file.write(content)


def generate_readme():
    """Generate Readme for GitHub."""
    home = os.path.expanduser('~')
    dir_recipes = Path('/g/data/kj13/admin/ESMValTool/recipes')

    environment = Environment(loader=FileSystemLoader("templates/"))
    template = environment.get_template("readme_template.txt")

    recipes = []
    for recipe in Path(dir_recipes).rglob('*.yml'):
        if recipe.stem in exclude:
            continue
        recipes.append(recipe.stem)
        
    content = template.render(
            recipes=recipes,
    )
    with open('Readme.md', 'w', encoding='utf-8') as file:
        file.write(content)


if __name__ == '__main__':
    generate_submit()
    generate_actions()
    generate_readme()
