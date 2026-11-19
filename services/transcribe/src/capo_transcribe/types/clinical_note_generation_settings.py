"""Generated from Smithy shape ``com.amazonaws.transcribe#ClinicalNoteGenerationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe.types.medical_scribe_note_template


class ClinicalNoteGenerationSettings(TypedDict, closed=True):
    note_template: NotRequired[
        "capo_transcribe.types.medical_scribe_note_template.MedicalScribeNoteTemplate"
    ]
    """<p>Specify one of the following templates to use for the clinical note summary. The default is <code>HISTORY_AND_PHYSICAL</code>.</p> <ul> <li> <p>HISTORY_AND_PHYSICAL: Provides summaries for key sections of the clinical documentation. Examples of sections include Chief Complaint, History of Present Illness, Review of Systems, Past Medical History, Assessment, and Plan. </p> </li> <li> <p>GIRPP: Provides summaries based on the patients progress toward goals. Examples of sections include Goal, Intervention, Response, Progress, and Plan.</p> </li> <li> <p>BIRP: Focuses on the patient's behavioral patterns and responses. Examples of sections include Behavior, Intervention, Response, and Plan.</p> </li> <li> <p>SIRP: Emphasizes the situational context of therapy. Examples of sections include Situation, Intervention, Response, and Plan.</p> </li> <li> <p>DAP: Provides a simplified format for clinical documentation. Examples of sections include Data, Assessment, and Plan.</p> </li> <li> <p>BEHAVIORAL_SOAP: Behavioral health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.</p> </li> <li> <p>PHYSICAL_SOAP: Physical health focused documentation format. Examples of sections include Subjective, Objective, Assessment, and Plan.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClinicalNoteGenerationSettings) -> dict:
    out: dict = {}
    if "note_template" in value:
        import capo_transcribe.types.medical_scribe_note_template

        out["NoteTemplate"] = (
            capo_transcribe.types.medical_scribe_note_template.serialize_aws_json_1_1(
                value["note_template"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClinicalNoteGenerationSettings:
    out: ClinicalNoteGenerationSettings = {}  # type: ignore[typeddict-item]
    if data.get("NoteTemplate") is not None:
        import capo_transcribe.types.medical_scribe_note_template

        out["note_template"] = (
            capo_transcribe.types.medical_scribe_note_template.deserialize_aws_json_1_1(
                data["NoteTemplate"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ClinicalNoteGenerationSettings) -> dict:
    out: dict = {}
    if "note_template" in value:
        import capo_transcribe.types.medical_scribe_note_template

        out["NoteTemplate"] = (
            capo_transcribe.types.medical_scribe_note_template.serialize_cbor(
                value["note_template"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ClinicalNoteGenerationSettings:
    out: ClinicalNoteGenerationSettings = {}  # type: ignore[typeddict-item]
    if data.get("NoteTemplate") is not None:
        import capo_transcribe.types.medical_scribe_note_template

        out["note_template"] = (
            capo_transcribe.types.medical_scribe_note_template.deserialize_cbor(
                data["NoteTemplate"]
            )
        )
    return out
