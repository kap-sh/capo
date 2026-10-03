"""Generated from Smithy shape ``com.amazonaws.route53#ListQueryLoggingConfigsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_route_53.types.pagination_token
    import capo_route_53.types.resource_id


class ListQueryLoggingConfigsRequest(TypedDict, closed=True):
    hosted_zone_id: NotRequired["capo_route_53.types.resource_id.ResourceId"]
    """<p>(Optional) If you want to list the query logging configuration that is associated with a hosted zone, specify the ID in <code>HostedZoneId</code>. </p> <p>If you don't specify a hosted zone ID, <code>ListQueryLoggingConfigs</code> returns all of the configurations that are associated with the current Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>(Optional) If the current Amazon Web Services account has more than <code>MaxResults</code> query logging configurations, use <code>NextToken</code> to get the second and subsequent pages of results.</p> <p>For the first <code>ListQueryLoggingConfigs</code> request, omit this value.</p> <p>For the second and subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request.</p>"""
    max_results: NotRequired["int"]
    """<p>(Optional) The maximum number of query logging configurations that you want Amazon Route 53 to return in response to the current request. If the current Amazon Web Services account has more than <code>MaxResults</code> configurations, use the value of <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html#API_ListQueryLoggingConfigs_RequestSyntax">NextToken</a> in the response to get the next page of results.</p> <p>If you don't specify a value for <code>MaxResults</code>, Route 53 returns up to 100 configurations.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListQueryLoggingConfigsRequest, parent: Element, tag: str
) -> None:
    SubElement(parent, tag)


def deserialize_xml(el: Element) -> ListQueryLoggingConfigsRequest:
    out: ListQueryLoggingConfigsRequest = {}  # type: ignore[typeddict-item]
    return out
