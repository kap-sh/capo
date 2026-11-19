"""Generated from Smithy shape ``com.amazonaws.guardduty#TypeDistributions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.type_distribution

TypeDistributions: TypeAlias = list[
    "capo_guardduty.types.type_distribution.TypeDistribution"
]


# --- restJson1 ser/de ---
def serialize_json(value: TypeDistributions) -> list:
    import capo_guardduty.types.type_distribution

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.type_distribution.serialize_json(item))
    return out


def deserialize_json(data: list) -> TypeDistributions:
    import capo_guardduty.types.type_distribution

    out: TypeDistributions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.type_distribution.deserialize_json(item))
    return out
