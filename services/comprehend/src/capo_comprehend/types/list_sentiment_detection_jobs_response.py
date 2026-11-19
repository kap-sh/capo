"""Generated from Smithy shape ``com.amazonaws.comprehend#ListSentimentDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.sentiment_detection_job_properties_list
    import capo_comprehend.types.string


class ListSentimentDetectionJobsResponse(TypedDict, closed=True):
    sentiment_detection_job_properties_list: NotRequired[
        "capo_comprehend.types.sentiment_detection_job_properties_list.SentimentDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["capo_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSentimentDetectionJobsResponse) -> dict:
    out: dict = {}
    if "sentiment_detection_job_properties_list" in value:
        import capo_comprehend.types.sentiment_detection_job_properties_list

        out["SentimentDetectionJobPropertiesList"] = (
            capo_comprehend.types.sentiment_detection_job_properties_list.serialize_aws_json_1_1(
                value["sentiment_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSentimentDetectionJobsResponse:
    out: ListSentimentDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SentimentDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.sentiment_detection_job_properties_list

        out["sentiment_detection_job_properties_list"] = (
            capo_comprehend.types.sentiment_detection_job_properties_list.deserialize_aws_json_1_1(
                data["SentimentDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListSentimentDetectionJobsResponse) -> dict:
    out: dict = {}
    if "sentiment_detection_job_properties_list" in value:
        import capo_comprehend.types.sentiment_detection_job_properties_list

        out["SentimentDetectionJobPropertiesList"] = (
            capo_comprehend.types.sentiment_detection_job_properties_list.serialize_cbor(
                value["sentiment_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListSentimentDetectionJobsResponse:
    out: ListSentimentDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SentimentDetectionJobPropertiesList") is not None:
        import capo_comprehend.types.sentiment_detection_job_properties_list

        out["sentiment_detection_job_properties_list"] = (
            capo_comprehend.types.sentiment_detection_job_properties_list.deserialize_cbor(
                data["SentimentDetectionJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
