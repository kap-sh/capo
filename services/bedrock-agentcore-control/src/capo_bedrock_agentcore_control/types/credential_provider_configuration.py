"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProviderConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credential_provider
    import capo_bedrock_agentcore_control.types.credential_provider_type


class CredentialProviderConfiguration(TypedDict, closed=True):
    credential_provider_type: "capo_bedrock_agentcore_control.types.credential_provider_type.CredentialProviderType"
    """<p>The type of credential provider. This field specifies which authentication method the gateway uses.</p>"""
    credential_provider: NotRequired[
        "capo_bedrock_agentcore_control.types.credential_provider.CredentialProvider"
    ]
    """<p>The credential provider. This field contains the specific configuration for the credential provider type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CredentialProviderConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.credential_provider_type

    out["credentialProviderType"] = (
        capo_bedrock_agentcore_control.types.credential_provider_type.serialize_json(
            value["credential_provider_type"]
        )
    )
    if "credential_provider" in value:
        import capo_bedrock_agentcore_control.types.credential_provider

        out["credentialProvider"] = (
            capo_bedrock_agentcore_control.types.credential_provider.serialize_json(
                value["credential_provider"]
            )
        )
    return out


def deserialize_json(data: dict) -> CredentialProviderConfiguration:
    out: CredentialProviderConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("credentialProviderType") is not None:
        import capo_bedrock_agentcore_control.types.credential_provider_type

        out["credential_provider_type"] = (
            capo_bedrock_agentcore_control.types.credential_provider_type.deserialize_json(
                data["credentialProviderType"]
            )
        )
    else:
        import typing

        out["credential_provider_type"] = typing.cast(
            "capo_bedrock_agentcore_control.types.credential_provider_type.CredentialProviderType",
            "",
        )
    if data.get("credentialProvider") is not None:
        import capo_bedrock_agentcore_control.types.credential_provider

        out["credential_provider"] = (
            capo_bedrock_agentcore_control.types.credential_provider.deserialize_json(
                data["credentialProvider"]
            )
        )
    return out


def redact_sensitive(value: CredentialProviderConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credential_provider" in value:
        import capo_bedrock_agentcore_control.types.credential_provider

        out["credential_provider"] = (
            capo_bedrock_agentcore_control.types.credential_provider.redact_sensitive(
                value["credential_provider"]
            )
        )
    return out
