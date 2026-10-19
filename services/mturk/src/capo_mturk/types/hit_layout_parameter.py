"""Generated from Smithy shape ``com.amazonaws.mturk#HITLayoutParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.string


class HITLayoutParameter(TypedDict, closed=True):
    name: "capo_mturk.types.string.String"
    """<p> The name of the parameter in the HITLayout. </p>"""
    value: "capo_mturk.types.string.String"
    """<p>The value substituted for the parameter referenced in the HITLayout. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HITLayoutParameter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HITLayoutParameter:
    out: HITLayoutParameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
