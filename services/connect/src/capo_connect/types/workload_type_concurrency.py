"""Generated from Smithy shape ``com.amazonaws.connect#WorkloadTypeConcurrency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.cross_channel_workload_behavior
    import capo_connect.types.workload_type
    import capo_connect.types.workload_type_concurrency_type


class WorkloadTypeConcurrency(TypedDict, closed=True):
    workload_type: "capo_connect.types.workload_type.WorkloadType"
    """<p>The value of the workload type.</p>"""
    concurrency: (
        "capo_connect.types.workload_type_concurrency_type.WorkloadTypeConcurrencyType"
    )
    """<p>The maximum number of contacts an agent can handle simultaneously for a specific channel and workload type combination.</p> <p>Valid Range for <code>VOICE</code>: Minimum value of 1. Maximum value of 1.</p> <p>Valid Range for <code>CHAT</code>: Minimum value of 1. Maximum value of 10.</p> <p>Valid Range for <code>TASK</code>: Minimum value of 1. Maximum value of 10.</p>"""
    cross_channel_workload_behavior: NotRequired[
        "capo_connect.types.cross_channel_workload_behavior.CrossChannelWorkloadBehavior"
    ]
    """<p>Defines the cross-channel and workload type routing behavior for each channel and workload type combination that is enabled for this Routing Profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkloadTypeConcurrency) -> dict:
    out: dict = {}
    out["WorkloadType"] = value["workload_type"]
    out["Concurrency"] = value["concurrency"]
    if "cross_channel_workload_behavior" in value:
        import capo_connect.types.cross_channel_workload_behavior

        out["CrossChannelWorkloadBehavior"] = (
            capo_connect.types.cross_channel_workload_behavior.serialize_json(
                value["cross_channel_workload_behavior"]
            )
        )
    return out


def deserialize_json(data: dict) -> WorkloadTypeConcurrency:
    out: WorkloadTypeConcurrency = {}  # type: ignore[typeddict-item]
    if data.get("WorkloadType") is not None:
        out["workload_type"] = data["WorkloadType"]
    else:
        out["workload_type"] = ""
    if data.get("Concurrency") is not None:
        out["concurrency"] = data["Concurrency"]
    else:
        out["concurrency"] = 0
    if data.get("CrossChannelWorkloadBehavior") is not None:
        import capo_connect.types.cross_channel_workload_behavior

        out["cross_channel_workload_behavior"] = (
            capo_connect.types.cross_channel_workload_behavior.deserialize_json(
                data["CrossChannelWorkloadBehavior"]
            )
        )
    return out
