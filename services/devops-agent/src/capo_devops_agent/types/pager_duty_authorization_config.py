"""Generated from Smithy shape ``com.amazonaws.devopsagent#PagerDutyAuthorizationConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.pager_duty_o_auth_client_credentials_config


class _PagerDutyAuthorizationConfig_oAuthClientCredentials(TypedDict, closed=True):
    oAuthClientCredentials: "capo_devops_agent.types.pager_duty_o_auth_client_credentials_config.PagerDutyOAuthClientCredentialsConfig"


PagerDutyAuthorizationConfig: TypeAlias = (
    _PagerDutyAuthorizationConfig_oAuthClientCredentials | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PagerDutyAuthorizationConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PagerDutyAuthorizationConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "oAuthClientCredentials" in value:
        import capo_devops_agent.types.pager_duty_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.pager_duty_o_auth_client_credentials_config.serialize_json(
                value["oAuthClientCredentials"]
            )
        }
    else:
        raise SerializationError("PagerDutyAuthorizationConfig: no variant present")


def deserialize_json(data: dict) -> PagerDutyAuthorizationConfig:
    if data.get("oAuthClientCredentials") is not None:
        import capo_devops_agent.types.pager_duty_o_auth_client_credentials_config

        return {
            "oAuthClientCredentials": capo_devops_agent.types.pager_duty_o_auth_client_credentials_config.deserialize_json(
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
            "PagerDutyAuthorizationConfig: no recognized variant key"
        )


def redact_sensitive(value: PagerDutyAuthorizationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oAuthClientCredentials" in value:
        import capo_devops_agent.types.pager_duty_o_auth_client_credentials_config

        out["oAuthClientCredentials"] = (
            capo_devops_agent.types.pager_duty_o_auth_client_credentials_config.redact_sensitive(
                value["oAuthClientCredentials"]
            )
        )
    return out
