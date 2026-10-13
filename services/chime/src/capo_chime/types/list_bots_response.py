"""Generated from Smithy shape ``com.amazonaws.chime#ListBotsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime.types.bot_list
    import capo_chime.types.string


class ListBotsResponse(TypedDict, closed=True):
    bots: NotRequired["capo_chime.types.bot_list.BotList"]
    """<p>List of bots and bot details.</p>"""
    next_token: NotRequired["capo_chime.types.string.String"]
    """<p>The token to use to retrieve the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBotsResponse) -> dict:
    out: dict = {}
    if "bots" in value:
        import capo_chime.types.bot_list

        out["Bots"] = capo_chime.types.bot_list.serialize_json(value["bots"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBotsResponse:
    out: ListBotsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Bots") is not None:
        import capo_chime.types.bot_list

        out["bots"] = capo_chime.types.bot_list.deserialize_json(data["Bots"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListBotsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "bots" in value:
        import capo_chime.types.bot_list

        out["bots"] = capo_chime.types.bot_list.redact_sensitive(value["bots"])
    return out
