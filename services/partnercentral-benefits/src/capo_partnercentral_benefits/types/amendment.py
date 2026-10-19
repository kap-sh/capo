"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Amendment``."""

from typing_extensions import TypedDict


class Amendment(TypedDict, closed=True):
    field_path: "str"
    """<p>The JSON path or field identifier specifying which field in the benefit application to modify.</p>"""
    new_value: "str"
    """<p>The new value to set for the specified field in the benefit application.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Amendment) -> dict:
    out: dict = {}
    out["FieldPath"] = value["field_path"]
    out["NewValue"] = value["new_value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Amendment:
    out: Amendment = {}  # type: ignore[typeddict-item]
    if data.get("FieldPath") is not None:
        out["field_path"] = data["FieldPath"]
    else:
        out["field_path"] = ""
    if data.get("NewValue") is not None:
        out["new_value"] = data["NewValue"]
    else:
        out["new_value"] = ""
    return out
