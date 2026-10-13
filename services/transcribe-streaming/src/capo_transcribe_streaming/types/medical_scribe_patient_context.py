"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribePatientContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.pronouns


class MedicalScribePatientContext(TypedDict, closed=True):
    pronouns: NotRequired["capo_transcribe_streaming.types.pronouns.Pronouns"]
    """<p>The patient's preferred pronouns that the user wants to provide as a context for clinical note generation .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribePatientContext) -> dict:
    out: dict = {}
    if "pronouns" in value:
        import capo_transcribe_streaming.types.pronouns

        out["Pronouns"] = capo_transcribe_streaming.types.pronouns.serialize_json(
            value["pronouns"]
        )
    return out


def deserialize_json(data: dict) -> MedicalScribePatientContext:
    out: MedicalScribePatientContext = {}  # type: ignore[typeddict-item]
    if data.get("Pronouns") is not None:
        import capo_transcribe_streaming.types.pronouns

        out["pronouns"] = capo_transcribe_streaming.types.pronouns.deserialize_json(
            data["Pronouns"]
        )
    return out


def redact_sensitive(value: MedicalScribePatientContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pronouns" in value:
        out["pronouns"] = "*** Sensitive Data Redacted ***"
    return out
