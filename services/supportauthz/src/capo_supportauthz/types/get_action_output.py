"""Generated from Smithy shape ``com.amazonaws.supportauthz#GetActionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_supportauthz.errors import DeserializationError

if TYPE_CHECKING:
    import capo_supportauthz.types.action
    import capo_supportauthz.types.action_description
    import capo_supportauthz.types.service


class GetActionOutput(TypedDict, closed=True):
    action: "capo_supportauthz.types.action.Action"
    """<p>The name of the support action.</p>"""
    service: "capo_supportauthz.types.service.Service"
    """<p>The AWS service associated with the support action.</p>"""
    description: "capo_supportauthz.types.action_description.ActionDescription"
    """<p>A description of what the support action does.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetActionOutput) -> dict:
    out: dict = {}
    out["action"] = value["action"]
    out["service"] = value["service"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> GetActionOutput:
    out: GetActionOutput = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        raise DeserializationError("GetActionOutput.action required")
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        raise DeserializationError("GetActionOutput.service required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        raise DeserializationError("GetActionOutput.description required")
    return out
