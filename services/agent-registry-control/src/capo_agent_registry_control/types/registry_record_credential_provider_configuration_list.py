"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordCredentialProviderConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_record_credential_provider_configuration

RegistryRecordCredentialProviderConfigurationList: TypeAlias = list[
    "capo_agent_registry_control.types.registry_record_credential_provider_configuration.RegistryRecordCredentialProviderConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordCredentialProviderConfigurationList) -> list:
    import capo_agent_registry_control.types.registry_record_credential_provider_configuration

    out: list = []
    for item in value:
        out.append(
            capo_agent_registry_control.types.registry_record_credential_provider_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RegistryRecordCredentialProviderConfigurationList:
    import capo_agent_registry_control.types.registry_record_credential_provider_configuration

    out: RegistryRecordCredentialProviderConfigurationList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_agent_registry_control.types.registry_record_credential_provider_configuration.deserialize_json(
                item
            )
        )
    return out
