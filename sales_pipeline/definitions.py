import os
from dagster import Definitions
from dagster_duckdb import DuckDBResource

from sales_pipeline.assets import raw, cleaned, marts

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sales.duckdb")

defs = Definitions(
    assets=[*raw.raw_assets, *cleaned.cleaned_assets, *marts.mart_assets],
    resources={
        "duckdb": DuckDBResource(database=DB_PATH),
    },
)
