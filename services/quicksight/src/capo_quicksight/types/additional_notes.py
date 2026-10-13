"""Generated from Smithy shape ``com.amazonaws.quicksight#AdditionalNotes``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.additional_notes_text


class AdditionalNotes(TypedDict, closed=True):
    text: NotRequired["capo_quicksight.types.additional_notes_text.AdditionalNotesText"]
    """<p>The additional notes text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalNotes) -> dict:
    out: dict = {}
    if "text" in value:
        out["Text"] = value["text"]
    return out


def deserialize_json(data: dict) -> AdditionalNotes:
    out: AdditionalNotes = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    return out


def redact_sensitive(value: AdditionalNotes) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
