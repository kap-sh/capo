"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeTargetedSentimentDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.targeted_sentiment_detection_job_properties


class DescribeTargetedSentimentDetectionJobResponse(TypedDict, closed=True):
    targeted_sentiment_detection_job_properties: NotRequired[
        "capo_comprehend.types.targeted_sentiment_detection_job_properties.TargetedSentimentDetectionJobProperties"
    ]
    """<p>An object that contains the properties associated with a targeted sentiment detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeTargetedSentimentDetectionJobResponse,
) -> dict:
    out: dict = {}
    if "targeted_sentiment_detection_job_properties" in value:
        import capo_comprehend.types.targeted_sentiment_detection_job_properties

        out["TargetedSentimentDetectionJobProperties"] = (
            capo_comprehend.types.targeted_sentiment_detection_job_properties.serialize_aws_json_1_1(
                value["targeted_sentiment_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTargetedSentimentDetectionJobResponse:
    out: DescribeTargetedSentimentDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TargetedSentimentDetectionJobProperties") is not None:
        import capo_comprehend.types.targeted_sentiment_detection_job_properties

        out["targeted_sentiment_detection_job_properties"] = (
            capo_comprehend.types.targeted_sentiment_detection_job_properties.deserialize_aws_json_1_1(
                data["TargetedSentimentDetectionJobProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTargetedSentimentDetectionJobResponse) -> dict:
    out: dict = {}
    if "targeted_sentiment_detection_job_properties" in value:
        import capo_comprehend.types.targeted_sentiment_detection_job_properties

        out["TargetedSentimentDetectionJobProperties"] = (
            capo_comprehend.types.targeted_sentiment_detection_job_properties.serialize_cbor(
                value["targeted_sentiment_detection_job_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeTargetedSentimentDetectionJobResponse:
    out: DescribeTargetedSentimentDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TargetedSentimentDetectionJobProperties") is not None:
        import capo_comprehend.types.targeted_sentiment_detection_job_properties

        out["targeted_sentiment_detection_job_properties"] = (
            capo_comprehend.types.targeted_sentiment_detection_job_properties.deserialize_cbor(
                data["TargetedSentimentDetectionJobProperties"]
            )
        )
    return out
