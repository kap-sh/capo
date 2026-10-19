"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyImportSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.draft_bot_version
    import capo_lex_models_v2.types.id
    import capo_lex_models_v2.types.locale_id


class CustomVocabularyImportSpecification(TypedDict, closed=True):
    bot_id: "capo_lex_models_v2.types.id.Id"
    """<p>The identifier of the bot to import the custom vocabulary to.</p>"""
    bot_version: "capo_lex_models_v2.types.draft_bot_version.DraftBotVersion"
    """<p>The version of the bot to import the custom vocabulary to.</p>"""
    locale_id: "capo_lex_models_v2.types.locale_id.LocaleId"
    """<p>The identifier of the local to import the custom vocabulary to. The value must be <code>en_GB</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomVocabularyImportSpecification) -> dict:
    out: dict = {}
    out["botId"] = value["bot_id"]
    out["botVersion"] = value["bot_version"]
    out["localeId"] = value["locale_id"]
    return out


def deserialize_json(data: dict) -> CustomVocabularyImportSpecification:
    out: CustomVocabularyImportSpecification = {}  # type: ignore[typeddict-item]
    if data.get("botId") is not None:
        out["bot_id"] = data["botId"]
    else:
        out["bot_id"] = ""
    if data.get("botVersion") is not None:
        out["bot_version"] = data["botVersion"]
    else:
        out["bot_version"] = ""
    if data.get("localeId") is not None:
        out["locale_id"] = data["localeId"]
    else:
        out["locale_id"] = ""
    return out
