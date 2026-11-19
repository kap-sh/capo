"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.network_migration_insights_list
    import capo_mgn.types.pagination_token


class ListNetworkMigrationInsightsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_mgn.types.network_migration_insights_list.NetworkMigrationInsightsList"
    ]
    """<p>A list of network migration insights.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationInsightsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.network_migration_insights_list

        out["items"] = capo_mgn.types.network_migration_insights_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationInsightsResponse:
    out: ListNetworkMigrationInsightsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_mgn.types.network_migration_insights_list

        out["items"] = capo_mgn.types.network_migration_insights_list.deserialize_json(
            data["items"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
