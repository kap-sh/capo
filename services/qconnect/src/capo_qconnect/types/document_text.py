"""Generated from Smithy shape ``com.amazonaws.qconnect#DocumentText``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.highlights
    import capo_qconnect.types.sensitive_string


class DocumentText(TypedDict, closed=True):
    text: NotRequired["capo_qconnect.types.sensitive_string.SensitiveString"]
    """<p>Text in the document.</p>"""
    highlights: NotRequired["capo_qconnect.types.highlights.Highlights"]
    """<p>Highlights in the document text.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentText) -> dict:
    out: dict = {}
    if "text" in value:
        out["text"] = value["text"]
    if "highlights" in value:
        import capo_qconnect.types.highlights

        out["highlights"] = capo_qconnect.types.highlights.serialize_json(
            value["highlights"]
        )
    return out


def deserialize_json(data: dict) -> DocumentText:
    out: DocumentText = {}  # type: ignore[typeddict-item]
    if data.get("text") is not None:
        out["text"] = data["text"]
    if data.get("highlights") is not None:
        import capo_qconnect.types.highlights

        out["highlights"] = capo_qconnect.types.highlights.deserialize_json(
            data["highlights"]
        )
    return out


def redact_sensitive(value: DocumentText) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
