"""Generated from Smithy shape ``com.amazonaws.devopsagent#MCPServerAuthorizationConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.mcp_server_api_key_config
    import capo_devops_agent.types.mcp_server_authorization_discovery_config
    import capo_devops_agent.types.mcp_server_bearer_token_config
    import capo_devops_agent.types.mcp_server_o_auth3_lo_config
    import capo_devops_agent.types.mcp_server_o_auth_client_credentials_config


class _MCPServerAuthorizationConfig_oAuthClientCredentials(TypedDict, closed=True):
    oAuthClientCredentials: "capo_devops_agent.types.mcp_server_o_auth_client_credentials_config.MCPServerOAuthClientCredentialsConfig"


class _MCPServerAuthorizationConfig_oAuth3LO(TypedDict, closed=True):
    oAuth3LO: (
        "capo_devops_agent.types.mcp_server_o_auth3_lo_config.MCPServerOAuth3LOConfig"
    )


class _MCPServerAuthorizationConfig_apiKey(TypedDict, closed=True):
    apiKey: "capo_devops_agent.types.mcp_server_api_key_config.MCPServerAPIKeyConfig"


class _MCPServerAuthorizationConfig_bearerToken(TypedDict, closed=True):
    bearerToken: "capo_devops_agent.types.mcp_server_bearer_token_config.MCPServerBearerTokenConfig"


class _MCPServerAuthorizationConfig_authorizationDiscovery(TypedDict, closed=True):
    authorizationDiscovery: "capo_devops_agent.types.mcp_server_authorization_discovery_config.MCPServerAuthorizationDiscoveryConfig"


MCPServerAuthorizationConfig: TypeAlias = (
    _MCPServerAuthorizationConfig_oAuthClientCredentials
    | _MCPServerAuthorizationConfig_oAuth3LO
    | _MCPServerAuthorizationConfig_apiKey
    | _MCPServerAuthorizationConfig_bearerToken
    | _MCPServerAuthorizationConfig_authorizationDiscovery
)


# --- restJson1 ser/de ---
def serialize_json(value: MCPServerAuthorizationConfig) -> dict:
    if "oAuthClientCredentials" in value:
        import capo_devops_agent.types.mcp_server_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.mcp_server_o_auth_client_credentials_config.serialize_json(
                value["oAuthClientCredentials"]
            )
        }
    elif "oAuth3LO" in value:
        import capo_devops_agent.types.mcp_server_o_auth3_lo_config

        return {
            "oAuth3LO": capo_devops_agent.types.mcp_server_o_auth3_lo_config.serialize_json(
                value["oAuth3LO"]
            )
        }
    elif "apiKey" in value:
        import capo_devops_agent.types.mcp_server_api_key_config

        return {
            "apiKey": capo_devops_agent.types.mcp_server_api_key_config.serialize_json(
                value["apiKey"]
            )
        }
    elif "bearerToken" in value:
        import capo_devops_agent.types.mcp_server_bearer_token_config

        return {
            "bearerToken": capo_devops_agent.types.mcp_server_bearer_token_config.serialize_json(
                value["bearerToken"]
            )
        }
    elif "authorizationDiscovery" in value:
        import capo_devops_agent.types.mcp_server_authorization_discovery_config

        return {
            "authorizationDiscovery": capo_devops_agent.types.mcp_server_authorization_discovery_config.serialize_json(
                value["authorizationDiscovery"]
            )
        }
    else:
        raise SerializationError("MCPServerAuthorizationConfig: no variant present")


def deserialize_json(data: dict) -> MCPServerAuthorizationConfig:
    if data.get("oAuthClientCredentials") is not None:
        import capo_devops_agent.types.mcp_server_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.mcp_server_o_auth_client_credentials_config.deserialize_json(
                data["oAuthClientCredentials"]
            )
        }
    elif data.get("oAuth3LO") is not None:
        import capo_devops_agent.types.mcp_server_o_auth3_lo_config

        return {
            "oAuth3LO": capo_devops_agent.types.mcp_server_o_auth3_lo_config.deserialize_json(
                data["oAuth3LO"]
            )
        }
    elif data.get("apiKey") is not None:
        import capo_devops_agent.types.mcp_server_api_key_config

        return {
            "apiKey": capo_devops_agent.types.mcp_server_api_key_config.deserialize_json(
                data["apiKey"]
            )
        }
    elif data.get("bearerToken") is not None:
        import capo_devops_agent.types.mcp_server_bearer_token_config

        return {
            "bearerToken": capo_devops_agent.types.mcp_server_bearer_token_config.deserialize_json(
                data["bearerToken"]
            )
        }
    elif data.get("authorizationDiscovery") is not None:
        import capo_devops_agent.types.mcp_server_authorization_discovery_config

        return {
            "authorizationDiscovery": capo_devops_agent.types.mcp_server_authorization_discovery_config.deserialize_json(
                data["authorizationDiscovery"]
            )
        }
    else:
        raise DeserializationError(
            "MCPServerAuthorizationConfig: no recognized variant key"
        )


def redact_sensitive(value: MCPServerAuthorizationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oAuthClientCredentials" in value:
        import capo_devops_agent.types.mcp_server_o_auth_client_credentials_config

        out["oAuthClientCredentials"] = (
            capo_devops_agent.types.mcp_server_o_auth_client_credentials_config.redact_sensitive(
                value["oAuthClientCredentials"]
            )
        )
    if "oAuth3LO" in value:
        import capo_devops_agent.types.mcp_server_o_auth3_lo_config

        out["oAuth3LO"] = (
            capo_devops_agent.types.mcp_server_o_auth3_lo_config.redact_sensitive(
                value["oAuth3LO"]
            )
        )
    if "apiKey" in value:
        import capo_devops_agent.types.mcp_server_api_key_config

        out["apiKey"] = (
            capo_devops_agent.types.mcp_server_api_key_config.redact_sensitive(
                value["apiKey"]
            )
        )
    if "bearerToken" in value:
        import capo_devops_agent.types.mcp_server_bearer_token_config

        out["bearerToken"] = (
            capo_devops_agent.types.mcp_server_bearer_token_config.redact_sensitive(
                value["bearerToken"]
            )
        )
    return out
