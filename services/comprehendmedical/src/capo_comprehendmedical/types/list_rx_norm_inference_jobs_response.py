"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ListRxNormInferenceJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.comprehend_medical_async_job_properties_list
    import capo_comprehendmedical.types.string


class ListRxNormInferenceJobsResponse(TypedDict, closed=True):
    comprehend_medical_async_job_properties_list: NotRequired[
        "capo_comprehendmedical.types.comprehend_medical_async_job_properties_list.ComprehendMedicalAsyncJobPropertiesList"
    ]
    """<p>The maximum number of results to return in each page. The default is 100.</p>"""
    next_token: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRxNormInferenceJobsResponse) -> dict:
    out: dict = {}
    if "comprehend_medical_async_job_properties_list" in value:
        import capo_comprehendmedical.types.comprehend_medical_async_job_properties_list

        out["ComprehendMedicalAsyncJobPropertiesList"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_properties_list.serialize_aws_json_1_1(
                value["comprehend_medical_async_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRxNormInferenceJobsResponse:
    out: ListRxNormInferenceJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ComprehendMedicalAsyncJobPropertiesList") is not None:
        import capo_comprehendmedical.types.comprehend_medical_async_job_properties_list

        out["comprehend_medical_async_job_properties_list"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_properties_list.deserialize_aws_json_1_1(
                data["ComprehendMedicalAsyncJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRxNormInferenceJobsResponse) -> dict:
    out: dict = {}
    if "comprehend_medical_async_job_properties_list" in value:
        import capo_comprehendmedical.types.comprehend_medical_async_job_properties_list

        out["ComprehendMedicalAsyncJobPropertiesList"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_properties_list.serialize_cbor(
                value["comprehend_medical_async_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListRxNormInferenceJobsResponse:
    out: ListRxNormInferenceJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ComprehendMedicalAsyncJobPropertiesList") is not None:
        import capo_comprehendmedical.types.comprehend_medical_async_job_properties_list

        out["comprehend_medical_async_job_properties_list"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_properties_list.deserialize_cbor(
                data["ComprehendMedicalAsyncJobPropertiesList"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
