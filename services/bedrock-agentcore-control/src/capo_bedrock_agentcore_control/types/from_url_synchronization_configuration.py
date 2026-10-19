"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FromUrlSynchronizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.mcp_server_url
    import capo_bedrock_agentcore_control.types.registry_record_credential_provider_configuration_list


class FromUrlSynchronizationConfiguration(TypedDict, closed=True):
    url: "capo_bedrock_agentcore_control.types.mcp_server_url.McpServerUrl"
    """<p>The HTTPS URL of the MCP server to synchronize from.</p>"""
    credential_provider_configurations: NotRequired[
        "capo_bedrock_agentcore_control.types.registry_record_credential_provider_configuration_list.RegistryRecordCredentialProviderConfigurationList"
    ]
    """<p>Optional list of credential provider configurations for authenticating with the MCP server. At most one credential provider configuration can be specified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FromUrlSynchronizationConfiguration) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    if "credential_provider_configurations" in value:
        import capo_bedrock_agentcore_control.types.registry_record_credential_provider_configuration_list

        out["credentialProviderConfigurations"] = (
            capo_bedrock_agentcore_control.types.registry_record_credential_provider_configuration_list.serialize_json(
                value["credential_provider_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> FromUrlSynchronizationConfiguration:
    out: FromUrlSynchronizationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        out["url"] = ""
    if data.get("credentialProviderConfigurations") is not None:
        import capo_bedrock_agentcore_control.types.registry_record_credential_provider_configuration_list

        out["credential_provider_configurations"] = (
            capo_bedrock_agentcore_control.types.registry_record_credential_provider_configuration_list.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    return out
