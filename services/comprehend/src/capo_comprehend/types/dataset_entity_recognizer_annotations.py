"""Generated from Smithy shape ``com.amazonaws.comprehend#DatasetEntityRecognizerAnnotations``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.s3_uri


class DatasetEntityRecognizerAnnotations(TypedDict, closed=True):
    s3_uri: "capo_comprehend.types.s3_uri.S3Uri"
    """<p> Specifies the Amazon S3 location where the training documents for an entity recognizer are located. The URI must be in the same Region as the API endpoint that you are calling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatasetEntityRecognizerAnnotations) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatasetEntityRecognizerAnnotations:
    out: DatasetEntityRecognizerAnnotations = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    return out
