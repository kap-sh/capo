"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeGatewayConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError, SerializationError
from capo_ecs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ecs.types.describe_gateway_alb_configuration


class _DescribeGatewayConfiguration_hostSharedAlb(TypedDict, closed=True):
    hostSharedAlb: "capo_ecs.types.describe_gateway_alb_configuration.DescribeGatewayAlbConfiguration"


DescribeGatewayConfiguration: TypeAlias = (
    _DescribeGatewayConfiguration_hostSharedAlb | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGatewayConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"DescribeGatewayConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "hostSharedAlb" in value:
        import capo_ecs.types.describe_gateway_alb_configuration

        return {
            "hostSharedAlb": capo_ecs.types.describe_gateway_alb_configuration.serialize_aws_json_1_1(
                value["hostSharedAlb"]
            )
        }
    else:
        raise SerializationError("DescribeGatewayConfiguration: no variant present")


def deserialize_aws_json_1_1(data: dict) -> DescribeGatewayConfiguration:
    if data.get("hostSharedAlb") is not None:
        import capo_ecs.types.describe_gateway_alb_configuration

        return {
            "hostSharedAlb": capo_ecs.types.describe_gateway_alb_configuration.deserialize_aws_json_1_1(
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
            "DescribeGatewayConfiguration: no recognized variant key"
        )
