"""Generated from Smithy shape ``com.amazonaws.workspacesweb#NetworkSettingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn
    import capo_workspaces_web.types.vpc_id


class NetworkSettingsSummary(TypedDict, closed=True):
    network_settings_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the network settings.</p>"""
    vpc_id: NotRequired["capo_workspaces_web.types.vpc_id.VpcId"]
    """<p>The VPC ID of the network settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSettingsSummary) -> dict:
    out: dict = {}
    out["networkSettingsArn"] = value["network_settings_arn"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> NetworkSettingsSummary:
    out: NetworkSettingsSummary = {}  # type: ignore[typeddict-item]
    if data.get("networkSettingsArn") is not None:
        out["network_settings_arn"] = data["networkSettingsArn"]
    else:
        out["network_settings_arn"] = ""
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    return out
