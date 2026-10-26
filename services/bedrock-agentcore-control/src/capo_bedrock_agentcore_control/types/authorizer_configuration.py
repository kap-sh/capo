"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AuthorizerConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration


class _AuthorizerConfiguration_customJWTAuthorizer(TypedDict, closed=True):
    customJWTAuthorizer: "capo_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration.CustomJWTAuthorizerConfiguration"


AuthorizerConfiguration: TypeAlias = (
    _AuthorizerConfiguration_customJWTAuthorizer | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizerConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AuthorizerConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "customJWTAuthorizer" in value:
        import capo_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration

        return {
            "customJWTAuthorizer": capo_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration.serialize_json(
                value["customJWTAuthorizer"]
            )
        }
    else:
        raise SerializationError("AuthorizerConfiguration: no variant present")


def deserialize_json(data: dict) -> AuthorizerConfiguration:
    if data.get("customJWTAuthorizer") is not None:
        import capo_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration

        return {
            "customJWTAuthorizer": capo_bedrock_agentcore_control.types.custom_jwt_authorizer_configuration.deserialize_json(
                data["customJWTAuthorizer"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AuthorizerConfiguration: no recognized variant key")
