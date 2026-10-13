"""Generated from Smithy shape ``com.amazonaws.translate#TranslatedDocument``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_translate.errors import DeserializationError

if TYPE_CHECKING:
    import capo_translate.types.translated_document_content


class TranslatedDocument(TypedDict, closed=True):
    content: (
        "capo_translate.types.translated_document_content.TranslatedDocumentContent"
    )
    """<p>The document containing the translated content.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TranslatedDocument) -> dict:
    out: dict = {}
    import capo_translate.types.translated_document_content

    out["Content"] = (
        capo_translate.types.translated_document_content.serialize_aws_json_1_1(
            value["content"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TranslatedDocument:
    out: TranslatedDocument = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        import capo_translate.types.translated_document_content

        out["content"] = (
            capo_translate.types.translated_document_content.deserialize_aws_json_1_1(
                data["Content"]
            )
        )
    else:
        raise DeserializationError("TranslatedDocument.content required")
    return out


def redact_sensitive(value: TranslatedDocument) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
