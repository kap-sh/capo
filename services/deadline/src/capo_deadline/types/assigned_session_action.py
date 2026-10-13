"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSessionAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_deadline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_deadline.types.assigned_session_action_definition
    import capo_deadline.types.session_action_id


class AssignedSessionAction(TypedDict, closed=True):
    session_action_id: "capo_deadline.types.session_action_id.SessionActionId"
    """<p>The session action ID for the assigned session.</p>"""
    definition: "capo_deadline.types.assigned_session_action_definition.AssignedSessionActionDefinition"
    """<p>The definition of the assigned session action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssignedSessionAction) -> dict:
    out: dict = {}
    out["sessionActionId"] = value["session_action_id"]
    import capo_deadline.types.assigned_session_action_definition

    out["definition"] = (
        capo_deadline.types.assigned_session_action_definition.serialize_json(
            value["definition"]
        )
    )
    return out


def deserialize_json(data: dict) -> AssignedSessionAction:
    out: AssignedSessionAction = {}  # type: ignore[typeddict-item]
    if data.get("sessionActionId") is not None:
        out["session_action_id"] = data["sessionActionId"]
    else:
        raise DeserializationError("AssignedSessionAction.session_action_id required")
    if data.get("definition") is not None:
        import capo_deadline.types.assigned_session_action_definition

        out["definition"] = (
            capo_deadline.types.assigned_session_action_definition.deserialize_json(
                data["definition"]
            )
        )
    else:
        raise DeserializationError("AssignedSessionAction.definition required")
    return out


def redact_sensitive(value: AssignedSessionAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "definition" in value:
        import capo_deadline.types.assigned_session_action_definition

        out["definition"] = (
            capo_deadline.types.assigned_session_action_definition.redact_sensitive(
                value["definition"]
            )
        )
    return out
