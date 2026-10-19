"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationExecutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.list_network_migration_execution_request_filters
    import capo_mgn.types.max_results_type
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.pagination_token


class ListNetworkMigrationExecutionsRequest(TypedDict, closed=True):
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition to list executions for.</p>"""
    filters: NotRequired[
        "capo_mgn.types.list_network_migration_execution_request_filters.ListNetworkMigrationExecutionRequestFilters"
    ]
    """<p>Filters to apply when listing executions, such as status or execution ID.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationExecutionsRequest) -> dict:
    out: dict = {}
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "filters" in value:
        import capo_mgn.types.list_network_migration_execution_request_filters

        out["filters"] = (
            capo_mgn.types.list_network_migration_execution_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationExecutionsRequest:
    out: ListNetworkMigrationExecutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        out["network_migration_definition_id"] = ""
    if data.get("filters") is not None:
        import capo_mgn.types.list_network_migration_execution_request_filters

        out["filters"] = (
            capo_mgn.types.list_network_migration_execution_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
