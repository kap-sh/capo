"""Generated from Smithy shape ``com.amazonaws.datazone#CloudFormationProperties``."""

from typing_extensions import TypedDict


class CloudFormationProperties(TypedDict, closed=True):
    template_url: "str"
    """<p>The template URL of the cloud formation provisioning properties of the environment blueprint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudFormationProperties) -> dict:
    out: dict = {}
    out["templateUrl"] = value["template_url"]
    return out


def deserialize_json(data: dict) -> CloudFormationProperties:
    out: CloudFormationProperties = {}  # type: ignore[typeddict-item]
    if data.get("templateUrl") is not None:
        out["template_url"] = data["templateUrl"]
    else:
        out["template_url"] = ""
    return out
