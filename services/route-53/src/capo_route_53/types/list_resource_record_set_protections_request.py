"""Generated from Smithy shape ``com.amazonaws.route53#ListResourceRecordSetProtectionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.dns_name
    import capo_route_53.types.pagination_token
    import capo_route_53.types.resource_id
    import capo_route_53.types.rr_type


class ListResourceRecordSetProtectionsRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the hosted zone that contains the protections that you want to list.</p>"""
    start_record_name: NotRequired["capo_route_53.types.dns_name.DNSName"]
    """<p>The first resource record set name that you want Route 53 to list protections for. If you don't specify a value, the list starts with the first protection in the hosted zone.</p> <p>If you specify <code>NextToken</code>, Route 53 ignores <code>StartRecordName</code>.</p>"""
    start_record_type: NotRequired["capo_route_53.types.rr_type.RRType"]
    """<p>The first resource record set type, within the name specified by <code>StartRecordName</code>, that you want Route 53 to list protections for. If you specify <code>StartRecordType</code>, you must also specify <code>StartRecordName</code>.</p> <p>If you specify <code>NextToken</code>, Route 53 ignores <code>StartRecordType</code>.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of protections that you want Route 53 to return in this response. If you don't specify a value, or if you specify a value greater than 300, Route 53 returns up to 300 protections.</p>"""
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>If the response to a previous <code>ListResourceRecordSetProtections</code> request included a <code>NextToken</code> element, specify that value here to get the next page of results.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListResourceRecordSetProtectionsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListResourceRecordSetProtectionsRequest:
    out: ListResourceRecordSetProtectionsRequest = {}  # type: ignore[typeddict-item]
    return out
