"""Generated from Smithy shape ``com.amazonaws.workspacesweb#BrowserSettingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class BrowserSettingsSummary(TypedDict, closed=True):
    browser_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the browser settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSettingsSummary) -> dict:
    out: dict = {}
    out["browserSettingsArn"] = value["browser_settings_arn"]
    return out


def deserialize_json(data: dict) -> BrowserSettingsSummary:
    out: BrowserSettingsSummary = {}  # type: ignore[typeddict-item]
    if data.get("browserSettingsArn") is not None:
        out["browser_settings_arn"] = data["browserSettingsArn"]
    else:
        out["browser_settings_arn"] = ""
    return out
