"""Generated from Smithy shape ``com.amazonaws.translate#Document``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_translate.errors import DeserializationError

if TYPE_CHECKING:
    import capo_translate.types.content_type
    import capo_translate.types.document_content


class Document(TypedDict, closed=True):
    content: "capo_translate.types.document_content.DocumentContent"
    """<p>The <code>Content</code>field type is Binary large object (blob). This object contains the document content converted into base64-encoded binary data. If you use one of the AWS SDKs, the SDK performs the Base64-encoding on this field before sending the request. </p>"""
    content_type: "capo_translate.types.content_type.ContentType"
    """<p>Describes the format of the document. You can specify one of the following:</p> <ul> <li> <p> <code>text/html</code> - The input data consists of HTML content. Amazon Translate translates only the text in the HTML element.</p> </li> <li> <p> <code>text/plain</code> - The input data consists of unformatted text. Amazon Translate translates every character in the content. </p> </li> <li> <p> <code>application/vnd.openxmlformats-officedocument.wordprocessingml.document</code> - The input data consists of a Word document (.docx).</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Document) -> dict:
    out: dict = {}
    import capo_translate.types.document_content

    out["Content"] = capo_translate.types.document_content.serialize_aws_json_1_1(
        value["content"]
    )
    out["ContentType"] = value["content_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if data.get("Content") is not None:
        import capo_translate.types.document_content

        out["content"] = capo_translate.types.document_content.deserialize_aws_json_1_1(
            data["Content"]
        )
    else:
        raise DeserializationError("Document.content required")
    if data.get("ContentType") is not None:
        out["content_type"] = data["ContentType"]
    else:
        raise DeserializationError("Document.content_type required")
    return out


def redact_sensitive(value: Document) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "content" in value:
        out["content"] = "*** Sensitive Data Redacted ***"
    return out
