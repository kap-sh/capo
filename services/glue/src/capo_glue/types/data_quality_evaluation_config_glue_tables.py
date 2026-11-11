"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityEvaluationConfigGlueTables``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glue_table_additional_options
    import capo_glue.types.name_string
    import capo_glue.types.pre_processing_query_string


class DataQualityEvaluationConfigGlueTables(TypedDict, closed=True):
    catalog_id: "capo_glue.types.name_string.NameString"
    """<p>A unique identifier for the Glue Data Catalog.</p>"""
    database_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>A database name in the Glue Data Catalog.</p>"""
    table_name_pattern: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>For the <code>CATALOG</code> and <code>DATABASE</code> levels, a glob pattern, such as <code>orders_*</code>, that selects tables. If you don't specify a pattern, every table at the level is in scope. For the <code>TABLE</code> level, the name of the table.</p>"""
    pre_processing_query: NotRequired[
        "capo_glue.types.pre_processing_query_string.PreProcessingQueryString"
    ]
    """<p>SQL Query of SparkSQL format that can be used to pre-process the data for the table in Glue Data Catalog, before running the Data Quality Operation.</p> <p>For the <code>CATALOG</code> and <code>DATABASE</code> levels, use the <code>{{DATABASE_NAME}}</code> and <code>{{TABLE_NAME}}</code> placeholders, which are filled in for each table.</p>"""
    connection_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the connection to the Glue Data Catalog.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.glue_table_additional_options.GlueTableAdditionalOptions"
    ]
    """<p>Options for reading the table. The following keys are supported:</p> <ul> <li> <p> <code>pushDownPredicate</code>: to filter on partitions without having to list and read all the files in your dataset.</p> </li> <li> <p> <code>catalogPartitionPredicate</code>: to use server-side partition pruning using partition indexes in the Glue Data Catalog.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityEvaluationConfigGlueTables) -> dict:
    out: dict = {}
    out["CatalogId"] = value["catalog_id"]
    if "database_name" in value:
        out["DatabaseName"] = value["database_name"]
    if "table_name_pattern" in value:
        out["TableNamePattern"] = value["table_name_pattern"]
    if "pre_processing_query" in value:
        out["PreProcessingQuery"] = value["pre_processing_query"]
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "additional_options" in value:
        import capo_glue.types.glue_table_additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.glue_table_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityEvaluationConfigGlueTables:
    out: DataQualityEvaluationConfigGlueTables = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    else:
        out["catalog_id"] = ""
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    if data.get("TableNamePattern") is not None:
        out["table_name_pattern"] = data["TableNamePattern"]
    if data.get("PreProcessingQuery") is not None:
        out["pre_processing_query"] = data["PreProcessingQuery"]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.glue_table_additional_options

        out["additional_options"] = (
            capo_glue.types.glue_table_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    return out
