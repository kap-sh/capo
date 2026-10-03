"""Generated from Smithy shape ``com.amazonaws.glue#CreateJsonClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_glue.errors import DeserializationError

if TYPE_CHECKING:
    import capo_glue.types.json_path
    import capo_glue.types.name_string


class CreateJsonClassifierRequest(TypedDict, closed=True):
    name: "capo_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    json_path: "capo_glue.types.json_path.JsonPath"
    """<p>A <code>JsonPath</code> string defining the JSON data for the classifier to classify. Glue supports a subset of JsonPath, as described in <a href="https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json">Writing JsonPath Custom Classifiers</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateJsonClassifierRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["JsonPath"] = value["json_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateJsonClassifierRequest:
    out: CreateJsonClassifierRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateJsonClassifierRequest.name required")
    if data.get("JsonPath") is not None:
        out["json_path"] = data["JsonPath"]
    else:
        raise DeserializationError("CreateJsonClassifierRequest.json_path required")
    return out
