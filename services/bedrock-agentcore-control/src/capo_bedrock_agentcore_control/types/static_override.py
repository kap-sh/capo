"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StaticOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.gateway_configuration_bundle_arn


class StaticOverride(TypedDict, closed=True):
    bundle_arn: "capo_bedrock_agentcore_control.types.gateway_configuration_bundle_arn.GatewayConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the configuration bundle to apply.</p>"""
    bundle_version: "str"
    """<p>The version of the configuration bundle to apply.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StaticOverride) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleVersion"] = value["bundle_version"]
    return out


def deserialize_json(data: dict) -> StaticOverride:
    out: StaticOverride = {}  # type: ignore[typeddict-item]
    if data.get("bundleArn") is not None:
        out["bundle_arn"] = data["bundleArn"]
    else:
        out["bundle_arn"] = ""
    if data.get("bundleVersion") is not None:
        out["bundle_version"] = data["bundleVersion"]
    else:
        out["bundle_version"] = ""
    return out
