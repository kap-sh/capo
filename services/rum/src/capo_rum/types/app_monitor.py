"""Generated from Smithy shape ``com.amazonaws.rum#AppMonitor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rum.types.app_monitor_configuration
    import capo_rum.types.app_monitor_domain
    import capo_rum.types.app_monitor_domain_list
    import capo_rum.types.app_monitor_id
    import capo_rum.types.app_monitor_name
    import capo_rum.types.app_monitor_platform
    import capo_rum.types.custom_events
    import capo_rum.types.data_storage
    import capo_rum.types.deobfuscation_configuration
    import capo_rum.types.iso_timestamp_string
    import capo_rum.types.state_enum
    import capo_rum.types.tag_map


class AppMonitor(TypedDict, closed=True):
    name: NotRequired["capo_rum.types.app_monitor_name.AppMonitorName"]
    """<p>The name of the app monitor.</p>"""
    domain: NotRequired["capo_rum.types.app_monitor_domain.AppMonitorDomain"]
    """<p>The top-level internet domain name for which your application has administrative authority.</p>"""
    domain_list: NotRequired[
        "capo_rum.types.app_monitor_domain_list.AppMonitorDomainList"
    ]
    """<p> List the domain names for which your application has administrative authority. </p>"""
    id: NotRequired["capo_rum.types.app_monitor_id.AppMonitorId"]
    """<p>The unique ID of this app monitor.</p>"""
    created: NotRequired["capo_rum.types.iso_timestamp_string.ISOTimestampString"]
    """<p>The date and time that this app monitor was created.</p>"""
    last_modified: NotRequired["capo_rum.types.iso_timestamp_string.ISOTimestampString"]
    """<p>The date and time of the most recent changes to this app monitor's configuration.</p>"""
    tags: NotRequired["capo_rum.types.tag_map.TagMap"]
    """<p>The list of tag keys and values associated with this app monitor.</p>"""
    state: NotRequired["capo_rum.types.state_enum.StateEnum"]
    """<p>The current state of the app monitor.</p>"""
    app_monitor_configuration: NotRequired[
        "capo_rum.types.app_monitor_configuration.AppMonitorConfiguration"
    ]
    """<p>A structure that contains much of the configuration data for the app monitor.</p>"""
    data_storage: NotRequired["capo_rum.types.data_storage.DataStorage"]
    """<p>A structure that contains information about whether this app monitor stores a copy of the telemetry data that RUM collects using CloudWatch Logs.</p>"""
    custom_events: NotRequired["capo_rum.types.custom_events.CustomEvents"]
    """<p>Specifies whether this app monitor allows the web client to define and send custom events.</p> <p>For more information about custom events, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-custom-events.html">Send custom events</a>.</p>"""
    deobfuscation_configuration: NotRequired[
        "capo_rum.types.deobfuscation_configuration.DeobfuscationConfiguration"
    ]
    """<p> A structure that contains the configuration for how an app monitor can deobfuscate stack traces. </p>"""
    platform: NotRequired["capo_rum.types.app_monitor_platform.AppMonitorPlatform"]
    """<p>The platform type for this app monitor. Valid values are <code>Web</code> for web applications , <code>Android</code> for Android applications, and <code>iOS</code> for IOS applications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppMonitor) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "domain" in value:
        out["Domain"] = value["domain"]
    if "domain_list" in value:
        import capo_rum.types.app_monitor_domain_list

        out["DomainList"] = capo_rum.types.app_monitor_domain_list.serialize_json(
            value["domain_list"]
        )
    if "id" in value:
        out["Id"] = value["id"]
    if "created" in value:
        out["Created"] = value["created"]
    if "last_modified" in value:
        out["LastModified"] = value["last_modified"]
    if "tags" in value:
        import capo_rum.types.tag_map

        out["Tags"] = capo_rum.types.tag_map.serialize_json(value["tags"])
    if "state" in value:
        out["State"] = value["state"]
    if "app_monitor_configuration" in value:
        import capo_rum.types.app_monitor_configuration

        out["AppMonitorConfiguration"] = (
            capo_rum.types.app_monitor_configuration.serialize_json(
                value["app_monitor_configuration"]
            )
        )
    if "data_storage" in value:
        import capo_rum.types.data_storage

        out["DataStorage"] = capo_rum.types.data_storage.serialize_json(
            value["data_storage"]
        )
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


def deserialize_json(data: dict) -> AppMonitor:
    out: AppMonitor = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    if data.get("DomainList") is not None:
        import capo_rum.types.app_monitor_domain_list

        out["domain_list"] = capo_rum.types.app_monitor_domain_list.deserialize_json(
            data["DomainList"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Created") is not None:
        out["created"] = data["Created"]
    if data.get("LastModified") is not None:
        out["last_modified"] = data["LastModified"]
    if data.get("Tags") is not None:
        import capo_rum.types.tag_map

        out["tags"] = capo_rum.types.tag_map.deserialize_json(data["Tags"])
    if data.get("State") is not None:
        out["state"] = data["State"]
    if data.get("AppMonitorConfiguration") is not None:
        import capo_rum.types.app_monitor_configuration

        out["app_monitor_configuration"] = (
            capo_rum.types.app_monitor_configuration.deserialize_json(
                data["AppMonitorConfiguration"]
            )
        )
    if data.get("DataStorage") is not None:
        import capo_rum.types.data_storage

        out["data_storage"] = capo_rum.types.data_storage.deserialize_json(
            data["DataStorage"]
        )
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
