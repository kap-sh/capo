"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RecordColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.record_column_mapping
    import capo_kinesis_analytics_v2.types.record_column_name
    import capo_kinesis_analytics_v2.types.record_column_sql_type


class RecordColumn(TypedDict, closed=True):
    name: "capo_kinesis_analytics_v2.types.record_column_name.RecordColumnName"
    """<p>The name of the column that is created in the in-application input stream or reference table.</p>"""
    mapping: NotRequired[
        "capo_kinesis_analytics_v2.types.record_column_mapping.RecordColumnMapping"
    ]
    """<p>A reference to the data element in the streaming input or the reference data source.</p>"""
    sql_type: (
        "capo_kinesis_analytics_v2.types.record_column_sql_type.RecordColumnSqlType"
    )
    """<p>The type of column created in the in-application input stream or reference table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordColumn) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "mapping" in value:
        out["Mapping"] = value["mapping"]
    out["SqlType"] = value["sql_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordColumn:
    out: RecordColumn = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Mapping") is not None:
        out["mapping"] = data["Mapping"]
    if data.get("SqlType") is not None:
        out["sql_type"] = data["SqlType"]
    else:
        out["sql_type"] = ""
    return out
