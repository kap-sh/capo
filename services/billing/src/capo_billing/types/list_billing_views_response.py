"""Generated from Smithy shape ``com.amazonaws.billing#ListBillingViewsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_view_list
    import capo_billing.types.page_token


class ListBillingViewsResponse(TypedDict, closed=True):
    billing_views: "capo_billing.types.billing_view_list.BillingViewList"
    """<p>A list of <code>BillingViewListElement</code> retrieved.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token to use on subsequent calls to list billing views. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillingViewsResponse) -> dict:
    out: dict = {}
    import capo_billing.types.billing_view_list

    out["billingViews"] = capo_billing.types.billing_view_list.serialize_aws_json_1_0(
        value["billing_views"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillingViewsResponse:
    out: ListBillingViewsResponse = {}  # type: ignore[typeddict-item]
    if data.get("billingViews") is not None:
        import capo_billing.types.billing_view_list

        out["billing_views"] = (
            capo_billing.types.billing_view_list.deserialize_aws_json_1_0(
                data["billingViews"]
            )
        )
    else:
        out["billing_views"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListBillingViewsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "billing_views" in value:
        import capo_billing.types.billing_view_list

        out["billing_views"] = capo_billing.types.billing_view_list.redact_sensitive(
            value["billing_views"]
        )
    return out
