"""Generated from Smithy shape ``com.amazonaws.ecs#DescribeGatewayAlbConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.gateway_alb_desync_mitigation_mode
    import capo_ecs.types.gateway_alb_protocol
    import capo_ecs.types.gateway_alb_test_traffic_rules
    import capo_ecs.types.gateway_elb_access_log_configuration
    import capo_ecs.types.gateway_elb_network_configuration
    import capo_ecs.types.gateway_elb_scheme
    import capo_ecs.types.string


class DescribeGatewayAlbConfiguration(TypedDict, closed=True):
    network_configuration: NotRequired[
        "capo_ecs.types.gateway_elb_network_configuration.GatewayElbNetworkConfiguration"
    ]
    """<p>The network configuration for the load balancers that the gateway manages.</p>"""
    scheme: NotRequired["capo_ecs.types.gateway_elb_scheme.GatewayElbScheme"]
    """<p>Specifies whether the load balancers the gateway manages are <code>internet-facing</code> or <code>internal</code>.</p>"""
    access_logs: NotRequired[
        "capo_ecs.types.gateway_elb_access_log_configuration.GatewayElbAccessLogConfiguration"
    ]
    """<p>The access log configuration for the load balancers that the gateway manages.</p>"""
    web_acl_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the WAF web ACL associated with the load balancers that the gateway manages.</p>"""
    port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port that the load balancer listener uses is 443. The gateway supports only HTTPS at port 443.</p>"""
    protocol: NotRequired["capo_ecs.types.gateway_alb_protocol.GatewayAlbProtocol"]
    """<p>The protocol for the load balancer listener is <code>HTTPS</code>. No other protocol is supported.</p>"""
    max_alb_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of Application Load Balancers that the gateway manages.</p>"""
    current_alb_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The current number of Application Load Balancers that the gateway has allocated.</p>"""
    http_desync: NotRequired[
        "capo_ecs.types.gateway_alb_desync_mitigation_mode.GatewayAlbDesyncMitigationMode"
    ]
    """<p>The desync mitigation mode for the load balancers that the gateway manages.</p>"""
    test_traffic_rules: NotRequired[
        "capo_ecs.types.gateway_alb_test_traffic_rules.GatewayAlbTestTrafficRules"
    ]
    """<p>The rules that route test traffic for progressive deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGatewayAlbConfiguration) -> dict:
    out: dict = {}
    if "network_configuration" in value:
        import capo_ecs.types.gateway_elb_network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.gateway_elb_network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "scheme" in value:
        import capo_ecs.types.gateway_elb_scheme

        out["scheme"] = capo_ecs.types.gateway_elb_scheme.serialize_aws_json_1_1(
            value["scheme"]
        )
    if "access_logs" in value:
        import capo_ecs.types.gateway_elb_access_log_configuration

        out["accessLogs"] = (
            capo_ecs.types.gateway_elb_access_log_configuration.serialize_aws_json_1_1(
                value["access_logs"]
            )
        )
    if "web_acl_arn" in value:
        out["webACLArn"] = value["web_acl_arn"]
    if "port" in value:
        out["port"] = value["port"]
    if "protocol" in value:
        import capo_ecs.types.gateway_alb_protocol

        out["protocol"] = capo_ecs.types.gateway_alb_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "max_alb_count" in value:
        out["maxAlbCount"] = value["max_alb_count"]
    if "current_alb_count" in value:
        out["currentAlbCount"] = value["current_alb_count"]
    if "http_desync" in value:
        import capo_ecs.types.gateway_alb_desync_mitigation_mode

        out["httpDesync"] = (
            capo_ecs.types.gateway_alb_desync_mitigation_mode.serialize_aws_json_1_1(
                value["http_desync"]
            )
        )
    if "test_traffic_rules" in value:
        import capo_ecs.types.gateway_alb_test_traffic_rules

        out["testTrafficRules"] = (
            capo_ecs.types.gateway_alb_test_traffic_rules.serialize_aws_json_1_1(
                value["test_traffic_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGatewayAlbConfiguration:
    out: DescribeGatewayAlbConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.gateway_elb_network_configuration

        out["network_configuration"] = (
            capo_ecs.types.gateway_elb_network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if data.get("scheme") is not None:
        import capo_ecs.types.gateway_elb_scheme

        out["scheme"] = capo_ecs.types.gateway_elb_scheme.deserialize_aws_json_1_1(
            data["scheme"]
        )
    if data.get("accessLogs") is not None:
        import capo_ecs.types.gateway_elb_access_log_configuration

        out["access_logs"] = (
            capo_ecs.types.gateway_elb_access_log_configuration.deserialize_aws_json_1_1(
                data["accessLogs"]
            )
        )
    if data.get("webACLArn") is not None:
        out["web_acl_arn"] = data["webACLArn"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("protocol") is not None:
        import capo_ecs.types.gateway_alb_protocol

        out["protocol"] = capo_ecs.types.gateway_alb_protocol.deserialize_aws_json_1_1(
            data["protocol"]
        )
    if data.get("maxAlbCount") is not None:
        out["max_alb_count"] = data["maxAlbCount"]
    if data.get("currentAlbCount") is not None:
        out["current_alb_count"] = data["currentAlbCount"]
    if data.get("httpDesync") is not None:
        import capo_ecs.types.gateway_alb_desync_mitigation_mode

        out["http_desync"] = (
            capo_ecs.types.gateway_alb_desync_mitigation_mode.deserialize_aws_json_1_1(
                data["httpDesync"]
            )
        )
    if data.get("testTrafficRules") is not None:
        import capo_ecs.types.gateway_alb_test_traffic_rules

        out["test_traffic_rules"] = (
            capo_ecs.types.gateway_alb_test_traffic_rules.deserialize_aws_json_1_1(
                data["testTrafficRules"]
            )
        )
    return out
