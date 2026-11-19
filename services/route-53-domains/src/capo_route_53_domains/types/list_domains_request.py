"""Generated from Smithy shape ``com.amazonaws.route53domains#ListDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.filter_conditions
    import capo_route_53_domains.types.page_marker
    import capo_route_53_domains.types.page_max_items
    import capo_route_53_domains.types.sort_condition


class ListDomainsRequest(TypedDict, closed=True):
    filter_conditions: NotRequired[
        "capo_route_53_domains.types.filter_conditions.FilterConditions"
    ]
    """<p>A complex type that contains information about the filters applied during the <code>ListDomains</code> request. The filter conditions can include domain name and domain expiration.</p>"""
    sort_condition: NotRequired[
        "capo_route_53_domains.types.sort_condition.SortCondition"
    ]
    """<p>A complex type that contains information about the requested ordering of domains in the returned list.</p>"""
    marker: NotRequired["capo_route_53_domains.types.page_marker.PageMarker"]
    """<p>For an initial request for a list of domains, omit this element. If the number of domains that are associated with the current Amazon Web Services account is greater than the value that you specified for <code>MaxItems</code>, you can use <code>Marker</code> to return additional domains. Get the value of <code>NextPageMarker</code> from the previous response, and submit another request that includes the value of <code>NextPageMarker</code> in the <code>Marker</code> element.</p> <p>Constraints: The marker must match the value specified in the previous request.</p>"""
    max_items: NotRequired["capo_route_53_domains.types.page_max_items.PageMaxItems"]
    """<p>Number of domains to be returned.</p> <p>Default: 20</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDomainsRequest) -> dict:
    out: dict = {}
    if "filter_conditions" in value:
        import capo_route_53_domains.types.filter_conditions

        out["FilterConditions"] = (
            capo_route_53_domains.types.filter_conditions.serialize_aws_json_1_1(
                value["filter_conditions"]
            )
        )
    if "sort_condition" in value:
        import capo_route_53_domains.types.sort_condition

        out["SortCondition"] = (
            capo_route_53_domains.types.sort_condition.serialize_aws_json_1_1(
                value["sort_condition"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDomainsRequest:
    out: ListDomainsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FilterConditions") is not None:
        import capo_route_53_domains.types.filter_conditions

        out["filter_conditions"] = (
            capo_route_53_domains.types.filter_conditions.deserialize_aws_json_1_1(
                data["FilterConditions"]
            )
        )
    if data.get("SortCondition") is not None:
        import capo_route_53_domains.types.sort_condition

        out["sort_condition"] = (
            capo_route_53_domains.types.sort_condition.deserialize_aws_json_1_1(
                data["SortCondition"]
            )
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDomainsRequest) -> dict:
    out: dict = {}
    if "filter_conditions" in value:
        import capo_route_53_domains.types.filter_conditions

        out["FilterConditions"] = (
            capo_route_53_domains.types.filter_conditions.serialize_cbor(
                value["filter_conditions"]
            )
        )
    if "sort_condition" in value:
        import capo_route_53_domains.types.sort_condition

        out["SortCondition"] = (
            capo_route_53_domains.types.sort_condition.serialize_cbor(
                value["sort_condition"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    return out


def deserialize_cbor(data: dict) -> ListDomainsRequest:
    out: ListDomainsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FilterConditions") is not None:
        import capo_route_53_domains.types.filter_conditions

        out["filter_conditions"] = (
            capo_route_53_domains.types.filter_conditions.deserialize_cbor(
                data["FilterConditions"]
            )
        )
    if data.get("SortCondition") is not None:
        import capo_route_53_domains.types.sort_condition

        out["sort_condition"] = (
            capo_route_53_domains.types.sort_condition.deserialize_cbor(
                data["SortCondition"]
            )
        )
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    return out
