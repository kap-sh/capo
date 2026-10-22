"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateGatewayAlbConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.gateway_alb_desync_mitigation_mode
    import capo_ecs.types.gateway_alb_test_traffic_rules
    import capo_ecs.types.gateway_elb_access_log_configuration
    import capo_ecs.types.string
    import capo_ecs.types.update_gateway_network_configuration


class UpdateGatewayAlbConfiguration(TypedDict, closed=True):
    network_configuration: NotRequired[
        "capo_ecs.types.update_gateway_network_configuration.UpdateGatewayNetworkConfiguration"
    ]
    """<p>The mutable network configuration for the load balancers that the gateway manages.</p>"""
    max_alb_count: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of Application Load Balancers that the gateway manages.</p>"""
    web_acl_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the WAF web ACL to associate with the load balancers that the gateway manages.</p>"""
    access_logs: NotRequired[
        "capo_ecs.types.gateway_elb_access_log_configuration.GatewayElbAccessLogConfiguration"
    ]
    """<p>The access log configuration for the load balancers that the gateway manages.</p>"""
    http_desync: NotRequired[
        "capo_ecs.types.gateway_alb_desync_mitigation_mode.GatewayAlbDesyncMitigationMode"
    ]
    """<p>The desync mitigation mode for the load balancers that the gateway manages.</p>"""
    test_traffic_rules: NotRequired[
        "capo_ecs.types.gateway_alb_test_traffic_rules.GatewayAlbTestTrafficRules"
    ]
    """<p>The rules that route test traffic for progressive deployments.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGatewayAlbConfiguration) -> dict:
    out: dict = {}
    if "network_configuration" in value:
        import capo_ecs.types.update_gateway_network_configuration

        out["networkConfiguration"] = (
            capo_ecs.types.update_gateway_network_configuration.serialize_aws_json_1_1(
                value["network_configuration"]
            )
        )
    if "max_alb_count" in value:
        out["maxAlbCount"] = value["max_alb_count"]
    if "web_acl_arn" in value:
        out["webACLArn"] = value["web_acl_arn"]
    if "access_logs" in value:
        import capo_ecs.types.gateway_elb_access_log_configuration

        out["accessLogs"] = (
            capo_ecs.types.gateway_elb_access_log_configuration.serialize_aws_json_1_1(
                value["access_logs"]
            )
        )
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


def deserialize_aws_json_1_1(data: dict) -> UpdateGatewayAlbConfiguration:
    out: UpdateGatewayAlbConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("networkConfiguration") is not None:
        import capo_ecs.types.update_gateway_network_configuration

        out["network_configuration"] = (
            capo_ecs.types.update_gateway_network_configuration.deserialize_aws_json_1_1(
                data["networkConfiguration"]
            )
        )
    if data.get("maxAlbCount") is not None:
        out["max_alb_count"] = data["maxAlbCount"]
    if data.get("webACLArn") is not None:
        out["web_acl_arn"] = data["webACLArn"]
    if data.get("accessLogs") is not None:
        import capo_ecs.types.gateway_elb_access_log_configuration

        out["access_logs"] = (
            capo_ecs.types.gateway_elb_access_log_configuration.deserialize_aws_json_1_1(
                data["accessLogs"]
            )
        )
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
