"""Generated from Smithy shape ``com.amazonaws.deadline#UpdatedSessionActions``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.session_action_id
    import capo_deadline.types.updated_session_action_info

UpdatedSessionActions: TypeAlias = dict[
    "capo_deadline.types.session_action_id.SessionActionId",
    "capo_deadline.types.updated_session_action_info.UpdatedSessionActionInfo",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UpdatedSessionActions) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_deadline.types.updated_session_action_info

        out[key] = capo_deadline.types.updated_session_action_info.serialize_json(value)
    return out


def deserialize_json(data: dict) -> UpdatedSessionActions:
    out: UpdatedSessionActions = {}
    for key, value in data.items():
        if value is None:
            continue
        import capo_deadline.types.updated_session_action_info

        out[key] = capo_deadline.types.updated_session_action_info.deserialize_json(
            value
        )
    return out


def redact_sensitive(value: UpdatedSessionActions) -> dict[str, Any]:
    import capo_deadline.types.updated_session_action_info

    return {
        key: capo_deadline.types.updated_session_action_info.redact_sensitive(item)
        for key, item in value.items()
    }
