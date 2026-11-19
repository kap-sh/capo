"""Generated from Smithy shape ``com.amazonaws.comprehend#DominantLanguageDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.dominant_language_detection_job_properties

DominantLanguageDetectionJobPropertiesList: TypeAlias = list[
    "capo_comprehend.types.dominant_language_detection_job_properties.DominantLanguageDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DominantLanguageDetectionJobPropertiesList) -> list:
    import capo_comprehend.types.dominant_language_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.dominant_language_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DominantLanguageDetectionJobPropertiesList:
    import capo_comprehend.types.dominant_language_detection_job_properties

    out: DominantLanguageDetectionJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.dominant_language_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DominantLanguageDetectionJobPropertiesList) -> list:
    import capo_comprehend.types.dominant_language_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.dominant_language_detection_job_properties.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> DominantLanguageDetectionJobPropertiesList:
    import capo_comprehend.types.dominant_language_detection_job_properties

    out: DominantLanguageDetectionJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehend.types.dominant_language_detection_job_properties.deserialize_cbor(
                item
            )
        )
    return out
