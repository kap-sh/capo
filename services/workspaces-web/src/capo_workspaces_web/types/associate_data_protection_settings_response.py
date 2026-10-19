"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateDataProtectionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateDataProtectionSettingsResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    data_protection_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the data protection settings resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateDataProtectionSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["dataProtectionSettingsArn"] = value["data_protection_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateDataProtectionSettingsResponse:
    out: AssociateDataProtectionSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("dataProtectionSettingsArn") is not None:
        out["data_protection_settings_arn"] = data["dataProtectionSettingsArn"]
    else:
        out["data_protection_settings_arn"] = ""
    return out
