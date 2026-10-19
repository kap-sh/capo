"""Generated from Smithy shape ``com.amazonaws.eventbridge#Condition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.string


class Condition(TypedDict, closed=True):
    type: "capo_eventbridge.types.string.String"
    """<p>Specifies the type of condition. Currently the only supported value is <code>StringEquals</code>.</p>"""
    key: "capo_eventbridge.types.string.String"
    """<p>Specifies the key for the condition. Currently the only supported key is <code>aws:PrincipalOrgID</code>.</p>"""
    value: "capo_eventbridge.types.string.String"
    """<p>Specifies the value for the key. Currently, this must be the ID of the organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Condition) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    out["Key"] = value["key"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
