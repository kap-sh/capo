"""Generated from Smithy shape ``com.amazonaws.rum#UpdateAppMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_configuration
    import capo_rum.types.app_monitor_domain
    import capo_rum.types.app_monitor_domain_list
    import capo_rum.types.app_monitor_name
    import capo_rum.types.custom_events
    import capo_rum.types.deobfuscation_configuration


class UpdateAppMonitorRequest(TypedDict, closed=True):
    name: "capo_rum.types.app_monitor_name.AppMonitorName"
    """<p>The name of the app monitor to update.</p>"""
    domain: NotRequired["capo_rum.types.app_monitor_domain.AppMonitorDomain"]
    """<p>The top-level internet domain name for which your application has administrative authority.</p>"""
    domain_list: NotRequired[
        "capo_rum.types.app_monitor_domain_list.AppMonitorDomainList"
    ]
    """<p> List the domain names for which your application has administrative authority. The <code>UpdateAppMonitor</code> allows either the domain or the domain list. </p>"""
    app_monitor_configuration: NotRequired[
        "capo_rum.types.app_monitor_configuration.AppMonitorConfiguration"
    ]
    """<p>A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include <code>AppMonitorConfiguration</code>, you must set up your own authorization method. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html">Authorize your application to send data to Amazon Web Services</a>.</p>"""
    cw_log_enabled: NotRequired["bool"]
    """<p>Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.</p>"""
    custom_events: NotRequired["capo_rum.types.custom_events.CustomEvents"]
    """<p>Specifies whether this app monitor allows the web client to define and send custom events. The default is for custom events to be <code>DISABLED</code>.</p> <p>For more information about custom events, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html">Send custom events</a>.</p>"""
    deobfuscation_configuration: NotRequired[
        "capo_rum.types.deobfuscation_configuration.DeobfuscationConfiguration"
    ]
    """<p> A structure that contains the configuration for how an app monitor can deobfuscate stack traces. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppMonitorRequest) -> dict:
    out: dict = {}
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "domain_list" in value:
        import capo_rum.types.app_monitor_domain_list

        out["DomainList"] = capo_rum.types.app_monitor_domain_list.serialize_json(
            value["domain_list"]
        )
    if "app_monitor_configuration" in value:
        import capo_rum.types.app_monitor_configuration

        out["AppMonitorConfiguration"] = (
            capo_rum.types.app_monitor_configuration.serialize_json(
                value["app_monitor_configuration"]
            )
        )
    if "cw_log_enabled" in value:
        out["CwLogEnabled"] = value["cw_log_enabled"]
    if "custom_events" in value:
        import capo_rum.types.custom_events

        out["CustomEvents"] = capo_rum.types.custom_events.serialize_json(
            value["custom_events"]
        )
    if "deobfuscation_configuration" in value:
        import capo_rum.types.deobfuscation_configuration

        out["DeobfuscationConfiguration"] = (
            capo_rum.types.deobfuscation_configuration.serialize_json(
                value["deobfuscation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAppMonitorRequest:
    out: UpdateAppMonitorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("DomainList") is not None:
        import capo_rum.types.app_monitor_domain_list

        out["domain_list"] = capo_rum.types.app_monitor_domain_list.deserialize_json(
            data["DomainList"]
        )
    if data.get("AppMonitorConfiguration") is not None:
        import capo_rum.types.app_monitor_configuration

        out["app_monitor_configuration"] = (
            capo_rum.types.app_monitor_configuration.deserialize_json(
                data["AppMonitorConfiguration"]
            )
        )
    if data.get("CwLogEnabled") is not None:
        out["cw_log_enabled"] = data["CwLogEnabled"]
    if data.get("CustomEvents") is not None:
        import capo_rum.types.custom_events

        out["custom_events"] = capo_rum.types.custom_events.deserialize_json(
            data["CustomEvents"]
        )
    if data.get("DeobfuscationConfiguration") is not None:
        import capo_rum.types.deobfuscation_configuration

        out["deobfuscation_configuration"] = (
            capo_rum.types.deobfuscation_configuration.deserialize_json(
                data["DeobfuscationConfiguration"]
            )
        )
    return out
