"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.item_id
    import capo_lex_models_v2.types.phrase
    import capo_lex_models_v2.types.weight


class CustomVocabularyItem(TypedDict, closed=True):
    item_id: "capo_lex_models_v2.types.item_id.ItemId"
    """<p>The unique item identifer for the custom vocabulary item from the custom vocabulary list.</p>"""
    phrase: "capo_lex_models_v2.types.phrase.Phrase"
    """<p>The unique phrase for the custom vocabulary item from the custom vocabulary list.</p>"""
    weight: NotRequired["capo_lex_models_v2.types.weight.Weight"]
    """<p>The weight assigned for the custom vocabulary item from the custom vocabulary list.</p>"""
    display_as: NotRequired["capo_lex_models_v2.types.phrase.Phrase"]
    """<p>The DisplayAs value for the custom vocabulary item from the custom vocabulary list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomVocabularyItem) -> dict:
    out: dict = {}
    out["itemId"] = value["item_id"]
    out["phrase"] = value["phrase"]
    if "weight" in value:
        out["weight"] = value["weight"]
    if "display_as" in value:
        out["displayAs"] = value["display_as"]
    return out


def deserialize_json(data: dict) -> CustomVocabularyItem:
    out: CustomVocabularyItem = {}  # type: ignore[typeddict-item]
    if data.get("itemId") is not None:
        out["item_id"] = data["itemId"]
    else:
        out["item_id"] = ""
    if data.get("phrase") is not None:
        out["phrase"] = data["phrase"]
    else:
        out["phrase"] = ""
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    if data.get("displayAs") is not None:
        out["display_as"] = data["displayAs"]
    return out
