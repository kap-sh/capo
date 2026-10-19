"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerAnnotations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.s3_uri


class EntityRecognizerAnnotations(TypedDict, closed=True):
    s3_uri: "capo_comprehend.types.s3_uri.S3Uri"
    """<p> Specifies the Amazon S3 location where the annotations for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>"""
    test_s3_uri: NotRequired["capo_comprehend.types.s3_uri.S3Uri"]
    """<p> Specifies the Amazon S3 location where the test annotations for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerAnnotations) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    if "test_s3_uri" in value:
        out["TestS3Uri"] = value["test_s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerAnnotations:
    out: EntityRecognizerAnnotations = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("TestS3Uri") is not None:
        out["test_s3_uri"] = data["TestS3Uri"]
    return out
