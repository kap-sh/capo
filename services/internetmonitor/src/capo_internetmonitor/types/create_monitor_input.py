"""Generated from Smithy shape ``com.amazonaws.internetmonitor#CreateMonitorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_internetmonitor.types.health_events_config
    import capo_internetmonitor.types.internet_measurements_log_delivery
    import capo_internetmonitor.types.max_city_networks_to_monitor
    import capo_internetmonitor.types.resource_name
    import capo_internetmonitor.types.set_of_ar_ns
    import capo_internetmonitor.types.tag_map
    import capo_internetmonitor.types.traffic_percentage_to_monitor


class CreateMonitorInput(TypedDict, closed=True):
    monitor_name: "capo_internetmonitor.types.resource_name.ResourceName"
    """<p>The name of the monitor. </p>"""
    resources: NotRequired["capo_internetmonitor.types.set_of_ar_ns.SetOfARNs"]
    """<p>The resources to include in a monitor, which you provide as a set of Amazon Resource Names (ARNs). Resources can be VPCs, NLBs, Amazon CloudFront distributions, or Amazon WorkSpaces directories.</p> <p>You can add a combination of VPCs and CloudFront distributions, or you can add WorkSpaces directories, or you can add NLBs. You can't add NLBs or WorkSpaces directories together with any other resources.</p> <note> <p>If you add only Amazon VPC resources, at least one VPC must have an Internet Gateway attached to it, to make sure that it has internet connectivity.</p> </note>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive string of up to 64 ASCII characters that you specify to make an idempotent API request. Don't reuse the same client token for other API requests.</p>"""
    tags: NotRequired["capo_internetmonitor.types.tag_map.TagMap"]
    """<p>The tags for a monitor. You can add a maximum of 50 tags in Internet Monitor.</p>"""
    max_city_networks_to_monitor: NotRequired[
        "capo_internetmonitor.types.max_city_networks_to_monitor.MaxCityNetworksToMonitor"
    ]
    """<p>The maximum number of city-networks to monitor for your resources. A city-network is the location (city) where clients access your application resources from and the ASN or network provider, such as an internet service provider (ISP), that clients access the resources through. Setting this limit can help control billing costs.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMCityNetworksMaximum.html">Choosing a city-network maximum value </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    internet_measurements_log_delivery: NotRequired[
        "capo_internetmonitor.types.internet_measurements_log_delivery.InternetMeasurementsLogDelivery"
    ]
    """<p>Publish internet measurements for Internet Monitor to an Amazon S3 bucket in addition to CloudWatch Logs.</p>"""
    traffic_percentage_to_monitor: NotRequired[
        "capo_internetmonitor.types.traffic_percentage_to_monitor.TrafficPercentageToMonitor"
    ]
    """<p>The percentage of the internet-facing traffic for your application that you want to monitor with this monitor. If you set a city-networks maximum, that limit overrides the traffic percentage that you set.</p> <p>To learn more, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/IMTrafficPercentage.html">Choosing an application traffic percentage to monitor </a> in the Amazon CloudWatch Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""
    health_events_config: NotRequired[
        "capo_internetmonitor.types.health_events_config.HealthEventsConfig"
    ]
    """<p>Defines the threshold percentages and other configuration information for when Amazon CloudWatch Internet Monitor creates a health event. Internet Monitor creates a health event when an internet issue that affects your application end users has a health score percentage that is at or below a specific threshold, and, sometimes, when other criteria are met.</p> <p>If you don't set a health event threshold, the default value is 95%.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-overview.html#IMUpdateThresholdFromOverview"> Change health event thresholds</a> in the Internet Monitor section of the <i>CloudWatch User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorInput) -> dict:
    out: dict = {}
    out["MonitorName"] = value["monitor_name"]
    if "resources" in value:
        import capo_internetmonitor.types.set_of_ar_ns

        out["Resources"] = capo_internetmonitor.types.set_of_ar_ns.serialize_json(
            value["resources"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_internetmonitor.types.tag_map

        out["Tags"] = capo_internetmonitor.types.tag_map.serialize_json(value["tags"])
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


def deserialize_json(data: dict) -> CreateMonitorInput:
    out: CreateMonitorInput = {}  # type: ignore[typeddict-item]
    if data.get("MonitorName") is not None:
        out["monitor_name"] = data["MonitorName"]
    else:
        raise DeserializationError("CreateMonitorInput.monitor_name required")
    if data.get("Resources") is not None:
        import capo_internetmonitor.types.set_of_ar_ns

        out["resources"] = capo_internetmonitor.types.set_of_ar_ns.deserialize_json(
            data["Resources"]
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_internetmonitor.types.tag_map

        out["tags"] = capo_internetmonitor.types.tag_map.deserialize_json(data["Tags"])
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
