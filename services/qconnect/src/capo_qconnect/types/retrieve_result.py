"""Generated from Smithy shape ``com.amazonaws.qconnect#RetrieveResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.reference_type
    import capo_qconnect.types.sensitive_string
    import capo_qconnect.types.uuid


class RetrieveResult(TypedDict, closed=True):
    association_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the assistant association for the retrieved result.</p>"""
    source_id: "capo_qconnect.types.sensitive_string.SensitiveString"
    """<p>The URL, URI, or ID of the retrieved content when available, or a UUID when unavailable.</p>"""
    reference_type: "capo_qconnect.types.reference_type.ReferenceType"
    """<p>A type to define the KB origin of a retrieved content.</p>"""
    content_text: "capo_qconnect.types.sensitive_string.SensitiveString"
    """<p>The text content of the retrieved result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RetrieveResult) -> dict:
    out: dict = {}
    out["associationId"] = value["association_id"]
    out["sourceId"] = value["source_id"]
    out["referenceType"] = value["reference_type"]
    out["contentText"] = value["content_text"]
    return out


def deserialize_json(data: dict) -> RetrieveResult:
    out: RetrieveResult = {}  # type: ignore[typeddict-item]
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    else:
        out["association_id"] = ""
    if data.get("sourceId") is not None:
        out["source_id"] = data["sourceId"]
    else:
        out["source_id"] = ""
    if data.get("referenceType") is not None:
        out["reference_type"] = data["referenceType"]
    else:
        out["reference_type"] = ""
    if data.get("contentText") is not None:
        out["content_text"] = data["contentText"]
    else:
        out["content_text"] = ""
    return out


def redact_sensitive(value: RetrieveResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_id" in value:
        out["source_id"] = "*** Sensitive Data Redacted ***"
    if "content_text" in value:
        out["content_text"] = "*** Sensitive Data Redacted ***"
    return out
