"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSessions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.assigned_session
    import capo_deadline.types.session_id

AssignedSessions: TypeAlias = dict[
    "capo_deadline.types.session_id.SessionId",
    "capo_deadline.types.assigned_session.AssignedSession",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AssignedSessions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_deadline.types.assigned_session

        out[key] = capo_deadline.types.assigned_session.serialize_json(value)
    return out


def deserialize_json(data: dict) -> AssignedSessions:
    out: AssignedSessions = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_deadline.types.assigned_session

        out[key] = capo_deadline.types.assigned_session.deserialize_json(value)
    return out


def redact_sensitive(value: AssignedSessions) -> dict[str, Any]:
    import capo_deadline.types.assigned_session

    return {
        key: capo_deadline.types.assigned_session.redact_sensitive(item)
        for key, item in value.items()
    }
