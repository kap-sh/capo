"""Generated from Smithy shape ``com.amazonaws.billing#ListSourceViewsForBillingViewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_view_source_views_list
    import capo_billing.types.page_token


class ListSourceViewsForBillingViewResponse(TypedDict, closed=True):
    source_views: (
        "capo_billing.types.billing_view_source_views_list.BillingViewSourceViewsList"
    )
    """<p>A list of billing views used as the data source for the custom billing view. </p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p> The pagination token that is used on subsequent calls to list billing views. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSourceViewsForBillingViewResponse) -> dict:
    out: dict = {}
    import capo_billing.types.billing_view_source_views_list

    out["sourceViews"] = (
        capo_billing.types.billing_view_source_views_list.serialize_aws_json_1_0(
            value["source_views"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSourceViewsForBillingViewResponse:
    out: ListSourceViewsForBillingViewResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceViews") is not None:
        import capo_billing.types.billing_view_source_views_list

        out["source_views"] = (
            capo_billing.types.billing_view_source_views_list.deserialize_aws_json_1_0(
                data["sourceViews"]
            )
        )
    else:
        out["source_views"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
