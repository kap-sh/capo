"""Generated from Smithy shape ``com.amazonaws.transcribe#ListMedicalTranscriptionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.medical_transcription_job_summaries
    import capo_transcribe.types.next_token
    import capo_transcribe.types.transcription_job_status


class ListMedicalTranscriptionJobsResponse(TypedDict, closed=True):
    status: NotRequired[
        "capo_transcribe.types.transcription_job_status.TranscriptionJobStatus"
    ]
    """<p>Lists all medical transcription jobs that have the status specified in your request. Jobs are ordered by creation date, with the newest job first.</p>"""
    next_token: NotRequired["capo_transcribe.types.next_token.NextToken"]
    """<p>If <code>NextToken</code> is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the <code>NextToken</code> parameter in your results output, then run your request again including <code>NextToken</code> with the value of the copied string. Repeat as needed to view all your results.</p>"""
    medical_transcription_job_summaries: NotRequired[
        "capo_transcribe.types.medical_transcription_job_summaries.MedicalTranscriptionJobSummaries"
    ]
    """<p>Provides a summary of information about each result.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMedicalTranscriptionJobsResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_transcribe.types.transcription_job_status

        out["Status"] = (
            capo_transcribe.types.transcription_job_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "medical_transcription_job_summaries" in value:
        import capo_transcribe.types.medical_transcription_job_summaries

        out["MedicalTranscriptionJobSummaries"] = (
            capo_transcribe.types.medical_transcription_job_summaries.serialize_aws_json_1_1(
                value["medical_transcription_job_summaries"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMedicalTranscriptionJobsResponse:
    out: ListMedicalTranscriptionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_transcribe.types.transcription_job_status

        out["status"] = (
            capo_transcribe.types.transcription_job_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MedicalTranscriptionJobSummaries") is not None:
        import capo_transcribe.types.medical_transcription_job_summaries

        out["medical_transcription_job_summaries"] = (
            capo_transcribe.types.medical_transcription_job_summaries.deserialize_aws_json_1_1(
                data["MedicalTranscriptionJobSummaries"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListMedicalTranscriptionJobsResponse) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_transcribe.types.transcription_job_status

        out["Status"] = capo_transcribe.types.transcription_job_status.serialize_cbor(
            value["status"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "medical_transcription_job_summaries" in value:
        import capo_transcribe.types.medical_transcription_job_summaries

        out["MedicalTranscriptionJobSummaries"] = (
            capo_transcribe.types.medical_transcription_job_summaries.serialize_cbor(
                value["medical_transcription_job_summaries"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListMedicalTranscriptionJobsResponse:
    out: ListMedicalTranscriptionJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_transcribe.types.transcription_job_status

        out["status"] = capo_transcribe.types.transcription_job_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MedicalTranscriptionJobSummaries") is not None:
        import capo_transcribe.types.medical_transcription_job_summaries

        out["medical_transcription_job_summaries"] = (
            capo_transcribe.types.medical_transcription_job_summaries.deserialize_cbor(
                data["MedicalTranscriptionJobSummaries"]
            )
        )
    return out
