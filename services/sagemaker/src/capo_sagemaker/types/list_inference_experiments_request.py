"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListInferenceExperimentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_experiment_status
    import capo_sagemaker.types.inference_experiment_type
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.name_contains
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.sort_inference_experiments_by
    import capo_sagemaker.types.sort_order
    import capo_sagemaker.types.timestamp


class ListInferenceExperimentsRequest(TypedDict, closed=True):
    name_contains: NotRequired["capo_sagemaker.types.name_contains.NameContains"]
    """<p>Selects inference experiments whose names contain this name.</p>"""
    type: NotRequired[
        "capo_sagemaker.types.inference_experiment_type.InferenceExperimentType"
    ]
    """<p> Selects inference experiments of this type. For the possible types of inference experiments, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateInferenceExperiment.html">CreateInferenceExperiment</a>. </p>"""
    status_equals: NotRequired[
        "capo_sagemaker.types.inference_experiment_status.InferenceExperimentStatus"
    ]
    """<p> Selects inference experiments which are in this status. For the possible statuses, see <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeInferenceExperiment.html">DescribeInferenceExperiment</a>. </p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects inference experiments which were created after this timestamp.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects inference experiments which were created before this timestamp.</p>"""
    last_modified_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects inference experiments which were last modified after this timestamp.</p>"""
    last_modified_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Selects inference experiments which were last modified before this timestamp.</p>"""
    sort_by: NotRequired[
        "capo_sagemaker.types.sort_inference_experiments_by.SortInferenceExperimentsBy"
    ]
    """<p>The column by which to sort the listed inference experiments.</p>"""
    sort_order: NotRequired["capo_sagemaker.types.sort_order.SortOrder"]
    """<p>The direction of sorting (ascending or descending).</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p> The response from the last list when returning a list large enough to need tokening. </p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of results to select.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListInferenceExperimentsRequest) -> dict:
    out: dict = {}
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "type" in value:
        import capo_sagemaker.types.inference_experiment_type

        out["Type"] = (
            capo_sagemaker.types.inference_experiment_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "status_equals" in value:
        import capo_sagemaker.types.inference_experiment_status

        out["StatusEquals"] = (
            capo_sagemaker.types.inference_experiment_status.serialize_aws_json_1_1(
                value["status_equals"]
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
    if "sort_by" in value:
        import capo_sagemaker.types.sort_inference_experiments_by

        out["SortBy"] = (
            capo_sagemaker.types.sort_inference_experiments_by.serialize_aws_json_1_1(
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


def deserialize_aws_json_1_1(data: dict) -> ListInferenceExperimentsRequest:
    out: ListInferenceExperimentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NameContains") is not None:
        out["name_contains"] = data["NameContains"]
    if data.get("Type") is not None:
        import capo_sagemaker.types.inference_experiment_type

        out["type"] = (
            capo_sagemaker.types.inference_experiment_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("StatusEquals") is not None:
        import capo_sagemaker.types.inference_experiment_status

        out["status_equals"] = (
            capo_sagemaker.types.inference_experiment_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
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
    if data.get("SortBy") is not None:
        import capo_sagemaker.types.sort_inference_experiments_by

        out["sort_by"] = (
            capo_sagemaker.types.sort_inference_experiments_by.deserialize_aws_json_1_1(
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
