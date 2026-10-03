"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListCompilationJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.compilation_job_summaries
    import capo_sagemaker.types.next_token


class ListCompilationJobsResponse(TypedDict, closed=True):
    compilation_job_summaries: NotRequired[
        "capo_sagemaker.types.compilation_job_summaries.CompilationJobSummaries"
    ]
    """<p>An array of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CompilationJobSummary.html">CompilationJobSummary</a> objects, each describing a model compilation job. </p>"""
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, Amazon SageMaker AI returns this <code>NextToken</code>. To retrieve the next set of model compilation jobs, use this token in the next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListCompilationJobsResponse) -> dict:
    out: dict = {}
    if "compilation_job_summaries" in value:
        import capo_sagemaker.types.compilation_job_summaries

        out["CompilationJobSummaries"] = (
            capo_sagemaker.types.compilation_job_summaries.serialize_aws_json_1_1(
                value["compilation_job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListCompilationJobsResponse:
    out: ListCompilationJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("CompilationJobSummaries") is not None:
        import capo_sagemaker.types.compilation_job_summaries

        out["compilation_job_summaries"] = (
            capo_sagemaker.types.compilation_job_summaries.deserialize_aws_json_1_1(
                data["CompilationJobSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
