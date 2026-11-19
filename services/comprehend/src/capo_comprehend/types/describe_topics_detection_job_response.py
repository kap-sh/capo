"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeTopicsDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.topics_detection_job_properties


class DescribeTopicsDetectionJobResponse(TypedDict, closed=True):
    topics_detection_job_properties: NotRequired[
        "capo_comprehend.types.topics_detection_job_properties.TopicsDetectionJobProperties"
    ]
    """<p>The list of properties for the requested job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeTopicsDetectionJobResponse) -> dict:
    out: dict = {}
    if "topics_detection_job_properties" in value:
        import capo_comprehend.types.topics_detection_job_properties

        out["TopicsDetectionJobProperties"] = (
            capo_comprehend.types.topics_detection_job_properties.serialize_aws_json_1_1(
                value["topics_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeTopicsDetectionJobResponse:
    out: DescribeTopicsDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TopicsDetectionJobProperties") is not None:
        import capo_comprehend.types.topics_detection_job_properties

        out["topics_detection_job_properties"] = (
            capo_comprehend.types.topics_detection_job_properties.deserialize_aws_json_1_1(
                data["TopicsDetectionJobProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeTopicsDetectionJobResponse) -> dict:
    out: dict = {}
    if "topics_detection_job_properties" in value:
        import capo_comprehend.types.topics_detection_job_properties

        out["TopicsDetectionJobProperties"] = (
            capo_comprehend.types.topics_detection_job_properties.serialize_cbor(
                value["topics_detection_job_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeTopicsDetectionJobResponse:
    out: DescribeTopicsDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("TopicsDetectionJobProperties") is not None:
        import capo_comprehend.types.topics_detection_job_properties

        out["topics_detection_job_properties"] = (
            capo_comprehend.types.topics_detection_job_properties.deserialize_cbor(
                data["TopicsDetectionJobProperties"]
            )
        )
    return out
