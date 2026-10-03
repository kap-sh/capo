"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClusterSchedulerConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_arn
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.scheduler_resource_status
    import capo_sagemaker.types.sort_cluster_scheduler_config_by
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListClusterSchedulerConfigsRequest(TypedDict, closed=True):
    created_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter for after this creation time. The input for this parameter is a Unix timestamp. To convert a date and time into a Unix timestamp, see <a href="https://www.epochconverter.com/">EpochConverter</a>.</p>"""
    created_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Filter for before this creation time. The input for this parameter is a Unix timestamp. To convert a date and time into a Unix timestamp, see <a href="https://www.epochconverter.com/">EpochConverter</a>.</p>"""
    name_contains: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>Filter for name containing this string.</p>"""
    cluster_arn: NotRequired["capo_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>Filter for ARN of the cluster.</p>"""
    status: NotRequired[
        "capo_sagemaker.types.scheduler_resource_status.SchedulerResourceStatus"
    ]
    """<p>Filter for status.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.sort_cluster_scheduler_config_by.SortClusterSchedulerConfigBy"
    ]
    """<p>Filter for sorting the list by a given value. For example, sort by name, creation time, or status.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The order of the list. By default, listed in <code>Descending</code> order according to by <code>SortBy</code>. To change the list order, you can specify <code>SortOrder</code> to be <code>Ascending</code>.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of cluster policies to list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClusterSchedulerConfigsRequest) -> dict:
    out: dict = {}
    if "created_after" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedAfter"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_sagemaker.types.timestamp

        out["CreatedBefore"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["created_before"]
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "status" in value:
        import capo_sagemaker.types.scheduler_resource_status

        out["Status"] = (
            capo_sagemaker.types.scheduler_resource_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "sort_by" in value:
        import capo_sagemaker.types.sort_cluster_scheduler_config_by

        out["SortBy"] = (
            capo_sagemaker.types.sort_cluster_scheduler_config_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClusterSchedulerConfigsRequest:
    out: ListClusterSchedulerConfigsRequest = {}  # type: ignore[typeddict-item]
    if data.get("CreatedAfter") is not None:
        import capo_sagemaker.types.timestamp

        out["created_after"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAfter"]
        )
    if data.get("CreatedBefore") is not None:
        import capo_sagemaker.types.timestamp

        out["created_before"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedBefore"]
        )
    if data.get("NameContains") is not None:
        out["name_contains"] = data["NameContains"]
    if data.get("ClusterArn") is not None:
        out["cluster_arn"] = data["ClusterArn"]
    if data.get("Status") is not None:
        import capo_sagemaker.types.scheduler_resource_status

        out["status"] = (
            capo_sagemaker.types.scheduler_resource_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("SortBy") is not None:
        import capo_sagemaker.types.sort_cluster_scheduler_config_by

        out["sort_by"] = (
            capo_sagemaker.types.sort_cluster_scheduler_config_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
