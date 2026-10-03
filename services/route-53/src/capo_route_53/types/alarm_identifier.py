"""Generated from Smithy shape ``com.amazonaws.route53#AlarmIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.alarm_name
    import capo_route_53.types.cloud_watch_region


class AlarmIdentifier(TypedDict, closed=True):
    region: "capo_route_53.types.cloud_watch_region.CloudWatchRegion"
    """<p>For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.</p> <p>For the current list of CloudWatch regions, see <a href="https://docs.aws.amazon.com/general/latest/gr/cw_region.html">Amazon CloudWatch endpoints and quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    name: "capo_route_53.types.alarm_name.AlarmName"
    """<p>The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.</p> <note> <p>Route 53 supports CloudWatch alarms with the following features:</p> <ul> <li> <p>Standard-resolution metrics. High-resolution metrics aren't supported. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics">High-Resolution Metrics</a> in the <i>Amazon CloudWatch User Guide</i>.</p> </li> <li> <p>Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren't supported.</p> </li> </ul> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: AlarmIdentifier, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.cloud_watch_region

    capo_route_53.types.cloud_watch_region.serialize_xml(value["region"], el, "Region")
    SubElement(el, "Name").text = str(value["name"])


def deserialize_xml(el: Element) -> AlarmIdentifier:
    out: AlarmIdentifier = {}  # type: ignore[typeddict-item]
    child_region = el.find("Region")
    if child_region is not None:
        import capo_route_53.types.cloud_watch_region

        out["region"] = capo_route_53.types.cloud_watch_region.deserialize_xml(
            child_region
        )
    else:
        raise DeserializationError("AlarmIdentifier.region required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("AlarmIdentifier.name required")
    return out
