"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeGatewayRouteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class DescribeGatewayRouteRequest(TypedDict, closed=True):
    gateway_route_arn: "capo_ecs.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the gateway route to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGatewayRouteRequest) -> dict:
    out: dict = {}
    out["gatewayRouteArn"] = value["gateway_route_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGatewayRouteRequest:
    out: DescribeGatewayRouteRequest = {}  # type: ignore[typeddict-item]
    if data.get("gatewayRouteArn") is not None:
        out["gateway_route_arn"] = data["gatewayRouteArn"]
    else:
        out["gateway_route_arn"] = ""
    return out
