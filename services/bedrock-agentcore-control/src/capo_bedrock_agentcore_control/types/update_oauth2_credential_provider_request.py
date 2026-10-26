"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateOauth2CredentialProviderRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.credential_provider_vendor_type
    import capo_bedrock_agentcore_control.types.oauth2_provider_config_input


class UpdateOauth2CredentialProviderRequest(TypedDict, closed=True):
    name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName"
    """<p>The name of the OAuth2 credential provider to update.</p>"""
    credential_provider_vendor: "capo_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType"
    """<p>The vendor of the OAuth2 credential provider.</p>"""
    oauth2_provider_config_input: "capo_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput"
    """<p>The configuration input for the OAuth2 provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOauth2CredentialProviderRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agentcore_control.types.credential_provider_vendor_type

    out["credentialProviderVendor"] = (
        capo_bedrock_agentcore_control.types.credential_provider_vendor_type.serialize_json(
            value["credential_provider_vendor"]
        )
    )
    import capo_bedrock_agentcore_control.types.oauth2_provider_config_input

    out["oauth2ProviderConfigInput"] = (
        capo_bedrock_agentcore_control.types.oauth2_provider_config_input.serialize_json(
            value["oauth2_provider_config_input"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateOauth2CredentialProviderRequest:
    out: UpdateOauth2CredentialProviderRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("credentialProviderVendor") is not None:
        import capo_bedrock_agentcore_control.types.credential_provider_vendor_type

        out["credential_provider_vendor"] = (
            capo_bedrock_agentcore_control.types.credential_provider_vendor_type.deserialize_json(
                data["credentialProviderVendor"]
            )
        )
    else:
        import typing

        out["credential_provider_vendor"] = typing.cast(
            "capo_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
            "",
        )
    if data.get("oauth2ProviderConfigInput") is not None:
        import capo_bedrock_agentcore_control.types.oauth2_provider_config_input

        out["oauth2_provider_config_input"] = (
            capo_bedrock_agentcore_control.types.oauth2_provider_config_input.deserialize_json(
                data["oauth2ProviderConfigInput"]
            )
        )
    else:
        out["oauth2_provider_config_input"] = {"$unknown": {"name": ""}}
    return out


def redact_sensitive(value: UpdateOauth2CredentialProviderRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oauth2_provider_config_input" in value:
        import capo_bedrock_agentcore_control.types.oauth2_provider_config_input

        out["oauth2_provider_config_input"] = (
            capo_bedrock_agentcore_control.types.oauth2_provider_config_input.redact_sensitive(
                value["oauth2_provider_config_input"]
            )
        )
    return out
