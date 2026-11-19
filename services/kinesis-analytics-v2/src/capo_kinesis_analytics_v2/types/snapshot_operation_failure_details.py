"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotOperationFailureDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.snapshot_error_info


class SnapshotOperationFailureDetails(TypedDict, closed=True):
    error_info: NotRequired[
        "capo_kinesis_analytics_v2.types.snapshot_error_info.SnapshotErrorInfo"
    ]
    """<p>A description of the error that caused the snapshot operation to fail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotOperationFailureDetails) -> dict:
    out: dict = {}
    if "error_info" in value:
        import capo_kinesis_analytics_v2.types.snapshot_error_info

        out["ErrorInfo"] = (
            capo_kinesis_analytics_v2.types.snapshot_error_info.serialize_aws_json_1_1(
                value["error_info"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotOperationFailureDetails:
    out: SnapshotOperationFailureDetails = {}  # type: ignore[typeddict-item]
    if data.get("ErrorInfo") is not None:
        import capo_kinesis_analytics_v2.types.snapshot_error_info

        out["error_info"] = (
            capo_kinesis_analytics_v2.types.snapshot_error_info.deserialize_aws_json_1_1(
                data["ErrorInfo"]
            )
        )
    return out
