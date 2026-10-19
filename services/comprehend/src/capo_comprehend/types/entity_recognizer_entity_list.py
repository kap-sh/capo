"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityRecognizerEntityList``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.s3_uri


class EntityRecognizerEntityList(TypedDict, closed=True):
    s3_uri: "capo_comprehend.types.s3_uri.S3Uri"
    """<p>Specifies the Amazon S3 location where the entity list is located. The URI must be in the same Region as the API endpoint that you are calling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityRecognizerEntityList) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EntityRecognizerEntityList:
    out: EntityRecognizerEntityList = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    return out
