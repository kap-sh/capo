"""Generated from Smithy shape ``com.amazonaws.directoryservice#AssessmentValidations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.assessment_validation

AssessmentValidations: TypeAlias = list[
    "capo_directory_service.types.assessment_validation.AssessmentValidation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssessmentValidations) -> list:
    import capo_directory_service.types.assessment_validation

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.assessment_validation.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AssessmentValidations:
    import capo_directory_service.types.assessment_validation

    out: AssessmentValidations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.assessment_validation.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssessmentValidations) -> list:
    import capo_directory_service.types.assessment_validation

    out: list = []
    for item in value:
        out.append(
            capo_directory_service.types.assessment_validation.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> AssessmentValidations:
    import capo_directory_service.types.assessment_validation

    out: AssessmentValidations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_directory_service.types.assessment_validation.deserialize_cbor(item)
        )
    return out
