"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayInfrastructureResources``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError, SerializationError
from capo_ecs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ecs.types.elb_gateway_resources_list


class _GatewayInfrastructureResources_hostSharedAlb(TypedDict, closed=True):
    hostSharedAlb: "capo_ecs.types.elb_gateway_resources_list.ElbGatewayResourcesList"


GatewayInfrastructureResources: TypeAlias = (
    _GatewayInfrastructureResources_hostSharedAlb | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayInfrastructureResources) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"GatewayInfrastructureResources: cannot serialize unknown variant {value.name!r}"
        )
    elif "hostSharedAlb" in value:
        import capo_ecs.types.elb_gateway_resources_list

        return {
            "hostSharedAlb": capo_ecs.types.elb_gateway_resources_list.serialize_aws_json_1_1(
                value["hostSharedAlb"]
            )
        }
    else:
        raise SerializationError("GatewayInfrastructureResources: no variant present")


def deserialize_aws_json_1_1(data: dict) -> GatewayInfrastructureResources:
    if data.get("hostSharedAlb") is not None:
        import capo_ecs.types.elb_gateway_resources_list

        return {
            "hostSharedAlb": capo_ecs.types.elb_gateway_resources_list.deserialize_aws_json_1_1(
                data["hostSharedAlb"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "GatewayInfrastructureResources: no recognized variant key"
        )
