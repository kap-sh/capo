"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateBrowserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class AssociateBrowserSettingsResponse(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""
    browser_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the browser settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateBrowserSettingsResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["browserSettingsArn"] = value["browser_settings_arn"]
    return out


def deserialize_json(data: dict) -> AssociateBrowserSettingsResponse:
    out: AssociateBrowserSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("portalArn") is not None:
        out["portal_arn"] = data["portalArn"]
    else:
        out["portal_arn"] = ""
    if data.get("browserSettingsArn") is not None:
        out["browser_settings_arn"] = data["browserSettingsArn"]
    else:
        out["browser_settings_arn"] = ""
    return out
