"""Generated from Smithy shape ``com.amazonaws.textract#DocumentLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_textract.types.s3_object


class DocumentLocation(TypedDict, closed=True):
    s3_object: NotRequired["capo_textract.types.s3_object.S3Object"]
    """<p>The Amazon S3 bucket that contains the input document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentLocation) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import capo_textract.types.s3_object

        out["S3Object"] = capo_textract.types.s3_object.serialize_aws_json_1_1(
            value["s3_object"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentLocation:
    out: DocumentLocation = {}  # type: ignore[typeddict-item]
    if data.get("S3Object") is not None:
        import capo_textract.types.s3_object

        out["s3_object"] = capo_textract.types.s3_object.deserialize_aws_json_1_1(
            data["S3Object"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentLocation) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import capo_textract.types.s3_object

        out["S3Object"] = capo_textract.types.s3_object.serialize_cbor(
            value["s3_object"]
        )
    return out


def deserialize_cbor(data: dict) -> DocumentLocation:
    out: DocumentLocation = {}  # type: ignore[typeddict-item]
    if data.get("S3Object") is not None:
        import capo_textract.types.s3_object

        out["s3_object"] = capo_textract.types.s3_object.deserialize_cbor(
            data["S3Object"]
        )
    return out
