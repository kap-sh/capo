"""Generated from Smithy shape ``com.amazonaws.devopsagent#ServiceNowServiceAuthorizationConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.service_now_o_auth_client_credentials_config


class ServiceNowServiceAuthorizationConfigOAuthClientCredentialsMember(
    TypedDict, closed=True
):
    oAuthClientCredentials: "capo_devops_agent.types.service_now_o_auth_client_credentials_config.ServiceNowOAuthClientCredentialsConfig"


ServiceNowServiceAuthorizationConfig: TypeAlias = (
    ServiceNowServiceAuthorizationConfigOAuthClientCredentialsMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ServiceNowServiceAuthorizationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ServiceNowServiceAuthorizationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "oAuthClientCredentials" in value:
        import capo_devops_agent.types.service_now_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.service_now_o_auth_client_credentials_config.serialize_json(
                value["oAuthClientCredentials"]
            )
        }
    else:
        raise SerializationError(
            "ServiceNowServiceAuthorizationConfig: no variant present"
        )


def deserialize_json(data: dict) -> ServiceNowServiceAuthorizationConfig:
    if data.get("oAuthClientCredentials") is not None:
        import capo_devops_agent.types.service_now_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.service_now_o_auth_client_credentials_config.deserialize_json(
                data["oAuthClientCredentials"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ServiceNowServiceAuthorizationConfig: no recognized variant key"
        )


def redact_sensitive(value: ServiceNowServiceAuthorizationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oAuthClientCredentials" in value:
        import capo_devops_agent.types.service_now_o_auth_client_credentials_config

        out["oAuthClientCredentials"] = (
            capo_devops_agent.types.service_now_o_auth_client_credentials_config.redact_sensitive(
                value["oAuthClientCredentials"]
            )
        )
    return out
