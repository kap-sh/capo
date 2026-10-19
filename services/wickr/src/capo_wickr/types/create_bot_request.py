"""Generated from Smithy shape ``com.amazonaws.wickr#CreateBotRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id
    import capo_wickr.types.sensitive_string


class CreateBotRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network where the bot will be created.</p>"""
    username: "capo_wickr.types.generic_string.GenericString"
    """<p>The username for the bot. This must be unique within the network and follow the network's naming conventions.</p>"""
    display_name: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The display name for the bot that will be visible to users in the network.</p>"""
    group_id: "capo_wickr.types.generic_string.GenericString"
    """<p>The ID of the security group to which the bot will be assigned.</p>"""
    challenge: "capo_wickr.types.sensitive_string.SensitiveString"
    """<p>The password for the bot account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotRequest) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    out["groupId"] = value["group_id"]
    out["challenge"] = value["challenge"]
    return out


def deserialize_json(data: dict) -> CreateBotRequest:
    out: CreateBotRequest = {}  # type: ignore[typeddict-item]
    if data.get("username") is not None:
        out["username"] = data["username"]
    else:
        out["username"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    else:
        out["group_id"] = ""
    if data.get("challenge") is not None:
        out["challenge"] = data["challenge"]
    else:
        out["challenge"] = ""
    return out


def redact_sensitive(value: CreateBotRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "challenge" in value:
        out["challenge"] = "*** Sensitive Data Redacted ***"
    return out
