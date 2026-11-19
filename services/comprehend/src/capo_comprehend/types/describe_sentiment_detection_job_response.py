"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeSentimentDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.sentiment_detection_job_properties


class DescribeSentimentDetectionJobResponse(TypedDict, closed=True):
    sentiment_detection_job_properties: NotRequired[
        "capo_comprehend.types.sentiment_detection_job_properties.SentimentDetectionJobProperties"
    ]
    """<p>An object that contains the properties associated with a sentiment detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSentimentDetectionJobResponse) -> dict:
    out: dict = {}
    if "sentiment_detection_job_properties" in value:
        import capo_comprehend.types.sentiment_detection_job_properties

        out["SentimentDetectionJobProperties"] = (
            capo_comprehend.types.sentiment_detection_job_properties.serialize_aws_json_1_1(
                value["sentiment_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSentimentDetectionJobResponse:
    out: DescribeSentimentDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("SentimentDetectionJobProperties") is not None:
        import capo_comprehend.types.sentiment_detection_job_properties

        out["sentiment_detection_job_properties"] = (
            capo_comprehend.types.sentiment_detection_job_properties.deserialize_aws_json_1_1(
                data["SentimentDetectionJobProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeSentimentDetectionJobResponse) -> dict:
    out: dict = {}
    if "sentiment_detection_job_properties" in value:
        import capo_comprehend.types.sentiment_detection_job_properties

        out["SentimentDetectionJobProperties"] = (
            capo_comprehend.types.sentiment_detection_job_properties.serialize_cbor(
                value["sentiment_detection_job_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeSentimentDetectionJobResponse:
    out: DescribeSentimentDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("SentimentDetectionJobProperties") is not None:
        import capo_comprehend.types.sentiment_detection_job_properties

        out["sentiment_detection_job_properties"] = (
            capo_comprehend.types.sentiment_detection_job_properties.deserialize_cbor(
                data["SentimentDetectionJobProperties"]
            )
        )
    return out
