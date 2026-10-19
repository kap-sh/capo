"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#DescribeCustomRoutingEndpointGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.generic_string


class DescribeCustomRoutingEndpointGroupRequest(TypedDict, closed=True):
    endpoint_group_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the endpoint group to describe.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCustomRoutingEndpointGroupRequest) -> dict:
    out: dict = {}
    out["EndpointGroupArn"] = value["endpoint_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCustomRoutingEndpointGroupRequest:
    out: DescribeCustomRoutingEndpointGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointGroupArn") is not None:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    else:
        out["endpoint_group_arn"] = ""
    return out
