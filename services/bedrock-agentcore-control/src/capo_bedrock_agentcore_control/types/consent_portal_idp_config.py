"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConsentPortalIdpConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.allowed_audience_type
    import capo_bedrock_agentcore_control.types.allowed_scopes_type
    import capo_bedrock_agentcore_control.types.o_auth2_credential_provider_arn


class ConsentPortalIdpConfig(TypedDict, closed=True):
    credential_provider_arn: "capo_bedrock_agentcore_control.types.o_auth2_credential_provider_arn.OAuth2CredentialProviderArn"
    """<p>The Amazon Resource Name (ARN) of the OAuth2 credential provider used to authenticate end users to the consent portal.</p>"""
    scopes: "capo_bedrock_agentcore_control.types.allowed_scopes_type.AllowedScopesType"
    """<p>The OAuth2 scopes that the consent portal requests when authenticating end users.</p>"""
    audience: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_audience_type.AllowedAudienceType"
    ]
    """<p>The audience value that the consent portal includes when requesting tokens from the identity provider.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConsentPortalIdpConfig) -> dict:
    out: dict = {}
    out["credentialProviderArn"] = value["credential_provider_arn"]
    import capo_bedrock_agentcore_control.types.allowed_scopes_type

    out["scopes"] = (
        capo_bedrock_agentcore_control.types.allowed_scopes_type.serialize_json(
            value["scopes"]
        )
    )
    if "audience" in value:
        out["audience"] = value["audience"]
    return out


def deserialize_json(data: dict) -> ConsentPortalIdpConfig:
    out: ConsentPortalIdpConfig = {}  # type: ignore[typeddict-item]
    if data.get("credentialProviderArn") is not None:
        out["credential_provider_arn"] = data["credentialProviderArn"]
    else:
        out["credential_provider_arn"] = ""
    if data.get("scopes") is not None:
        import capo_bedrock_agentcore_control.types.allowed_scopes_type

        out["scopes"] = (
            capo_bedrock_agentcore_control.types.allowed_scopes_type.deserialize_json(
                data["scopes"]
            )
        )
    else:
        out["scopes"] = []
    if data.get("audience") is not None:
        out["audience"] = data["audience"]
    return out
