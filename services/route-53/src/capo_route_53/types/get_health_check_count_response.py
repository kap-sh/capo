"""Generated from Smithy shape ``com.amazonaws.route53#GetHealthCheckCountResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.health_check_count


class GetHealthCheckCountResponse(TypedDict, closed=True):
    health_check_count: "capo_route_53.types.health_check_count.HealthCheckCount"
    """<p>The number of health checks associated with the current Amazon Web Services account.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: GetHealthCheckCountResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HealthCheckCount").text = str(value["health_check_count"])


def deserialize_xml(el: Element) -> GetHealthCheckCountResponse:
    out: GetHealthCheckCountResponse = {}  # type: ignore[typeddict-item]
    child_health_check_count = el.find("HealthCheckCount")
    if child_health_check_count is not None:
        out["health_check_count"] = int(child_health_check_count.text or "")
    else:
        out["health_check_count"] = 0
    return out
