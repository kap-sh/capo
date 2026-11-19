"""Generated from Smithy shape ``com.amazonaws.mgn#ListNetworkMigrationInsightsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.construct_id
    import capo_mgn.types.insight_producer_id
    import capo_mgn.types.list_network_migration_insights_filters
    import capo_mgn.types.max_results_type
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.pagination_token
    import capo_mgn.types.segment_id


class ListNetworkMigrationInsightsRequest(TypedDict, closed=True):
    network_migration_definition_id: (
        "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID"
    )
    """<p>The unique identifier of the network migration definition.</p>"""
    network_migration_execution_id: NotRequired[
        "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID"
    ]
    """<p>The unique identifier of the network migration execution to narrow the results to.</p>"""
    producer_id: NotRequired["capo_mgn.types.insight_producer_id.InsightProducerID"]
    """<p>The identifier of the job or API request to narrow the results to.</p>"""
    segment_id: NotRequired["capo_mgn.types.segment_id.SegmentID"]
    """<p>The unique identifier of the segment to narrow the results to.</p>"""
    construct_id: NotRequired["capo_mgn.types.construct_id.ConstructID"]
    """<p>The unique identifier of the construct to narrow the results to.</p>"""
    filters: NotRequired[
        "capo_mgn.types.list_network_migration_insights_filters.ListNetworkMigrationInsightsFilters"
    ]
    """<p>Filters to apply when listing insights.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>The token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNetworkMigrationInsightsRequest) -> dict:
    out: dict = {}
    out["networkMigrationDefinitionID"] = value["network_migration_definition_id"]
    if "network_migration_execution_id" in value:
        out["networkMigrationExecutionID"] = value["network_migration_execution_id"]
    if "producer_id" in value:
        out["producerID"] = value["producer_id"]
    if "segment_id" in value:
        out["segmentID"] = value["segment_id"]
    if "construct_id" in value:
        out["constructID"] = value["construct_id"]
    if "filters" in value:
        import capo_mgn.types.list_network_migration_insights_filters

        out["filters"] = (
            capo_mgn.types.list_network_migration_insights_filters.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNetworkMigrationInsightsRequest:
    out: ListNetworkMigrationInsightsRequest = {}  # type: ignore[typeddict-item]
    if data.get("networkMigrationDefinitionID") is not None:
        out["network_migration_definition_id"] = data["networkMigrationDefinitionID"]
    else:
        out["network_migration_definition_id"] = ""
    if data.get("networkMigrationExecutionID") is not None:
        out["network_migration_execution_id"] = data["networkMigrationExecutionID"]
    if data.get("producerID") is not None:
        out["producer_id"] = data["producerID"]
    if data.get("segmentID") is not None:
        out["segment_id"] = data["segmentID"]
    if data.get("constructID") is not None:
        out["construct_id"] = data["constructID"]
    if data.get("filters") is not None:
        import capo_mgn.types.list_network_migration_insights_filters

        out["filters"] = (
            capo_mgn.types.list_network_migration_insights_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
