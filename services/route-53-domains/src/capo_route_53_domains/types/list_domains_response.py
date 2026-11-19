"""Generated from Smithy shape ``com.amazonaws.route53domains#ListDomainsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_summary_list
    import capo_route_53_domains.types.page_marker


class ListDomainsResponse(TypedDict, closed=True):
    domains: NotRequired[
        "capo_route_53_domains.types.domain_summary_list.DomainSummaryList"
    ]
    """<p>A list of domains.</p>"""
    next_page_marker: NotRequired["capo_route_53_domains.types.page_marker.PageMarker"]
    """<p>If there are more domains than you specified for <code>MaxItems</code> in the request, submit another request and include the value of <code>NextPageMarker</code> in the value of <code>Marker</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDomainsResponse) -> dict:
    out: dict = {}
    if "domains" in value:
        import capo_route_53_domains.types.domain_summary_list

        out["Domains"] = (
            capo_route_53_domains.types.domain_summary_list.serialize_aws_json_1_1(
                value["domains"]
            )
        )
    if "next_page_marker" in value:
        out["NextPageMarker"] = value["next_page_marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDomainsResponse:
    out: ListDomainsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Domains") is not None:
        import capo_route_53_domains.types.domain_summary_list

        out["domains"] = (
            capo_route_53_domains.types.domain_summary_list.deserialize_aws_json_1_1(
                data["Domains"]
            )
        )
    if data.get("NextPageMarker") is not None:
        out["next_page_marker"] = data["NextPageMarker"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListDomainsResponse) -> dict:
    out: dict = {}
    if "domains" in value:
        import capo_route_53_domains.types.domain_summary_list

        out["Domains"] = capo_route_53_domains.types.domain_summary_list.serialize_cbor(
            value["domains"]
        )
    if "next_page_marker" in value:
        out["NextPageMarker"] = value["next_page_marker"]
    return out


def deserialize_cbor(data: dict) -> ListDomainsResponse:
    out: ListDomainsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Domains") is not None:
        import capo_route_53_domains.types.domain_summary_list

        out["domains"] = (
            capo_route_53_domains.types.domain_summary_list.deserialize_cbor(
                data["Domains"]
            )
        )
    if data.get("NextPageMarker") is not None:
        out["next_page_marker"] = data["NextPageMarker"]
    return out
