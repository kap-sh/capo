"""Generated from Smithy shape ``com.amazonaws.opensearch#DivergentFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.divergent_field

DivergentFieldList: TypeAlias = list[
    "capo_opensearch.types.divergent_field.DivergentField"
]


# --- restJson1 ser/de ---
def serialize_json(value: DivergentFieldList) -> list:
    import capo_opensearch.types.divergent_field

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.divergent_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> DivergentFieldList:
    import capo_opensearch.types.divergent_field

    out: DivergentFieldList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_opensearch.types.divergent_field.deserialize_json(item))
    return out
