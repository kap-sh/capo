"""Generated from Smithy shape ``com.amazonaws.textract#Document``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.image_blob
    import capo_textract.types.s3_object


class Document(TypedDict, closed=True):
    bytes: NotRequired["capo_textract.types.image_blob.ImageBlob"]
    """<p>A blob of base64-encoded document bytes. The maximum size of a document that's provided in a blob of bytes is 5 MB. The document bytes must be in PNG or JPEG format.</p> <p>If you're using an AWS SDK to call Amazon Textract, you might not need to base64-encode image bytes passed using the <code>Bytes</code> field. </p>"""
    s3_object: NotRequired["capo_textract.types.s3_object.S3Object"]
    """<p>Identifies an S3 object as the document source. The maximum size of a document that's stored in an S3 bucket is 5 MB.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Document) -> dict:
    out: dict = {}
    if "bytes" in value:
        import capo_textract.types.image_blob

        out["Bytes"] = capo_textract.types.image_blob.serialize_aws_json_1_1(
            value["bytes"]
        )
    if "s3_object" in value:
        import capo_textract.types.s3_object

        out["S3Object"] = capo_textract.types.s3_object.serialize_aws_json_1_1(
            value["s3_object"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if data.get("Bytes") is not None:
        import capo_textract.types.image_blob

        out["bytes"] = capo_textract.types.image_blob.deserialize_aws_json_1_1(
            data["Bytes"]
        )
    if data.get("S3Object") is not None:
        import capo_textract.types.s3_object

        out["s3_object"] = capo_textract.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Document) -> dict:
    out: dict = {}
    if "bytes" in value:
        import capo_textract.types.image_blob

        out["Bytes"] = capo_textract.types.image_blob.serialize_cbor(value["bytes"])
    if "s3_object" in value:
        import capo_textract.types.s3_object

        out["S3Object"] = capo_textract.types.s3_object.serialize_cbor(
            value["s3_object"]
        )
    return out


def deserialize_cbor(data: dict) -> Document:
    out: Document = {}  # type: ignore[typeddict-item]
    if data.get("Bytes") is not None:
        import capo_textract.types.image_blob

        out["bytes"] = capo_textract.types.image_blob.deserialize_cbor(data["Bytes"])
    if data.get("S3Object") is not None:
        import capo_textract.types.s3_object

        out["s3_object"] = capo_textract.types.s3_object.deserialize_cbor(
            data["S3Object"]
        )
    return out
