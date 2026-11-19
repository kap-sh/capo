"""Generated from Smithy shape ``com.amazonaws.comprehend#ListTargetedSentimentDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.string
    import capo_comprehend.types.targeted_sentiment_detection_job_properties_list


class ListTargetedSentimentDetectionJobsResponse(TypedDict, closed=True):
    targeted_sentiment_detection_job_properties_list: NotRequired[
        "capo_comprehend.types.targeted_sentiment_detection_job_properties_list.TargetedSentimentDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTargetedSentimentDetectionJobsResponse) -> dict:
    out: dict = {}
    if "targeted_sentiment_detection_job_properties_list" in value:
        import capo_comprehend.types.targeted_sentiment_detection_job_properties_list

        out["TargetedSentimentDetectionJobPropertiesList"] = (
            capo_comprehend.types.targeted_sentiment_detection_job_properties_list.serialize_aws_json_1_1(
                value["targeted_sentiment_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTargetedSentimentDetectionJobsResponse:
    out: ListTargetedSentimentDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TargetedSentimentDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.targeted_sentiment_detection_job_properties_list

        out["targeted_sentiment_detection_job_properties_list"] = (
            capo_comprehend.types.targeted_sentiment_detection_job_properties_list.deserialize_aws_json_1_1(
                data["TargetedSentimentDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListTargetedSentimentDetectionJobsResponse) -> dict:
    out: dict = {}
    if "targeted_sentiment_detection_job_properties_list" in value:
        import capo_comprehend.types.targeted_sentiment_detection_job_properties_list

        out["TargetedSentimentDetectionJobPropertiesList"] = (
            capo_comprehend.types.targeted_sentiment_detection_job_properties_list.serialize_cbor(
                value["targeted_sentiment_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListTargetedSentimentDetectionJobsResponse:
    out: ListTargetedSentimentDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("TargetedSentimentDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.targeted_sentiment_detection_job_properties_list

        out["targeted_sentiment_detection_job_properties_list"] = (
            capo_comprehend.types.targeted_sentiment_detection_job_properties_list.deserialize_cbor(
                data["TargetedSentimentDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
