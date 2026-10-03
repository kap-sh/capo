"""Generated from Smithy shape ``com.amazonaws.eventbridge#DescribeEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import capo_eventbridge.types.endpoint_name
    import capo_eventbridge.types.home_region


class DescribeEndpointRequest(TypedDict, closed=True):
    name: "capo_eventbridge.types.endpoint_name.EndpointName"
    """<p>The name of the endpoint you want to get information about. For example, <code>"Name":"us-east-2-custom_bus_A-endpoint"</code>.</p>"""
    home_region: NotRequired["capo_eventbridge.types.home_region.HomeRegion"]
    """<p>The primary Region of the endpoint you want to get information about. For example <code>"HomeRegion": "us-east-1"</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEndpointRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "home_region" in value:
        out["HomeRegion"] = value["home_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEndpointRequest:
    out: DescribeEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DescribeEndpointRequest.name required")
    if data.get("HomeRegion") is not None:
        out["home_region"] = data["HomeRegion"]
    return out
