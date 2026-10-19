"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateDataRetentionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.data_retention_change_in_hours
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.stream_name
    import capo_kinesis_video.types.update_data_retention_operation
    import capo_kinesis_video.types.version


class UpdateDataRetentionInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream whose retention period you want to change.</p>"""
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream whose retention period you want to change.</p>"""
    current_version: "capo_kinesis_video.types.version.Version"
    """<p>The version of the stream whose retention period you want to change. To get the version, call either the <code>DescribeStream</code> or the <code>ListStreams</code> API.</p>"""
    operation: "capo_kinesis_video.types.update_data_retention_operation.UpdateDataRetentionOperation"
    """<p>Indicates whether you want to increase or decrease the retention period.</p>"""
    data_retention_change_in_hours: "capo_kinesis_video.types.data_retention_change_in_hours.DataRetentionChangeInHours"
    """<p>The number of hours to adjust the current retention by. The value you specify is added to or subtracted from the current value, depending on the <code>operation</code>.</p> <p>The minimum value for data retention is 0 and the maximum value is 87600 (ten years).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataRetentionInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    out["CurrentVersion"] = value["current_version"]
    import capo_kinesis_video.types.update_data_retention_operation

    out["Operation"] = (
        capo_kinesis_video.types.update_data_retention_operation.serialize_json(
            value["operation"]
        )
    )
    out["DataRetentionChangeInHours"] = value["data_retention_change_in_hours"]
    return out


def deserialize_json(data: dict) -> UpdateDataRetentionInput:
    out: UpdateDataRetentionInput = {}  # type: ignore[typeddict-item]
    if data.get("StreamName") is not None:
        out["stream_name"] = data["StreamName"]
    if data.get("StreamARN") is not None:
        out["stream_arn"] = data["StreamARN"]
    if data.get("CurrentVersion") is not None:
        out["current_version"] = data["CurrentVersion"]
    else:
        out["current_version"] = ""
    if data.get("Operation") is not None:
        import capo_kinesis_video.types.update_data_retention_operation

        out["operation"] = (
            capo_kinesis_video.types.update_data_retention_operation.deserialize_json(
                data["Operation"]
            )
        )
    else:
        import typing

        out["operation"] = typing.cast(
            "capo_kinesis_video.types.update_data_retention_operation.UpdateDataRetentionOperation",
            "",
        )
    if data.get("DataRetentionChangeInHours") is not None:
        out["data_retention_change_in_hours"] = data["DataRetentionChangeInHours"]
    else:
        out["data_retention_change_in_hours"] = 0
    return out
