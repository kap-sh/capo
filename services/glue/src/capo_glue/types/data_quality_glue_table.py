"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityGlueTable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.glue_table_additional_options
    import capo_glue.types.name_string
    import capo_glue.types.pre_processing_query_string


class DataQualityGlueTable(TypedDict, closed=True):
    database_name: "capo_glue.types.name_string.NameString"
    """<p>A database name in the Glue Data Catalog.</p>"""
    table_name: "capo_glue.types.name_string.NameString"
    """<p>A table name in the Glue Data Catalog.</p>"""
    catalog_id: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>A unique identifier for the Glue Data Catalog.</p>"""
    connection_name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The name of the connection to the Glue Data Catalog.</p>"""
    additional_options: NotRequired[
        "capo_glue.types.glue_table_additional_options.GlueTableAdditionalOptions"
    ]
    """<p>Additional options for the table. Currently there are two keys supported:</p> <ul> <li> <p> <code>pushDownPredicate</code>: to filter on partitions without having to list and read all the files in your dataset.</p> </li> <li> <p> <code>catalogPartitionPredicate</code>: to use server-side partition pruning using partition indexes in the Glue Data Catalog.</p> </li> </ul>"""
    pre_processing_query: NotRequired[
        "capo_glue.types.pre_processing_query_string.PreProcessingQueryString"
    ]
    """<p>SQL Query of SparkSQL format that can be used to pre-process the data for the table in Glue Data Catalog, before running the Data Quality Operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityGlueTable) -> dict:
    out: dict = {}
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    if "connection_name" in value:
        out["ConnectionName"] = value["connection_name"]
    if "additional_options" in value:
        import capo_glue.types.glue_table_additional_options

        out["AdditionalOptions"] = (
            capo_glue.types.glue_table_additional_options.serialize_aws_json_1_1(
                value["additional_options"]
            )
        )
    if "pre_processing_query" in value:
        out["PreProcessingQuery"] = value["pre_processing_query"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityGlueTable:
    out: DataQualityGlueTable = {}  # type: ignore[typeddict-item]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("TableName") is not None:
        out["table_name"] = data["TableName"]
    else:
        out["table_name"] = ""
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("ConnectionName") is not None:
        out["connection_name"] = data["ConnectionName"]
    if data.get("AdditionalOptions") is not None:
        import capo_glue.types.glue_table_additional_options

        out["additional_options"] = (
            capo_glue.types.glue_table_additional_options.deserialize_aws_json_1_1(
                data["AdditionalOptions"]
            )
        )
    if data.get("PreProcessingQuery") is not None:
        out["pre_processing_query"] = data["PreProcessingQuery"]
    return out
