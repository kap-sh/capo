"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierDocuments``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.s3_uri


class DocumentClassifierDocuments(TypedDict, closed=True):
    s3_uri: "capo_comprehend.types.s3_uri.S3Uri"
    """<p>The S3 URI location of the training documents specified in the S3Uri CSV file.</p>"""
    test_s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p>The S3 URI location of the test documents included in the TestS3Uri CSV file. This field is not required if you do not specify a test CSV file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentClassifierDocuments) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "test_s3_uri" in value:
        out["TestS3Uri"] = value["test_s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentClassifierDocuments:
    out: DocumentClassifierDocuments = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("TestS3Uri") is not None:
        out["test_s3_uri"] = data["TestS3Uri"]
    return out
