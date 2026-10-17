"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.contact_flow_description
    import capo_connect.types.resource_version


class ContactFlowVersionSummary(TypedDict, closed=True):
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the view version.</p>"""
    version_description: NotRequired[
        "capo_connect.types.contact_flow_description.ContactFlowDescription"
    ]
    """<p>The description of the flow version.</p>"""
    version: NotRequired["capo_connect.types.resource_version.ResourceVersion"]
    """<p>The identifier of the flow version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowVersionSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "version_description" in value:
        out["VersionDescription"] = value["version_description"]
    if "version" in value:
        out["Version"] = value["version"]
    return out


def deserialize_json(data: dict) -> ContactFlowVersionSummary:
    out: ContactFlowVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("VersionDescription") is not None:
        out["version_description"] = data["VersionDescription"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    return out
