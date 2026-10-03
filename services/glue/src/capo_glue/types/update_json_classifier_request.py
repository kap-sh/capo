"""Generated from Smithy shape ``com.amazonaws.glue#UpdateJsonClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.json_path
    import capo_glue.types.name_string


class UpdateJsonClassifierRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    json_path: NotRequired["capo_glue.types.json_path.JsonPath"]
    """<p>A <code>JsonPath</code> string defining the JSON data for the classifier to classify. Glue supports a subset of JsonPath, as described in <a href="https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json">Writing JsonPath Custom Classifiers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJsonClassifierRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "json_path" in value:
        out["JsonPath"] = value["json_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJsonClassifierRequest:
    out: UpdateJsonClassifierRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateJsonClassifierRequest.name required")
    if data.get("JsonPath") is not None:
        out["json_path"] = data["JsonPath"]
    return out
