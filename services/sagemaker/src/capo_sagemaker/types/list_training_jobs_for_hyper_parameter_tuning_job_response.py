"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingJobsForHyperParameterTuningJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_training_job_summaries
    import capo_sagemaker.types.next_token


class ListTrainingJobsForHyperParameterTuningJobResponse(TypedDict, closed=True):
    training_job_summaries: NotRequired[
        "capo_sagemaker.types.hyper_parameter_training_job_summaries.HyperParameterTrainingJobSummaries"
    ]
    """<p>A list of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobSummary.html">TrainingJobSummary</a> objects that describe the training jobs that the <code>ListTrainingJobsForHyperParameterTuningJob</code> request returned.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of this <code>ListTrainingJobsForHyperParameterTuningJob</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of training jobs, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListTrainingJobsForHyperParameterTuningJobResponse,
) -> dict:
    out: dict = {}
    if "training_job_summaries" in value:
        import capo_sagemaker.types.hyper_parameter_training_job_summaries

        out["TrainingJobSummaries"] = (
            capo_sagemaker.types.hyper_parameter_training_job_summaries.serialize_aws_json_1_1(
                value["training_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListTrainingJobsForHyperParameterTuningJobResponse:
    out: ListTrainingJobsForHyperParameterTuningJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TrainingJobSummaries") is not None:
        import capo_sagemaker.types.hyper_parameter_training_job_summaries

        out["training_job_summaries"] = (
            capo_sagemaker.types.hyper_parameter_training_job_summaries.deserialize_aws_json_1_1(
                data["TrainingJobSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
