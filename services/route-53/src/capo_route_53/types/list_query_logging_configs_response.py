"""Generated from Smithy shape ``com.amazonaws.route53#ListQueryLoggingConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.pagination_token
    import capo_route_53.types.query_logging_configs


class ListQueryLoggingConfigsResponse(TypedDict, closed=True):
    query_logging_configs: (
        "capo_route_53.types.query_logging_configs.QueryLoggingConfigs"
    )
    """<p>An array that contains one <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_QueryLoggingConfig.html">QueryLoggingConfig</a> element for each configuration for DNS query logging that is associated with the current Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_route_53.types.pagination_token.PaginationToken"]
    """<p>If a response includes the last of the query logging configurations that are associated with the current Amazon Web Services account, <code>NextToken</code> doesn't appear in the response.</p> <p>If a response doesn't include the last of the configurations, you can get more configurations by submitting another <a href="https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListQueryLoggingConfigs.html">ListQueryLoggingConfigs</a> request. Get the value of <code>NextToken</code> that Amazon Route 53 returned in the previous response and include it in <code>NextToken</code> in the next request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ListQueryLoggingConfigsResponse, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.query_logging_configs

    capo_route_53.types.query_logging_configs.serialize_xml(
        value["query_logging_configs"], el, "QueryLoggingConfigs"
    )
    if "next_token" in value:
        SubElement(el, "NextToken").text = str(value["next_token"])


def deserialize_xml(el: Element) -> ListQueryLoggingConfigsResponse:
    out: ListQueryLoggingConfigsResponse = {}  # type: ignore[typeddict-item]
    child_query_logging_configs = el.find("QueryLoggingConfigs")
    if child_query_logging_configs is not None:
        import capo_route_53.types.query_logging_configs

        out["query_logging_configs"] = (
            capo_route_53.types.query_logging_configs.deserialize_xml(
                child_query_logging_configs
            )
        )
    else:
        raise DeserializationError(
            "ListQueryLoggingConfigsResponse.query_logging_configs required"
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
