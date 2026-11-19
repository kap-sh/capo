"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationInsightsTypesFilter``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.insight_type

ListNetworkMigrationInsightsTypesFilter: TypeAlias = list[
    "capo_mgn.types.insight_type.InsightType"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationInsightsTypesFilter) -> list:
    return list(value)


def deserialize_json(data: list) -> ListNetworkMigrationInsightsTypesFilter:
    return [item for item in data if item is not None]
