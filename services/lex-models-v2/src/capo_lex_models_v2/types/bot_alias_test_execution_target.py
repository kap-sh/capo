"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BotAliasTestExecutionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_alias_id
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class BotAliasTestExecutionTarget(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The bot Id of the bot alias used in the test set execution.</p>"""
    bot_alias_id: "capo_lex_models_v2.types.bot_alias_id.BotAliasId"
    """<p>The bot alias Id of the bot alias used in the test set execution.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The locale Id of the bot alias used in the test set execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BotAliasTestExecutionTarget) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botAliasId"] = value["bot_alias_id"]
    out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> BotAliasTestExecutionTarget:
    out: BotAliasTestExecutionTarget = {}  # type: ignore[typeddict-item]
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
