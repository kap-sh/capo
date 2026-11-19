"""Generated from Smithy shape ``com.amazonaws.route53domains#ListPricesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.list_prices_page_max_items
    import capo_route_53_domains.types.page_marker
    import capo_route_53_domains.types.tld_name


class ListPricesRequest(TypedDict, closed=True):
    tld: NotRequired["capo_route_53_domains.types.tld_name.TldName"]
    """<p>The TLD for which you want to receive the pricing information. For example. <code>.net</code>.</p> <p>If a <code>Tld</code> value is not provided, a list of prices for all TLDs supported by Route 53 is returned.</p>"""
    marker: NotRequired["capo_route_53_domains.types.page_marker.PageMarker"]
    """<p>For an initial request for a list of prices, omit this element. If the number of prices that are not yet complete is greater than the value that you specified for <code>MaxItems</code>, you can use <code>Marker</code> to return additional prices. Get the value of <code>NextPageMarker</code> from the previous response, and submit another request that includes the value of <code>NextPageMarker</code> in the <code>Marker</code> element. </p> <p>Used only for all TLDs. If you specify a TLD, don't specify a <code>Marker</code>.</p>"""
    max_items: NotRequired[
        "capo_route_53_domains.types.list_prices_page_max_items.ListPricesPageMaxItems"
    ]
    """<p>Number of <code>Prices</code> to be returned.</p> <p>Used only for all TLDs. If you specify a TLD, don't specify a <code>MaxItems</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPricesRequest) -> dict:
    out: dict = {}
    if "tld" in value:
        out["Tld"] = value["tld"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPricesRequest:
    out: ListPricesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tld") is not None:
        out["tld"] = data["Tld"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPricesRequest) -> dict:
    out: dict = {}
    if "tld" in value:
        out["Tld"] = value["tld"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "max_items" in value:
        out["MaxItems"] = value["max_items"]
    return out


def deserialize_cbor(data: dict) -> ListPricesRequest:
    out: ListPricesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Tld") is not None:
        out["tld"] = data["Tld"]
    if data.get("Marker") is not None:
        out["marker"] = data["Marker"]
    if data.get("MaxItems") is not None:
        out["max_items"] = data["MaxItems"]
    return out
