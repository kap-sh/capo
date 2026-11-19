"""Generated from Smithy shape ``com.amazonaws.comprehend#TopicsDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.topics_detection_job_properties

TopicsDetectionJobPropertiesList: TypeAlias = list[
    "capo_comprehend.types.topics_detection_job_properties.TopicsDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TopicsDetectionJobPropertiesList) -> list:
    import capo_comprehend.types.topics_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.topics_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TopicsDetectionJobPropertiesList:
    import capo_comprehend.types.topics_detection_job_properties

    out: TopicsDetectionJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.topics_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TopicsDetectionJobPropertiesList) -> list:
    import capo_comprehend.types.topics_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.topics_detection_job_properties.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> TopicsDetectionJobPropertiesList:
    import capo_comprehend.types.topics_detection_job_properties

    out: TopicsDetectionJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.topics_detection_job_properties.deserialize_cbor(item)
        )
    return out
