"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSessionActions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.assigned_session_action

AssignedSessionActions: TypeAlias = list[
    "capo_deadline.types.assigned_session_action.AssignedSessionAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssignedSessionActions) -> list:
    import capo_deadline.types.assigned_session_action

    out: list = []
    for item in value:
        out.append(capo_deadline.types.assigned_session_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssignedSessionActions:
    import capo_deadline.types.assigned_session_action

    out: AssignedSessionActions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_deadline.types.assigned_session_action.deserialize_json(item))
    return out


def redact_sensitive(value: AssignedSessionActions) -> list[Any]:
    import capo_deadline.types.assigned_session_action

    return [
        capo_deadline.types.assigned_session_action.redact_sensitive(item)
        for item in value
    ]
