"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateDataProtectionSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class CreateDataProtectionSettingsResponse(TypedDict, closed=True):
    data_protection_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the data protection settings resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataProtectionSettingsResponse) -> dict:
    out: dict = {}
    out["dataProtectionSettingsArn"] = value["data_protection_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateDataProtectionSettingsResponse:
    out: CreateDataProtectionSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataProtectionSettingsArn") is not None:
        out["data_protection_settings_arn"] = data["dataProtectionSettingsArn"]
    else:
        out["data_protection_settings_arn"] = ""
    return out
