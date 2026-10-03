"""Generated from Smithy shape ``com.amazonaws.internetmonitor#UpdateMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_internetmonitor.types.health_events_config
    import capo_internetmonitor.types.internet_measurements_log_delivery
    import capo_internetmonitor.types.max_city_networks_to_monitor
    import capo_internetmonitor.types.monitor_config_state
    import capo_internetmonitor.types.resource_name
    import capo_internetmonitor.types.set_of_ar_ns
    import capo_internetmonitor.types.traffic_percentage_to_monitor


class UpdateMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor. </p>"""
    resources_to_add: NotRequired["capo_internetmonitor.types.set_of_ar_ns.SetOfARNs"]
    """<p>The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.</p> <p>You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.</p> <note> <p>If you add only Amazon Virtual Private Clouds resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.</p> </note>"""
    resources_to_remove: NotRequired[
        "capo_internetmonitor.types.set_of_ar_ns.SetOfARNs"
    ]
    """<p>The resources to remove from a monitor, which you provide as a set of Amazon Resource Names (ARNs).</p>"""
    status: NotRequired[
        "capo_internetmonitor.types.monitor_config_state.MonitorConfigState"
    ]
    """<p>The status for a monitor. The accepted values for <code>Status</code> with the <code>UpdateMonitor</code> API call are the following: <code>ACTIVE</code> and <code>INACTIVE</code>. The following values are <i>not</i> accepted: <code>PENDING</code>, and <code>ERROR</code>.</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. You should not reuse the same client token for other API requests.</p>"""
    max_city_networks_to_monitor: NotRequired[
        "capo_internetmonitor.types.max_city_networks_to_monitor.MaxCityNetworksToMonitor"
    ]
    """<p>The maximum number of city-networks to monitor for your application. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.</p>"""
    internet_measurements_log_delivery: NotRequired[
        "capo_internetmonitor.types.internet_measurements_log_delivery.InternetMeasurementsLogDelivery"
    ]
    """<p>Publish internet measurements for Internet Monitor to another location, such as an Amazon S3 bucket. The measurements are also published to Amazon CloudWatch Logs.</p>"""
    traffic_percentage_to_monitor: NotRequired[
        "capo_internetmonitor.types.traffic_percentage_to_monitor.TrafficPercentageToMonitor"
    ]
    """<p>The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html">Choosing an application traffic percentage to monitor </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    health_events_config: NotRequired[
        "capo_internetmonitor.types.health_events_config.HealthEventsConfig"
    ]
    """<p>The list of health score thresholds. A threshold percentage for health scores, along with other configuration information, determines when Internet Monitor creates a health event when there's an internet issue that affects your application end users.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview"> Change health event thresholds</a> in the Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMonitorInput) -> dict:
    out: dict = {}
    if "resources_to_add" in value:
        import capo_internetmonitor.types.set_of_ar_ns

        out["ResourcesToAdd"] = capo_internetmonitor.types.set_of_ar_ns.serialize_json(
            value["resources_to_add"]
        )
    if "resources_to_remove" in value:
        import capo_internetmonitor.types.set_of_ar_ns

        out["ResourcesToRemove"] = (
            capo_internetmonitor.types.set_of_ar_ns.serialize_json(
                value["resources_to_remove"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "max_city_networks_to_monitor" in value:
        out["MaxCityNetworksToMonitor"] = value["max_city_networks_to_monitor"]
    if "internet_measurements_log_delivery" in value:
        import capo_internetmonitor.types.internet_measurements_log_delivery

        out["InternetMeasurementsLogDelivery"] = (
            capo_internetmonitor.types.internet_measurements_log_delivery.serialize_json(
                value["internet_measurements_log_delivery"]
            )
        )
    if "traffic_percentage_to_monitor" in value:
        out["TrafficPercentageToMonitor"] = value["traffic_percentage_to_monitor"]
    if "health_events_config" in value:
        import capo_internetmonitor.types.health_events_config

        out["HealthEventsConfig"] = (
            capo_internetmonitor.types.health_events_config.serialize_json(
                value["health_events_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMonitorInput:
    out: UpdateMonitorInput = {}  # type: ignore[typeddict-item]
    if data.get("ResourcesToAdd") is not None:
        import capo_internetmonitor.types.set_of_ar_ns

        out["resources_to_add"] = (
            capo_internetmonitor.types.set_of_ar_ns.deserialize_json(
                data["ResourcesToAdd"]
            )
        )
    if data.get("ResourcesToRemove") is not None:
        import capo_internetmonitor.types.set_of_ar_ns

        out["resources_to_remove"] = (
            capo_internetmonitor.types.set_of_ar_ns.deserialize_json(
                data["ResourcesToRemove"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("MaxCityNetworksToMonitor") is not None:
        out["max_city_networks_to_monitor"] = data["MaxCityNetworksToMonitor"]
    if data.get("InternetMeasurementsLogDelivery") is not None:
        import capo_internetmonitor.types.internet_measurements_log_delivery

        out["internet_measurements_log_delivery"] = (
            capo_internetmonitor.types.internet_measurements_log_delivery.deserialize_json(
                data["InternetMeasurementsLogDelivery"]
            )
        )
    if data.get("TrafficPercentageToMonitor") is not None:
        out["traffic_percentage_to_monitor"] = data["TrafficPercentageToMonitor"]
    if data.get("HealthEventsConfig") is not None:
        import capo_internetmonitor.types.health_events_config

        out["health_events_config"] = (
            capo_internetmonitor.types.health_events_config.deserialize_json(
                data["HealthEventsConfig"]
            )
        )
    return out
