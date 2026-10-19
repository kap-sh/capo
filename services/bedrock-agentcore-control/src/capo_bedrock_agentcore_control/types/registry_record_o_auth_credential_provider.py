"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordOAuthCredentialProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.credential_provider_arn
    import capo_bedrock_agentcore_control.types.custom_parameter_map
    import capo_bedrock_agentcore_control.types.registry_record_o_auth_grant_type
    import capo_bedrock_agentcore_control.types.scope_list


class RegistryRecordOAuthCredentialProvider(TypedDict, closed=True):
    provider_arn: "capo_bedrock_agentcore_control.types.credential_provider_arn.CredentialProviderArn"
    """<p>The Amazon Resource Name (ARN) of the OAuth credential provider resource.</p>"""
    grant_type: NotRequired[
        "capo_bedrock_agentcore_control.types.registry_record_o_auth_grant_type.RegistryRecordOAuthGrantType"
    ]
    """<p>The OAuth grant type. Currently only <code>CLIENT_CREDENTIALS</code> is supported.</p>"""
    scopes: NotRequired["capo_bedrock_agentcore_control.types.scope_list.ScopeList"]
    """<p>The OAuth scopes to request during authentication.</p>"""
    custom_parameters: NotRequired[
        "capo_bedrock_agentcore_control.types.custom_parameter_map.CustomParameterMap"
    ]
    """<p>Additional custom parameters for the OAuth flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordOAuthCredentialProvider) -> dict:
    out: dict = {}
    out["providerArn"] = value["provider_arn"]
    if "grant_type" in value:
        import capo_bedrock_agentcore_control.types.registry_record_o_auth_grant_type

        out["grantType"] = (
            capo_bedrock_agentcore_control.types.registry_record_o_auth_grant_type.serialize_json(
                value["grant_type"]
            )
        )
    if "scopes" in value:
        import capo_bedrock_agentcore_control.types.scope_list

        out["scopes"] = capo_bedrock_agentcore_control.types.scope_list.serialize_json(
            value["scopes"]
        )
    if "custom_parameters" in value:
        import capo_bedrock_agentcore_control.types.custom_parameter_map

        out["customParameters"] = (
            capo_bedrock_agentcore_control.types.custom_parameter_map.serialize_json(
                value["custom_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegistryRecordOAuthCredentialProvider:
    out: RegistryRecordOAuthCredentialProvider = {}  # type: ignore[typeddict-item]
    if data.get("providerArn") is not None:
        out["provider_arn"] = data["providerArn"]
    else:
        out["provider_arn"] = ""
    if data.get("grantType") is not None:
        import capo_bedrock_agentcore_control.types.registry_record_o_auth_grant_type

        out["grant_type"] = (
            capo_bedrock_agentcore_control.types.registry_record_o_auth_grant_type.deserialize_json(
                data["grantType"]
            )
        )
    if data.get("scopes") is not None:
        import capo_bedrock_agentcore_control.types.scope_list

        out["scopes"] = (
            capo_bedrock_agentcore_control.types.scope_list.deserialize_json(
                data["scopes"]
            )
        )
    if data.get("customParameters") is not None:
        import capo_bedrock_agentcore_control.types.custom_parameter_map

        out["custom_parameters"] = (
            capo_bedrock_agentcore_control.types.custom_parameter_map.deserialize_json(
                data["customParameters"]
            )
        )
    return out
