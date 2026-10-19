"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ThemeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.theme_name
    import capo_amplifyuibuilder.types.uuid


class ThemeSummary(TypedDict, closed=True):
    app_id: "str"
    """<p>The unique ID for the app associated with the theme summary.</p>"""
    environment_name: "str"
    """<p>The name of the backend environment that is part of the Amplify app.</p>"""
    id: "capo_amplifyuibuilder.types.uuid.Uuid"
    """<p>The ID of the theme.</p>"""
    name: "capo_amplifyuibuilder.types.theme_name.ThemeName"
    """<p>The name of the theme.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThemeSummary) -> dict:
    out: dict = {}
    out["appId"] = value["app_id"]
    out["environmentName"] = value["environment_name"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ThemeSummary:
    out: ThemeSummary = {}  # type: ignore[typeddict-item]
    if data.get("appId") is not None:
        out["app_id"] = data["appId"]
    else:
        out["app_id"] = ""
    if data.get("environmentName") is not None:
        out["environment_name"] = data["environmentName"]
    else:
        out["environment_name"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
