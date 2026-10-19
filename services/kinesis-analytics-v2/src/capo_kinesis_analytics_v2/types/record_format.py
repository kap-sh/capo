"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RecordFormat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.mapping_parameters
    import capo_kinesis_analytics_v2.types.record_format_type


class RecordFormat(TypedDict, closed=True):
    record_format_type: (
        "capo_kinesis_analytics_v2.types.record_format_type.RecordFormatType"
    )
    """<p>The type of record format.</p>"""
    mapping_parameters: NotRequired[
        "capo_kinesis_analytics_v2.types.mapping_parameters.MappingParameters"
    ]
    """<p>When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordFormat) -> dict:
    out: dict = {}
    import capo_kinesis_analytics_v2.types.record_format_type

    out["RecordFormatType"] = (
        capo_kinesis_analytics_v2.types.record_format_type.serialize_aws_json_1_1(
            value["record_format_type"]
        )
    )
    if "mapping_parameters" in value:
        import capo_kinesis_analytics_v2.types.mapping_parameters

        out["MappingParameters"] = (
            capo_kinesis_analytics_v2.types.mapping_parameters.serialize_aws_json_1_1(
                value["mapping_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordFormat:
    out: RecordFormat = {}  # type: ignore[typeddict-item]
    if data.get("RecordFormatType") is not None:
        import capo_kinesis_analytics_v2.types.record_format_type

        out["record_format_type"] = (
            capo_kinesis_analytics_v2.types.record_format_type.deserialize_aws_json_1_1(
                data["RecordFormatType"]
            )
        )
    else:
        import typing

        out["record_format_type"] = typing.cast(
            "capo_kinesis_analytics_v2.types.record_format_type.RecordFormatType", ""
        )
    if data.get("MappingParameters") is not None:
        import capo_kinesis_analytics_v2.types.mapping_parameters

        out["mapping_parameters"] = (
            capo_kinesis_analytics_v2.types.mapping_parameters.deserialize_aws_json_1_1(
                data["MappingParameters"]
            )
        )
    return out
