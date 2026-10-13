"""Generated from Smithy shape ``com.amazonaws.connecthealth#ClinicalNoteGenerationSettings``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_connecthealth.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connecthealth.types.note_template_settings


class ClinicalNoteGenerationSettings(TypedDict, closed=True):
    note_template_settings: (
        "capo_connecthealth.types.note_template_settings.NoteTemplateSettings"
    )
    """<p>Settings for the note template to use</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClinicalNoteGenerationSettings) -> dict:
    out: dict = {}
    import capo_connecthealth.types.note_template_settings

    out["noteTemplateSettings"] = (
        capo_connecthealth.types.note_template_settings.serialize_json(
            value["note_template_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> ClinicalNoteGenerationSettings:
    out: ClinicalNoteGenerationSettings = {}  # type: ignore[typeddict-item]
    if data.get("noteTemplateSettings") is not None:
        import capo_connecthealth.types.note_template_settings

        out["note_template_settings"] = (
            capo_connecthealth.types.note_template_settings.deserialize_json(
                data["noteTemplateSettings"]
            )
        )
    else:
        raise DeserializationError(
            "ClinicalNoteGenerationSettings.note_template_settings required"
        )
    return out


def redact_sensitive(value: ClinicalNoteGenerationSettings) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "note_template_settings" in value:
        import capo_connecthealth.types.note_template_settings

        out["note_template_settings"] = (
            capo_connecthealth.types.note_template_settings.redact_sensitive(
                value["note_template_settings"]
            )
        )
    return out
