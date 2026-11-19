"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureManagementGroupSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_management_group_summary

AzureManagementGroupSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.azure_management_group_summary.AzureManagementGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzureManagementGroupSummaries) -> list:
    import capo_observabilityadmin.types.azure_management_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.azure_management_group_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AzureManagementGroupSummaries:
    import capo_observabilityadmin.types.azure_management_group_summary

    out: AzureManagementGroupSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_observabilityadmin.types.azure_management_group_summary.deserialize_json(
                item
            )
        )
    return out
