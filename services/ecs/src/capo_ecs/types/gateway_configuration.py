"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError, SerializationError
from capo_ecs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ecs.types.host_shared_alb_configuration


class _GatewayConfiguration_hostSharedAlb(TypedDict, closed=True):
    hostSharedAlb: (
        "capo_ecs.types.host_shared_alb_configuration.HostSharedAlbConfiguration"
    )


GatewayConfiguration: TypeAlias = (
    _GatewayConfiguration_hostSharedAlb | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GatewayConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "hostSharedAlb" in value:
        import capo_ecs.types.host_shared_alb_configuration

        return {
            "hostSharedAlb": capo_ecs.types.host_shared_alb_configuration.serialize_aws_json_1_1(
                value["hostSharedAlb"]
            )
        }
    else:
        raise SerializationError("GatewayConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> GatewayConfiguration:
    if data.get("hostSharedAlb") is not None:
        import capo_ecs.types.host_shared_alb_configuration

        return {
            "hostSharedAlb": capo_ecs.types.host_shared_alb_configuration.deserialize_aws_json_1_1(
                data["hostSharedAlb"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GatewayConfiguration: no recognized variant key")
