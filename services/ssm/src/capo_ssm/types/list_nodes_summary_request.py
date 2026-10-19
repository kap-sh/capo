"""Generated from Smithy shape ``com.amazonaws.ssm#ListNodesSummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.max_results
    import capo_ssm.types.next_token
    import capo_ssm.types.node_aggregator_list
    import capo_ssm.types.node_filter_list
    import capo_ssm.types.resource_data_sync_name


class ListNodesSummaryRequest(TypedDict, closed=True):
    sync_name: NotRequired[
        "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
    ]
    """<p>The name of the Amazon Web Services managed resource data sync to retrieve information about.</p> <p>For cross-account/cross-Region configurations, this parameter is required, and the name of the supported resource data sync is <code>AWS-QuickSetup-ManagedNode</code>.</p> <p>For single account/single-Region configurations, the parameter is not required.</p>"""
    filters: NotRequired["capo_ssm.types.node_filter_list.NodeFilterList"]
    """<p>One or more filters. Use a filter to generate a summary that matches your specified filter criteria.</p>"""
    aggregators: "capo_ssm.types.node_aggregator_list.NodeAggregatorList"
    """<p>Specify one or more aggregators to return a count of managed nodes that match that expression. For example, a count of managed nodes by operating system.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.) The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""
    max_results: NotRequired["capo_ssm.types.max_results.MaxResults"]
    """<p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNodesSummaryRequest) -> dict:
    out: dict = {}
    if "sync_name" in value:
        out["SyncName"] = value["sync_name"]
    if "filters" in value:
        import capo_ssm.types.node_filter_list

        out["Filters"] = capo_ssm.types.node_filter_list.serialize_aws_json_1_1(
            value["filters"]
        )
    import capo_ssm.types.node_aggregator_list

    out["Aggregators"] = capo_ssm.types.node_aggregator_list.serialize_aws_json_1_1(
        value["aggregators"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNodesSummaryRequest:
    out: ListNodesSummaryRequest = {}  # type: ignore[typeddict-item]
    if data.get("SyncName") is not None:
        out["sync_name"] = data["SyncName"]
    if data.get("Filters") is not None:
        import capo_ssm.types.node_filter_list

        out["filters"] = capo_ssm.types.node_filter_list.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if data.get("Aggregators") is not None:
        import capo_ssm.types.node_aggregator_list

        out["aggregators"] = (
            capo_ssm.types.node_aggregator_list.deserialize_aws_json_1_1(
                data["Aggregators"]
            )
        )
    else:
        out["aggregators"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
