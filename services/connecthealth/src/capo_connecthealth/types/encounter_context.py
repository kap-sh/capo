"""Generated from Smithy shape ``com.amazonaws.connecthealth#EncounterContext``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.medical_coding_context
    import capo_connecthealth.types.sensitive_markdown_string


class EncounterContext(TypedDict, closed=True):
    unstructured_context: NotRequired[
        "capo_connecthealth.types.sensitive_markdown_string.SensitiveMarkdownString"
    ]
    """<p>Unstructured context information in markdown format</p>"""
    medical_coding_context: NotRequired[
        "capo_connecthealth.types.medical_coding_context.MedicalCodingContext"
    ]
    """<p>Structured patient and encounter context for medical code generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncounterContext) -> dict:
    out: dict = {}
    if "unstructured_context" in value:
        out["unstructuredContext"] = value["unstructured_context"]
    if "medical_coding_context" in value:
        import capo_connecthealth.types.medical_coding_context

        out["medicalCodingContext"] = (
            capo_connecthealth.types.medical_coding_context.serialize_json(
                value["medical_coding_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> EncounterContext:
    out: EncounterContext = {}  # type: ignore[typeddict-item]
    if data.get("unstructuredContext") is not None:
        out["unstructured_context"] = data["unstructuredContext"]
    if data.get("medicalCodingContext") is not None:
        import capo_connecthealth.types.medical_coding_context

        out["medical_coding_context"] = (
            capo_connecthealth.types.medical_coding_context.deserialize_json(
                data["medicalCodingContext"]
            )
        )
    return out


def redact_sensitive(value: EncounterContext) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "unstructured_context" in value:
        out["unstructured_context"] = "*** Sensitive Data Redacted ***"
    if "medical_coding_context" in value:
        import capo_connecthealth.types.medical_coding_context

        out["medical_coding_context"] = (
            capo_connecthealth.types.medical_coding_context.redact_sensitive(
                value["medical_coding_context"]
            )
        )
    return out
