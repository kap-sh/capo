"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryDestinationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.cloudtrail_parameters
    import capo_observabilityadmin.types.destination_type
    import capo_observabilityadmin.types.elb_load_balancer_logging_parameters
    import capo_observabilityadmin.types.kms_key_arn
    import capo_observabilityadmin.types.log_delivery_parameters
    import capo_observabilityadmin.types.msk_monitoring_parameters
    import capo_observabilityadmin.types.retention_period_in_days
    import capo_observabilityadmin.types.vpc_flow_log_parameters
    import capo_observabilityadmin.types.waf_logging_parameters


class TelemetryDestinationConfiguration(TypedDict, closed=True):
    destination_type: NotRequired[
        "capo_observabilityadmin.types.destination_type.DestinationType"
    ]
    """<p> The type of destination for the telemetry data (e.g., "Amazon CloudWatch Logs", "S3"). </p>"""
    destination_pattern: NotRequired["str"]
    """<p> The pattern used to generate the destination path or name, supporting macros like &lt;resourceId&gt; and &lt;accountId&gt;. </p>"""
    retention_in_days: NotRequired[
        "capo_observabilityadmin.types.retention_period_in_days.RetentionPeriodInDays"
    ]
    """<p> The number of days to retain the telemetry data in the destination. </p>"""
    vpc_flow_log_parameters: NotRequired[
        "capo_observabilityadmin.types.vpc_flow_log_parameters.VPCFlowLogParameters"
    ]
    """<p> Configuration parameters specific to VPC Flow Logs when VPC is the resource type. </p>"""
    cloudtrail_parameters: NotRequired[
        "capo_observabilityadmin.types.cloudtrail_parameters.CloudtrailParameters"
    ]
    """<p> Configuration parameters specific to Amazon Web Services CloudTrail when CloudTrail is the source type. </p>"""
    elb_load_balancer_logging_parameters: NotRequired[
        "capo_observabilityadmin.types.elb_load_balancer_logging_parameters.ELBLoadBalancerLoggingParameters"
    ]
    """<p> Configuration parameters specific to ELB load balancer logging when ELB is the resource type. </p>"""
    waf_logging_parameters: NotRequired[
        "capo_observabilityadmin.types.waf_logging_parameters.WAFLoggingParameters"
    ]
    """<p> Configuration parameters specific to WAF logging when WAF is the resource type. </p>"""
    log_delivery_parameters: NotRequired[
        "capo_observabilityadmin.types.log_delivery_parameters.LogDeliveryParameters"
    ]
    """<p>The configuration parameters for log delivery when the resource type supports configurable log types, such as Amazon Bedrock Knowledge Bases or Elastic Load Balancing Application Load Balancers.</p>"""
    msk_monitoring_parameters: NotRequired[
        "capo_observabilityadmin.types.msk_monitoring_parameters.MskMonitoringParameters"
    ]
    """<p> Configuration parameters specific to MSK monitoring when MSK is the resource type. </p>"""
    kms_key_arn: NotRequired["capo_observabilityadmin.types.kms_key_arn.KmsKeyArn"]
    """<p> The Amazon Resource Name (ARN) of the customer-managed Amazon Web Services KMS key used to encrypt the log groups created during telemetry rule remediation. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryDestinationConfiguration) -> dict:
    out: dict = {}
    if "destination_type" in value:
        import capo_observabilityadmin.types.destination_type

        out["DestinationType"] = (
            capo_observabilityadmin.types.destination_type.serialize_json(
                value["destination_type"]
            )
        )
    if "destination_pattern" in value:
        out["DestinationPattern"] = value["destination_pattern"]
    if "retention_in_days" in value:
        out["RetentionInDays"] = value["retention_in_days"]
    if "vpc_flow_log_parameters" in value:
        import capo_observabilityadmin.types.vpc_flow_log_parameters

        out["VPCFlowLogParameters"] = (
            capo_observabilityadmin.types.vpc_flow_log_parameters.serialize_json(
                value["vpc_flow_log_parameters"]
            )
        )
    if "cloudtrail_parameters" in value:
        import capo_observabilityadmin.types.cloudtrail_parameters

        out["CloudtrailParameters"] = (
            capo_observabilityadmin.types.cloudtrail_parameters.serialize_json(
                value["cloudtrail_parameters"]
            )
        )
    if "elb_load_balancer_logging_parameters" in value:
        import capo_observabilityadmin.types.elb_load_balancer_logging_parameters

        out["ELBLoadBalancerLoggingParameters"] = (
            capo_observabilityadmin.types.elb_load_balancer_logging_parameters.serialize_json(
                value["elb_load_balancer_logging_parameters"]
            )
        )
    if "waf_logging_parameters" in value:
        import capo_observabilityadmin.types.waf_logging_parameters

        out["WAFLoggingParameters"] = (
            capo_observabilityadmin.types.waf_logging_parameters.serialize_json(
                value["waf_logging_parameters"]
            )
        )
    if "log_delivery_parameters" in value:
        import capo_observabilityadmin.types.log_delivery_parameters

        out["LogDeliveryParameters"] = (
            capo_observabilityadmin.types.log_delivery_parameters.serialize_json(
                value["log_delivery_parameters"]
            )
        )
    if "msk_monitoring_parameters" in value:
        import capo_observabilityadmin.types.msk_monitoring_parameters

        out["MskMonitoringParameters"] = (
            capo_observabilityadmin.types.msk_monitoring_parameters.serialize_json(
                value["msk_monitoring_parameters"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> TelemetryDestinationConfiguration:
    out: TelemetryDestinationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DestinationType") is not None:
        import capo_observabilityadmin.types.destination_type

        out["destination_type"] = (
            capo_observabilityadmin.types.destination_type.deserialize_json(
                data["DestinationType"]
            )
        )
    if data.get("DestinationPattern") is not None:
        out["destination_pattern"] = data["DestinationPattern"]
    if data.get("RetentionInDays") is not None:
        out["retention_in_days"] = data["RetentionInDays"]
    if data.get("VPCFlowLogParameters") is not None:
        import capo_observabilityadmin.types.vpc_flow_log_parameters

        out["vpc_flow_log_parameters"] = (
            capo_observabilityadmin.types.vpc_flow_log_parameters.deserialize_json(
                data["VPCFlowLogParameters"]
            )
        )
    if data.get("CloudtrailParameters") is not None:
        import capo_observabilityadmin.types.cloudtrail_parameters

        out["cloudtrail_parameters"] = (
            capo_observabilityadmin.types.cloudtrail_parameters.deserialize_json(
                data["CloudtrailParameters"]
            )
        )
    if data.get("ELBLoadBalancerLoggingParameters") is not None:
        import capo_observabilityadmin.types.elb_load_balancer_logging_parameters

        out["elb_load_balancer_logging_parameters"] = (
            capo_observabilityadmin.types.elb_load_balancer_logging_parameters.deserialize_json(
                data["ELBLoadBalancerLoggingParameters"]
            )
        )
    if data.get("WAFLoggingParameters") is not None:
        import capo_observabilityadmin.types.waf_logging_parameters

        out["waf_logging_parameters"] = (
            capo_observabilityadmin.types.waf_logging_parameters.deserialize_json(
                data["WAFLoggingParameters"]
            )
        )
    if data.get("LogDeliveryParameters") is not None:
        import capo_observabilityadmin.types.log_delivery_parameters

        out["log_delivery_parameters"] = (
            capo_observabilityadmin.types.log_delivery_parameters.deserialize_json(
                data["LogDeliveryParameters"]
            )
        )
    if data.get("MskMonitoringParameters") is not None:
        import capo_observabilityadmin.types.msk_monitoring_parameters

        out["msk_monitoring_parameters"] = (
            capo_observabilityadmin.types.msk_monitoring_parameters.deserialize_json(
                data["MskMonitoringParameters"]
            )
        )
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    return out
