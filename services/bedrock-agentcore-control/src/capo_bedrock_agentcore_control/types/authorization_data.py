"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AuthorizationData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.o_auth2_authorization_data


class AuthorizationDataOauth2Member(TypedDict, closed=True):
    oauth2: "capo_bedrock_agentcore_control.types.o_auth2_authorization_data.OAuth2AuthorizationData"


AuthorizationData: TypeAlias = AuthorizationDataOauth2Member | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AuthorizationData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "oauth2" in value:
        import capo_bedrock_agentcore_control.types.o_auth2_authorization_data

        return {
            "oauth2": capo_bedrock_agentcore_control.types.o_auth2_authorization_data.serialize_json(
                value["oauth2"]
            )
        }
    else:
        raise SerializationError("AuthorizationData: no variant present")


def deserialize_json(data: dict) -> AuthorizationData:
    if data.get("oauth2") is not None:
        import capo_bedrock_agentcore_control.types.o_auth2_authorization_data

        return {
            "oauth2": capo_bedrock_agentcore_control.types.o_auth2_authorization_data.deserialize_json(
                data["oauth2"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AuthorizationData: no recognized variant key")
