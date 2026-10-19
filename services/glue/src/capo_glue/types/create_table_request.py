"""Generated from Smithy shape ``com.amazonaws.glue#CreateTableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.catalog_id_string
    import capo_glue.types.name_string
    import capo_glue.types.open_table_format_input
    import capo_glue.types.partition_index_list
    import capo_glue.types.table_input
    import capo_glue.types.transaction_id_string


class CreateTableRequest(TypedDict, closed=True):
    catalog_id: NotRequired["capo_glue.types.catalog_id_string.CatalogIdString"]
    """<p>The ID of the Data Catalog in which to create the <code>Table</code>. If none is supplied, the Amazon Web Services account ID is used by default.</p>"""
    database_name: "capo_glue.types.name_string.NameString"
    """<p>The catalog database in which to create the new table. For Hive compatibility, this name is entirely lowercase.</p>"""
    name: NotRequired["capo_glue.types.name_string.NameString"]
    """<p>The unique identifier for the table within the specified database that will be created in the Glue Data Catalog.</p>"""
    table_input: NotRequired["capo_glue.types.table_input.TableInput"]
    """<p>The <code>TableInput</code> object that defines the metadata table to create in the catalog.</p>"""
    partition_indexes: NotRequired[
        "capo_glue.types.partition_index_list.PartitionIndexList"
    ]
    """<p>A list of partition indexes, <code>PartitionIndex</code> structures, to create in the table.</p>"""
    transaction_id: NotRequired[
        "capo_glue.types.transaction_id_string.TransactionIdString"
    ]
    """<p>The ID of the transaction.</p>"""
    open_table_format_input: NotRequired[
        "capo_glue.types.open_table_format_input.OpenTableFormatInput"
    ]
    """<p>Specifies an <code>OpenTableFormatInput</code> structure when creating an open format table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTableRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["DatabaseName"] = value["database_name"]
    if "name" in value:
        out["Name"] = value["name"]
    if "table_input" in value:
        import capo_glue.types.table_input

        out["TableInput"] = capo_glue.types.table_input.serialize_aws_json_1_1(
            value["table_input"]
        )
    if "partition_indexes" in value:
        import capo_glue.types.partition_index_list

        out["PartitionIndexes"] = (
            capo_glue.types.partition_index_list.serialize_aws_json_1_1(
                value["partition_indexes"]
            )
        )
    if "transaction_id" in value:
        out["TransactionId"] = value["transaction_id"]
    if "open_table_format_input" in value:
        import capo_glue.types.open_table_format_input

        out["OpenTableFormatInput"] = (
            capo_glue.types.open_table_format_input.serialize_aws_json_1_1(
                value["open_table_format_input"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTableRequest:
    out: CreateTableRequest = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("DatabaseName") is not None:
        out["database_name"] = data["DatabaseName"]
    else:
        out["database_name"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("TableInput") is not None:
        import capo_glue.types.table_input

        out["table_input"] = capo_glue.types.table_input.deserialize_aws_json_1_1(
            data["TableInput"]
        )
    if data.get("PartitionIndexes") is not None:
        import capo_glue.types.partition_index_list

        out["partition_indexes"] = (
            capo_glue.types.partition_index_list.deserialize_aws_json_1_1(
                data["PartitionIndexes"]
            )
        )
    if data.get("TransactionId") is not None:
        out["transaction_id"] = data["TransactionId"]
    if data.get("OpenTableFormatInput") is not None:
        import capo_glue.types.open_table_format_input

        out["open_table_format_input"] = (
            capo_glue.types.open_table_format_input.deserialize_aws_json_1_1(
                data["OpenTableFormatInput"]
            )
        )
    return out
