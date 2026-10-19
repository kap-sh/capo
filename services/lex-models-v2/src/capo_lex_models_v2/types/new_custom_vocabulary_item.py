"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#NewCustomVocabularyItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.phrase
    import capo_lex_models_v2.types.weight


class NewCustomVocabularyItem(TypedDict, closed=True):
    phrase: "capo_lex_models_v2.types.phrase.Phrase"
    """<p>The unique phrase for the new custom vocabulary item from the custom vocabulary list.</p>"""
    weight: NotRequired["capo_lex_models_v2.types.weight.Weight"]
    """<p>The weight assigned to the new custom vocabulary item from the custom vocabulary list.</p>"""
    display_as: NotRequired["capo_lex_models_v2.types.phrase.Phrase"]
    """<p>The display as value assigned to the new custom vocabulary item from the custom vocabulary list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NewCustomVocabularyItem) -> dict:
    out: dict = {}
    out["phrase"] = value["phrase"]
    if "weight" in value:
        out["weight"] = value["weight"]
    if "display_as" in value:
        out["displayAs"] = value["display_as"]
    return out


def deserialize_json(data: dict) -> NewCustomVocabularyItem:
    out: NewCustomVocabularyItem = {}  # type: ignore[typeddict-item]
    if data.get("phrase") is not None:
        out["phrase"] = data["phrase"]
    else:
        out["phrase"] = ""
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    if data.get("displayAs") is not None:
        out["display_as"] = data["displayAs"]
    return out
