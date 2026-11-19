"""Generated from Smithy shape ``com.amazonaws.guardduty#ResourceDistributions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.resource_distribution

ResourceDistributions: TypeAlias = list[
    "capo_guardduty.types.resource_distribution.ResourceDistribution"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceDistributions) -> list:
    import capo_guardduty.types.resource_distribution

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.resource_distribution.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceDistributions:
    import capo_guardduty.types.resource_distribution

    out: ResourceDistributions = []
    for item in data:
        if item is None:
            continue
        out.append(capo_guardduty.types.resource_distribution.deserialize_json(item))
    return out
