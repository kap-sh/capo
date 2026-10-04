"""Generated from Smithy shape ``com.amazonaws.securityhub#RemediationParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.boolean
    import capo_securityhub.types.non_empty_string


class RemediationParameter(TypedDict, closed=True):
    name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the parameter.</p>"""
    type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of the parameter.</p>"""
    description: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A description of the parameter.</p>"""
    required: NotRequired["capo_securityhub.types.boolean.Boolean"]
    """<p>Specifies whether the parameter is required for running the guidance steps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemediationParameter) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "type" in value:
        out["Type"] = value["type"]
    if "description" in value:
        out["Description"] = value["description"]
    if "required" in value:
        out["Required"] = value["required"]
    return out


def deserialize_json(data: dict) -> RemediationParameter:
    out: RemediationParameter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Required") is not None:
        out["required"] = data["Required"]
    return out
