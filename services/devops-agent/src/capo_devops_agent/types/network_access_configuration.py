"""Generated from Smithy shape ``com.amazonaws.devopsagent#NetworkAccessConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.private_network_access


class _NetworkAccessConfiguration_privateAccess(TypedDict, closed=True):
    privateAccess: "capo_devops_agent.types.private_network_access.PrivateNetworkAccess"


NetworkAccessConfiguration: TypeAlias = (
    _NetworkAccessConfiguration_privateAccess | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: NetworkAccessConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"NetworkAccessConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "privateAccess" in value:
        import capo_devops_agent.types.private_network_access

        return {
            "privateAccess": capo_devops_agent.types.private_network_access.serialize_json(
                value["privateAccess"]
            )
        }
    else:
        raise SerializationError("NetworkAccessConfiguration: no variant present")


def deserialize_json(data: dict) -> NetworkAccessConfiguration:
    if data.get("privateAccess") is not None:
        import capo_devops_agent.types.private_network_access

        return {
            "privateAccess": capo_devops_agent.types.private_network_access.deserialize_json(
                data["privateAccess"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "NetworkAccessConfiguration: no recognized variant key"
        )
