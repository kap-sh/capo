"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListHyperParameterTuningJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.hyper_parameter_tuning_job_summaries
    import capo_sagemaker.types.next_token


class ListHyperParameterTuningJobsResponse(TypedDict, closed=True):
    hyper_parameter_tuning_job_summaries: NotRequired[
        "capo_sagemaker.types.hyper_parameter_tuning_job_summaries.HyperParameterTuningJobSummaries"
    ]
    """<p>A list of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSummary.html">HyperParameterTuningJobSummary</a> objects that describe the tuning jobs that the <code>ListHyperParameterTuningJobs</code> request returned.</p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the result of this <code>ListHyperParameterTuningJobs</code> request was truncated, the response includes a <code>NextToken</code>. To retrieve the next set of tuning jobs, use the token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHyperParameterTuningJobsResponse) -> dict:
    out: dict = {}
    if "hyper_parameter_tuning_job_summaries" in value:
        import capo_sagemaker.types.hyper_parameter_tuning_job_summaries

        out["HyperParameterTuningJobSummaries"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_summaries.serialize_aws_json_1_1(
                value["hyper_parameter_tuning_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHyperParameterTuningJobsResponse:
    out: ListHyperParameterTuningJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("HyperParameterTuningJobSummaries") is not None:
        import capo_sagemaker.types.hyper_parameter_tuning_job_summaries

        out["hyper_parameter_tuning_job_summaries"] = (
            capo_sagemaker.types.hyper_parameter_tuning_job_summaries.deserialize_aws_json_1_1(
                data["HyperParameterTuningJobSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
