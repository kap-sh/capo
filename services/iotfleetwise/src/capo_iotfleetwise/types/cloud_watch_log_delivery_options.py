"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CloudWatchLogDeliveryOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.cloud_watch_log_group_name
    import capo_iotfleetwise.types.log_type


class CloudWatchLogDeliveryOptions(TypedDict, closed=True):
    log_type: "capo_iotfleetwise.types.log_type.LogType"
    """<p>The type of log to send data to Amazon CloudWatch Logs.</p>"""
    log_group_name: NotRequired[
        "capo_iotfleetwise.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
    ]
    """<p>The Amazon CloudWatch Logs group the operation sends data to.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloudWatchLogDeliveryOptions) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.log_type

    out["logType"] = capo_iotfleetwise.types.log_type.serialize_aws_json_1_0(
        value["log_type"]
    )
    if "log_group_name" in value:
        out["logGroupName"] = value["log_group_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CloudWatchLogDeliveryOptions:
    out: CloudWatchLogDeliveryOptions = {}  # type: ignore[typeddict-item]
    if data.get("logType") is not None:
        import capo_iotfleetwise.types.log_type

        out["log_type"] = capo_iotfleetwise.types.log_type.deserialize_aws_json_1_0(
            data["logType"]
        )
    else:
        import typing

        out["log_type"] = typing.cast("capo_iotfleetwise.types.log_type.LogType", "")
    if data.get("logGroupName") is not None:
        out["log_group_name"] = data["logGroupName"]
    return out
