"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.name_contains
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_by
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_job_status
    import capo_sagemaker.types.training_plan_arn
    import capo_sagemaker.types.warm_pool_resource_status


class ListTrainingJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of the previous <code>ListTrainingJobs</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of training jobs, use the token in the next request. </p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of training jobs to return in the response.</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only training jobs created after the specified time (timestamp).</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only training jobs created before the specified time (timestamp).</p>"""
    last_modified_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only training jobs modified after the specified time (timestamp).</p>"""
    last_modified_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only training jobs modified before the specified time (timestamp).</p>"""
    name_contains: NotRequired["capo_sagemaker.types.name_contains.NameContains"]
    """<p>A string in the training job name. This filter returns only training jobs whose name contains the specified string.</p>"""
    status_equals: NotRequired[
        "capo_sagemaker.types.training_job_status.TrainingJobStatus"
    ]
    """<p>A filter that retrieves only training jobs with a specific status.</p>"""
    sort_by: NotRequired["capo_sagemaker.types.sort_by.SortBy"]
    """<p>The field to sort results by. The default is <code>CreationTime</code>.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The sort order for results. The default is <code>Ascending</code>.</p>"""
    warm_pool_status_equals: NotRequired[
        "capo_sagemaker.types.warm_pool_resource_status.WarmPoolResourceStatus"
    ]
    """<p>A filter that retrieves only training jobs with a specific warm pool status.</p>"""
    training_plan_arn_equals: NotRequired[
        "capo_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the training plan to filter training jobs by. For more information about reserving GPU capacity for your SageMaker training jobs using Amazon SageMaker Training Plan, see <code> <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html">CreateTrainingPlan</a> </code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrainingJobsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
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
    if "last_modified_time_after" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTimeAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_after"]
            )
        )
    if "last_modified_time_before" in value:
        import capo_sagemaker.types.timestamp

        out["LastModifiedTimeBefore"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time_before"]
            )
        )
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "status_equals" in value:
        import capo_sagemaker.types.training_job_status

        out["StatusEquals"] = (
            capo_sagemaker.types.training_job_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    if "sort_by" in value:
        import capo_sagemaker.types.sort_by

        out["SortBy"] = capo_sagemaker.types.sort_by.serialize_aws_json_1_1(
            value["sort_by"]
        )
    if "sort_order" in value:
        import capo_sagemaker.types.sort_order

        out["SortOrder"] = capo_sagemaker.types.sort_order.serialize_aws_json_1_1(
            value["sort_order"]
        )
    if "warm_pool_status_equals" in value:
        import capo_sagemaker.types.warm_pool_resource_status

        out["WarmPoolStatusEquals"] = (
            capo_sagemaker.types.warm_pool_resource_status.serialize_aws_json_1_1(
                value["warm_pool_status_equals"]
            )
        )
    if "training_plan_arn_equals" in value:
        out["TrainingPlanArnEquals"] = value["training_plan_arn_equals"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrainingJobsRequest:
    out: ListTrainingJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
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
    if data.get("LastModifiedTimeAfter") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeAfter"]
            )
        )
    if data.get("LastModifiedTimeBefore") is not None:
        import capo_sagemaker.types.timestamp

        out["last_modified_time_before"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTimeBefore"]
            )
        )
    if data.get("NameContains") is not None:
        out["name_contains"] = data["NameContains"]
    if data.get("StatusEquals") is not None:
        import capo_sagemaker.types.training_job_status

        out["status_equals"] = (
            capo_sagemaker.types.training_job_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    if data.get("SortBy") is not None:
        import capo_sagemaker.types.sort_by

        out["sort_by"] = capo_sagemaker.types.sort_by.deserialize_aws_json_1_1(
            data["SortBy"]
        )
    if data.get("SortOrder") is not None:
        import capo_sagemaker.types.sort_order

        out["sort_order"] = capo_sagemaker.types.sort_order.deserialize_aws_json_1_1(
            data["SortOrder"]
        )
    if data.get("WarmPoolStatusEquals") is not None:
        import capo_sagemaker.types.warm_pool_resource_status

        out["warm_pool_status_equals"] = (
            capo_sagemaker.types.warm_pool_resource_status.deserialize_aws_json_1_1(
                data["WarmPoolStatusEquals"]
            )
        )
    if data.get("TrainingPlanArnEquals") is not None:
        out["training_plan_arn_equals"] = data["TrainingPlanArnEquals"]
    return out
