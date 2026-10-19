"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordCredentialProviderConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.registry_record_credential_provider_type
    import capo_agent_registry_control.types.registry_record_credential_provider_union


class RegistryRecordCredentialProviderConfiguration(TypedDict, closed=True):
    credential_provider_type: "capo_agent_registry_control.types.registry_record_credential_provider_type.RegistryRecordCredentialProviderType"
    """<p>The type of credential provider.</p>"""
    credential_provider: "capo_agent_registry_control.types.registry_record_credential_provider_union.RegistryRecordCredentialProviderUnion"
    """<p>The credential provider details corresponding to the specified credential provider type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordCredentialProviderConfiguration) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.registry_record_credential_provider_type

    out["credentialProviderType"] = (
        capo_agent_registry_control.types.registry_record_credential_provider_type.serialize_json(
            value["credential_provider_type"]
        )
    )
    import capo_agent_registry_control.types.registry_record_credential_provider_union

    out["credentialProvider"] = (
        capo_agent_registry_control.types.registry_record_credential_provider_union.serialize_json(
            value["credential_provider"]
        )
    )
    return out


def deserialize_json(data: dict) -> RegistryRecordCredentialProviderConfiguration:
    out: RegistryRecordCredentialProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("credentialProviderType") is not None:
        import capo_agent_registry_control.types.registry_record_credential_provider_type

        out["credential_provider_type"] = (
            capo_agent_registry_control.types.registry_record_credential_provider_type.deserialize_json(
                data["credentialProviderType"]
            )
        )
    else:
        import typing

        out["credential_provider_type"] = typing.cast(
            "capo_agent_registry_control.types.registry_record_credential_provider_type.RegistryRecordCredentialProviderType",
            "",
        )
    if data.get("credentialProvider") is not None:
        import capo_agent_registry_control.types.registry_record_credential_provider_union

        out["credential_provider"] = (
            capo_agent_registry_control.types.registry_record_credential_provider_union.deserialize_json(
                data["credentialProvider"]
            )
        )
    else:
        import capo_agent_registry_control.types._unknown

        out["credential_provider"] = (
            capo_agent_registry_control.types._unknown.UnknownUnionMember("")
        )
    return out
