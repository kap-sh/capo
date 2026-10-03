"""Generated from Smithy shape ``com.amazonaws.route53#StatusReport``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.status
    import capo_route_53.types.time_stamp


class StatusReport(TypedDict, closed=True):
    status: NotRequired["capo_route_53.types.status.Status"]
    """<p>A description of the status of the health check endpoint as reported by one of the Amazon Route 53 health checkers.</p>"""
    checked_time: NotRequired["capo_route_53.types.time_stamp.TimeStamp"]
    """<p>The date and time that the health checker performed the health check in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601 format</a> and Coordinated Universal Time (UTC). For example, the value <code>2017-03-27T17:48:16.751Z</code> represents March 27, 2017 at 17:48:16.751 UTC.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: StatusReport, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "status" in value:
        SubElement(el, "Status").text = str(value["status"])
    if "checked_time" in value:
        import capo_route_53.types.time_stamp

        capo_route_53.types.time_stamp.serialize_xml(
            value["checked_time"], el, "CheckedTime"
        )


def deserialize_xml(el: Element) -> StatusReport:
    out: StatusReport = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_checked_time = el.find("CheckedTime")
    if child_checked_time is not None:
        import capo_route_53.types.time_stamp

        out["checked_time"] = capo_route_53.types.time_stamp.deserialize_xml(
            child_checked_time
        )
    return out
