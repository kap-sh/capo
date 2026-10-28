"""Generated from Smithy shape ``com.amazonaws.devopsagent#RemoteAgentAuthorizationConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.remote_agent_api_key_config
    import capo_devops_agent.types.remote_agent_bearer_token_config
    import capo_devops_agent.types.remote_agent_o_auth_client_credentials_config


class RemoteAgentAuthorizationConfigApiKeyMember(TypedDict, closed=True):
    apiKey: (
        "capo_devops_agent.types.remote_agent_api_key_config.RemoteAgentAPIKeyConfig"
    )


class RemoteAgentAuthorizationConfigOAuthClientCredentialsMember(
    TypedDict, closed=True
):
    oAuthClientCredentials: "capo_devops_agent.types.remote_agent_o_auth_client_credentials_config.RemoteAgentOAuthClientCredentialsConfig"


class RemoteAgentAuthorizationConfigBearerTokenMember(TypedDict, closed=True):
    bearerToken: "capo_devops_agent.types.remote_agent_bearer_token_config.RemoteAgentBearerTokenConfig"


RemoteAgentAuthorizationConfig: TypeAlias = (
    RemoteAgentAuthorizationConfigApiKeyMember
    | RemoteAgentAuthorizationConfigOAuthClientCredentialsMember
    | RemoteAgentAuthorizationConfigBearerTokenMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RemoteAgentAuthorizationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RemoteAgentAuthorizationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "apiKey" in value:
        import capo_devops_agent.types.remote_agent_api_key_config

        return {
            "apiKey": capo_devops_agent.types.remote_agent_api_key_config.serialize_json(
                value["apiKey"]
            )
        }
    elif "oAuthClientCredentials" in value:
        import capo_devops_agent.types.remote_agent_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.remote_agent_o_auth_client_credentials_config.serialize_json(
                value["oAuthClientCredentials"]
            )
        }
    elif "bearerToken" in value:
        import capo_devops_agent.types.remote_agent_bearer_token_config

        return {
            "bearerToken": capo_devops_agent.types.remote_agent_bearer_token_config.serialize_json(
                value["bearerToken"]
            )
        }
    else:
        raise SerializationError("RemoteAgentAuthorizationConfig: no variant present")


def deserialize_json(data: dict) -> RemoteAgentAuthorizationConfig:
    if data.get("apiKey") is not None:
        import capo_devops_agent.types.remote_agent_api_key_config

        return {
            "apiKey": capo_devops_agent.types.remote_agent_api_key_config.deserialize_json(
                data["apiKey"]
            )
        }
    elif data.get("oAuthClientCredentials") is not None:
        import capo_devops_agent.types.remote_agent_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.remote_agent_o_auth_client_credentials_config.deserialize_json(
                data["oAuthClientCredentials"]
            )
        }
    elif data.get("bearerToken") is not None:
        import capo_devops_agent.types.remote_agent_bearer_token_config

        return {
            "bearerToken": capo_devops_agent.types.remote_agent_bearer_token_config.deserialize_json(
                data["bearerToken"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RemoteAgentAuthorizationConfig: no recognized variant key"
        )


def redact_sensitive(value: RemoteAgentAuthorizationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "apiKey" in value:
        import capo_devops_agent.types.remote_agent_api_key_config

        out["apiKey"] = (
            capo_devops_agent.types.remote_agent_api_key_config.redact_sensitive(
                value["apiKey"]
            )
        )
    if "oAuthClientCredentials" in value:
        import capo_devops_agent.types.remote_agent_o_auth_client_credentials_config

        out["oAuthClientCredentials"] = (
            capo_devops_agent.types.remote_agent_o_auth_client_credentials_config.redact_sensitive(
                value["oAuthClientCredentials"]
            )
        )
    if "bearerToken" in value:
        import capo_devops_agent.types.remote_agent_bearer_token_config

        out["bearerToken"] = (
            capo_devops_agent.types.remote_agent_bearer_token_config.redact_sensitive(
                value["bearerToken"]
            )
        )
    return out
