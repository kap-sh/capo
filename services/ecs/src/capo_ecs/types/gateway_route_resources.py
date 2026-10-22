"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayRouteResources``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError, SerializationError
from capo_ecs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route_alb_resources_list


class _GatewayRouteResources_hostSharedAlb(TypedDict, closed=True):
    hostSharedAlb: (
        "capo_ecs.types.gateway_route_alb_resources_list.GatewayRouteAlbResourcesList"
    )


GatewayRouteResources: TypeAlias = (
    _GatewayRouteResources_hostSharedAlb | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayRouteResources) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"GatewayRouteResources: cannot serialize unknown variant {value.name!r}"
        )
    elif "hostSharedAlb" in value:
        import capo_ecs.types.gateway_route_alb_resources_list

        return {
            "hostSharedAlb": capo_ecs.types.gateway_route_alb_resources_list.serialize_aws_json_1_1(
                value["hostSharedAlb"]
            )
        }
    else:
        raise SerializationError("GatewayRouteResources: no variant present")


def deserialize_aws_json_1_1(data: dict) -> GatewayRouteResources:
    if data.get("hostSharedAlb") is not None:
        import capo_ecs.types.gateway_route_alb_resources_list

        return {
            "hostSharedAlb": capo_ecs.types.gateway_route_alb_resources_list.deserialize_aws_json_1_1(
                data["hostSharedAlb"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("GatewayRouteResources: no recognized variant key")
