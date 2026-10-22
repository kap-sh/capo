"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayElbAccessLogDestination``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError, SerializationError
from capo_ecs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ecs.types.gateway_elb_access_log_s3_destination


class _GatewayElbAccessLogDestination_s3(TypedDict, closed=True):
    s3: "capo_ecs.types.gateway_elb_access_log_s3_destination.GatewayElbAccessLogS3Destination"


GatewayElbAccessLogDestination: TypeAlias = (
    _GatewayElbAccessLogDestination_s3 | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayElbAccessLogDestination) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"GatewayElbAccessLogDestination: cannot serialize unknown variant {value.name!r}"
        )
    elif "s3" in value:
        import capo_ecs.types.gateway_elb_access_log_s3_destination

        return {
            "s3": capo_ecs.types.gateway_elb_access_log_s3_destination.serialize_aws_json_1_1(
                value["s3"]
            )
        }
    else:
        raise SerializationError("GatewayElbAccessLogDestination: no variant present")


def deserialize_aws_json_1_1(data: dict) -> GatewayElbAccessLogDestination:
    if data.get("s3") is not None:
        import capo_ecs.types.gateway_elb_access_log_s3_destination

        return {
            "s3": capo_ecs.types.gateway_elb_access_log_s3_destination.deserialize_aws_json_1_1(
                data["s3"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "GatewayElbAccessLogDestination: no recognized variant key"
        )
