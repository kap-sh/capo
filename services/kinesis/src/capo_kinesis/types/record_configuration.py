"""Generated from Smithy shape ``com.amazonaws.kinesis#RecordConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis.types.gsr_schema_arn
    import capo_kinesis.types.record_format_type


class RecordConfiguration(TypedDict, closed=True):
    record_format_type: "capo_kinesis.types.record_format_type.RecordFormatType"
    """<p>The format of records on the source stream. Valid values:</p> <ul> <li> <p> <code>GSR_JSON</code> - Supported only for streaming table (Amazon S3 Tables) destinations.</p> </li> <li> <p> <code>JSON</code> - Supported for both general purpose Amazon S3 and streaming table destinations.</p> </li> <li> <p> <code>STRING</code> - Supported only for general purpose Amazon S3 destinations.</p> </li> <li> <p> <code>BYTE_ARRAY</code> - Supported only for general purpose Amazon S3 destinations.</p> </li> </ul>"""
    gsr_schema_arn: NotRequired["capo_kinesis.types.gsr_schema_arn.GSRSchemaARN"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Glue Schema Registry schema used to validate records. Required when the channel destination is a streaming table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordConfiguration) -> dict:
    out: dict = {}
    import capo_kinesis.types.record_format_type

    out["RecordFormatType"] = (
        capo_kinesis.types.record_format_type.serialize_aws_json_1_1(
            value["record_format_type"]
        )
    )
    if "gsr_schema_arn" in value:
        out["GSRSchemaARN"] = value["gsr_schema_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordConfiguration:
    out: RecordConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("RecordFormatType") is not None:
        import capo_kinesis.types.record_format_type

        out["record_format_type"] = (
            capo_kinesis.types.record_format_type.deserialize_aws_json_1_1(
                data["RecordFormatType"]
            )
        )
    else:
        import typing

        out["record_format_type"] = typing.cast(
            "capo_kinesis.types.record_format_type.RecordFormatType", ""
        )
    if data.get("GSRSchemaARN") is not None:
        out["gsr_schema_arn"] = data["GSRSchemaARN"]
    return out
