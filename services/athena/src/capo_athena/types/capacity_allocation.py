"""Generated from Smithy shape ``com.amazonaws.athena#CapacityAllocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.capacity_allocation_status
    import capo_athena.types.string
    import capo_athena.types.timestamp


class CapacityAllocation(TypedDict, closed=True):
    status: "capo_athena.types.capacity_allocation_status.CapacityAllocationStatus"
    """<p>The status of the capacity allocation.</p>"""
    status_message: NotRequired["capo_athena.types.string.String"]
    """<p>The status message of the capacity allocation.</p>"""
    request_time: "capo_athena.types.timestamp.Timestamp"
    """<p>The time when the capacity allocation was requested.</p>"""
    request_completion_time: NotRequired["capo_athena.types.timestamp.Timestamp"]
    """<p>The time when the capacity allocation request was completed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityAllocation) -> dict:
    out: dict = {}
    import capo_athena.types.capacity_allocation_status

    out["Status"] = capo_athena.types.capacity_allocation_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    import capo_athena.types.timestamp

    out["RequestTime"] = capo_athena.types.timestamp.serialize_aws_json_1_1(
        value["request_time"]
    )
    if "request_completion_time" in value:
        import capo_athena.types.timestamp

        out["RequestCompletionTime"] = (
            capo_athena.types.timestamp.serialize_aws_json_1_1(
                value["request_completion_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CapacityAllocation:
    out: CapacityAllocation = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_athena.types.capacity_allocation_status

        out["status"] = (
            capo_athena.types.capacity_allocation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_athena.types.capacity_allocation_status.CapacityAllocationStatus", ""
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("RequestTime") is not None:
        import capo_athena.types.timestamp

        out["request_time"] = capo_athena.types.timestamp.deserialize_aws_json_1_1(
            data["RequestTime"]
        )
    else:
        import datetime

        out["request_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("RequestCompletionTime") is not None:
        import capo_athena.types.timestamp

        out["request_completion_time"] = (
            capo_athena.types.timestamp.deserialize_aws_json_1_1(
                data["RequestCompletionTime"]
            )
        )
    return out
