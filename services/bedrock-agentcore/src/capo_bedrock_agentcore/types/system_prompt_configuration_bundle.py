"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SystemPromptConfigurationBundle``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.configuration_bundle_arn
    import capo_bedrock_agentcore.types.configuration_bundle_version_id


class SystemPromptConfigurationBundle(TypedDict, closed=True):
    bundle_arn: (
        "capo_bedrock_agentcore.types.configuration_bundle_arn.ConfigurationBundleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    version_id: "capo_bedrock_agentcore.types.configuration_bundle_version_id.ConfigurationBundleVersionId"
    """<p>The version identifier of the configuration bundle.</p>"""
    system_prompt_json_path: "str"
    """<p>The JSON path within the configuration bundle that contains the system prompt.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SystemPromptConfigurationBundle) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["versionId"] = value["version_id"]
    out["systemPromptJsonPath"] = value["system_prompt_json_path"]
    return out


def deserialize_json(data: dict) -> SystemPromptConfigurationBundle:
    out: SystemPromptConfigurationBundle = {}  # type: ignore[typeddict-item]
    if data.get("bundleArn") is not None:
        out["bundle_arn"] = data["bundleArn"]
    else:
        out["bundle_arn"] = ""
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        out["version_id"] = ""
    if data.get("systemPromptJsonPath") is not None:
        out["system_prompt_json_path"] = data["systemPromptJsonPath"]
    else:
        out["system_prompt_json_path"] = ""
    return out
