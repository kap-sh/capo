"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IpRule``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces_web.types.description
    import capo_workspaces_web.types.ip_range


class IpRule(TypedDict, closed=True):
    ip_range: "capo_workspaces_web.types.ip_range.IpRange"
    """<p>The IP range of the IP rule.</p>"""
    description: NotRequired["capo_workspaces_web.types.description.Description"]
    """<p>The description of the IP rule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpRule) -> dict:
    out: dict = {}
    out["ipRange"] = value["ip_range"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> IpRule:
    out: IpRule = {}  # type: ignore[typeddict-item]
    if data.get("ipRange") is not None:
        out["ip_range"] = data["ipRange"]
    else:
        raise DeserializationError("IpRule.ip_range required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out


def redact_sensitive(value: IpRule) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ip_range" in value:
        out["ip_range"] = "*** Sensitive Data Redacted ***"
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
