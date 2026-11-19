"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureResourceIdentifierSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_resource_identifier_summary

AzureResourceIdentifierSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.azure_resource_identifier_summary.AzureResourceIdentifierSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureResourceIdentifierSummaries) -> list:
    import capo_observabilityadmin.types.azure_resource_identifier_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.azure_resource_identifier_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AzureResourceIdentifierSummaries:
    import capo_observabilityadmin.types.azure_resource_identifier_summary

    out: AzureResourceIdentifierSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.azure_resource_identifier_summary.deserialize_json(
                item
            )
        )
    return out
