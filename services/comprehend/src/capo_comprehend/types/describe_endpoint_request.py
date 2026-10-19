"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_comprehend.types.comprehend_endpoint_arn


class DescribeEndpointRequest(TypedDict, closed=True):
    endpoint_arn: "capo_comprehend.types.comprehend_endpoint_arn.ComprehendEndpointArn"
    """<p>The Amazon Resource Number (ARN) of the endpoint being described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointRequest) -> dict:
    out: dict = {}
    out["EndpointArn"] = value["endpoint_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointRequest:
    out: DescribeEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("EndpointArn") is not None:
        out["endpoint_arn"] = data["EndpointArn"]
    else:
        out["endpoint_arn"] = ""
    return out
