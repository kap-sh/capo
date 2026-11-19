"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ComprehendMedicalAsyncJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehendmedical.types.comprehend_medical_async_job_properties

ComprehendMedicalAsyncJobPropertiesList: TypeAlias = list[
    "capo_comprehendmedical.types.comprehend_medical_async_job_properties.ComprehendMedicalAsyncJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComprehendMedicalAsyncJobPropertiesList) -> list:
    import capo_comprehendmedical.types.comprehend_medical_async_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.comprehend_medical_async_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ComprehendMedicalAsyncJobPropertiesList:
    import capo_comprehendmedical.types.comprehend_medical_async_job_properties

    out: ComprehendMedicalAsyncJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.comprehend_medical_async_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ComprehendMedicalAsyncJobPropertiesList) -> list:
    import capo_comprehendmedical.types.comprehend_medical_async_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehendmedical.types.comprehend_medical_async_job_properties.serialize_cbor(
                item
            )
        )
    return out


def deserialize_cbor(data: list) -> ComprehendMedicalAsyncJobPropertiesList:
    import capo_comprehendmedical.types.comprehend_medical_async_job_properties

    out: ComprehendMedicalAsyncJobPropertiesList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_comprehendmedical.types.comprehend_medical_async_job_properties.deserialize_cbor(
                item
            )
        )
    return out
