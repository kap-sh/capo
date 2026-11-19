"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_event_max_results
    import capo_sagemaker.types.cluster_event_resource_type
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_name_or_arn
    import capo_sagemaker.types.cluster_node_id
    import capo_sagemaker.types.cluster_operation_id
    import capo_sagemaker.types.event_sort_by
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListClusterEventsRequest(TypedDict, closed=True):
    cluster_name: NotRequired[
        "capo_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the HyperPod cluster for which to list events.</p>"""
    instance_group_name: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>The name of the instance group to filter events. If specified, only events related to this instance group are returned.</p>"""
    node_id: NotRequired["capo_sagemaker.types.cluster_node_id.ClusterNodeId"]
    """<p>The EC2 instance ID to filter events. If specified, only events related to this instance are returned.</p>"""
    event_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The start of the time range for filtering events. Only events that occurred after this time are included in the results.</p>"""
    event_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The end of the time range for filtering events. Only events that occurred before this time are included in the results.</p>"""
    sort_by: NotRequired["capo_sagemaker.types.event_sort_by.EventSortBy"]
    """<p>The field to use for sorting the event list. Currently, the only supported value is <code>EventTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The order in which to sort the results. Valid values are <code>Ascending</code> or <code>Descending</code> (the default is <code>Descending</code>).</p>"""
    resource_type: NotRequired[
        "capo_sagemaker.types.cluster_event_resource_type.ClusterEventResourceType"
    ]
    """<p>The type of resource for which to filter events. Valid values are <code>Cluster</code>, <code>InstanceGroup</code>, or <code>Instance</code>.</p>"""
    operation_id: NotRequired[
        "capo_sagemaker.types.cluster_operation_id.ClusterOperationId"
    ]
    """<p>The unique identifier (UUID) of a cluster operation for which to filter events. If specified, only events associated with this operation are returned. This ID can be obtained from the <code>ListClusterOperations</code> operation.</p>"""
    max_results: NotRequired[
        "capo_sagemaker.types.cluster_event_max_results.ClusterEventMaxResults"
    ]
    """<p>The maximum number of events to return in the response. Valid range is 1 to 100.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. This token is obtained from the output of a previous <code>ListClusterEvents</code> call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterEventsRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "instance_group_name" in value:
        out["InstanceGroupName"] = value["instance_group_name"]
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "event_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["EventTimeAfter"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["event_time_after"]
        )
    if "event_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["EventTimeBefore"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["event_time_before"]
        )
    if "sort_by" in value:
        import capo_sagemaker.types.event_sort_by

        out["SortBy"] = capo_sagemaker.types.event_sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "resource_type" in value:
        import capo_sagemaker.types.cluster_event_resource_type

        out["ResourceType"] = (
            capo_sagemaker.types.cluster_event_resource_type.serialize_aws_json_1_1(
                value["resource_type"]
            )
        )
    if "operation_id" in value:
        out["OperationId"] = value["operation_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterEventsRequest:
    out: ListClusterEventsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("InstanceGroupName") is not None:
        out["instance_group_name"] = data["InstanceGroupName"]
    if data.get("NodeId") is not None:
        out["node_id"] = data["NodeId"]
    if data.get("EventTimeAfter") is not None:
        import capo_sagemaker.types.timestamp

        out["event_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["EventTimeAfter"]
            )
        )
    if data.get("EventTimeBefore") is not None:
        import capo_sagemaker.types.timestamp

        out["event_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["EventTimeBefore"]
            )
        )
    if data.get("SortBy") is not None:
        import capo_sagemaker.types.event_sort_by

        out["sort_by"] = capo_sagemaker.types.event_sort_by.deserialize_aws_json_1_1(
            data["SortBy"]
        )
    if data.get("SortOrder") is not None:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("ResourceType") is not None:
        import capo_sagemaker.types.cluster_event_resource_type

        out["resource_type"] = (
            capo_sagemaker.types.cluster_event_resource_type.deserialize_aws_json_1_1(
                data["ResourceType"]
            )
        )
    if data.get("OperationId") is not None:
        out["operation_id"] = data["OperationId"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
