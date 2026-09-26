"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#AuthorizerConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.custom_jwt_authorizer_configuration


class _AuthorizerConfiguration_customJWTAuthorizer(TypedDict, closed=True):
    customJWTAuthorizer: "capo_agent_registry_control.types.custom_jwt_authorizer_configuration.CustomJWTAuthorizerConfiguration"


AuthorizerConfiguration: TypeAlias = _AuthorizerConfiguration_customJWTAuthorizer


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizerConfiguration) -> dict:
    if "customJWTAuthorizer" in value:
        import capo_agent_registry_control.types.custom_jwt_authorizer_configuration

        return {
            "customJWTAuthorizer": capo_agent_registry_control.types.custom_jwt_authorizer_configuration.serialize_json(
                value["customJWTAuthorizer"]
            )
        }
    else:
        raise SerializationError("AuthorizerConfiguration: no variant present")


def deserialize_json(data: dict) -> AuthorizerConfiguration:
    if data.get("customJWTAuthorizer") is not None:
        import capo_agent_registry_control.types.custom_jwt_authorizer_configuration

        return {
            "customJWTAuthorizer": capo_agent_registry_control.types.custom_jwt_authorizer_configuration.deserialize_json(
                data["customJWTAuthorizer"]
            )
        }
    else:
        raise DeserializationError("AuthorizerConfiguration: no recognized variant key")
