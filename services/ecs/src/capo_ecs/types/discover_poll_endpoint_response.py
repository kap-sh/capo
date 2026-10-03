"""Generated from Smithy shape ``com.amazonaws.ecs#DiscoverPollEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class DiscoverPollEndpointResponse(TypedDict, closed=True):
    endpoint: NotRequired["capo_ecs.types.string.String"]
    """<p>The endpoint for the Amazon ECS agent to poll.</p>"""
    telemetry_endpoint: NotRequired["capo_ecs.types.string.String"]
    """<p>The telemetry endpoint for the Amazon ECS agent.</p>"""
    service_connect_endpoint: NotRequired["capo_ecs.types.string.String"]
    """<p>The endpoint for the Amazon ECS agent to poll for Service Connect configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html">Service Connect</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverPollEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        out["endpoint"] = value["endpoint"]
    if "telemetry_endpoint" in value:
        out["telemetryEndpoint"] = value["telemetry_endpoint"]
    if "service_connect_endpoint" in value:
        out["serviceConnectEndpoint"] = value["service_connect_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverPollEndpointResponse:
    out: DiscoverPollEndpointResponse = {}  # type: ignore[typeddict-item]
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    if data.get("telemetryEndpoint") is not None:
        out["telemetry_endpoint"] = data["telemetryEndpoint"]
    if data.get("serviceConnectEndpoint") is not None:
        out["service_connect_endpoint"] = data["serviceConnectEndpoint"]
    return out
