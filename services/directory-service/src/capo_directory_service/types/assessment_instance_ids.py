"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentInstanceIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_instance_id

AssessmentInstanceIds: TypeAlias = list[
    "capo_directory_service.types.assessment_instance_id.AssessmentInstanceId"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentInstanceIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AssessmentInstanceIds:
    return [item for item in data if item is not None]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssessmentInstanceIds) -> list:
    return list(value)


def deserialize_cbor(data: list) -> AssessmentInstanceIds:
    return [item for item in data if item is not None]
