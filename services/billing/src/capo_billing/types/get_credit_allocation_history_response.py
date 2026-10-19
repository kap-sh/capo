"""Generated from Smithy shape ``com.amazonaws.billing#GetCreditAllocationHistoryResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.credit_allocation_history_list
    import capo_billing.types.failed_months_list
    import capo_billing.types.page_token


class GetCreditAllocationHistoryResponse(TypedDict, closed=True):
    credit_allocation_history_list: NotRequired[
        "capo_billing.types.credit_allocation_history_list.CreditAllocationHistoryList"
    ]
    """<p>Allocation entries sorted by <code>billingMonth</code> in descending order.</p>"""
    partial_results: "bool"
    """<p> <code>true</code> when data could not be retrieved for one or more billing months. The <code>failedMonths</code> field lists which months are missing.</p>"""
    failed_months: NotRequired["capo_billing.types.failed_months_list.FailedMonthsList"]
    """<p>Billing months in <code>YYYY-MM</code> format that failed to return data. Non-empty only when <code>partialResults</code> is <code>true</code>.</p>"""
    next_token: NotRequired["capo_billing.types.page_token.PageToken"]
    """<p>Pagination token. Present when more pages are available; <code>null</code> when there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetCreditAllocationHistoryResponse) -> dict:
    out: dict = {}
    if "credit_allocation_history_list" in value:
        import capo_billing.types.credit_allocation_history_list

        out["creditAllocationHistoryList"] = (
            capo_billing.types.credit_allocation_history_list.serialize_aws_json_1_0(
                value["credit_allocation_history_list"]
            )
        )
    out["partialResults"] = value["partial_results"]
    if "failed_months" in value:
        import capo_billing.types.failed_months_list

        out["failedMonths"] = (
            capo_billing.types.failed_months_list.serialize_aws_json_1_0(
                value["failed_months"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetCreditAllocationHistoryResponse:
    out: GetCreditAllocationHistoryResponse = {}  # type: ignore[typeddict-item]
    if data.get("creditAllocationHistoryList") is not None:
        import capo_billing.types.credit_allocation_history_list

        out["credit_allocation_history_list"] = (
            capo_billing.types.credit_allocation_history_list.deserialize_aws_json_1_0(
                data["creditAllocationHistoryList"]
            )
        )
    if data.get("partialResults") is not None:
        out["partial_results"] = data["partialResults"]
    else:
        out["partial_results"] = False
    if data.get("failedMonths") is not None:
        import capo_billing.types.failed_months_list

        out["failed_months"] = (
            capo_billing.types.failed_months_list.deserialize_aws_json_1_0(
                data["failedMonths"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
