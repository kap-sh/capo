"""Generated from Smithy shape ``com.amazonaws.wickr#UpdateBotRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.bot_id
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id
    import capo_wickr.types.sensitive_string


class UpdateBotRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the bot to update.</p>"""
    bot_id: "capo_wickr.types.bot_id.BotId"
    """<p>The unique identifier of the bot to update.</p>"""
    display_name: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The new display name for the bot.</p>"""
    group_id: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The ID of the new security group to assign the bot to.</p>"""
    challenge: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The new password for the bot account.</p>"""
    suspend: NotRequired["bool"]
    """<p>Set to true to suspend the bot or false to unsuspend it. Omit this field for standard updates that don't affect suspension status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBotRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "challenge" in value:
        out["challenge"] = value["challenge"]
    if "suspend" in value:
        out["suspend"] = value["suspend"]
    return out


def deserialize_json(data: dict) -> UpdateBotRequest:
    out: UpdateBotRequest = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    if data.get("challenge") is not None:
        out["challenge"] = data["challenge"]
    if data.get("suspend") is not None:
        out["suspend"] = data["suspend"]
    return out


def redact_sensitive(value: UpdateBotRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "challenge" in value:
        out["challenge"] = "*** Sensitive Data Redacted ***"
    return out
