"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateIpAccessSettingsResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateIpAccessSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["ipAccessSettingsArn"] = value["ip_access_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateIpAccessSettingsResponse:
    out: AssociateIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("ipAccessSettingsArn") is not None:
        out["ip_access_settings_arn"] = data["ipAccessSettingsArn"]
    else:
        out["ip_access_settings_arn"] = ""
    return out
