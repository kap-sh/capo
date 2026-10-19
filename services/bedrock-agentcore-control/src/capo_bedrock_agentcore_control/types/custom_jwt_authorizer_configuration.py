"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CustomJWTAuthorizerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.advertised_scope_mapping_type
    import capo_bedrock_agentcore_control.types.allowed_audience_list
    import capo_bedrock_agentcore_control.types.allowed_clients_list
    import capo_bedrock_agentcore_control.types.allowed_scopes_type
    import capo_bedrock_agentcore_control.types.allowed_workload_configuration
    import capo_bedrock_agentcore_control.types.custom_claim_validations_type
    import capo_bedrock_agentcore_control.types.discovery_url
    import capo_bedrock_agentcore_control.types.private_endpoint
    import capo_bedrock_agentcore_control.types.private_endpoint_overrides


class CustomJWTAuthorizerConfiguration(TypedDict, closed=True):
    discovery_url: "capo_bedrock_agentcore_control.types.discovery_url.DiscoveryUrl"
    """<p>This URL is used to fetch OpenID Connect configuration or authorization server metadata for validating incoming tokens.</p>"""
    allowed_audience: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_audience_list.AllowedAudienceList"
    ]
    """<p>Represents individual audience values that are validated in the incoming JWT token validation process.</p>"""
    allowed_clients: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_clients_list.AllowedClientsList"
    ]
    """<p>Represents individual client IDs that are validated in the incoming JWT token validation process.</p>"""
    allowed_scopes: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_scopes_type.AllowedScopesType"
    ]
    """<p>An array of scopes that are allowed to access the token.</p>"""
    advertised_scope_mapping: NotRequired[
        "capo_bedrock_agentcore_control.types.advertised_scope_mapping_type.AdvertisedScopeMappingType"
    ]
    """<p>A map that associates each scope in <code>allowedScopes</code> with a corresponding advertised scope value. The advertised scope appears in OAuth protected resource metadata and <code>WWW-Authenticate</code> response headers. Use this parameter when the scope that clients request from your identity provider differs from the scope in the validated token. Each key is a scope from <code>allowedScopes</code> that the service uses for token validation. Each value is the corresponding scope that the service advertises to clients. Scopes without a mapping entry appear unchanged to clients.</p>"""
    custom_claims: NotRequired[
        "capo_bedrock_agentcore_control.types.custom_claim_validations_type.CustomClaimValidationsType"
    ]
    """<p>An array of objects that define a custom claim validation name, value, and operation </p>"""
    private_endpoint: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
    ]
    private_endpoint_overrides: NotRequired[
        "capo_bedrock_agentcore_control.types.private_endpoint_overrides.PrivateEndpointOverrides"
    ]
    """<p>The private endpoint overrides for the custom JWT authorizer configuration.</p>"""
    allowed_workload_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.allowed_workload_configuration.AllowedWorkloadConfiguration"
    ]
    """<p>The configuration that restricts which workloads in the request's identity chain are allowed to invoke the target, identified by their hosting environments and workload identities. At launch, this is supported only for AgentCore Runtime targets, and the allowed workloads are AgentCore Gateways.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomJWTAuthorizerConfiguration) -> dict:
    out: dict = {}
    out["discoveryUrl"] = value["discovery_url"]
    if "allowed_audience" in value:
        import capo_bedrock_agentcore_control.types.allowed_audience_list

        out["allowedAudience"] = (
            capo_bedrock_agentcore_control.types.allowed_audience_list.serialize_json(
                value["allowed_audience"]
            )
        )
    if "allowed_clients" in value:
        import capo_bedrock_agentcore_control.types.allowed_clients_list

        out["allowedClients"] = (
            capo_bedrock_agentcore_control.types.allowed_clients_list.serialize_json(
                value["allowed_clients"]
            )
        )
    if "allowed_scopes" in value:
        import capo_bedrock_agentcore_control.types.allowed_scopes_type

        out["allowedScopes"] = (
            capo_bedrock_agentcore_control.types.allowed_scopes_type.serialize_json(
                value["allowed_scopes"]
            )
        )
    if "advertised_scope_mapping" in value:
        import capo_bedrock_agentcore_control.types.advertised_scope_mapping_type

        out["advertisedScopeMapping"] = (
            capo_bedrock_agentcore_control.types.advertised_scope_mapping_type.serialize_json(
                value["advertised_scope_mapping"]
            )
        )
    if "custom_claims" in value:
        import capo_bedrock_agentcore_control.types.custom_claim_validations_type

        out["customClaims"] = (
            capo_bedrock_agentcore_control.types.custom_claim_validations_type.serialize_json(
                value["custom_claims"]
            )
        )
    if "private_endpoint" in value:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["privateEndpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.serialize_json(
                value["private_endpoint"]
            )
        )
    if "private_endpoint_overrides" in value:
        import capo_bedrock_agentcore_control.types.private_endpoint_overrides

        out["privateEndpointOverrides"] = (
            capo_bedrock_agentcore_control.types.private_endpoint_overrides.serialize_json(
                value["private_endpoint_overrides"]
            )
        )
    if "allowed_workload_configuration" in value:
        import capo_bedrock_agentcore_control.types.allowed_workload_configuration

        out["allowedWorkloadConfiguration"] = (
            capo_bedrock_agentcore_control.types.allowed_workload_configuration.serialize_json(
                value["allowed_workload_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomJWTAuthorizerConfiguration:
    out: CustomJWTAuthorizerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("discoveryUrl") is not None:
        out["discovery_url"] = data["discoveryUrl"]
    else:
        out["discovery_url"] = ""
    if data.get("allowedAudience") is not None:
        import capo_bedrock_agentcore_control.types.allowed_audience_list

        out["allowed_audience"] = (
            capo_bedrock_agentcore_control.types.allowed_audience_list.deserialize_json(
                data["allowedAudience"]
            )
        )
    if data.get("allowedClients") is not None:
        import capo_bedrock_agentcore_control.types.allowed_clients_list

        out["allowed_clients"] = (
            capo_bedrock_agentcore_control.types.allowed_clients_list.deserialize_json(
                data["allowedClients"]
            )
        )
    if data.get("allowedScopes") is not None:
        import capo_bedrock_agentcore_control.types.allowed_scopes_type

        out["allowed_scopes"] = (
            capo_bedrock_agentcore_control.types.allowed_scopes_type.deserialize_json(
                data["allowedScopes"]
            )
        )
    if data.get("advertisedScopeMapping") is not None:
        import capo_bedrock_agentcore_control.types.advertised_scope_mapping_type

        out["advertised_scope_mapping"] = (
            capo_bedrock_agentcore_control.types.advertised_scope_mapping_type.deserialize_json(
                data["advertisedScopeMapping"]
            )
        )
    if data.get("customClaims") is not None:
        import capo_bedrock_agentcore_control.types.custom_claim_validations_type

        out["custom_claims"] = (
            capo_bedrock_agentcore_control.types.custom_claim_validations_type.deserialize_json(
                data["customClaims"]
            )
        )
    if data.get("privateEndpoint") is not None:
        import capo_bedrock_agentcore_control.types.private_endpoint

        out["private_endpoint"] = (
            capo_bedrock_agentcore_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    if data.get("privateEndpointOverrides") is not None:
        import capo_bedrock_agentcore_control.types.private_endpoint_overrides

        out["private_endpoint_overrides"] = (
            capo_bedrock_agentcore_control.types.private_endpoint_overrides.deserialize_json(
                data["privateEndpointOverrides"]
            )
        )
    if data.get("allowedWorkloadConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.allowed_workload_configuration

        out["allowed_workload_configuration"] = (
            capo_bedrock_agentcore_control.types.allowed_workload_configuration.deserialize_json(
                data["allowedWorkloadConfiguration"]
            )
        )
    return out
