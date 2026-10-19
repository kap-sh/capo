"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateUserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateUserSettingsResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    user_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateUserSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["userSettingsArn"] = value["user_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateUserSettingsResponse:
    out: AssociateUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("userSettingsArn") is not None:
        out["user_settings_arn"] = data["userSettingsArn"]
    else:
        out["user_settings_arn"] = ""
    return out
