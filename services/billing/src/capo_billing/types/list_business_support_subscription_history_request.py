"""Generated from Smithy shape ``com.amazonaws.billing#ListBusinessSupportSubscriptionHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.account_id
    import capo_billing.types.business_support_billing_month
    import capo_billing.types.page_token


class ListBusinessSupportSubscriptionHistoryRequest(TypedDict, closed=True):
    billing_month: NotRequired[
        "capo_billing.types.business_support_billing_month.BusinessSupportBillingMonth"
    ]
    """<p>The billing month to retrieve subscription contracts for, in YYYY-MM format. If you don't specify a value, defaults to the current month.</p>"""
    account_id: NotRequired["capo_billing.types.account_id.AccountId"]
    """<p>The account ID to filter results to a specific account. If you don't specify a value, the response includes subscription history for all accounts.</p>"""
    start_date: NotRequired["datetime.datetime"]
    """<p>The start date to filter subscription contracts from.</p>"""
    end_date: NotRequired["datetime.datetime"]
    """<p>The end date to filter subscription contracts to.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page. Default is 100.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>The pagination token for the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: ListBusinessSupportSubscriptionHistoryRequest,
) -> dict:
    out: dict = {}
    if "billing_month" in value:
        out["billingMonth"] = value["billing_month"]
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "start_date" in value:
        import capo_billing.types._prelude.timestamp

        out["startDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["start_date"]
        )
    if "end_date" in value:
        import capo_billing.types._prelude.timestamp

        out["endDate"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["end_date"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> ListBusinessSupportSubscriptionHistoryRequest:
    out: ListBusinessSupportSubscriptionHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("billingMonth") is not None:
        out["billing_month"] = data["billingMonth"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("startDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["start_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startDate"]
            )
        )
    if data.get("endDate") is not None:
        import capo_billing.types._prelude.timestamp

        out["end_date"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["endDate"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
