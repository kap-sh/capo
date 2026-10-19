"""Generated from Smithy shape ``com.amazonaws.wickr#CreateBotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.bot_id
    import capo_wickr.types.generic_string
    import capo_wickr.types.network_id


class CreateBotResponse(TypedDict, closed=True):
    message: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the result of the bot creation operation.</p>"""
    bot_id: "capo_wickr.types.bot_id.BotId"
    """<p>The unique identifier assigned to the newly created bot.</p>"""
    network_id: NotRequired["capo_wickr.types.network_id.NetworkId"]
    """<p>The ID of the network where the bot was created.</p>"""
    username: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The username of the newly created bot.</p>"""
    display_name: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The display name of the newly created bot.</p>"""
    group_id: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The ID of the security group to which the bot was assigned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBotResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    out["botId"] = value["bot_id"]
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    if "username" in value:
        out["username"] = value["username"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> CreateBotResponse:
    out: CreateBotResponse = {}  # type: ignore[typeddict-item]
    if data.get("message") is not None:
        out["message"] = data["message"]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    else:
        out["bot_id"] = ""
    if data.get("networkId") is not None:
        out["network_id"] = data["networkId"]
    if data.get("username") is not None:
        out["username"] = data["username"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    return out
