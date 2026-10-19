"""Generated from Smithy shape ``com.amazonaws.route53#GetCheckerIpRangesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.checker_ip_ranges


class GetCheckerIpRangesResponse(TypedDict, closed=True):
    checker_ip_ranges: "capo_route_53.types.checker_ip_ranges.CheckerIpRanges"
    """<p>A complex type that contains sorted list of IP ranges in CIDR format for Amazon Route 53 health checkers.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetCheckerIpRangesResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.checker_ip_ranges

    capo_route_53.types.checker_ip_ranges.serialize_xml(
        value["checker_ip_ranges"], el, "CheckerIpRanges"
    )


def deserialize_xml(el: Element) -> GetCheckerIpRangesResponse:
    out: GetCheckerIpRangesResponse = {}  # type: ignore[typeddict-item]
    child_checker_ip_ranges = el.find("CheckerIpRanges")
    if child_checker_ip_ranges is not None:
        import capo_route_53.types.checker_ip_ranges

        out["checker_ip_ranges"] = (
            capo_route_53.types.checker_ip_ranges.deserialize_xml(
                child_checker_ip_ranges
            )
        )
    else:
        out["checker_ip_ranges"] = []
    return out
