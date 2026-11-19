"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.enable_monitoring_dashboard
    import capo_network_firewall.types.logging_configuration
    import capo_network_firewall.types.resource_arn


class DescribeLoggingConfigurationResponse(TypedDict, closed=True):
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    logging_configuration: NotRequired[
        "capo_network_firewall.types.logging_configuration.LoggingConfiguration"
    ]
    enable_monitoring_dashboard: NotRequired[
        "capo_network_firewall.types.enable_monitoring_dashboard.EnableMonitoringDashboard"
    ]
    """<p>A boolean that reflects whether or not the firewall monitoring dashboard is enabled on a firewall.</p> <p> Returns <code>TRUE</code> when the firewall monitoring dashboard is enabled on the firewall. Returns <code>FALSE</code> when the firewall monitoring dashboard is not enabled on the firewall. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeLoggingConfigurationResponse) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
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


def deserialize_aws_json_1_0(data: dict) -> DescribeLoggingConfigurationResponse:
    out: DescribeLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
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
def serialize_cbor(value: DescribeLoggingConfigurationResponse) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
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


def deserialize_cbor(data: dict) -> DescribeLoggingConfigurationResponse:
    out: DescribeLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
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
