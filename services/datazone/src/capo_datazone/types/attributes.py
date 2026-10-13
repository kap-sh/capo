"""Generated from Smithy shape ``com.amazonaws.datazone#Attributes``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.attribute_input

Attributes: TypeAlias = list["capo_datazone.types.attribute_input.AttributeInput"]


# --- restJson1 ser/de ---
def serialize_json(value: Attributes) -> list:
    import capo_datazone.types.attribute_input

    out: list = []
    for item in value:
        out.append(capo_datazone.types.attribute_input.serialize_json(item))
    return out


def deserialize_json(data: list) -> Attributes:
    import capo_datazone.types.attribute_input

    out: Attributes = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.attribute_input.deserialize_json(item))
    return out


def redact_sensitive(value: Attributes) -> list[Any]:
    import capo_datazone.types.attribute_input

    return [
        capo_datazone.types.attribute_input.redact_sensitive(item) for item in value
    ]
