"""Generated from Smithy shape ``com.amazonaws.transcribe#DeleteTranscriptionJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.transcription_job_name


class DeleteTranscriptionJobRequest(TypedDict, closed=True):
    transcription_job_name: (
        "capo_transcribe.types.transcription_job_name.TranscriptionJobName"
    )
    """<p>The name of the transcription job you want to delete. Job names are case sensitive.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTranscriptionJobRequest) -> dict:
    out: dict = {}
    out["TranscriptionJobName"] = value["transcription_job_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTranscriptionJobRequest:
    out: DeleteTranscriptionJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptionJobName") is not None:
        out["transcription_job_name"] = data["TranscriptionJobName"]
    else:
        out["transcription_job_name"] = ""
    return out
