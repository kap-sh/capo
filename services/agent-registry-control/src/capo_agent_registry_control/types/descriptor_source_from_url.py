"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#DescriptorSourceFromUrl``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.descriptor_source_url
    import capo_agent_registry_control.types.registry_record_credential_provider_configuration_list


class DescriptorSourceFromUrl(TypedDict, closed=True):
    url: "capo_agent_registry_control.types.descriptor_source_url.DescriptorSourceUrl"
    """<p>The URL from which the descriptor content is retrieved.</p>"""
    credential_provider_configurations: NotRequired[
        "capo_agent_registry_control.types.registry_record_credential_provider_configuration_list.RegistryRecordCredentialProviderConfigurationList"
    ]
    """<p>The credential providers used to authenticate when fetching descriptor content from the source URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescriptorSourceFromUrl) -> dict:
    out: dict = {}
    out["url"] = value["url"]
    if "credential_provider_configurations" in value:
        import capo_agent_registry_control.types.registry_record_credential_provider_configuration_list

        out["credentialProviderConfigurations"] = (
            capo_agent_registry_control.types.registry_record_credential_provider_configuration_list.serialize_json(
                value["credential_provider_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescriptorSourceFromUrl:
    out: DescriptorSourceFromUrl = {}  # type: ignore[typeddict-item]
    if data.get("url") is not None:
        out["url"] = data["url"]
    else:
        raise DeserializationError("DescriptorSourceFromUrl.url required")
    if data.get("credentialProviderConfigurations") is not None:
        import capo_agent_registry_control.types.registry_record_credential_provider_configuration_list

        out["credential_provider_configurations"] = (
            capo_agent_registry_control.types.registry_record_credential_provider_configuration_list.deserialize_json(
                data["credentialProviderConfigurations"]
            )
        )
    return out
