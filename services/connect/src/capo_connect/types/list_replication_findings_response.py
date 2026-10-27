"""Generated from Smithy shape ``com.amazonaws.connect#ListReplicationFindingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.approximate_drifted_resource_counts
    import capo_connect.types.large_next_token
    import capo_connect.types.replication_findings_list
    import capo_connect.types.resource_replication_statuses


class ListReplicationFindingsResponse(TypedDict, closed=True):
    replication_findings_list: (
        "capo_connect.types.replication_findings_list.ReplicationFindingsList"
    )
    """<p>A list of replication findings for the requested resource type. Only findings that require your action are returned, so this list can be empty even when a drift count is nonzero. Results are paginated.</p>"""
    approximate_drifted_resource_counts: NotRequired[
        "capo_connect.types.approximate_drifted_resource_counts.ApproximateDriftedResourceCounts"
    ]
    """<p>The approximate number of resources of the requested type that are not yet in sync, reported per Amazon Web Services Region. This count is independent of <code>ReplicationFindingsList</code> and can be higher than the number of findings returned. It is eventually consistent and can lag the current state of the instance. Each entry is the <code>ApproximateDriftedResourceCount</code> for one Region; a Region appears only when its count has been computed.</p>"""
    next_token: NotRequired["capo_connect.types.large_next_token.LargeNextToken"]
    """<p>If there are additional results, this is the token for retrieving the next page of <code>ReplicationFindingsList</code>.</p>"""
    resource_replication_statuses: NotRequired[
        "capo_connect.types.resource_replication_statuses.ResourceReplicationStatuses"
    ]
    """<p>The replication status of the requested resource type in each Amazon Web Services Region across which the Connect Customer instance is deployed for Global Resiliency, with one entry per Region. This set describes the overall replication state for the request and is returned in full on every page of results, so it does not change as you paginate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReplicationFindingsResponse) -> dict:
    out: dict = {}
    import capo_connect.types.replication_findings_list

    out["ReplicationFindingsList"] = (
        capo_connect.types.replication_findings_list.serialize_json(
            value["replication_findings_list"]
        )
    )
    if "approximate_drifted_resource_counts" in value:
        import capo_connect.types.approximate_drifted_resource_counts

        out["ApproximateDriftedResourceCounts"] = (
            capo_connect.types.approximate_drifted_resource_counts.serialize_json(
                value["approximate_drifted_resource_counts"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "resource_replication_statuses" in value:
        import capo_connect.types.resource_replication_statuses

        out["ResourceReplicationStatuses"] = (
            capo_connect.types.resource_replication_statuses.serialize_json(
                value["resource_replication_statuses"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListReplicationFindingsResponse:
    out: ListReplicationFindingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ReplicationFindingsList") is not None:
        import capo_connect.types.replication_findings_list

        out["replication_findings_list"] = (
            capo_connect.types.replication_findings_list.deserialize_json(
                data["ReplicationFindingsList"]
            )
        )
    else:
        out["replication_findings_list"] = []
    if data.get("ApproximateDriftedResourceCounts") is not None:
        import capo_connect.types.approximate_drifted_resource_counts

        out["approximate_drifted_resource_counts"] = (
            capo_connect.types.approximate_drifted_resource_counts.deserialize_json(
                data["ApproximateDriftedResourceCounts"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ResourceReplicationStatuses") is not None:
        import capo_connect.types.resource_replication_statuses

        out["resource_replication_statuses"] = (
            capo_connect.types.resource_replication_statuses.deserialize_json(
                data["ResourceReplicationStatuses"]
            )
        )
    return out
