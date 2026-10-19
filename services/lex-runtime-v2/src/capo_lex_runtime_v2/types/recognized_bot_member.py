"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#RecognizedBotMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_runtime_v2.types.bot_identifier
    import capo_lex_runtime_v2.types.name


class RecognizedBotMember(TypedDict, closed=True):
    bot_id: "capo_lex_runtime_v2.types.bot_identifier.BotIdentifier"
    """<p>The identifier of the bot member that processes the request.</p>"""
    bot_name: NotRequired["capo_lex_runtime_v2.types.name.Name"]
    """<p>The name of the bot member that processes the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecognizedBotMember) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    if "bot_name" in value:
        out["botName"] = value["bot_name"]
    return out


def deserialize_json(data: dict) -> RecognizedBotMember:
    out: RecognizedBotMember = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    else:
        out["bot_id"] = ""
    if data.get("botName") is not None:
        out["bot_name"] = data["botName"]
    return out
