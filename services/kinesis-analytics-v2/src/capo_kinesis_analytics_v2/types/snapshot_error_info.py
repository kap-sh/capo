"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotErrorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.error_string
    import capo_kinesis_analytics_v2.types.snapshot_operation_error_code


class SnapshotErrorInfo(TypedDict, closed=True):
    error_code: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_operation_error_code.SnapshotOperationErrorCode"
    ]
    """<p>The error code that identifies the cause of the failure.</p>"""
    error_string: NotRequired[
        "capo_kinesis_analytics_v2.types.error_string.ErrorString"
    ]
    """<p>An error message that is returned when an operation fails.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotErrorInfo) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_string" in value:
        out["ErrorString"] = value["error_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotErrorInfo:
    out: SnapshotErrorInfo = {}  # type: ignore[typeddict-item]
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    if data.get("ErrorString") is not None:
        out["error_string"] = data["ErrorString"]
    return out
