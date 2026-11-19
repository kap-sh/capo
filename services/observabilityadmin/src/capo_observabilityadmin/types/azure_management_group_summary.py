"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureManagementGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_management_group_id


class AzureManagementGroupSummary(TypedDict, closed=True):
    id: "capo_observabilityadmin.types.azure_management_group_id.AzureManagementGroupId"
    """<p>The ID of the management group.</p>"""
    name: NotRequired["str"]
    """<p>The name of the management group.</p>"""
    display_name: NotRequired["str"]
    """<p>The display name of the management group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureManagementGroupSummary) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> AzureManagementGroupSummary:
    out: AzureManagementGroupSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    return out
