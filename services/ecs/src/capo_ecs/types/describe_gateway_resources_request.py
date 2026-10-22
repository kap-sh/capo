"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeGatewayResourcesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string


class DescribeGatewayResourcesRequest(TypedDict, closed=True):
    gateway: "capo_ecs.types.string.String"
    """<p>The name or Amazon Resource Name (ARN) of the gateway.</p>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of results that the operation returns in a single page. The maximum value is 20 and the default is 10.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGatewayResourcesRequest) -> dict:
    out: dict = {}
    out["gateway"] = value["gateway"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGatewayResourcesRequest:
    out: DescribeGatewayResourcesRequest = {}  # type: ignore[typeddict-item]
    if data.get("gateway") is not None:
        out["gateway"] = data["gateway"]
    else:
        out["gateway"] = ""
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
