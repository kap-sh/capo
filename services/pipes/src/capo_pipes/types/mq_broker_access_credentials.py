"""Generated from Smithy shape ``com.amazonaws.pipes#MQBrokerAccessCredentials``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pipes.errors import DeserializationError, SerializationError
from capo_pipes.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_pipes.types.secret_manager_arn


class MQBrokerAccessCredentialsBasicAuthMember(TypedDict, closed=True):
    BasicAuth: "capo_pipes.types.secret_manager_arn.SecretManagerArn"


MQBrokerAccessCredentials: TypeAlias = (
    MQBrokerAccessCredentialsBasicAuthMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MQBrokerAccessCredentials) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MQBrokerAccessCredentials: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "BasicAuth" in value:
        return {"BasicAuth": value["BasicAuth"]}
    else:
        raise SerializationError("MQBrokerAccessCredentials: no variant present")


def deserialize_json(data: dict) -> MQBrokerAccessCredentials:
    if data.get("BasicAuth") is not None:
        return {"BasicAuth": data["BasicAuth"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "MQBrokerAccessCredentials: no recognized variant key"
        )
