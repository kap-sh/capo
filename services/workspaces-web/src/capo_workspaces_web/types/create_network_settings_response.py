"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateNetworkSettingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class CreateNetworkSettingsResponse(TypedDict, closed=True):
    network_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkSettingsResponse) -> dict:
    out: dict = {}
    out["networkSettingsArn"] = value["network_settings_arn"]
    return out


def deserialize_json(data: dict) -> CreateNetworkSettingsResponse:
    out: CreateNetworkSettingsResponse = {}  # type: ignore[typeddict-item]
    if data.get("networkSettingsArn") is not None:
        out["network_settings_arn"] = data["networkSettingsArn"]
    else:
        out["network_settings_arn"] = ""
    return out
