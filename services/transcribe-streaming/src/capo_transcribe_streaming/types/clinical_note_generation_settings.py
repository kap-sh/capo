"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ClinicalNoteGenerationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transcribe_streaming.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.bucket_name
    import capo_transcribe_streaming.types.medical_scribe_note_template


class ClinicalNoteGenerationSettings(TypedDict, closed=True):
    output_bucket_name: "capo_transcribe_streaming.types.bucket_name.BucketName"
    """<p>The name of the Amazon S3 bucket where you want the output of Amazon Web Services HealthScribe post-stream analytics stored. Don't include the <code>S3://</code> prefix of the specified bucket. </p> <p>HealthScribe outputs transcript and clinical note files under the prefix: <code>S3://$output-bucket-name/healthscribe-streaming/session-id/post-stream-analytics/clinical-notes</code> </p> <p>The role <code>ResourceAccessRoleArn</code> specified in the <code>MedicalScribeConfigurationEvent</code> must have permission to use the specified location. You can change Amazon S3 permissions using the <a href="https://console.aws.amazon.com/s3"> Amazon Web Services Management Console </a>. See also <a href="https://docs.aws.amazon.com/transcribe/latest/dg/security_iam_id-based-policy-examples.html#auth-role-iam-user">Permissions Required for IAM User Roles </a> . </p>"""
    note_template: NotRequired[
        "capo_transcribe_streaming.types.medical_scribe_note_template.MedicalScribeNoteTemplate"
    ]
    """<p>Specify one of the following templates to use for the clinical note summary. The default is <code>HISTORY_AND_PHYSICAL</code>.</p> <ul> <li> <p>HISTORY_AND_PHYSICAL: Provides summaries for key sections of the clinical documentation. Examples of sections include Chief Complaint, History of Present Illness, Review of Systems, Past Medical History, Assessment, and Plan. </p> </li> <li> <p>GIRPP: Provides summaries based on the patients progress toward goals. Examples of sections include Goal, Intervention, Response, Progress, and Plan.</p> </li> <li> <p>BIRP: Focuses on the patient's behavioral patterns and responses. Examples of sections include Behavior, Intervention, Response, and Plan.</p> </li> <li> <p>SIRP: Emphasizes the situational context of therapy. Examples of sections include Situation, Intervention, Response, and Plan.</p> </li> <li> <p>DAP: Provides a simplified format for clinical documentation. Examples of sections include Data, Assessment, and Plan.</p> </li> <li> <p>BEHAVIORAL_SOAP: Behavioral health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.</p> </li> <li> <p>PHYSICAL_SOAP: Physical health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClinicalNoteGenerationSettings) -> dict:
    out: dict = {}
    out["OutputBucketName"] = value["output_bucket_name"]
    if "note_template" in value:
        import capo_transcribe_streaming.types.medical_scribe_note_template

        out["NoteTemplate"] = (
            capo_transcribe_streaming.types.medical_scribe_note_template.serialize_json(
                value["note_template"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClinicalNoteGenerationSettings:
    out: ClinicalNoteGenerationSettings = {}  # type: ignore[typeddict-item]
    if data.get("OutputBucketName") is not None:
        out["output_bucket_name"] = data["OutputBucketName"]
    else:
        raise DeserializationError(
            "ClinicalNoteGenerationSettings.output_bucket_name required"
        )
    if data.get("NoteTemplate") is not None:
        import capo_transcribe_streaming.types.medical_scribe_note_template

        out["note_template"] = (
            capo_transcribe_streaming.types.medical_scribe_note_template.deserialize_json(
                data["NoteTemplate"]
            )
        )
    return out
