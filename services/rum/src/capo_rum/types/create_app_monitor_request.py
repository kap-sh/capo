"""Generated from Smithy shape ``com.amazonaws.rum#CreateAppMonitorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rum.errors import DeserializationError

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_configuration
    import capo_rum.types.app_monitor_domain
    import capo_rum.types.app_monitor_domain_list
    import capo_rum.types.app_monitor_name
    import capo_rum.types.app_monitor_platform
    import capo_rum.types.custom_events
    import capo_rum.types.deobfuscation_configuration
    import capo_rum.types.tag_map


class CreateAppMonitorRequest(TypedDict, closed=True):
    name: "capo_rum.types.app_monitor_name.AppMonitorName"
    """<p>A name for the app monitor.</p>"""
    domain: NotRequired["capo_rum.types.app_monitor_domain.AppMonitorDomain"]
    """<p>The top-level internet domain name for which your application has administrative authority.</p>"""
    domain_list: NotRequired[
        "capo_rum.types.app_monitor_domain_list.AppMonitorDomainList"
    ]
    """<p> List the domain names for which your application has administrative authority. The <code>CreateAppMonitor</code> requires either the domain or the domain list. </p>"""
    tags: NotRequired["capo_rum.types.tag_map.TagMap"]
    """<p>Assigns one or more tags (key-value pairs) to the app monitor.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can associate as many as 50 tags with an app monitor.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>.</p>"""
    app_monitor_configuration: NotRequired[
        "capo_rum.types.app_monitor_configuration.AppMonitorConfiguration"
    ]
    """<p>A structure that contains much of the configuration data for the app monitor. If you are using Amazon Cognito for authorization, you must include this structure in your request, and it must include the ID of the Amazon Cognito identity pool to use for authorization. If you don't include <code>AppMonitorConfiguration</code>, you must set up your own authorization method. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-get-started-authorization.html">Authorize your application to send data to Amazon Web Services</a>.</p> <p>If you omit this argument, the sample rate used for RUM is set to 10% of the user sessions.</p>"""
    cw_log_enabled: NotRequired["bool"]
    """<p>Data collected by RUM is kept by RUM for 30 days and then deleted. This parameter specifies whether RUM sends a copy of this telemetry data to Amazon CloudWatch Logs in your account. This enables you to keep the telemetry data for more than 30 days, but it does incur Amazon CloudWatch Logs charges.</p> <p>If you omit this parameter, the default is <code>false</code>.</p>"""
    custom_events: NotRequired["capo_rum.types.custom_events.CustomEvents"]
    """<p>Specifies whether this app monitor allows the web client to define and send custom events. If you omit this parameter, custom events are <code>DISABLED</code>.</p> <p>For more information about custom events, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html">Send custom events</a>.</p>"""
    deobfuscation_configuration: NotRequired[
        "capo_rum.types.deobfuscation_configuration.DeobfuscationConfiguration"
    ]
    """<p> A structure that contains the configuration for how an app monitor can deobfuscate stack traces. </p>"""
    platform: NotRequired["capo_rum.types.app_monitor_platform.AppMonitorPlatform"]
    """<p>The platform type for the app monitor. Valid values are <code>Web</code> for web applications, <code>Android</code> for Android applications, and <code>iOS</code> for IOS applications. If you omit this parameter, the default is <code>Web</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppMonitorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "domain_list" in value:
        import capo_rum.types.app_monitor_domain_list

        out["DomainList"] = capo_rum.types.app_monitor_domain_list.serialize_json(
            value["domain_list"]
        )
    if "tags" in value:
        import capo_rum.types.tag_map

        out["Tags"] = capo_rum.types.tag_map.serialize_json(value["tags"])
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
    if "platform" in value:
        out["Platform"] = value["platform"]
    return out


def deserialize_json(data: dict) -> CreateAppMonitorRequest:
    out: CreateAppMonitorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateAppMonitorRequest.name required")
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("DomainList") is not None:
        import capo_rum.types.app_monitor_domain_list

        out["domain_list"] = capo_rum.types.app_monitor_domain_list.deserialize_json(
            data["DomainList"]
        )
    if data.get("Tags") is not None:
        import capo_rum.types.tag_map

        out["tags"] = capo_rum.types.tag_map.deserialize_json(data["Tags"])
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
    if data.get("Platform") is not None:
        out["platform"] = data["Platform"]
    return out
