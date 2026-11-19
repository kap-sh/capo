"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationInsightsFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.list_network_migration_insights_types_filter


class ListNetworkMigrationInsightsFilters(TypedDict, closed=True):
    insight_types: NotRequired[
        "capo_mgn.types.list_network_migration_insights_types_filter.ListNetworkMigrationInsightsTypesFilter"
    ]
    """<p>The insight types to include in the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationInsightsFilters) -> dict:
    out: dict = {}
    if "insight_types" in value:
        import capo_mgn.types.list_network_migration_insights_types_filter

        out["insightTypes"] = (
            capo_mgn.types.list_network_migration_insights_types_filter.serialize_json(
                value["insight_types"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationInsightsFilters:
    out: ListNetworkMigrationInsightsFilters = {}  # type: ignore[typeddict-item]
    if data.get("insightTypes") is not None:
        import capo_mgn.types.list_network_migration_insights_types_filter

        out["insight_types"] = (
            capo_mgn.types.list_network_migration_insights_types_filter.deserialize_json(
                data["insightTypes"]
            )
        )
    return out
