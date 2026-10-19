"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#GenerateBotElementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class GenerateBotElementRequest(TypedDict, closed=True):
    intent_id: "capo_lex_models_v2.types.id.Id"
    """<p>The intent unique Id for the bot request to generate utterances.</p>"""
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The bot unique Id for the bot request to generate utterances.</p>"""
    bot_version: "capo_lex_models_v2.types.bot_version.BotVersion"
    """<p>The bot version for the bot request to generate utterances.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The unique locale Id for the bot request to generate utterances.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateBotElementRequest) -> dict:
    out: dict = {}
    out["intentId"] = value["intent_id"]
    return out


def deserialize_json(data: dict) -> GenerateBotElementRequest:
    out: GenerateBotElementRequest = {}  # type: ignore[typeddict-item]
    if data.get("intentId") is not None:
        out["intent_id"] = data["intentId"]
    else:
        out["intent_id"] = ""
    return out
