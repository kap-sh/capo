"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeKeyPhrasesDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.key_phrases_detection_job_properties


class DescribeKeyPhrasesDetectionJobResponse(TypedDict, closed=True):
    key_phrases_detection_job_properties: NotRequired[
        "capo_comprehend.types.key_phrases_detection_job_properties.KeyPhrasesDetectionJobProperties"
    ]
    """<p>An object that contains the properties associated with a key phrases detection job. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeKeyPhrasesDetectionJobResponse) -> dict:
    out: dict = {}
    if "key_phrases_detection_job_properties" in value:
        import capo_comprehend.types.key_phrases_detection_job_properties

        out["KeyPhrasesDetectionJobProperties"] = (
            capo_comprehend.types.key_phrases_detection_job_properties.serialize_aws_json_1_1(
                value["key_phrases_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeKeyPhrasesDetectionJobResponse:
    out: DescribeKeyPhrasesDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyPhrasesDetectionJobProperties") is not None:
        import capo_comprehend.types.key_phrases_detection_job_properties

        out["key_phrases_detection_job_properties"] = (
            capo_comprehend.types.key_phrases_detection_job_properties.deserialize_aws_json_1_1(
                data["KeyPhrasesDetectionJobProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeKeyPhrasesDetectionJobResponse) -> dict:
    out: dict = {}
    if "key_phrases_detection_job_properties" in value:
        import capo_comprehend.types.key_phrases_detection_job_properties

        out["KeyPhrasesDetectionJobProperties"] = (
            capo_comprehend.types.key_phrases_detection_job_properties.serialize_cbor(
                value["key_phrases_detection_job_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeKeyPhrasesDetectionJobResponse:
    out: DescribeKeyPhrasesDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("KeyPhrasesDetectionJobProperties") is not None:
        import capo_comprehend.types.key_phrases_detection_job_properties

        out["key_phrases_detection_job_properties"] = (
            capo_comprehend.types.key_phrases_detection_job_properties.deserialize_cbor(
                data["KeyPhrasesDetectionJobProperties"]
            )
        )
    return out
