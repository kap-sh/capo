"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigListGlueTables``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string


class DataQualityEvaluationConfigListGlueTables(TypedDict, closed=True):
    catalog_id: "capo_glue.types.name_string.NameString"
    """<p>A unique identifier for the Glue Data Catalog.</p>"""
    database_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>A database name in the Glue Data Catalog.</p>"""
    table_name_pattern: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>For the <code>CATALOG</code> and <code>DATABASE</code> levels, a glob pattern, such as <code>orders_*</code>, that selects tables. If you don't specify a pattern, every table at the level is in scope. For the <code>TABLE</code> level, the name of the table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationConfigListGlueTables) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name_pattern" in value:
        out["TableNamePattern"] = value["table_name_pattern"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityEvaluationConfigListGlueTables:
    out: DataQualityEvaluationConfigListGlueTables = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        out["catalog_id"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("TableNamePattern") is not None:
        out["table_name_pattern"] = data["TableNamePattern"]
    return out
