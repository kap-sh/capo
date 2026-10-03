"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateVariableRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.string


class UpdateVariableRequest(TypedDict, closed=True):
    name: "capo_frauddetector.types.string.string"
    """<p>The name of the variable.</p>"""
    default_value: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The new default value of the variable.</p>"""
    description: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The new description.</p>"""
    variable_type: NotRequired["capo_frauddetector.types.string.string"]
    """<p>The variable type. For more information see <a href="https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types">Variable types</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateVariableRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "description" in value:
        out["description"] = value["description"]
    if "variable_type" in value:
        out["variableType"] = value["variable_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateVariableRequest:
    out: UpdateVariableRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateVariableRequest.name required")
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("variableType") is not None:
        out["variable_type"] = data["variableType"]
    return out
