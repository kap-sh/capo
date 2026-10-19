"""Generated from Smithy shape ``com.amazonaws.keyspaces#PointInTimeRecoverySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.point_in_time_recovery_status
    import capo_keyspaces.types.timestamp


class PointInTimeRecoverySummary(TypedDict, closed=True):
    status: (
        "capo_keyspaces.types.point_in_time_recovery_status.PointInTimeRecoveryStatus"
    )
    """<p>Shows if point-in-time recovery is enabled or disabled for the specified table.</p>"""
    earliest_restorable_timestamp: NotRequired[
        "capo_keyspaces.types.timestamp.Timestamp"
    ]
    """<p>Specifies the earliest possible restore point of the table in ISO 8601 format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PointInTimeRecoverySummary) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "earliest_restorable_timestamp" in value:
        import capo_keyspaces.types.timestamp

        out["earliestRestorableTimestamp"] = (
            capo_keyspaces.types.timestamp.serialize_aws_json_1_0(
                value["earliest_restorable_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PointInTimeRecoverySummary:
    out: PointInTimeRecoverySummary = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("earliestRestorableTimestamp") is not None:
        import capo_keyspaces.types.timestamp

        out["earliest_restorable_timestamp"] = (
            capo_keyspaces.types.timestamp.deserialize_aws_json_1_0(
                data["earliestRestorableTimestamp"]
            )
        )
    return out
