"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.reference_line

ReferenceLineList: TypeAlias = list[
    "capo_quicksight.types.reference_line.ReferenceLine"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineList) -> list:
    import capo_quicksight.types.reference_line

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.reference_line.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReferenceLineList:
    import capo_quicksight.types.reference_line

    out: ReferenceLineList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.reference_line.deserialize_json(item))
    return out


def redact_sensitive(value: ReferenceLineList) -> list[Any]:
    import capo_quicksight.types.reference_line

    return [
        capo_quicksight.types.reference_line.redact_sensitive(item) for item in value
    ]
