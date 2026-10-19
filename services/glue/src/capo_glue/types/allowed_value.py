"""Generated from Smithy shape ``com.amazonaws.glue#AllowedValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.allowed_value_description_string
    import capo_glue.types.allowed_value_value_string


class AllowedValue(TypedDict, closed=True):
    description: NotRequired[
        "capo_glue.types.allowed_value_description_string.AllowedValueDescriptionString"
    ]
    """<p>A description of the allowed value.</p>"""
    value: "capo_glue.types.allowed_value_value_string.AllowedValueValueString"
    """<p>The value allowed for the property.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllowedValue) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AllowedValue:
    out: AllowedValue = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
