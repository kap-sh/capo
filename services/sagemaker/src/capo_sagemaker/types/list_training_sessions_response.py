"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingSessionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.training_session_summaries


class ListTrainingSessionsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, this token retrieves the next set of results.</p>"""
    training_session_summaries: NotRequired[
        "capo_sagemaker.types.training_session_summaries.TrainingSessionSummaries"
    ]
    """<p>An array of <code>TrainingSessionSummary</code> objects that provide summary information about the training sessions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrainingSessionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "training_session_summaries" in value:
        import capo_sagemaker.types.training_session_summaries

        out["TrainingSessionSummaries"] = (
            capo_sagemaker.types.training_session_summaries.serialize_aws_json_1_1(
                value["training_session_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrainingSessionsResponse:
    out: ListTrainingSessionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("TrainingSessionSummaries") is not None:
        import capo_sagemaker.types.training_session_summaries

        out["training_session_summaries"] = (
            capo_sagemaker.types.training_session_summaries.deserialize_aws_json_1_1(
                data["TrainingSessionSummaries"]
            )
        )
    return out
