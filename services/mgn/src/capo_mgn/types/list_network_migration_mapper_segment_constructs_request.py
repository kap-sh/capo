"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationMapperSegmentConstructsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.list_network_migration_mapper_segment_constructs_filters
    import capo_mgn.types.max_results_type
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.pagination_token
    import capo_mgn.types.segment_id


class ListNetworkMigrationMapperSegmentConstructsRequest(TypedDict, closed=True):
    network_migration_execution_id: (
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    )
    """<p>The unique identifier of the network migration execution.</p>"""
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    segment_id: "capo_mgn.types.segment_id.SegmentID"
    """<p>The unique identifier of the segment to list constructs for.</p>"""
    filters: NotRequired[
        "capo_mgn.types.list_network_migration_mapper_segment_constructs_filters.ListNetworkMigrationMapperSegmentConstructsFilters"
    ]
    """<p>Filters to apply when listing constructs, such as construct type or ID.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationMapperSegmentConstructsRequest) -> dict:
    out: dict = {}
    out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    out["segmentID"] = value["segment_id"]
    if "filters" in value:
        import capo_mgn.types.list_network_migration_mapper_segment_constructs_filters

        out["filters"] = (
            capo_mgn.types.list_network_migration_mapper_segment_constructs_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationMapperSegmentConstructsRequest:
    out: ListNetworkMigrationMapperSegmentConstructsRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    else:
        out["network_migration_execution_id"] = ""
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        out["network_migration_definition_id"] = ""
    if data.get("segmentID") is not None:
        out["segment_id"] = data["segmentID"]
    else:
        out["segment_id"] = ""
    if data.get("filters") is not None:
        import capo_mgn.types.list_network_migration_mapper_segment_constructs_filters

        out["filters"] = (
            capo_mgn.types.list_network_migration_mapper_segment_constructs_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
