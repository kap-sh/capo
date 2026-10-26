"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConnectionResources``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError, SerializationError
from capo_ecs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ecs.types.gateway_connection_alb_resources_list


class _GatewayConnectionResources_hostSharedAlb(TypedDict, closed=True):
    hostSharedAlb: "capo_ecs.types.gateway_connection_alb_resources_list.GatewayConnectionAlbResourcesList"


GatewayConnectionResources: TypeAlias = (
    _GatewayConnectionResources_hostSharedAlb | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConnectionResources) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GatewayConnectionResources: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "hostSharedAlb" in value:
        import capo_ecs.types.gateway_connection_alb_resources_list

        return {
            "hostSharedAlb": capo_ecs.types.gateway_connection_alb_resources_list.serialize_aws_json_1_1(
                value["hostSharedAlb"]
            )
        }
    else:
        raise SerializationError("GatewayConnectionResources: no variant present")


def deserialize_aws_json_1_1(data: dict) -> GatewayConnectionResources:
    if data.get("hostSharedAlb") is not None:
        import capo_ecs.types.gateway_connection_alb_resources_list

        return {
            "hostSharedAlb": capo_ecs.types.gateway_connection_alb_resources_list.deserialize_aws_json_1_1(
                data["hostSharedAlb"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "GatewayConnectionResources: no recognized variant key"
        )
