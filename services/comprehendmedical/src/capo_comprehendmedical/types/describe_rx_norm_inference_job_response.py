"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DescribeRxNormInferenceJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.comprehend_medical_async_job_properties


class DescribeRxNormInferenceJobResponse(TypedDict, closed=True):
    comprehend_medical_async_job_properties: NotRequired[
        "capo_comprehendmedical.types.comprehend_medical_async_job_properties.ComprehendMedicalAsyncJobProperties"
    ]
    """<p>An object that contains the properties associated with a detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeRxNormInferenceJobResponse) -> dict:
    out: dict = {}
    if "comprehend_medical_async_job_properties" in value:
        import capo_comprehendmedical.types.comprehend_medical_async_job_properties

        out["ComprehendMedicalAsyncJobProperties"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_properties.serialize_aws_json_1_1(
                value["comprehend_medical_async_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeRxNormInferenceJobResponse:
    out: DescribeRxNormInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("ComprehendMedicalAsyncJobProperties") is not None:
        import capo_comprehendmedical.types.comprehend_medical_async_job_properties

        out["comprehend_medical_async_job_properties"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_properties.deserialize_aws_json_1_1(
                data["ComprehendMedicalAsyncJobProperties"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeRxNormInferenceJobResponse) -> dict:
    out: dict = {}
    if "comprehend_medical_async_job_properties" in value:
        import capo_comprehendmedical.types.comprehend_medical_async_job_properties

        out["ComprehendMedicalAsyncJobProperties"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_properties.serialize_cbor(
                value["comprehend_medical_async_job_properties"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeRxNormInferenceJobResponse:
    out: DescribeRxNormInferenceJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("ComprehendMedicalAsyncJobProperties") is not None:
        import capo_comprehendmedical.types.comprehend_medical_async_job_properties

        out["comprehend_medical_async_job_properties"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_properties.deserialize_cbor(
                data["ComprehendMedicalAsyncJobProperties"]
            )
        )
    return out
