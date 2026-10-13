"""Generated from Smithy shape ``com.amazonaws.voiceid#ListSpeakerEnrollmentJobsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.speaker_enrollment_job_summaries
    import capo_voice_id.types.string


class ListSpeakerEnrollmentJobsResponse(TypedDict, closed=True):
    job_summaries: NotRequired[
        "capo_voice_id.types.speaker_enrollment_job_summaries.SpeakerEnrollmentJobSummaries"
    ]
    """<p>A list containing details about each specified speaker enrollment job.</p>"""
    next_token: NotRequired["capo_voice_id.types.string.String"]
    """<p>If <code>NextToken</code> is returned, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSpeakerEnrollmentJobsResponse) -> dict:
    out: dict = {}
    if "job_summaries" in value:
        import capo_voice_id.types.speaker_enrollment_job_summaries

        out["JobSummaries"] = (
            capo_voice_id.types.speaker_enrollment_job_summaries.serialize_aws_json_1_0(
                value["job_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSpeakerEnrollmentJobsResponse:
    out: ListSpeakerEnrollmentJobsResponse = {}  # type: ignore[typeddict-item]
    if data.get("JobSummaries") is not None:
        import capo_voice_id.types.speaker_enrollment_job_summaries

        out["job_summaries"] = (
            capo_voice_id.types.speaker_enrollment_job_summaries.deserialize_aws_json_1_0(
                data["JobSummaries"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListSpeakerEnrollmentJobsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "job_summaries" in value:
        import capo_voice_id.types.speaker_enrollment_job_summaries

        out["job_summaries"] = (
            capo_voice_id.types.speaker_enrollment_job_summaries.redact_sensitive(
                value["job_summaries"]
            )
        )
    return out
