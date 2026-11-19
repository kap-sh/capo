"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ListEntitiesDetectionV2JobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.comprehend_medical_async_job_properties_list
    import capo_comprehendmedical.types.string


class ListEntitiesDetectionV2JobsResponse(TypedDict, closed=True):
    comprehend_medical_async_job_properties_list: NotRequired[
        "capo_comprehendmedical.types.comprehend_medical_async_job_properties_list.ComprehendMedicalAsyncJobPropertiesList"
    ]
    """<p>A list containing the properties of each job returned.</p>"""
    next_token: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntitiesDetectionV2JobsResponse) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> ListEntitiesDetectionV2JobsResponse:
    out: ListEntitiesDetectionV2JobsResponse = {}  # type: ignore[typeddict-item]
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
def serialize_cbor(value: ListEntitiesDetectionV2JobsResponse) -> dict:
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


def deserialize_cbor(data: dict) -> ListEntitiesDetectionV2JobsResponse:
    out: ListEntitiesDetectionV2JobsResponse = {}  # type: ignore[typeddict-item]
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
