"""Generated from Smithy shape ``com.amazonaws.supportauthz#ActionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supportauthz.types.action
    import capo_supportauthz.types.action_description
    import capo_supportauthz.types.service


class ActionSummary(TypedDict, closed=True):
    action: "capo_supportauthz.types.action.Action"
    """<p>The name of the support action.</p>"""
    service: "capo_supportauthz.types.service.Service"
    """<p>The AWS service associated with the support action.</p>"""
    description: "capo_supportauthz.types.action_description.ActionDescription"
    """<p>A description of what the support action does.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionSummary) -> dict:
    out: dict = {}
    out["action"] = value["action"]
    out["service"] = value["service"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ActionSummary:
    out: ActionSummary = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        out["action"] = data["action"]
    else:
        out["action"] = ""
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        out["service"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
