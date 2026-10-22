"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateGatewayNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class UpdateGatewayNetworkConfiguration(TypedDict, closed=True):
    inbound_security_group: NotRequired["capo_ecs.types.string.String"]
    """<p>The ID of a security group that you provide to control inbound traffic to the load balancers that the gateway manages. When you specify a security group, the gateway doesn't create inbound rules on the security group it manages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGatewayNetworkConfiguration) -> dict:
    out: dict = {}
    if "inbound_security_group" in value:
        out["inboundSecurityGroup"] = value["inbound_security_group"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGatewayNetworkConfiguration:
    out: UpdateGatewayNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("inboundSecurityGroup") is not None:
        out["inbound_security_group"] = data["inboundSecurityGroup"]
    return out
