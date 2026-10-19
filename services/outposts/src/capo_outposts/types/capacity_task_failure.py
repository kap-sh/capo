"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskFailure``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.capacity_task_failure_type
    import capo_outposts.types.capacity_task_status_reason


class CapacityTaskFailure(TypedDict, closed=True):
    reason: "capo_outposts.types.capacity_task_status_reason.CapacityTaskStatusReason"
    """<p>The reason that the specified capacity task failed.</p>"""
    type: NotRequired[
        "capo_outposts.types.capacity_task_failure_type.CapacityTaskFailureType"
    ]
    """<p>The type of failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityTaskFailure) -> dict:
    out: dict = {}
    out["Reason"] = value["reason"]
    if "type" in value:
        import capo_outposts.types.capacity_task_failure_type

        out["Type"] = capo_outposts.types.capacity_task_failure_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> CapacityTaskFailure:
    out: CapacityTaskFailure = {}  # type: ignore[typeddict-item]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    else:
        out["reason"] = ""
    if data.get("Type") is not None:
        import capo_outposts.types.capacity_task_failure_type

        out["type"] = capo_outposts.types.capacity_task_failure_type.deserialize_json(
            data["Type"]
        )
    return out
