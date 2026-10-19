"""Generated from Smithy shape ``com.amazonaws.route53#ListHostedZonesByVPCResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.hosted_zone_summaries
    import capo_route_53.types.pagination_token


class ListHostedZonesByVPCResponse(TypedDict, closed=True):
    hosted_zone_summaries: (
        "capo_route_53.types.hosted_zone_summaries.HostedZoneSummaries"
    )
    """<p>A list that contains one <code>HostedZoneSummary</code> element for each hosted zone that the specified Amazon VPC is associated with. Each <code>HostedZoneSummary</code> element contains the hosted zone name and ID, and information about who owns the hosted zone.</p>"""
    max_items: "int"
    """<p>The value that you specified for <code>MaxItems</code> in the most recent <code>ListHostedZonesByVPC</code> request.</p>"""
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>The value that you will use for <code>NextToken</code> in the next <code>ListHostedZonesByVPC</code> request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListHostedZonesByVPCResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.hosted_zone_summaries

    capo_route_53.types.hosted_zone_summaries.serialize_xml(
        value["hosted_zone_summaries"], el, "HostedZoneSummaries"
    )
    SubElement(el, "MaxItems").text = str(value["max_items"])
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])


def deserialize_xml(el: Element) -> ListHostedZonesByVPCResponse:
    out: ListHostedZonesByVPCResponse = {}  # type: ignore[typeddict-item]
    child_hosted_zone_summaries = el.find("HostedZoneSummaries")
    if child_hosted_zone_summaries is not None:
        import capo_route_53.types.hosted_zone_summaries

        out["hosted_zone_summaries"] = (
            capo_route_53.types.hosted_zone_summaries.deserialize_xml(
                child_hosted_zone_summaries
            )
        )
    else:
        out["hosted_zone_summaries"] = []
    child_max_items = el.find("MaxItems")
    if child_max_items is not None:
        out["max_items"] = int(child_max_items.text or "")
    else:
        out["max_items"] = 0
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
