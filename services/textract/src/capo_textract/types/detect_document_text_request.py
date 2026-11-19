"""Generated from Smithy shape ``com.amazonaws.textract#DetectDocumentTextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_textract.errors import DeserializationError

if TYPE_CHECKING:
    import capo_textract.types.document


class DetectDocumentTextRequest(TypedDict, closed=True):
    document: "capo_textract.types.document.Document"
    """<p>The input document as base64-encoded bytes or an Amazon S3 object. If you use the AWS CLI to call Amazon Textract operations, you can't pass image bytes. The document must be an image in JPEG or PNG format.</p> <p>If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes that are passed using the <code>Bytes</code> field. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectDocumentTextRequest) -> dict:
    out: dict = {}
    import capo_textract.types.document

    out["Document"] = capo_textract.types.document.serialize_aws_json_1_1(
        value["document"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectDocumentTextRequest:
    out: DetectDocumentTextRequest = {}  # type: ignore[typeddict-item]
    if data.get("Document") is not None:
        import capo_textract.types.document

        out["document"] = capo_textract.types.document.deserialize_aws_json_1_1(
            data["Document"]
        )
    else:
        raise DeserializationError("DetectDocumentTextRequest.document required")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DetectDocumentTextRequest) -> dict:
    out: dict = {}
    import capo_textract.types.document

    out["Document"] = capo_textract.types.document.serialize_cbor(value["document"])
    return out


def deserialize_cbor(data: dict) -> DetectDocumentTextRequest:
    out: DetectDocumentTextRequest = {}  # type: ignore[typeddict-item]
    if data.get("Document") is not None:
        import capo_textract.types.document

        out["document"] = capo_textract.types.document.deserialize_cbor(
            data["Document"]
        )
    else:
        raise DeserializationError("DetectDocumentTextRequest.document required")
    return out
