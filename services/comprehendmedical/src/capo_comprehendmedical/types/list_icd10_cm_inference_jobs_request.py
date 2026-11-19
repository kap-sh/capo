"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#ListICD10CMInferenceJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehendmedical.types.comprehend_medical_async_job_filter
    import capo_comprehendmedical.types.max_results_integer
    import capo_comprehendmedical.types.string


class ListICD10CMInferenceJobsRequest(TypedDict, closed=True):
    filter: NotRequired[
        "capo_comprehendmedical.types.comprehend_medical_async_job_filter.ComprehendMedicalAsyncJobFilter"
    ]
    """<p>Filters the jobs that are returned. You can filter jobs based on their names, status, or the date and time that they were submitted. You can only set one filter at a time.</p>"""
    next_token: NotRequired["capo_comprehendmedical.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""
    max_results: NotRequired[
        "capo_comprehendmedical.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of results to return in each page. The default is 100.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListICD10CMInferenceJobsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_comprehendmedical.types.comprehend_medical_async_job_filter

        out["Filter"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_filter.serialize_aws_json_1_1(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListICD10CMInferenceJobsRequest:
    out: ListICD10CMInferenceJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_comprehendmedical.types.comprehend_medical_async_job_filter

        out["filter"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_filter.deserialize_aws_json_1_1(
                data["Filter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListICD10CMInferenceJobsRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_comprehendmedical.types.comprehend_medical_async_job_filter

        out["Filter"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_filter.serialize_cbor(
                value["filter"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListICD10CMInferenceJobsRequest:
    out: ListICD10CMInferenceJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        import capo_comprehendmedical.types.comprehend_medical_async_job_filter

        out["filter"] = (
            capo_comprehendmedical.types.comprehend_medical_async_job_filter.deserialize_cbor(
                data["Filter"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
