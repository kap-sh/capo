"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#TestSetDiscrepancyReportBotAliasTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class TestSetDiscrepancyReportBotAliasTarget(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The unique identifier for the bot alias.</p>"""
    bot_alias_id: "capo_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The unique identifier for the bot associated with the bot alias.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The unique identifier of the locale associated with the bot alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestSetDiscrepancyReportBotAliasTarget) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botAliasId"] = value["bot_alias_id"]
    out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> TestSetDiscrepancyReportBotAliasTarget:
    out: TestSetDiscrepancyReportBotAliasTarget = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    else:
        out["bot_id"] = ""
    if data.get("botAliasId") is not None:
        out["bot_alias_id"] = data["botAliasId"]
    else:
        out["bot_alias_id"] = ""
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    else:
        out["locale_id"] = ""
    return out
