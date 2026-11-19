"""Generated from Smithy shape ``com.amazonaws.transcribe#ListMedicalTranscriptionJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.max_results
    import capo_transcribe.types.next_token
    import capo_transcribe.types.transcription_job_name
    import capo_transcribe.types.transcription_job_status


class ListMedicalTranscriptionJobsRequest(TypedDict, closed=True):
    status: NotRequired[
        "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Returns only medical transcription jobs with the specified status. Jobs are ordered by creation date, with the newest job first. If you do not include <code>Status</code>, all medical transcription jobs are returned.</p>"""
    job_name_contains: NotRequired[
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    ]
    """<p>Returns only the medical transcription jobs that contain the specified string. The search is not case sensitive.</p>"""
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If your <code>ListMedicalTranscriptionJobs</code> request returns more results than can be displayed, <code>NextToken</code> is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    max_results: NotRequired["capo_transcribe.types.max_results.MaxResults"]
    """<p>The maximum number of medical transcription jobs to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMedicalTranscriptionJobsRequest) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_transcribe.types.transcription_job_status

        out["Status"] = (
            capo_transcribe.types.transcription_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "job_name_contains" in value:
        out["JobNameContains"] = value["job_name_contains"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMedicalTranscriptionJobsRequest:
    out: ListMedicalTranscriptionJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_transcribe.types.transcription_job_status

        out["status"] = (
            capo_transcribe.types.transcription_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("JobNameContains") is not None:
        out["job_name_contains"] = data["JobNameContains"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMedicalTranscriptionJobsRequest) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_transcribe.types.transcription_job_status

        out["Status"] = capo_transcribe.types.transcription_job_status.serialize_cbor(
            value["status"]
        )
    if "job_name_contains" in value:
        out["JobNameContains"] = value["job_name_contains"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_cbor(data: dict) -> ListMedicalTranscriptionJobsRequest:
    out: ListMedicalTranscriptionJobsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_transcribe.types.transcription_job_status

        out["status"] = capo_transcribe.types.transcription_job_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("JobNameContains") is not None:
        out["job_name_contains"] = data["JobNameContains"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
