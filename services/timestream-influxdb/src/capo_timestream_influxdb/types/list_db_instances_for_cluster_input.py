"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#ListDbInstancesForClusterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.db_cluster_id
    import capo_timestream_influxdb.types.max_results
    import capo_timestream_influxdb.types.next_token


class ListDbInstancesForClusterInput(TypedDict, closed=True):
    db_cluster_id: "capo_timestream_influxdb.types.db_cluster_id.DbClusterId"
    """<p>Service-generated unique identifier of the DB cluster.</p>"""
    next_token: NotRequired["capo_timestream_influxdb.types.next_token.NextToken"]
    """<p>The pagination token. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>"""
    max_results: NotRequired["capo_timestream_influxdb.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the output. If the total number of items available is more than the value specified, a nextToken is provided in the output. To resume pagination, provide the nextToken value as an argument of a subsequent API invocation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbInstancesForClusterInput) -> dict:
    out: dict = {}
    out["dbClusterId"] = value["db_cluster_id"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbInstancesForClusterInput:
    out: ListDbInstancesForClusterInput = {}  # type: ignore[typeddict-item]
    if data.get("dbClusterId") is not None:
        out["db_cluster_id"] = data["dbClusterId"]
    else:
        out["db_cluster_id"] = ""
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    return out
