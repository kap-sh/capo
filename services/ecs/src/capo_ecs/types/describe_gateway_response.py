"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeGatewayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway


class DescribeGatewayResponse(TypedDict, closed=True):
    gateway: NotRequired["capo_ecs.types.gateway.Gateway"]
    """<p>The details of the gateway.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGatewayResponse) -> dict:
    out: dict = {}
    if "gateway" in value:
        import capo_ecs.types.gateway

        out["gateway"] = capo_ecs.types.gateway.serialize_aws_json_1_1(value["gateway"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGatewayResponse:
    out: DescribeGatewayResponse = {}  # type: ignore[typeddict-item]
    if data.get("gateway") is not None:
        import capo_ecs.types.gateway

        out["gateway"] = capo_ecs.types.gateway.deserialize_aws_json_1_1(
            data["gateway"]
        )
    return out
