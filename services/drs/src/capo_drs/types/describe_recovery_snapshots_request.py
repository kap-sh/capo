"""Generated from Smithy shape ``com.amazonaws.drs#DescribeRecoverySnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.describe_recovery_snapshots_request_filters
    import capo_drs.types.pagination_token
    import capo_drs.types.recovery_snapshots_order
    import capo_drs.types.source_server_id
    import capo_drs.types.strictly_positive_integer


class DescribeRecoverySnapshotsRequest(TypedDict, closed=True):
    source_server_id: "capo_drs.types.source_server_id.SourceServerID"
    """<p>Filter Recovery Snapshots by Source Server ID.</p>"""
    filters: NotRequired[
        "capo_drs.types.describe_recovery_snapshots_request_filters.DescribeRecoverySnapshotsRequestFilters"
    ]
    """<p>A set of filters by which to return Recovery Snapshots.</p>"""
    order: NotRequired["capo_drs.types.recovery_snapshots_order.RecoverySnapshotsOrder"]
    """<p>The sorted ordering by which to return Recovery Snapshots.</p>"""
    max_results: NotRequired[
        "capo_drs.types.strictly_positive_integer.StrictlyPositiveInteger"
    ]
    """<p>Maximum number of Recovery Snapshots to retrieve.</p>"""
    next_token: NotRequired["capo_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next Recovery Snapshot to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRecoverySnapshotsRequest) -> dict:
    out: dict = {}
    out["sourceServerID"] = value["source_server_id"]
    if "filters" in value:
        import capo_drs.types.describe_recovery_snapshots_request_filters

        out["filters"] = (
            capo_drs.types.describe_recovery_snapshots_request_filters.serialize_json(
                value["filters"]
            )
        )
    if "order" in value:
        out["order"] = value["order"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> DescribeRecoverySnapshotsRequest:
    out: DescribeRecoverySnapshotsRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceServerID") is not None:
        out["source_server_id"] = data["sourceServerID"]
    else:
        out["source_server_id"] = ""
    if data.get("filters") is not None:
        import capo_drs.types.describe_recovery_snapshots_request_filters

        out["filters"] = (
            capo_drs.types.describe_recovery_snapshots_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if data.get("order") is not None:
        out["order"] = data["order"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
