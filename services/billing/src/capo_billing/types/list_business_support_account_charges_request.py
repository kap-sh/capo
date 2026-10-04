"""Generated from Smithy shape ``com.amazonaws.billing#ListBusinessSupportAccountChargesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.business_support_billing_month
    import capo_billing.types.page_token


class ListBusinessSupportAccountChargesRequest(TypedDict, closed=True):
    billing_month: (
        "capo_billing.types.business_support_billing_month.BusinessSupportBillingMonth"
    )
    """<p>The billing month to retrieve Business Support charges for, in YYYY-MM format. You can request the current month (charges will be estimated) or a past month (charges will be finalized).</p>"""
    account_id: NotRequired["capo_billing.types.account_id.AccountId"]
    """<p>The linked account ID to filter results to a specific account. If you don't specify a value, the response includes charges for all linked accounts.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page. Default is 100.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token for the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListBusinessSupportAccountChargesRequest) -> dict:
    out: dict = {}
    out["billingMonth"] = value["billing_month"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListBusinessSupportAccountChargesRequest:
    out: ListBusinessSupportAccountChargesRequest = {}  # type: ignore[typeddict-item]
    if data.get("billingMonth") is not None:
        out["billing_month"] = data["billingMonth"]
    else:
        raise DeserializationError(
            "ListBusinessSupportAccountChargesRequest.billing_month required"
        )
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
