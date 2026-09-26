"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordOAuthCredentialProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.credential_provider_arn
    import capo_agent_registry_control.types.custom_parameter_map
    import capo_agent_registry_control.types.registry_record_o_auth_grant_type
    import capo_agent_registry_control.types.scope_list


class RegistryRecordOAuthCredentialProvider(TypedDict, closed=True):
    provider_arn: "capo_agent_registry_control.types.credential_provider_arn.CredentialProviderArn"
    """<p>The Amazon Resource Name (ARN) of the OAuth 2.0 credential provider resource in Amazon Bedrock AgentCore Identity.</p>"""
    grant_type: NotRequired[
        "capo_agent_registry_control.types.registry_record_o_auth_grant_type.RegistryRecordOAuthGrantType"
    ]
    """<p>The OAuth 2.0 grant type used to obtain access tokens.</p>"""
    scopes: NotRequired["capo_agent_registry_control.types.scope_list.ScopeList"]
    """<p>The OAuth 2.0 scopes to request when obtaining access tokens.</p>"""
    custom_parameters: NotRequired[
        "capo_agent_registry_control.types.custom_parameter_map.CustomParameterMap"
    ]
    """<p>Additional parameters to include in the OAuth 2.0 token request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordOAuthCredentialProvider) -> dict:
    out: dict = {}
    out["providerArn"] = value["provider_arn"]
    if "grant_type" in value:
        import capo_agent_registry_control.types.registry_record_o_auth_grant_type

        out["grantType"] = (
            capo_agent_registry_control.types.registry_record_o_auth_grant_type.serialize_json(
                value["grant_type"]
            )
        )
    if "scopes" in value:
        import capo_agent_registry_control.types.scope_list

        out["scopes"] = capo_agent_registry_control.types.scope_list.serialize_json(
            value["scopes"]
        )
    if "custom_parameters" in value:
        import capo_agent_registry_control.types.custom_parameter_map

        out["customParameters"] = (
            capo_agent_registry_control.types.custom_parameter_map.serialize_json(
                value["custom_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> RegistryRecordOAuthCredentialProvider:
    out: RegistryRecordOAuthCredentialProvider = {}  # type: ignore[typeddict-item]
    if data.get("providerArn") is not None:
        out["provider_arn"] = data["providerArn"]
    else:
        raise DeserializationError(
            "RegistryRecordOAuthCredentialProvider.provider_arn required"
        )
    if data.get("grantType") is not None:
        import capo_agent_registry_control.types.registry_record_o_auth_grant_type

        out["grant_type"] = (
            capo_agent_registry_control.types.registry_record_o_auth_grant_type.deserialize_json(
                data["grantType"]
            )
        )
    if data.get("scopes") is not None:
        import capo_agent_registry_control.types.scope_list

        out["scopes"] = capo_agent_registry_control.types.scope_list.deserialize_json(
            data["scopes"]
        )
    if data.get("customParameters") is not None:
        import capo_agent_registry_control.types.custom_parameter_map

        out["custom_parameters"] = (
            capo_agent_registry_control.types.custom_parameter_map.deserialize_json(
                data["customParameters"]
            )
        )
    return out
