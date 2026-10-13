"""Generated from Smithy shape ``com.amazonaws.wisdom#Document``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.content_reference
    import capo_wisdom.types.document_text


class Document(TypedDict, closed=True):
    content_reference: "capo_wisdom.types.content_reference.ContentReference"
    """<p>A reference to the content resource.</p>"""
    title: NotRequired["capo_wisdom.types.document_text.DocumentText"]
    """<p>The title of the document.</p>"""
    excerpt: NotRequired["capo_wisdom.types.document_text.DocumentText"]
    """<p>The excerpt from the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Document) -> dict:
    out: dict = {}
    import capo_wisdom.types.content_reference

    out["contentReference"] = capo_wisdom.types.content_reference.serialize_json(
        value["content_reference"]
    )
    if "title" in value:
        import capo_wisdom.types.document_text

        out["title"] = capo_wisdom.types.document_text.serialize_json(value["title"])
    if "excerpt" in value:
        import capo_wisdom.types.document_text

        out["excerpt"] = capo_wisdom.types.document_text.serialize_json(
            value["excerpt"]
        )
    return out


def deserialize_json(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if data.get("contentReference") is not None:
        import capo_wisdom.types.content_reference

        out["content_reference"] = capo_wisdom.types.content_reference.deserialize_json(
            data["contentReference"]
        )
    else:
        raise DeserializationError("Document.content_reference required")
    if data.get("title") is not None:
        import capo_wisdom.types.document_text

        out["title"] = capo_wisdom.types.document_text.deserialize_json(data["title"])
    if data.get("excerpt") is not None:
        import capo_wisdom.types.document_text

        out["excerpt"] = capo_wisdom.types.document_text.deserialize_json(
            data["excerpt"]
        )
    return out


def redact_sensitive(value: Document) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        import capo_wisdom.types.document_text

        out["title"] = capo_wisdom.types.document_text.redact_sensitive(value["title"])
    if "excerpt" in value:
        import capo_wisdom.types.document_text

        out["excerpt"] = capo_wisdom.types.document_text.redact_sensitive(
            value["excerpt"]
        )
    return out
