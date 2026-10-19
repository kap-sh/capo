"""Generated from Smithy shape ``com.amazonaws.route53#GetHostedZoneCountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.hosted_zone_count


class GetHostedZoneCountResponse(TypedDict, closed=True):
    hosted_zone_count: "capo_route_53.types.hosted_zone_count.HostedZoneCount"
    """<p>The total number of public and private hosted zones that are associated with the current Amazon Web Services account.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetHostedZoneCountResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HostedZoneCount").text = str(value["hosted_zone_count"])


def deserialize_xml(el: Element) -> GetHostedZoneCountResponse:
    out: GetHostedZoneCountResponse = {}  # type: ignore[typeddict-item]
    child_hosted_zone_count = el.find("HostedZoneCount")
    if child_hosted_zone_count is not None:
        out["hosted_zone_count"] = int(child_hosted_zone_count.text or "")
    else:
        out["hosted_zone_count"] = 0
    return out
