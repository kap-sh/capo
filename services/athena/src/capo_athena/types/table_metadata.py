"""Generated from Smithy shape ``com.amazonaws.athena#TableMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.column_list
    import capo_athena.types.name_string
    import capo_athena.types.parameters_map
    import capo_athena.types.table_type_string
    import capo_athena.types.timestamp


class TableMetadata(TypedDict, closed=True):
    name: "capo_athena.types.name_string.NameString"
    """<p>The name of the table.</p>"""
    create_time: NotRequired["capo_athena.types.timestamp.Timestamp"]
    """<p>The time that the table was created.</p>"""
    last_access_time: NotRequired["capo_athena.types.timestamp.Timestamp"]
    """<p>The last time the table was accessed.</p>"""
    table_type: NotRequired["capo_athena.types.table_type_string.TableTypeString"]
    """<p>The type of table. In Athena, only <code>EXTERNAL_TABLE</code> is supported.</p>"""
    columns: NotRequired["capo_athena.types.column_list.ColumnList"]
    """<p>A list of the columns in the table.</p>"""
    partition_keys: NotRequired["capo_athena.types.column_list.ColumnList"]
    """<p>A list of the partition keys in the table.</p>"""
    parameters: NotRequired["capo_athena.types.parameters_map.ParametersMap"]
    """<p>A set of custom key/value pairs for table properties.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableMetadata) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "create_time" in value:
        import capo_athena.types.timestamp

        out["CreateTime"] = capo_athena.types.timestamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "last_access_time" in value:
        import capo_athena.types.timestamp

        out["LastAccessTime"] = capo_athena.types.timestamp.serialize_aws_json_1_1(
            value["last_access_time"]
        )
    if "table_type" in value:
        out["TableType"] = value["table_type"]
    if "columns" in value:
        import capo_athena.types.column_list

        out["Columns"] = capo_athena.types.column_list.serialize_aws_json_1_1(
            value["columns"]
        )
    if "partition_keys" in value:
        import capo_athena.types.column_list

        out["PartitionKeys"] = capo_athena.types.column_list.serialize_aws_json_1_1(
            value["partition_keys"]
        )
    if "parameters" in value:
        import capo_athena.types.parameters_map

        out["Parameters"] = capo_athena.types.parameters_map.serialize_aws_json_1_1(
            value["parameters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableMetadata:
    out: TableMetadata = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("CreateTime") is not None:
        import capo_athena.types.timestamp

        out["create_time"] = capo_athena.types.timestamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if data.get("LastAccessTime") is not None:
        import capo_athena.types.timestamp

        out["last_access_time"] = capo_athena.types.timestamp.deserialize_aws_json_1_1(
            data["LastAccessTime"]
        )
    if data.get("TableType") is not None:
        out["table_type"] = data["TableType"]
    if data.get("Columns") is not None:
        import capo_athena.types.column_list

        out["columns"] = capo_athena.types.column_list.deserialize_aws_json_1_1(
            data["Columns"]
        )
    if data.get("PartitionKeys") is not None:
        import capo_athena.types.column_list

        out["partition_keys"] = capo_athena.types.column_list.deserialize_aws_json_1_1(
            data["PartitionKeys"]
        )
    if data.get("Parameters") is not None:
        import capo_athena.types.parameters_map

        out["parameters"] = capo_athena.types.parameters_map.deserialize_aws_json_1_1(
            data["Parameters"]
        )
    return out
