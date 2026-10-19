"""Generated from Smithy shape ``com.amazonaws.quicksight#InlineCustomInstruction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.inline_custom_instruction_text
    import capo_quicksight.types.uploaded_document_metadata


class InlineCustomInstruction(TypedDict, closed=True):
    instruction_text: "capo_quicksight.types.inline_custom_instruction_text.InlineCustomInstructionText"
    """<p>The instruction text content.</p>"""
    uploaded_document_metadata: NotRequired[
        "capo_quicksight.types.uploaded_document_metadata.UploadedDocumentMetadata"
    ]
    """<p>Metadata about an uploaded document associated with this instruction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InlineCustomInstruction) -> dict:
    out: dict = {}
    out["InstructionText"] = value["instruction_text"]
    if "uploaded_document_metadata" in value:
        import capo_quicksight.types.uploaded_document_metadata

        out["UploadedDocumentMetadata"] = (
            capo_quicksight.types.uploaded_document_metadata.serialize_json(
                value["uploaded_document_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> InlineCustomInstruction:
    out: InlineCustomInstruction = {}  # type: ignore[typeddict-item]
    if data.get("InstructionText") is not None:
        out["instruction_text"] = data["InstructionText"]
    else:
        out["instruction_text"] = ""
    if data.get("UploadedDocumentMetadata") is not None:
        import capo_quicksight.types.uploaded_document_metadata

        out["uploaded_document_metadata"] = (
            capo_quicksight.types.uploaded_document_metadata.deserialize_json(
                data["UploadedDocumentMetadata"]
            )
        )
    return out


def redact_sensitive(value: InlineCustomInstruction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instruction_text" in value:
        out["instruction_text"] = "*** Sensitive Data Redacted ***"
    return out
