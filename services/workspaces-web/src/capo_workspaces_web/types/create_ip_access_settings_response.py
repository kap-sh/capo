"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateIpAccessSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class CreateIpAccessSettingsResponse(TypedDict, closed=True):
    ip_access_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIpAccessSettingsResponse) -> dict:
    out: dict = {}
    out["ipAccessSettingsArn"] = value["ip_access_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateIpAccessSettingsResponse:
    out: CreateIpAccessSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ipAccessSettingsArn") is not None:
        out["ip_access_settings_arn"] = data["ipAccessSettingsArn"]
    else:
        out["ip_access_settings_arn"] = ""
    return out
