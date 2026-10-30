"""Generated from Smithy shape ``com.amazonaws.continuum#IntegrationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.integration_summary

IntegrationSummaries: TypeAlias = list[
    "capo_continuum.types.integration_summary.IntegrationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationSummaries) -> list:
    import capo_continuum.types.integration_summary

    out: list = []
    for item in value:
        out.append(capo_continuum.types.integration_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntegrationSummaries:
    import capo_continuum.types.integration_summary

    out: IntegrationSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.integration_summary.deserialize_json(item))
    return out
