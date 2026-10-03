"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListClustersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.cluster_sort_by
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.name_contains
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_plan_arn


class ListClustersRequest(TypedDict, closed=True):
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Set a start time for the time range during which you want to list SageMaker HyperPod clusters. Timestamps are formatted according to the ISO 8601 standard. </p> <p>Acceptable formats include:</p> <ul> <li> <p> <code>YYYY-MM-DDThh:mm:ss.sssTZD</code> (UTC), for example, <code>2014-10-01T20:30:00.000Z</code> </p> </li> <li> <p> <code>YYYY-MM-DDThh:mm:ss.sssTZD</code> (with offset), for example, <code>2014-10-01T12:30:00.000-08:00</code> </p> </li> <li> <p> <code>YYYY-MM-DD</code>, for example, <code>2014-10-01</code> </p> </li> <li> <p>Unix time in seconds, for example, <code>1412195400</code>. This is also referred to as Unix Epoch time and represents the number of seconds since midnight, January 1, 1970 UTC.</p> </li> </ul> <p>For more information about the timestamp format, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp">Timestamp</a> in the <i>Amazon Web Services Command Line Interface User Guide</i>.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Set an end time for the time range during which you want to list SageMaker HyperPod clusters. A filter that returns nodes in a SageMaker HyperPod cluster created before the specified time. The acceptable formats are the same as the timestamp formats for <code>CreationTimeAfter</code>. For more information about the timestamp format, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-types.html#parameter-type-timestamp">Timestamp</a> in the <i>Amazon Web Services Command Line Interface User Guide</i>.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of clusters to evaluate for the operation (not necessarily the number of matching items). After SageMaker processes the number of clusters up to <code>MaxResults</code>, it stops the operation and returns the matching clusters up to that point. If all the matching clusters are desired, SageMaker will go through all the clusters until <code>NextToken</code> is empty.</p>"""
    name_contains: NotRequired["capo_sagemaker.types.name_contains.NameContains"]
    """<p>Set the maximum number of instances to print in the list.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>Set the next token to retrieve the list of SageMaker HyperPod clusters.</p>"""
    sort_by: NotRequired["capo_sagemaker.types.cluster_sort_by.ClusterSortBy"]
    """<p>The field by which to sort results. The default value is <code>CREATION_TIME</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default value is <code>Ascending</code>.</p>"""
    training_plan_arn: NotRequired[
        "capo_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the training plan to filter clusters by. For more information about reserving GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see <code> <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html">CreateTrainingPlan</a> </code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListClustersRequest) -> dict:
    out: dict = {}
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
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
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
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListClustersRequest:
    out: ListClustersRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NameContains") is not None:
        out["name_contains"] = data["NameContains"]
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
    if data.get("TrainingPlanArn") is not None:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    return out
