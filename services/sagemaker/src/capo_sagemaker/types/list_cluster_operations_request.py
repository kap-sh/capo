"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_name_or_arn
    import capo_sagemaker.types.cluster_operation_max_results
    import capo_sagemaker.types.cluster_operation_sort_by
    import capo_sagemaker.types.cluster_operation_status
    import capo_sagemaker.types.cluster_operation_type
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListClusterOperationsRequest(TypedDict, closed=True):
    cluster_name: NotRequired[
        "capo_sagemaker.types.cluster_name_or_arn.ClusterNameOrArn"
    ]
    """<p>The name or Amazon Resource Name (ARN) of the HyperPod cluster for which to list operations.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.cluster_operation_status.ClusterOperationStatus"
    ]
    """<p>The operation status to filter by. If specified, only operations with this status are returned. Valid values are <code>InProgress</code>, <code>Superseded</code>, or <code>Done</code>.</p>"""
    type: NotRequired[
        "capo_sagemaker.types.cluster_operation_type.ClusterOperationType"
    ]
    """<p>The operation type to filter by. If specified, only operations of this type are returned. Valid values are <code>Scaling</code> or <code>DeepHealthCheck</code>.</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The start of the time range for filtering operations. Only operations created after this time are included in the results.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The end of the time range for filtering operations. Only operations created before this time are included in the results.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.cluster_operation_sort_by.ClusterOperationSortBy"
    ]
    """<p>The field to use for sorting the operation list. Currently, the only supported value is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The order in which to sort the results. Valid values are <code>Ascending</code> or <code>Descending</code> (the default is <code>Descending</code>).</p>"""
    max_results: NotRequired[
        "capo_sagemaker.types.cluster_operation_max_results.ClusterOperationMaxResults"
    ]
    """<p>The maximum number of operations to return in the response. Valid range is 1 to 100.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>A token to retrieve the next set of results. This token is obtained from the output of a previous <code>ListClusterOperations</code> call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterOperationsRequest) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "status" in value:
        import capo_sagemaker.types.cluster_operation_status

        out["Status"] = (
            capo_sagemaker.types.cluster_operation_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "type" in value:
        import capo_sagemaker.types.cluster_operation_type

        out["Type"] = (
            capo_sagemaker.types.cluster_operation_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
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
    if "sort_by" in value:
        import capo_sagemaker.types.cluster_operation_sort_by

        out["SortBy"] = (
            capo_sagemaker.types.cluster_operation_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterOperationsRequest:
    out: ListClusterOperationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterName") is not None:
        out["cluster_name"] = data["ClusterName"]
    if data.get("Status") is not None:
        import capo_sagemaker.types.cluster_operation_status

        out["status"] = (
            capo_sagemaker.types.cluster_operation_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Type") is not None:
        import capo_sagemaker.types.cluster_operation_type

        out["type"] = (
            capo_sagemaker.types.cluster_operation_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
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
    if data.get("SortBy") is not None:
        import capo_sagemaker.types.cluster_operation_sort_by

        out["sort_by"] = (
            capo_sagemaker.types.cluster_operation_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
