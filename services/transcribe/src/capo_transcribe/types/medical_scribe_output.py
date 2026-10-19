"""Generated from Smithy shape ``com.amazonaws.transcribe#MedicalScribeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.uri


class MedicalScribeOutput(TypedDict, closed=True):
    transcript_file_uri: "capo_transcribe.types.uri.Uri"
    """<p>Holds the Amazon S3 URI for the Transcript.</p>"""
    clinical_document_uri: "capo_transcribe.types.uri.Uri"
    """<p>Holds the Amazon S3 URI for the Clinical Document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MedicalScribeOutput) -> dict:
    out: dict = {}
    out["TranscriptFileUri"] = value["transcript_file_uri"]
    out["ClinicalDocumentUri"] = value["clinical_document_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MedicalScribeOutput:
    out: MedicalScribeOutput = {}  # type: ignore[typeddict-item]
    if data.get("TranscriptFileUri") is not None:
        out["transcript_file_uri"] = data["TranscriptFileUri"]
    else:
        out["transcript_file_uri"] = ""
    if data.get("ClinicalDocumentUri") is not None:
        out["clinical_document_uri"] = data["ClinicalDocumentUri"]
    else:
        out["clinical_document_uri"] = ""
    return out
