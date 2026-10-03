"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#RecordColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.record_column_mapping
    import capo_kinesis_analytics.types.record_column_name
    import capo_kinesis_analytics.types.record_column_sql_type


class RecordColumn(TypedDict, closed=True):
    name: "capo_kinesis_analytics.types.record_column_name.RecordColumnName"
    """<p>Name of the column created in the in-application input stream or reference table.</p>"""
    mapping: NotRequired[
        "capo_kinesis_analytics.types.record_column_mapping.RecordColumnMapping"
    ]
    """<p>Reference to the data element in the streaming input or the reference data source. This element is required if the <a href="https://docs.aws.amazon.com/kinesisanalytics/latest/dev/API_RecordFormat.html#analytics-Type-RecordFormat-RecordFormatTypel">RecordFormatType</a> is <code>JSON</code>.</p>"""
    sql_type: "capo_kinesis_analytics.types.record_column_sql_type.RecordColumnSqlType"
    """<p>Type of column created in the in-application input stream or reference table.</p>"""


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
        raise DeserializationError("RecordColumn.name required")
    if data.get("Mapping") is not None:
        out["mapping"] = data["Mapping"]
    if data.get("SqlType") is not None:
        out["sql_type"] = data["SqlType"]
    else:
        raise DeserializationError("RecordColumn.sql_type required")
    return out
