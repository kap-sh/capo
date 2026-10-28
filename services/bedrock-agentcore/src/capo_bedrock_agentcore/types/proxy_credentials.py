"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ProxyCredentials``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.basic_auth


class ProxyCredentialsBasicAuthMember(TypedDict, closed=True):
    basicAuth: "capo_bedrock_agentcore.types.basic_auth.BasicAuth"


ProxyCredentials: TypeAlias = ProxyCredentialsBasicAuthMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ProxyCredentials) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ProxyCredentials: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "basicAuth" in value:
        import capo_bedrock_agentcore.types.basic_auth

        return {
            "basicAuth": capo_bedrock_agentcore.types.basic_auth.serialize_json(
                value["basicAuth"]
            )
        }
    else:
        raise SerializationError("ProxyCredentials: no variant present")


def deserialize_json(data: dict) -> ProxyCredentials:
    if data.get("basicAuth") is not None:
        import capo_bedrock_agentcore.types.basic_auth

        return {
            "basicAuth": capo_bedrock_agentcore.types.basic_auth.deserialize_json(
                data["basicAuth"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ProxyCredentials: no recognized variant key")
