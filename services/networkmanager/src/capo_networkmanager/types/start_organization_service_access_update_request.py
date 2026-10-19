"""Generated from Smithy shape ``com.amazonaws.networkmanager#StartOrganizationServiceAccessUpdateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.action


class StartOrganizationServiceAccessUpdateRequest(TypedDict, closed=True):
    action: "capo_networkmanager.types.action.Action"
    """<p>The action to take for the update request. This can be either <code>ENABLE</code> or <code>DISABLE</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartOrganizationServiceAccessUpdateRequest) -> dict:
    out: dict = {}
    out["Action"] = value["action"]
    return out


def deserialize_json(data: dict) -> StartOrganizationServiceAccessUpdateRequest:
    out: StartOrganizationServiceAccessUpdateRequest = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        out["action"] = data["Action"]
    else:
        out["action"] = ""
    return out
