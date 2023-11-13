
## Version 1.0.0 - 2023-11 Pre-release

### Included
- Support for ESMValTool/ESMValCore 2.9 via `xp65` module `esmvaltool`:
  - `esmvaltool` / `esmvaltool_29` 
- Automated (nightly) updates of docker images:
  - `esmvaltool_latest`
  - `esmvaltool_development`
  - `esmvaltool_experimental`
- CI/CD Using Github Actions with current recipes' status (Failed / Success)
This only checks that the recipe runs to completion and succeeds.
- **Tier 1** and **Tier 2** observation datasets available via the ACCESS-NRI replicas NCI collection
for model evaluation (ct11).

### Not Included

- **Tier 3** observation datasets.
- Julia is currently not supported.
- ARE (Jupyter and VDI) not supported.

### In development

- Report of ressource requirement per recipe.
- Jupyter notebook support.
- Julia support
- Support of ACCESS-ESM native outputs.