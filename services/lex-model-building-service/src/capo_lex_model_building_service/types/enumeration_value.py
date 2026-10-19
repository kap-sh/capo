"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#EnumerationValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.synonym_list
    import capo_lex_model_building_service.types.value


class EnumerationValue(TypedDict, closed=True):
    value: "capo_lex_model_building_service.types.value.Value"
    """<p>The value of the slot type.</p>"""
    synonyms: NotRequired[
        "capo_lex_model_building_service.types.synonym_list.SynonymList"
    ]
    """<p>Additional values related to the slot type value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnumerationValue) -> dict:
    out: dict = {}
    out["value"] = value["value"]
    if "synonyms" in value:
        import capo_lex_model_building_service.types.synonym_list

        out["synonyms"] = (
            capo_lex_model_building_service.types.synonym_list.serialize_json(
                value["synonyms"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnumerationValue:
    out: EnumerationValue = {}  # type: ignore[typeddict-item]
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("synonyms") is not None:
        import capo_lex_model_building_service.types.synonym_list

        out["synonyms"] = (
            capo_lex_model_building_service.types.synonym_list.deserialize_json(
                data["synonyms"]
            )
        )
    return out
