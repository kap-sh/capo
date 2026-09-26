"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#CustomJWTAuthorizerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.allowed_audience_list
    import capo_agent_registry_control.types.allowed_clients_list
    import capo_agent_registry_control.types.allowed_scopes_type
    import capo_agent_registry_control.types.custom_claim_validations_type
    import capo_agent_registry_control.types.discovery_url
    import capo_agent_registry_control.types.private_endpoint
    import capo_agent_registry_control.types.private_endpoint_overrides


class CustomJWTAuthorizerConfiguration(TypedDict, closed=True):
    discovery_url: "capo_agent_registry_control.types.discovery_url.DiscoveryUrl"
    """<p>The OpenID Connect discovery URL used to retrieve the identity provider's metadata and signing keys.</p>"""
    allowed_audience: NotRequired[
        "capo_agent_registry_control.types.allowed_audience_list.AllowedAudienceList"
    ]
    """<p>The audience values accepted during JWT validation. A token is rejected if none of its audience claims match.</p>"""
    allowed_clients: NotRequired[
        "capo_agent_registry_control.types.allowed_clients_list.AllowedClientsList"
    ]
    """<p>The client identifiers accepted during JWT validation. A token is rejected if it was not issued to one of these clients.</p>"""
    allowed_scopes: NotRequired[
        "capo_agent_registry_control.types.allowed_scopes_type.AllowedScopesType"
    ]
    """<p>The scopes accepted during JWT validation. A token is rejected if it does not carry one of these scopes.</p>"""
    custom_claims: NotRequired[
        "capo_agent_registry_control.types.custom_claim_validations_type.CustomClaimValidationsType"
    ]
    """<p>Additional custom claim validations applied to the inbound JWT.</p>"""
    private_endpoint: NotRequired[
        "capo_agent_registry_control.types.private_endpoint.PrivateEndpoint"
    ]
    """<p>The private endpoint used to reach the identity provider's discovery URL over a private network path.</p>"""
    private_endpoint_overrides: NotRequired[
        "capo_agent_registry_control.types.private_endpoint_overrides.PrivateEndpointOverrides"
    ]
    """<p>Per-domain private endpoint overrides that route specific identity provider domains through distinct private endpoints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomJWTAuthorizerConfiguration) -> dict:
    out: dict = {}
    out["discoveryUrl"] = value["discovery_url"]
    if "allowed_audience" in value:
        import capo_agent_registry_control.types.allowed_audience_list

        out["allowedAudience"] = (
            capo_agent_registry_control.types.allowed_audience_list.serialize_json(
                value["allowed_audience"]
            )
        )
    if "allowed_clients" in value:
        import capo_agent_registry_control.types.allowed_clients_list

        out["allowedClients"] = (
            capo_agent_registry_control.types.allowed_clients_list.serialize_json(
                value["allowed_clients"]
            )
        )
    if "allowed_scopes" in value:
        import capo_agent_registry_control.types.allowed_scopes_type

        out["allowedScopes"] = (
            capo_agent_registry_control.types.allowed_scopes_type.serialize_json(
                value["allowed_scopes"]
            )
        )
    if "custom_claims" in value:
        import capo_agent_registry_control.types.custom_claim_validations_type

        out["customClaims"] = (
            capo_agent_registry_control.types.custom_claim_validations_type.serialize_json(
                value["custom_claims"]
            )
        )
    if "private_endpoint" in value:
        import capo_agent_registry_control.types.private_endpoint

        out["privateEndpoint"] = (
            capo_agent_registry_control.types.private_endpoint.serialize_json(
                value["private_endpoint"]
            )
        )
    if "private_endpoint_overrides" in value:
        import capo_agent_registry_control.types.private_endpoint_overrides

        out["privateEndpointOverrides"] = (
            capo_agent_registry_control.types.private_endpoint_overrides.serialize_json(
                value["private_endpoint_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomJWTAuthorizerConfiguration:
    out: CustomJWTAuthorizerConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("discoveryUrl") is not None:
        out["discovery_url"] = data["discoveryUrl"]
    else:
        raise DeserializationError(
            "CustomJWTAuthorizerConfiguration.discovery_url required"
        )
    if data.get("allowedAudience") is not None:
        import capo_agent_registry_control.types.allowed_audience_list

        out["allowed_audience"] = (
            capo_agent_registry_control.types.allowed_audience_list.deserialize_json(
                data["allowedAudience"]
            )
        )
    if data.get("allowedClients") is not None:
        import capo_agent_registry_control.types.allowed_clients_list

        out["allowed_clients"] = (
            capo_agent_registry_control.types.allowed_clients_list.deserialize_json(
                data["allowedClients"]
            )
        )
    if data.get("allowedScopes") is not None:
        import capo_agent_registry_control.types.allowed_scopes_type

        out["allowed_scopes"] = (
            capo_agent_registry_control.types.allowed_scopes_type.deserialize_json(
                data["allowedScopes"]
            )
        )
    if data.get("customClaims") is not None:
        import capo_agent_registry_control.types.custom_claim_validations_type

        out["custom_claims"] = (
            capo_agent_registry_control.types.custom_claim_validations_type.deserialize_json(
                data["customClaims"]
            )
        )
    if data.get("privateEndpoint") is not None:
        import capo_agent_registry_control.types.private_endpoint

        out["private_endpoint"] = (
            capo_agent_registry_control.types.private_endpoint.deserialize_json(
                data["privateEndpoint"]
            )
        )
    if data.get("privateEndpointOverrides") is not None:
        import capo_agent_registry_control.types.private_endpoint_overrides

        out["private_endpoint_overrides"] = (
            capo_agent_registry_control.types.private_endpoint_overrides.deserialize_json(
                data["privateEndpointOverrides"]
            )
        )
    return out
