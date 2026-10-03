"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#BatchUpdateCustomVocabularyItemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lex_models_v2.types.bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id
    import capo_lex_models_v2.types.update_custom_vocabulary_items_list


class BatchUpdateCustomVocabularyItemRequest(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot associated with this custom vocabulary</p>"""
    bot_version: "capo_lex_models_v2.types.bot_version.BotVersion"
    """<p>The identifier of the version of the bot associated with this custom vocabulary.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the language and locale where this custom vocabulary is used. The string must match one of the supported locales. For more information, see <a href="https://docs.aws.amazon.com/lexv2/latest/dg/how-languages.html"> Supported Languages </a>.</p>"""
    custom_vocabulary_item_list: "capo_lex_models_v2.types.update_custom_vocabulary_items_list.UpdateCustomVocabularyItemsList"
    """<p>A list of custom vocabulary items with updated fields. Each entry must contain a phrase and can optionally contain a displayAs and/or a weight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateCustomVocabularyItemRequest) -> dict:
    out: dict = {}
    import capo_lex_models_v2.types.update_custom_vocabulary_items_list

    out["customVocabularyItemList"] = (
        capo_lex_models_v2.types.update_custom_vocabulary_items_list.serialize_json(
            value["custom_vocabulary_item_list"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchUpdateCustomVocabularyItemRequest:
    out: BatchUpdateCustomVocabularyItemRequest = {}  # type: ignore[typeddict-item]
    if data.get("customVocabularyItemList") is not None:
        import capo_lex_models_v2.types.update_custom_vocabulary_items_list

        out["custom_vocabulary_item_list"] = (
            capo_lex_models_v2.types.update_custom_vocabulary_items_list.deserialize_json(
                data["customVocabularyItemList"]
            )
        )
    else:
        raise DeserializationError(
            "BatchUpdateCustomVocabularyItemRequest.custom_vocabulary_item_list required"
        )
    return out
