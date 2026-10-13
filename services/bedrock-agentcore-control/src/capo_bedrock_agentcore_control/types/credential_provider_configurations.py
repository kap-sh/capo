"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProviderConfigurations``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credential_provider_configuration

CredentialProviderConfigurations: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.credential_provider_configuration.CredentialProviderConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialProviderConfigurations) -> list:
    import capo_bedrock_agentcore_control.types.credential_provider_configuration

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.credential_provider_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CredentialProviderConfigurations:
    import capo_bedrock_agentcore_control.types.credential_provider_configuration

    out: CredentialProviderConfigurations = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_agentcore_control.types.credential_provider_configuration.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: CredentialProviderConfigurations) -> list[Any]:
    import capo_bedrock_agentcore_control.types.credential_provider_configuration

    return [
        capo_bedrock_agentcore_control.types.credential_provider_configuration.redact_sensitive(
            item
        )
        for item in value
    ]
