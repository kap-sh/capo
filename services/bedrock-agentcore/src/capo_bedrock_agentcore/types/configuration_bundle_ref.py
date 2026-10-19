"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ConfigurationBundleRef``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.configuration_bundle_arn
    import capo_bedrock_agentcore.types.configuration_bundle_version


class ConfigurationBundleRef(TypedDict, closed=True):
    bundle_arn: (
        "capo_bedrock_agentcore.types.configuration_bundle_arn.ConfigurationBundleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    bundle_version: "capo_bedrock_agentcore.types.configuration_bundle_version.ConfigurationBundleVersion"
    """<p>The version of the configuration bundle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleRef) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleVersion"] = value["bundle_version"]
    return out


def deserialize_json(data: dict) -> ConfigurationBundleRef:
    out: ConfigurationBundleRef = {}  # type: ignore[typeddict-item]
    if data.get("bundleArn") is not None:
        out["bundle_arn"] = data["bundleArn"]
    else:
        out["bundle_arn"] = ""
    if data.get("bundleVersion") is not None:
        out["bundle_version"] = data["bundleVersion"]
    else:
        out["bundle_version"] = ""
    return out
