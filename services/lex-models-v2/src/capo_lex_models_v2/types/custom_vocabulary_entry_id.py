"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#CustomVocabularyEntryId``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.item_id


class CustomVocabularyEntryId(TypedDict, closed=True):
    item_id: "capo_lex_models_v2.types.item_id.ItemId"
    """<p>The unique item identifier for the custom vocabulary items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomVocabularyEntryId) -> dict:
    out: dict = {}
    out["itemId"] = value["item_id"]
    return out


def deserialize_json(data: dict) -> CustomVocabularyEntryId:
    out: CustomVocabularyEntryId = {}  # type: ignore[typeddict-item]
    if data.get("itemId") is not None:
        out["item_id"] = data["itemId"]
    else:
        out["item_id"] = ""
    return out
