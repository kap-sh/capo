"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotVersionLocaleDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version


class BotVersionLocaleDetails(TypedDict, closed=True):
    source_bot_version: "capo_lex_models_v2.types.bot_version.BotVersion"
    """<p>The version of a bot used for a bot locale.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotVersionLocaleDetails) -> dict:
    out: dict = {}
    out["sourceBotVersion"] = value["source_bot_version"]
    return out


def deserialize_json(data: dict) -> BotVersionLocaleDetails:
    out: BotVersionLocaleDetails = {}  # type: ignore[typeddict-item]
    if data.get("sourceBotVersion") is not None:
        out["source_bot_version"] = data["sourceBotVersion"]
    else:
        out["source_bot_version"] = ""
    return out
