"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateUserAccessLoggingSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateUserAccessLoggingSettingsResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    user_access_logging_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user access logging settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateUserAccessLoggingSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["userAccessLoggingSettingsArn"] = value["user_access_logging_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateUserAccessLoggingSettingsResponse:
    out: AssociateUserAccessLoggingSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("userAccessLoggingSettingsArn") is not None:
        out["user_access_logging_settings_arn"] = data["userAccessLoggingSettingsArn"]
    else:
        out["user_access_logging_settings_arn"] = ""
    return out
