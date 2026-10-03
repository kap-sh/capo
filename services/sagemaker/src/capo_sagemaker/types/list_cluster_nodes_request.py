"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterNodesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_instance_group_name
    import capo_sagemaker.types.cluster_name_or_arn
    import capo_sagemaker.types.cluster_sort_by
    import capo_sagemaker.types.include_node_logical_ids_boolean
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListClusterNodesRequest(TypedDict, closed=True):
    cluster_name: NotRequired[
        "capo_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>The string name or the Amazon Resource Name (ARN) of the SageMaker HyperPod cluster in which you want to retrieve the list of nodes.</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns nodes in a SageMaker HyperPod cluster created after the specified time. Timestamps are formatted according to the ISO 8601 standard. </p> <p>Acceptable formats include:</p> <ul> <li> <p> <code>YYYY-MM-DDThh:mm:ss.sssTZD</code> (UTC), for example, <code>2014-10-01T20:30:00.000Z</code> </p> </li> <li> <p> <code>YYYY-MM-DDThh:mm:ss.sssTZD</code> (with offset), for example, <code>2014-10-01T12:30:00.000-08:00</code> </p> </li> <li> <p> <code>YYYY-MM-DD</code>, for example, <code>2014-10-01</code> </p> </li> <li> <p>Unix time in seconds, for example, <code>1412195400</code>. This is also referred to as Unix Epoch time and represents the number of seconds since midnight, January 1, 1970 UTC.</p> </li> </ul> <p>For more information about the timestamp format, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp">Timestamp</a> in the <i>Amazon Web Services Command Line Interface User Guide</i>.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns nodes in a SageMaker HyperPod cluster created before the specified time. The acceptable formats are the same as the timestamp formats for <code>CreationTimeAfter</code>. For more information about the timestamp format, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp">Timestamp</a> in the <i>Amazon Web Services Command Line Interface User Guide</i>.</p>"""
    instance_group_name_contains: NotRequired[
        "capo_sagemaker.types.cluster_instance_group_name.ClusterInstanceGroupName"
    ]
    """<p>A filter that returns the instance groups whose name contain a specified string.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of nodes to return in the response.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListClusterNodes</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of cluster nodes, use the token in the next request.</p>"""
    sort_by: NotRequired["capo_sagemaker.types.cluster_sort_by.ClusterSortBy"]
    """<p>The field by which to sort results. The default value is <code>CREATION_TIME</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default value is <code>Ascending</code>.</p>"""
    include_node_logical_ids: NotRequired[
        "capo_sagemaker.types.include_node_logical_ids_boolean.IncludeNodeLogicalIdsBoolean"
    ]
    """<p>Specifies whether to include nodes that are still being provisioned in the response. When set to true, the response includes all nodes regardless of their provisioning status. When set to <code>False</code> (default), only nodes with assigned <code>InstanceIds</code> are returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterNodesRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "creation_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_after"]
            )
        )
    if "creation_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["creation_time_before"]
            )
        )
    if "instance_group_name_contains" in value:
        out["InstanceGroupNameContains"] = value["instance_group_name_contains"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import capo_sagemaker.types.cluster_sort_by

        out["SortBy"] = capo_sagemaker.types.cluster_sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "include_node_logical_ids" in value:
        out["IncludeNodeLogicalIds"] = value["include_node_logical_ids"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterNodesRequest:
    out: ListClusterNodesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("CreationTimeAfter") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeAfter"]
            )
        )
    if data.get("CreationTimeBefore") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTimeBefore"]
            )
        )
    if data.get("InstanceGroupNameContains") is not None:
        out["instance_group_name_contains"] = data["InstanceGroupNameContains"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SortBy") is not None:
        import capo_sagemaker.types.cluster_sort_by

        out["sort_by"] = capo_sagemaker.types.cluster_sort_by.deserialize_aws_json_1_1(
            data["SortBy"]
        )
    if data.get("SortOrder") is not None:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("IncludeNodeLogicalIds") is not None:
        out["include_node_logical_ids"] = data["IncludeNodeLogicalIds"]
    return out
