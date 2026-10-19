"""Generated from Smithy shape ``com.amazonaws.connect#LexBot``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.bot_name
    import capo_connect.types.lex_region


class LexBot(TypedDict, closed=True):
    name: "capo_connect.types.bot_name.BotName"
    """<p>The name of the Amazon Lex bot.</p>"""
    lex_region: "capo_connect.types.lex_region.LexRegion"
    """<p>The Amazon Web Services Region where the Amazon Lex bot was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LexBot) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["LexRegion"] = value["lex_region"]
    return out


def deserialize_json(data: dict) -> LexBot:
    out: LexBot = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("LexRegion") is not None:
        out["lex_region"] = data["LexRegion"]
    else:
        out["lex_region"] = ""
    return out
