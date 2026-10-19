"""Generated from Smithy shape ``com.amazonaws.billing#ListBillingViewSegmentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.billing_view_segments_list
    import capo_billing.types.page_token


class ListBillingViewSegmentsResponse(TypedDict, closed=True):
    items: "capo_billing.types.billing_view_segments_list.BillingViewSegmentsList"
    """<p> A list of billing view segments. Each segment covers a portion of the requested time period. The response omits hidden segments, so the segments it returns might not cover the entire requested time period. </p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p> The pagination token that is used on subsequent calls to list billing view segments. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBillingViewSegmentsResponse) -> dict:
    out: dict = {}
    import capo_billing.types.billing_view_segments_list

    out["items"] = capo_billing.types.billing_view_segments_list.serialize_aws_json_1_0(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBillingViewSegmentsResponse:
    out: ListBillingViewSegmentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_billing.types.billing_view_segments_list

        out["items"] = (
            capo_billing.types.billing_view_segments_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
