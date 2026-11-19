"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.enable_monitoring_dashboard
    import capo_network_firewall.types.logging_configuration
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class UpdateLoggingConfigurationRequest(TypedDict, closed=True):
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    firewall_name: NotRequired["capo_network_firewall.types.resource_name.ResourceName"]
    """<p>The descriptive name of the firewall. You can't change the name of a firewall after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    logging_configuration: NotRequired[
        "capo_network_firewall.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>Defines how Network Firewall performs logging for a firewall. If you omit this setting, Network Firewall disables logging for the firewall.</p>"""
    enable_monitoring_dashboard: NotRequired[
        "capo_network_firewall.types.enable_monitoring_dashboard.EnableMonitoringDashboard"
    ]
    """<p>A boolean that lets you enable or disable the detailed firewall monitoring dashboard on the firewall. </p> <p>The monitoring dashboard provides comprehensive visibility into your firewall's flow logs and alert logs. After you enable detailed monitoring, you can access these dashboards directly from the <b>Monitoring</b> page of the Network Firewall console.</p> <p> Specify <code>TRUE</code> to enable the the detailed monitoring dashboard on the firewall. Specify <code>FALSE</code> to disable the the detailed monitoring dashboard on the firewall. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateLoggingConfigurationRequest) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "logging_configuration" in value:
        import capo_network_firewall.types.logging_configuration

        out["LoggingConfiguration"] = (
            capo_network_firewall.types.logging_configuration.serialize_aws_json_1_0(
                value["logging_configuration"]
            )
        )
    if "enable_monitoring_dashboard" in value:
        out["EnableMonitoringDashboard"] = value["enable_monitoring_dashboard"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateLoggingConfigurationRequest:
    out: UpdateLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("LoggingConfiguration") is not None:
        import capo_network_firewall.types.logging_configuration

        out["logging_configuration"] = (
            capo_network_firewall.types.logging_configuration.deserialize_aws_json_1_0(
                data["LoggingConfiguration"]
            )
        )
    if data.get("EnableMonitoringDashboard") is not None:
        out["enable_monitoring_dashboard"] = data["EnableMonitoringDashboard"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateLoggingConfigurationRequest) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "firewall_name" in value:
        out["FirewallName"] = value["firewall_name"]
    if "logging_configuration" in value:
        import capo_network_firewall.types.logging_configuration

        out["LoggingConfiguration"] = (
            capo_network_firewall.types.logging_configuration.serialize_cbor(
                value["logging_configuration"]
            )
        )
    if "enable_monitoring_dashboard" in value:
        out["EnableMonitoringDashboard"] = value["enable_monitoring_dashboard"]
    return out


def deserialize_cbor(data: dict) -> UpdateLoggingConfigurationRequest:
    out: UpdateLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    if data.get("FirewallName") is not None:
        out["firewall_name"] = data["FirewallName"]
    if data.get("LoggingConfiguration") is not None:
        import capo_network_firewall.types.logging_configuration

        out["logging_configuration"] = (
            capo_network_firewall.types.logging_configuration.deserialize_cbor(
                data["LoggingConfiguration"]
            )
        )
    if data.get("EnableMonitoringDashboard") is not None:
        out["enable_monitoring_dashboard"] = data["EnableMonitoringDashboard"]
    return out
