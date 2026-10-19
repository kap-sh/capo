"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionConfigurationBundle``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.configuration_bundle_arn
    import capo_bedrock_agentcore.types.configuration_bundle_tool_entry_list
    import capo_bedrock_agentcore.types.configuration_bundle_version_id


class ToolDescriptionConfigurationBundle(TypedDict, closed=True):
    bundle_arn: (
        "capo_bedrock_agentcore.types.configuration_bundle_arn.ConfigurationBundleArn"
    )
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    version_id: "capo_bedrock_agentcore.types.configuration_bundle_version_id.ConfigurationBundleVersionId"
    """<p>The version identifier of the configuration bundle.</p>"""
    tools: "capo_bedrock_agentcore.types.configuration_bundle_tool_entry_list.ConfigurationBundleToolEntryList"
    """<p>The list of tool entries mapping tool names to their JSON paths within the bundle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionConfigurationBundle) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["versionId"] = value["version_id"]
    import capo_bedrock_agentcore.types.configuration_bundle_tool_entry_list

    out["tools"] = (
        capo_bedrock_agentcore.types.configuration_bundle_tool_entry_list.serialize_json(
            value["tools"]
        )
    )
    return out


def deserialize_json(data: dict) -> ToolDescriptionConfigurationBundle:
    out: ToolDescriptionConfigurationBundle = {}  # type: ignore[typeddict-item]
    if data.get("bundleArn") is not None:
        out["bundle_arn"] = data["bundleArn"]
    else:
        out["bundle_arn"] = ""
    if data.get("versionId") is not None:
        out["version_id"] = data["versionId"]
    else:
        out["version_id"] = ""
    if data.get("tools") is not None:
        import capo_bedrock_agentcore.types.configuration_bundle_tool_entry_list

        out["tools"] = (
            capo_bedrock_agentcore.types.configuration_bundle_tool_entry_list.deserialize_json(
                data["tools"]
            )
        )
    else:
        out["tools"] = []
    return out
