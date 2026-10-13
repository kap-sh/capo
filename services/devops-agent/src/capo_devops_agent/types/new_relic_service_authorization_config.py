"""Generated from Smithy shape ``com.amazonaws.devopsagent#NewRelicServiceAuthorizationConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.new_relic_api_key_config


class _NewRelicServiceAuthorizationConfig_apiKey(TypedDict, closed=True):
    apiKey: "capo_devops_agent.types.new_relic_api_key_config.NewRelicApiKeyConfig"


NewRelicServiceAuthorizationConfig: TypeAlias = (
    _NewRelicServiceAuthorizationConfig_apiKey
)


# --- restJson1 ser/de ---
def serialize_json(value: NewRelicServiceAuthorizationConfig) -> dict:
    if "apiKey" in value:
        import capo_devops_agent.types.new_relic_api_key_config

        return {
            "apiKey": capo_devops_agent.types.new_relic_api_key_config.serialize_json(
                value["apiKey"]
            )
        }
    else:
        raise SerializationError(
            "NewRelicServiceAuthorizationConfig: no variant present"
        )


def deserialize_json(data: dict) -> NewRelicServiceAuthorizationConfig:
    if data.get("apiKey") is not None:
        import capo_devops_agent.types.new_relic_api_key_config

        return {
            "apiKey": capo_devops_agent.types.new_relic_api_key_config.deserialize_json(
                data["apiKey"]
            )
        }
    else:
        raise DeserializationError(
            "NewRelicServiceAuthorizationConfig: no recognized variant key"
        )


def redact_sensitive(value: NewRelicServiceAuthorizationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "apiKey" in value:
        import capo_devops_agent.types.new_relic_api_key_config

        out["apiKey"] = (
            capo_devops_agent.types.new_relic_api_key_config.redact_sensitive(
                value["apiKey"]
            )
        )
    return out
