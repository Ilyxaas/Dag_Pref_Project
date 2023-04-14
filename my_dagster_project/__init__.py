from dagster import Definitions, load_assets_from_modules, define_asset_job
from my_dagster_project import assets

defs = Definitions(assets=load_assets_from_modules([assets]),
                   jobs=[define_asset_job("all_assets", description="task_dagster")])
