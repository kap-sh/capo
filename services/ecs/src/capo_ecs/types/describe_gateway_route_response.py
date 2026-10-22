"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeGatewayRouteResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_route


class DescribeGatewayRouteResponse(TypedDict, closed=True):
    gateway_route: NotRequired["capo_ecs.types.gateway_route.GatewayRoute"]
    """<p>The details of the gateway route.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGatewayRouteResponse) -> dict:
    out: dict = {}
    if "gateway_route" in value:
        import capo_ecs.types.gateway_route

        out["gatewayRoute"] = capo_ecs.types.gateway_route.serialize_aws_json_1_1(
            value["gateway_route"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGatewayRouteResponse:
    out: DescribeGatewayRouteResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayRoute") is not None:
        import capo_ecs.types.gateway_route

        out["gateway_route"] = capo_ecs.types.gateway_route.deserialize_aws_json_1_1(
            data["gatewayRoute"]
        )
    return out
