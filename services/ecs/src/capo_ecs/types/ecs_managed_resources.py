"""Generated from Smithy shape ``com.amazonaws.ecs#ECSManagedResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_connection_list
    import capo_ecs.types.managed_auto_scaling
    import capo_ecs.types.managed_ingress_paths
    import capo_ecs.types.managed_log_groups
    import capo_ecs.types.managed_metric_alarms
    import capo_ecs.types.managed_security_groups


class ECSManagedResources(TypedDict, closed=True):
    ingress_paths: NotRequired[
        "capo_ecs.types.managed_ingress_paths.ManagedIngressPaths"
    ]
    """<p>The ingress paths and endpoints for the Express service.</p>"""
    auto_scaling: NotRequired["capo_ecs.types.managed_auto_scaling.ManagedAutoScaling"]
    """<p>The auto-scaling configuration and policies for the Express service.</p>"""
    metric_alarms: NotRequired[
        "capo_ecs.types.managed_metric_alarms.ManagedMetricAlarms"
    ]
    """<p>The CloudWatch metric alarms associated with the Express service.</p>"""
    service_security_groups: NotRequired[
        "capo_ecs.types.managed_security_groups.ManagedSecurityGroups"
    ]
    """<p>The security groups managed by the Express service.</p>"""
    log_groups: NotRequired["capo_ecs.types.managed_log_groups.ManagedLogGroups"]
    """<p>The log groups managed by the Express service.</p>"""
    gateway_connections: NotRequired[
        "capo_ecs.types.gateway_connection_list.GatewayConnectionList"
    ]
    """<p>The gateway-managed connections for the service revision, including the gateway routes and infrastructure that a gateway created for the service's connector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSManagedResources) -> dict:
    out: dict = {}
    if "ingress_paths" in value:
        import capo_ecs.types.managed_ingress_paths

        out["ingressPaths"] = (
            capo_ecs.types.managed_ingress_paths.serialize_aws_json_1_1(
                value["ingress_paths"]
            )
        )
    if "auto_scaling" in value:
        import capo_ecs.types.managed_auto_scaling

        out["autoScaling"] = capo_ecs.types.managed_auto_scaling.serialize_aws_json_1_1(
            value["auto_scaling"]
        )
    if "metric_alarms" in value:
        import capo_ecs.types.managed_metric_alarms

        out["metricAlarms"] = (
            capo_ecs.types.managed_metric_alarms.serialize_aws_json_1_1(
                value["metric_alarms"]
            )
        )
    if "service_security_groups" in value:
        import capo_ecs.types.managed_security_groups

        out["serviceSecurityGroups"] = (
            capo_ecs.types.managed_security_groups.serialize_aws_json_1_1(
                value["service_security_groups"]
            )
        )
    if "log_groups" in value:
        import capo_ecs.types.managed_log_groups

        out["logGroups"] = capo_ecs.types.managed_log_groups.serialize_aws_json_1_1(
            value["log_groups"]
        )
    if "gateway_connections" in value:
        import capo_ecs.types.gateway_connection_list

        out["gatewayConnections"] = (
            capo_ecs.types.gateway_connection_list.serialize_aws_json_1_1(
                value["gateway_connections"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ECSManagedResources:
    out: ECSManagedResources = {}  # type: ignore[typeddict-item]
    if data.get("ingressPaths") is not None:
        import capo_ecs.types.managed_ingress_paths

        out["ingress_paths"] = (
            capo_ecs.types.managed_ingress_paths.deserialize_aws_json_1_1(
                data["ingressPaths"]
            )
        )
    if data.get("autoScaling") is not None:
        import capo_ecs.types.managed_auto_scaling

        out["auto_scaling"] = (
            capo_ecs.types.managed_auto_scaling.deserialize_aws_json_1_1(
                data["autoScaling"]
            )
        )
    if data.get("metricAlarms") is not None:
        import capo_ecs.types.managed_metric_alarms

        out["metric_alarms"] = (
            capo_ecs.types.managed_metric_alarms.deserialize_aws_json_1_1(
                data["metricAlarms"]
            )
        )
    if data.get("serviceSecurityGroups") is not None:
        import capo_ecs.types.managed_security_groups

        out["service_security_groups"] = (
            capo_ecs.types.managed_security_groups.deserialize_aws_json_1_1(
                data["serviceSecurityGroups"]
            )
        )
    if data.get("logGroups") is not None:
        import capo_ecs.types.managed_log_groups

        out["log_groups"] = capo_ecs.types.managed_log_groups.deserialize_aws_json_1_1(
            data["logGroups"]
        )
    if data.get("gatewayConnections") is not None:
        import capo_ecs.types.gateway_connection_list

        out["gateway_connections"] = (
            capo_ecs.types.gateway_connection_list.deserialize_aws_json_1_1(
                data["gatewayConnections"]
            )
        )
    return out
