"""Generated from Smithy shape ``com.amazonaws.groundstation#UpdateAgentStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.aggregate_status
    import capo_groundstation.types.component_status_list
    import capo_groundstation.types.uuid


class UpdateAgentStatusRequest(TypedDict, closed=True):
    agent_id: "capo_groundstation.types.uuid.Uuid"
    """<p>UUID of agent to update.</p>"""
    task_id: "capo_groundstation.types.uuid.Uuid"
    """<p>GUID of agent task.</p>"""
    aggregate_status: "capo_groundstation.types.aggregate_status.AggregateStatus"
    """<p>Aggregate status for agent.</p>"""
    component_statuses: (
        "capo_groundstation.types.component_status_list.ComponentStatusList"
    )
    """<p>List of component statuses for agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentStatusRequest) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    import capo_groundstation.types.aggregate_status

    out["aggregateStatus"] = capo_groundstation.types.aggregate_status.serialize_json(
        value["aggregate_status"]
    )
    import capo_groundstation.types.component_status_list

    out["componentStatuses"] = (
        capo_groundstation.types.component_status_list.serialize_json(
            value["component_statuses"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAgentStatusRequest:
    out: UpdateAgentStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    else:
        out["task_id"] = ""
    if data.get("aggregateStatus") is not None:
        import capo_groundstation.types.aggregate_status

        out["aggregate_status"] = (
            capo_groundstation.types.aggregate_status.deserialize_json(
                data["aggregateStatus"]
            )
        )
    else:
        raise DeserializationError("UpdateAgentStatusRequest.aggregate_status required")
    if data.get("componentStatuses") is not None:
        import capo_groundstation.types.component_status_list

        out["component_statuses"] = (
            capo_groundstation.types.component_status_list.deserialize_json(
                data["componentStatuses"]
            )
        )
    else:
        out["component_statuses"] = []
    return out
