"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateUserSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class CreateUserSettingsResponse(TypedDict, closed=True):
    user_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserSettingsResponse) -> dict:
    out: dict = {}
    out["userSettingsArn"] = value["user_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateUserSettingsResponse:
    out: CreateUserSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("userSettingsArn") is not None:
        out["user_settings_arn"] = data["userSettingsArn"]
    else:
        out["user_settings_arn"] = ""
    return out
