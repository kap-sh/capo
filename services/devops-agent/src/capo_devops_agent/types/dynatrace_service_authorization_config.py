"""Generated from Smithy shape ``com.amazonaws.devopsagent#DynatraceServiceAuthorizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.dynatrace_o_auth_client_credentials_config


class _DynatraceServiceAuthorizationConfig_oAuthClientCredentials(
    TypedDict, closed=True
):
    oAuthClientCredentials: "capo_devops_agent.types.dynatrace_o_auth_client_credentials_config.DynatraceOAuthClientCredentialsConfig"


DynatraceServiceAuthorizationConfig: TypeAlias = (
    _DynatraceServiceAuthorizationConfig_oAuthClientCredentials | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceServiceAuthorizationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DynatraceServiceAuthorizationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "oAuthClientCredentials" in value:
        import capo_devops_agent.types.dynatrace_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.dynatrace_o_auth_client_credentials_config.serialize_json(
                value["oAuthClientCredentials"]
            )
        }
    else:
        raise SerializationError(
            "DynatraceServiceAuthorizationConfig: no variant present"
        )


def deserialize_json(data: dict) -> DynatraceServiceAuthorizationConfig:
    if data.get("oAuthClientCredentials") is not None:
        import capo_devops_agent.types.dynatrace_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.dynatrace_o_auth_client_credentials_config.deserialize_json(
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
            "DynatraceServiceAuthorizationConfig: no recognized variant key"
        )
