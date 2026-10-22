"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeGatewayResourcesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_resources
    import capo_ecs.types.string


class DescribeGatewayResourcesResponse(TypedDict, closed=True):
    gateway_resources: NotRequired["capo_ecs.types.gateway_resources.GatewayResources"]
    """<p>The infrastructure resources that the gateway manages, grouped by gateway type.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future request to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGatewayResourcesResponse) -> dict:
    out: dict = {}
    if "gateway_resources" in value:
        import capo_ecs.types.gateway_resources

        out["gatewayResources"] = (
            capo_ecs.types.gateway_resources.serialize_aws_json_1_1(
                value["gateway_resources"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGatewayResourcesResponse:
    out: DescribeGatewayResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayResources") is not None:
        import capo_ecs.types.gateway_resources

        out["gateway_resources"] = (
            capo_ecs.types.gateway_resources.deserialize_aws_json_1_1(
                data["gatewayResources"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
