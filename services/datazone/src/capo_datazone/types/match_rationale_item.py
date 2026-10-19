"""Generated from Smithy shape ``com.amazonaws.datazone#MatchRationaleItem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.text_matches


class _MatchRationaleItem_textMatches(TypedDict, closed=True):
    textMatches: "capo_datazone.types.text_matches.TextMatches"


MatchRationaleItem: TypeAlias = _MatchRationaleItem_textMatches | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: MatchRationaleItem) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MatchRationaleItem: cannot serialize unknown variant {value.name!r}"
        )
    elif "textMatches" in value:
        import capo_datazone.types.text_matches

        return {
            "textMatches": capo_datazone.types.text_matches.serialize_json(
                value["textMatches"]
            )
        }
    else:
        raise SerializationError("MatchRationaleItem: no variant present")


def deserialize_json(data: dict) -> MatchRationaleItem:
    if data.get("textMatches") is not None:
        import capo_datazone.types.text_matches

        return {
            "textMatches": capo_datazone.types.text_matches.deserialize_json(
                data["textMatches"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("MatchRationaleItem: no recognized variant key")
