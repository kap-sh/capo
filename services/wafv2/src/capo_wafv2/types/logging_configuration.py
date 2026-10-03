"""Generated from Smithy shape ``com.amazonaws.wafv2#LoggingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wafv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wafv2.types.boolean
    import capo_wafv2.types.log_destination_configs
    import capo_wafv2.types.log_scope
    import capo_wafv2.types.log_type
    import capo_wafv2.types.logging_filter
    import capo_wafv2.types.redacted_fields
    import capo_wafv2.types.resource_arn


class LoggingConfiguration(TypedDict, closed=True):
    resource_arn: "capo_wafv2.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the web ACL that you want to associate with <code>LogDestinationConfigs</code>.</p>"""
    log_destination_configs: (
        "capo_wafv2.types.log_destination_configs.LogDestinationConfigs"
    )
    """<p>The logging destination configuration that you want to associate with the web ACL.</p> <note> <p>You can associate one logging destination to a web ACL.</p> </note>"""
    redacted_fields: NotRequired["capo_wafv2.types.redacted_fields.RedactedFields"]
    """<p>The parts of the request that you want to keep out of the logs.</p> <p>For example, if you redact the <code>SingleHeader</code> field, the <code>HEADER</code> field in the logs will be <code>REDACTED</code> for all rules that use the <code>SingleHeader</code> <code>FieldToMatch</code> setting. </p> <p>If you configure data protection for the web ACL, the protection applies to the data that WAF sends to the logs. </p> <p>Redaction applies only to the component that's specified in the rule's <code>FieldToMatch</code> setting, so the <code>SingleHeader</code> redaction doesn't apply to rules that use the <code>Headers</code> <code>FieldToMatch</code>.</p> <note> <p>You can specify only the following fields for redaction: <code>UriPath</code>, <code>QueryString</code>, <code>SingleHeader</code>, and <code>Method</code>.</p> </note> <note> <p>This setting has no impact on request sampling. You can only exclude fields from request sampling by disabling sampling in the web ACL visibility configuration or by configuring data protection for the web ACL.</p> </note>"""
    managed_by_firewall_manager: "capo_wafv2.types.boolean.Boolean"
    """<p>Indicates whether the logging configuration was created by Firewall Manager, as part of an WAF policy configuration. If true, only Firewall Manager can modify or delete the configuration. </p> <p>The logging configuration can be created by Firewall Manager for use with any web ACL that Firewall Manager is using for an WAF policy. Web ACLs that Firewall Manager creates and uses have their <code>ManagedByFirewallManager</code> property set to true. Web ACLs that were created by a customer account and then retrofitted by Firewall Manager for use by a policy have their <code>RetrofittedByFirewallManager</code> property set to true. For either case, any corresponding logging configuration will indicate <code>ManagedByFirewallManager</code>.</p>"""
    logging_filter: NotRequired["capo_wafv2.types.logging_filter.LoggingFilter"]
    """<p>Filtering that specifies which web requests are kept in the logs and which are dropped. You can filter on the rule action and on the web request labels that were applied by matching rules during web ACL evaluation. </p>"""
    log_type: NotRequired["capo_wafv2.types.log_type.LogType"]
    """<p>Used to distinguish between various logging options. Currently, there is one option.</p> <p>Default: <code>WAF_LOGS</code> </p>"""
    log_scope: NotRequired["capo_wafv2.types.log_scope.LogScope"]
    """<p>The owner of the logging configuration, which must be set to <code>CUSTOMER</code> for the configurations that you manage. </p> <p>The log scope <code>SECURITY_LAKE</code> indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see <a href="https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html">Collecting data from Amazon Web Services services</a> in the <i>Amazon Security Lake user guide</i>. </p> <p>The log scope <code>CLOUDWATCH_TELEMETRY_RULE_MANAGED</code> indicates a configuration that is managed through Amazon CloudWatch Logs for telemetry data collection and analysis. For information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html">What is Amazon CloudWatch Logs ?</a> in the <i>Amazon CloudWatch Logs user guide</i>. </p> <p>Default: <code>CUSTOMER</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoggingConfiguration) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_wafv2.types.log_destination_configs

    out["LogDestinationConfigs"] = (
        capo_wafv2.types.log_destination_configs.serialize_aws_json_1_1(
            value["log_destination_configs"]
        )
    )
    if "redacted_fields" in value:
        import capo_wafv2.types.redacted_fields

        out["RedactedFields"] = capo_wafv2.types.redacted_fields.serialize_aws_json_1_1(
            value["redacted_fields"]
        )
    out["ManagedByFirewallManager"] = value.get("managed_by_firewall_manager", False)
    if "logging_filter" in value:
        import capo_wafv2.types.logging_filter

        out["LoggingFilter"] = capo_wafv2.types.logging_filter.serialize_aws_json_1_1(
            value["logging_filter"]
        )
    if "log_type" in value:
        import capo_wafv2.types.log_type

        out["LogType"] = capo_wafv2.types.log_type.serialize_aws_json_1_1(
            value["log_type"]
        )
    if "log_scope" in value:
        import capo_wafv2.types.log_scope

        out["LogScope"] = capo_wafv2.types.log_scope.serialize_aws_json_1_1(
            value["log_scope"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LoggingConfiguration:
    out: LoggingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        raise DeserializationError("LoggingConfiguration.resource_arn required")
    if data.get("LogDestinationConfigs") is not None:
        import capo_wafv2.types.log_destination_configs

        out["log_destination_configs"] = (
            capo_wafv2.types.log_destination_configs.deserialize_aws_json_1_1(
                data["LogDestinationConfigs"]
            )
        )
    else:
        raise DeserializationError(
            "LoggingConfiguration.log_destination_configs required"
        )
    if data.get("RedactedFields") is not None:
        import capo_wafv2.types.redacted_fields

        out["redacted_fields"] = (
            capo_wafv2.types.redacted_fields.deserialize_aws_json_1_1(
                data["RedactedFields"]
            )
        )
    if data.get("ManagedByFirewallManager") is not None:
        out["managed_by_firewall_manager"] = data["ManagedByFirewallManager"]
    else:
        out["managed_by_firewall_manager"] = False
    if data.get("LoggingFilter") is not None:
        import capo_wafv2.types.logging_filter

        out["logging_filter"] = (
            capo_wafv2.types.logging_filter.deserialize_aws_json_1_1(
                data["LoggingFilter"]
            )
        )
    if data.get("LogType") is not None:
        import capo_wafv2.types.log_type

        out["log_type"] = capo_wafv2.types.log_type.deserialize_aws_json_1_1(
            data["LogType"]
        )
    if data.get("LogScope") is not None:
        import capo_wafv2.types.log_scope

        out["log_scope"] = capo_wafv2.types.log_scope.deserialize_aws_json_1_1(
            data["LogScope"]
        )
    return out
