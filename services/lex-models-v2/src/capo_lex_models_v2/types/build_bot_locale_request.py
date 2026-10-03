"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BuildBotLocaleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class BuildBotLocaleRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to build. The identifier is returned in the response from the <a href="https://docs.aws.amazon.com/lexv2/latest/APIReference/API_CreateBot.html">CreateBot</a> operation.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot to build. This can only be the draft version of the bot.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale that the bot will be used in. The string must match one of the supported locales. All of the intents, slot types, and slots used in the bot must have the same locale. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html">Supported languages</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BuildBotLocaleRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> BuildBotLocaleRequest:
    out: BuildBotLocaleRequest = {}  # type: ignore[typeddict-item]
    return out
