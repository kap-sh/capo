"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.text_attributes


class _FieldAttributes_text(TypedDict, closed=True):
    text: "capo_connectcases.types.text_attributes.TextAttributes"


FieldAttributes: TypeAlias = _FieldAttributes_text | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: FieldAttributes) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"FieldAttributes: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        import capo_connectcases.types.text_attributes

        return {
            "text": capo_connectcases.types.text_attributes.serialize_json(
                value["text"]
            )
        }
    else:
        raise SerializationError("FieldAttributes: no variant present")


def deserialize_json(data: dict) -> FieldAttributes:
    if data.get("text") is not None:
        import capo_connectcases.types.text_attributes

        return {
            "text": capo_connectcases.types.text_attributes.deserialize_json(
                data["text"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("FieldAttributes: no recognized variant key")
