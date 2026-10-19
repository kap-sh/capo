"""Generated from Smithy shape ``com.amazonaws.connect#UserProficiency``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.predefined_attribute_name
    import capo_connect.types.predefined_attribute_string_value
    import capo_connect.types.proficiency_level


class UserProficiency(TypedDict, closed=True):
    attribute_name: (
        "capo_connect.types.predefined_attribute_name.PredefinedAttributeName"
    )
    """<p>The name of user's proficiency. You must use name of predefined attribute present in the Connect Customer instance.</p>"""
    attribute_value: "capo_connect.types.predefined_attribute_string_value.PredefinedAttributeStringValue"
    """<p>The value of user's proficiency. You must use value of predefined attribute present in the Connect Customer instance.</p>"""
    level: "capo_connect.types.proficiency_level.ProficiencyLevel"
    """<p>The level of the proficiency. The valid values are 1, 2, 3, 4 and 5.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserProficiency) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    out["AttributeValue"] = value["attribute_value"]
    out["Level"] = (
        "NaN"
        if value.get("level", 1) != value.get("level", 1)
        else "Infinity"
        if value.get("level", 1) == float("inf")
        else "-Infinity"
        if value.get("level", 1) == float("-inf")
        else value.get("level", 1)
    )
    return out


def deserialize_json(data: dict) -> UserProficiency:
    out: UserProficiency = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("AttributeValue") is not None:
        out["attribute_value"] = data["AttributeValue"]
    else:
        out["attribute_value"] = ""
    if data.get("Level") is not None:
        out["level"] = float(data["Level"])
    else:
        out["level"] = 1
    return out
