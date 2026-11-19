"""Generated from Smithy shape ``com.amazonaws.route53domains#ViewBillingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.billing_records
    import capo_route_53_domains.types.page_marker


class ViewBillingResponse(TypedDict, closed=True):
    next_page_marker: NotRequired["capo_route_53_domains.types.page_marker.PageMarker"]
    """<p>If there are more billing records than you specified for <code>MaxItems</code> in the request, submit another request and include the value of <code>NextPageMarker</code> in the value of <code>Marker</code>.</p>"""
    billing_records: NotRequired[
        "capo_route_53_domains.types.billing_records.BillingRecords"
    ]
    """<p>A summary of billing records.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViewBillingResponse) -> dict:
    out: dict = {}
    if "next_page_marker" in value:
        out["NextPageMarker"] = value["next_page_marker"]
    if "billing_records" in value:
        import capo_route_53_domains.types.billing_records

        out["BillingRecords"] = (
            capo_route_53_domains.types.billing_records.serialize_aws_json_1_1(
                value["billing_records"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ViewBillingResponse:
    out: ViewBillingResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextPageMarker") is not None:
        out["next_page_marker"] = data["NextPageMarker"]
    if data.get("BillingRecords") is not None:
        import capo_route_53_domains.types.billing_records

        out["billing_records"] = (
            capo_route_53_domains.types.billing_records.deserialize_aws_json_1_1(
                data["BillingRecords"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ViewBillingResponse) -> dict:
    out: dict = {}
    if "next_page_marker" in value:
        out["NextPageMarker"] = value["next_page_marker"]
    if "billing_records" in value:
        import capo_route_53_domains.types.billing_records

        out["BillingRecords"] = (
            capo_route_53_domains.types.billing_records.serialize_cbor(
                value["billing_records"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ViewBillingResponse:
    out: ViewBillingResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextPageMarker") is not None:
        out["next_page_marker"] = data["NextPageMarker"]
    if data.get("BillingRecords") is not None:
        import capo_route_53_domains.types.billing_records

        out["billing_records"] = (
            capo_route_53_domains.types.billing_records.deserialize_cbor(
                data["BillingRecords"]
            )
        )
    return out
