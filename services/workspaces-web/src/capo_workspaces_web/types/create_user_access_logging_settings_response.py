"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateUserAccessLoggingSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class CreateUserAccessLoggingSettingsResponse(TypedDict, closed=True):
    user_access_logging_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the user access logging settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserAccessLoggingSettingsResponse) -> dict:
    out: dict = {}
    out["userAccessLoggingSettingsArn"] = value["user_access_logging_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateUserAccessLoggingSettingsResponse:
    out: CreateUserAccessLoggingSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("userAccessLoggingSettingsArn") is not None:
        out["user_access_logging_settings_arn"] = data["userAccessLoggingSettingsArn"]
    else:
        out["user_access_logging_settings_arn"] = ""
    return out
