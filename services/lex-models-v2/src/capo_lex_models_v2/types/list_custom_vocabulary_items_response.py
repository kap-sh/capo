"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#ListCustomVocabularyItemsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.custom_vocabulary_items
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.next_token


class ListCustomVocabularyItemsResponse(TypedDict, closed=True):
    bot_id: NotRequired["capo_lex_models_v2.types.id.Id"]
    """<p>The identifier of the bot associated with this custom vocabulary.</p>"""
    bot_version: NotRequired["capo_lex_models_v2.types.bot_version.BotVersion"]
    """<p>The identifier of the version of the bot associated with this custom vocabulary.</p>"""
    locale_id: NotRequired["capo_lex_models_v2.types.locale_id.LocaleId"]
    """<p>The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html"> Supported Languages </a>.</p>"""
    custom_vocabulary_items: NotRequired[
        "capo_lex_models_v2.types.custom_vocabulary_items.CustomVocabularyItems"
    ]
    """<p>The custom vocabulary items from the list custom vocabulary response.</p>"""
    next_token: NotRequired["capo_lex_models_v2.types.next_token.NextToken"]
    """<p>The nextToken identifier to the list custom vocabulary response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomVocabularyItemsResponse) -> dict:
    out: dict = {}
    if "bot_id" in value:
        out["botId"] = value["bot_id"]
    if "bot_version" in value:
        out["botVersion"] = value["bot_version"]
    if "locale_id" in value:
        out["localeId"] = value["locale_id"]
    if "custom_vocabulary_items" in value:
        import capo_lex_models_v2.types.custom_vocabulary_items

        out["customVocabularyItems"] = (
            capo_lex_models_v2.types.custom_vocabulary_items.serialize_json(
                value["custom_vocabulary_items"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCustomVocabularyItemsResponse:
    out: ListCustomVocabularyItemsResponse = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    if data.get("customVocabularyItems") is not None:
        import capo_lex_models_v2.types.custom_vocabulary_items

        out["custom_vocabulary_items"] = (
            capo_lex_models_v2.types.custom_vocabulary_items.deserialize_json(
                data["customVocabularyItems"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
