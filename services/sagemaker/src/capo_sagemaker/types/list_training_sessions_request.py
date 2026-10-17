"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListTrainingSessionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.max_results
    import capo_sagemaker.types.name_contains
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.timestamp
    import capo_sagemaker.types.training_session_status


class ListTrainingSessionsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>If the response was truncated, use the token returned in the previous response to retrieve the next page of results.</p>"""
    max_results: NotRequired["capo_sagemaker.types.max_results.MaxResults"]
    """<p>The maximum number of training sessions to return in the response.</p>"""
    creation_time_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only training sessions created after the specified time.</p>"""
    creation_time_before: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>A filter that returns only training sessions created before the specified time.</p>"""
    name_contains: NotRequired["capo_sagemaker.types.name_contains.NameContains"]
    """<p>A string in the training session name to filter results. Only sessions whose name contains the specified string are returned.</p>"""
    status_equals: NotRequired[
        "capo_sagemaker.types.training_session_status.TrainingSessionStatus"
    ]
    """<p>A filter that returns only training sessions with the specified status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTrainingSessionsRequest) -> dict:
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
    if "name_contains" in value:
        out["NameContains"] = value["name_contains"]
    if "status_equals" in value:
        import capo_sagemaker.types.training_session_status

        out["StatusEquals"] = (
            capo_sagemaker.types.training_session_status.serialize_aws_json_1_1(
                value["status_equals"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTrainingSessionsRequest:
    out: ListTrainingSessionsRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("NameContains") is not None:
        out["name_contains"] = data["NameContains"]
    if data.get("StatusEquals") is not None:
        import capo_sagemaker.types.training_session_status

        out["status_equals"] = (
            capo_sagemaker.types.training_session_status.deserialize_aws_json_1_1(
                data["StatusEquals"]
            )
        )
    return out
