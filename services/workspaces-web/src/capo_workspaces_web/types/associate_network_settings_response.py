"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateNetworkSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateNetworkSettingsResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    network_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateNetworkSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["networkSettingsArn"] = value["network_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateNetworkSettingsResponse:
    out: AssociateNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("networkSettingsArn") is not None:
        out["network_settings_arn"] = data["networkSettingsArn"]
    else:
        out["network_settings_arn"] = ""
    return out
