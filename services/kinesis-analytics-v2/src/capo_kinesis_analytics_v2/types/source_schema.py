"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SourceSchema``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.record_columns
    import capo_kinesis_analytics_v2.types.record_encoding
    import capo_kinesis_analytics_v2.types.record_format


class SourceSchema(TypedDict, closed=True):
    record_format: "capo_kinesis_analytics_v2.types.record_format.RecordFormat"
    """<p>Specifies the format of the records on the streaming source.</p>"""
    record_encoding: NotRequired[
        "capo_kinesis_analytics_v2.types.record_encoding.RecordEncoding"
    ]
    """<p>Specifies the encoding of the records in the streaming source. For example, UTF-8.</p>"""
    record_columns: "capo_kinesis_analytics_v2.types.record_columns.RecordColumns"
    """<p>A list of <code>RecordColumn</code> objects. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceSchema) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.record_format

    out["RecordFormat"] = (
        capo_kinesis_analytics_v2.types.record_format.serialize_aws_json_1_1(
            value["record_format"]
        )
    )
    if "record_encoding" in value:
        out["RecordEncoding"] = value["record_encoding"]
    import capo_kinesis_analytics_v2.types.record_columns

    out["RecordColumns"] = (
        capo_kinesis_analytics_v2.types.record_columns.serialize_aws_json_1_1(
            value["record_columns"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceSchema:
    out: SourceSchema = {}  # type: ignore[typeddict-item]
    if data.get("RecordFormat") is not None:
        import capo_kinesis_analytics_v2.types.record_format

        out["record_format"] = (
            capo_kinesis_analytics_v2.types.record_format.deserialize_aws_json_1_1(
                data["RecordFormat"]
            )
        )
    else:
        raise DeserializationError("SourceSchema.record_format required")
    if data.get("RecordEncoding") is not None:
        out["record_encoding"] = data["RecordEncoding"]
    if data.get("RecordColumns") is not None:
        import capo_kinesis_analytics_v2.types.record_columns

        out["record_columns"] = (
            capo_kinesis_analytics_v2.types.record_columns.deserialize_aws_json_1_1(
                data["RecordColumns"]
            )
        )
    else:
        out["record_columns"] = []
    return out
