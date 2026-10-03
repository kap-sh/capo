"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateEndpointGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_global_accelerator.types.endpoint_configurations
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.health_check_interval_seconds
    import capo_global_accelerator.types.health_check_path
    import capo_global_accelerator.types.health_check_port
    import capo_global_accelerator.types.health_check_protocol
    import capo_global_accelerator.types.idempotency_token
    import capo_global_accelerator.types.port_overrides
    import capo_global_accelerator.types.threshold_count
    import capo_global_accelerator.types.traffic_dial_percentage


class CreateEndpointGroupRequest(TypedDict, closed=True):
    listener_arn: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the listener.</p>"""
    endpoint_group_region: "capo_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Web Services Region where the endpoint group is located. A listener can have only one endpoint group in a specific Region.</p>"""
    endpoint_configurations: NotRequired[
        "capo_global_accelerator.types.endpoint_configurations.EndpointConfigurations"
    ]
    """<p>The list of endpoint objects.</p>"""
    traffic_dial_percentage: NotRequired[
        "capo_global_accelerator.types.traffic_dial_percentage.TrafficDialPercentage"
    ]
    """<p>The percentage of traffic to send to an Amazon Web Services Region. Additional traffic is distributed to other endpoint groups for this listener. </p> <p>Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.</p> <p>The default value is 100.</p>"""
    health_check_port: NotRequired[
        "capo_global_accelerator.types.health_check_port.HealthCheckPort"
    ]
    """<p>The port that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If listener port is a list of ports, Global Accelerator uses the first port in the list.</p>"""
    health_check_protocol: NotRequired[
        "capo_global_accelerator.types.health_check_protocol.HealthCheckProtocol"
    ]
    """<p>The protocol that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.</p>"""
    health_check_path: NotRequired[
        "capo_global_accelerator.types.health_check_path.HealthCheckPath"
    ]
    """<p>If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).</p>"""
    health_check_interval_seconds: NotRequired[
        "capo_global_accelerator.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
    ]
    """<p>The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.</p>"""
    threshold_count: NotRequired[
        "capo_global_accelerator.types.threshold_count.ThresholdCount"
    ]
    """<p>The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</p>"""
    idempotency_token: (
        "capo_global_accelerator.types.idempotency_token.IdempotencyToken"
    )
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency—that is, the uniqueness—of the request.</p>"""
    port_overrides: NotRequired[
        "capo_global_accelerator.types.port_overrides.PortOverrides"
    ]
    """<p>Override specific listener ports used to route traffic to endpoints that are part of this endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html"> Overriding listener ports</a> in the <i>Global Accelerator Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointGroupRequest) -> dict:
    out: dict = {}
    out["ListenerArn"] = value["listener_arn"]
    out["EndpointGroupRegion"] = value["endpoint_group_region"]
    if "endpoint_configurations" in value:
        import capo_global_accelerator.types.endpoint_configurations

        out["EndpointConfigurations"] = (
            capo_global_accelerator.types.endpoint_configurations.serialize_aws_json_1_1(
                value["endpoint_configurations"]
            )
        )
    if "traffic_dial_percentage" in value:
        out["TrafficDialPercentage"] = (
            "NaN"
            if value["traffic_dial_percentage"] != value["traffic_dial_percentage"]
            else "Infinity"
            if value["traffic_dial_percentage"] == float("inf")
            else "-Infinity"
            if value["traffic_dial_percentage"] == float("-inf")
            else value["traffic_dial_percentage"]
        )
    if "health_check_port" in value:
        out["HealthCheckPort"] = value["health_check_port"]
    if "health_check_protocol" in value:
        import capo_global_accelerator.types.health_check_protocol

        out["HealthCheckProtocol"] = (
            capo_global_accelerator.types.health_check_protocol.serialize_aws_json_1_1(
                value["health_check_protocol"]
            )
        )
    if "health_check_path" in value:
        out["HealthCheckPath"] = value["health_check_path"]
    if "health_check_interval_seconds" in value:
        out["HealthCheckIntervalSeconds"] = value["health_check_interval_seconds"]
    if "threshold_count" in value:
        out["ThresholdCount"] = value["threshold_count"]
    out["IdempotencyToken"] = value["idempotency_token"]
    if "port_overrides" in value:
        import capo_global_accelerator.types.port_overrides

        out["PortOverrides"] = (
            capo_global_accelerator.types.port_overrides.serialize_aws_json_1_1(
                value["port_overrides"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointGroupRequest:
    out: CreateEndpointGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("ListenerArn") is not None:
        out["listener_arn"] = data["ListenerArn"]
    else:
        raise DeserializationError("CreateEndpointGroupRequest.listener_arn required")
    if data.get("EndpointGroupRegion") is not None:
        out["endpoint_group_region"] = data["EndpointGroupRegion"]
    else:
        raise DeserializationError(
            "CreateEndpointGroupRequest.endpoint_group_region required"
        )
    if data.get("EndpointConfigurations") is not None:
        import capo_global_accelerator.types.endpoint_configurations

        out["endpoint_configurations"] = (
            capo_global_accelerator.types.endpoint_configurations.deserialize_aws_json_1_1(
                data["EndpointConfigurations"]
            )
        )
    if data.get("TrafficDialPercentage") is not None:
        out["traffic_dial_percentage"] = float(data["TrafficDialPercentage"])
    if data.get("HealthCheckPort") is not None:
        out["health_check_port"] = data["HealthCheckPort"]
    if data.get("HealthCheckProtocol") is not None:
        import capo_global_accelerator.types.health_check_protocol

        out["health_check_protocol"] = (
            capo_global_accelerator.types.health_check_protocol.deserialize_aws_json_1_1(
                data["HealthCheckProtocol"]
            )
        )
    if data.get("HealthCheckPath") is not None:
        out["health_check_path"] = data["HealthCheckPath"]
    if data.get("HealthCheckIntervalSeconds") is not None:
        out["health_check_interval_seconds"] = data["HealthCheckIntervalSeconds"]
    if data.get("ThresholdCount") is not None:
        out["threshold_count"] = data["ThresholdCount"]
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "CreateEndpointGroupRequest.idempotency_token required"
        )
    if data.get("PortOverrides") is not None:
        import capo_global_accelerator.types.port_overrides

        out["port_overrides"] = (
            capo_global_accelerator.types.port_overrides.deserialize_aws_json_1_1(
                data["PortOverrides"]
            )
        )
    return out
