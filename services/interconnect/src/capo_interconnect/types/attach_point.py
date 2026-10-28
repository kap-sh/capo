"""Generated from Smithy shape ``com.amazonaws.interconnect#AttachPoint``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_interconnect.errors import DeserializationError, SerializationError
from capo_interconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_interconnect.types.amazon_resource_name
    import capo_interconnect.types.direct_connect_gateway_attach_point


class AttachPointDirectConnectGatewayMember(TypedDict, closed=True):
    directConnectGateway: "capo_interconnect.types.direct_connect_gateway_attach_point.DirectConnectGatewayAttachPoint"


class AttachPointArnMember(TypedDict, closed=True):
    arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName"


AttachPoint: TypeAlias = (
    AttachPointDirectConnectGatewayMember | AttachPointArnMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachPoint) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AttachPoint: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "directConnectGateway" in value:
        return {"directConnectGateway": value["directConnectGateway"]}
    elif "arn" in value:
        return {"arn": value["arn"]}
    else:
        raise SerializationError("AttachPoint: no variant present")


def deserialize_aws_json_1_0(data: dict) -> AttachPoint:
    if data.get("directConnectGateway") is not None:
        return {"directConnectGateway": data["directConnectGateway"]}
    elif data.get("arn") is not None:
        return {"arn": data["arn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AttachPoint: no recognized variant key")
