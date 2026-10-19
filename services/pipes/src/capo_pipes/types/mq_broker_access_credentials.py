"""Generated from Smithy shape ``com.amazonaws.pipes#MQBrokerAccessCredentials``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_pipes.errors import DeserializationError, SerializationError
from capo_pipes.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_pipes.types.secret_manager_arn


class _MQBrokerAccessCredentials_BasicAuth(TypedDict, closed=True):
    BasicAuth: "capo_pipes.types.secret_manager_arn.SecretManagerArn"


MQBrokerAccessCredentials: TypeAlias = (
    _MQBrokerAccessCredentials_BasicAuth | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: MQBrokerAccessCredentials) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"MQBrokerAccessCredentials: cannot serialize unknown variant {value.name!r}"
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
            return UnknownUnionMember(name)
        raise DeserializationError(
            "MQBrokerAccessCredentials: no recognized variant key"
        )
