"""Generated from Smithy shape ``com.amazonaws.route53domains#ListPricesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_price_list
    import capo_route_53_domains.types.page_marker


class ListPricesResponse(TypedDict, closed=True):
    prices: NotRequired["capo_route_53_domains.types.domain_price_list.DomainPriceList"]
    """<p>A complex type that includes all the pricing information. If you specify a TLD, this array contains only the pricing for that TLD.</p>"""
    next_page_marker: NotRequired["capo_route_53_domains.types.page_marker.PageMarker"]
    """<p>If there are more prices than you specified for <code>MaxItems</code> in the request, submit another request and include the value of <code>NextPageMarker</code> in the value of <code>Marker</code>. </p> <p>Used only for all TLDs. If you specify a TLD, don't specify a <code>NextPageMarker</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListPricesResponse) -> dict:
    out: dict = {}
    if "prices" in value:
        import capo_route_53_domains.types.domain_price_list

        out["Prices"] = (
            capo_route_53_domains.types.domain_price_list.serialize_aws_json_1_1(
                value["prices"]
            )
        )
    if "next_page_marker" in value:
        out["NextPageMarker"] = value["next_page_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListPricesResponse:
    out: ListPricesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Prices") is not None:
        import capo_route_53_domains.types.domain_price_list

        out["prices"] = (
            capo_route_53_domains.types.domain_price_list.deserialize_aws_json_1_1(
                data["Prices"]
            )
        )
    if data.get("NextPageMarker") is not None:
        out["next_page_marker"] = data["NextPageMarker"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListPricesResponse) -> dict:
    out: dict = {}
    if "prices" in value:
        import capo_route_53_domains.types.domain_price_list

        out["Prices"] = capo_route_53_domains.types.domain_price_list.serialize_cbor(
            value["prices"]
        )
    if "next_page_marker" in value:
        out["NextPageMarker"] = value["next_page_marker"]
    return out


def deserialize_cbor(data: dict) -> ListPricesResponse:
    out: ListPricesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Prices") is not None:
        import capo_route_53_domains.types.domain_price_list

        out["prices"] = capo_route_53_domains.types.domain_price_list.deserialize_cbor(
            data["Prices"]
        )
    if data.get("NextPageMarker") is not None:
        out["next_page_marker"] = data["NextPageMarker"]
    return out
