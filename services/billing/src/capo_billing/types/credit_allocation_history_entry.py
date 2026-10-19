"""Generated from Smithy shape ``com.amazonaws.billing#CreditAllocationHistoryEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.amount
    import capo_billing.types.billing_month
    import capo_billing.types.credit_id


class CreditAllocationHistoryEntry(TypedDict, closed=True):
    credit_id: "capo_billing.types.credit_id.CreditId"
    """<p>The identifier of the credit that was applied.</p>"""
    credit_amount: "capo_billing.types.amount.Amount"
    """<p>The amount of credit applied. Negative values represent credits that reduced the bill.</p>"""
    description: NotRequired["str"]
    """<p>A human-readable description of the credit allocation.</p>"""
    account_id: "capo_billing.types.account_id.AccountId"
    """<p>The Amazon Web Services account the credit was applied to.</p>"""
    applied_service_name: "str"
    """<p>The Amazon Web Services service the credit was applied to.</p>"""
    billing_month: "capo_billing.types.billing_month.BillingMonth"
    """<p>The billing month of the application in <code>YYYY-MM</code> format.</p>"""
    is_estimated_bill: "bool"
    """<p> <code>true</code> when the entry was applied to an in-flight bill that has not yet been finalized.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreditAllocationHistoryEntry) -> dict:
    out: dict = {}
    out["creditId"] = value["credit_id"]
    import capo_billing.types.amount

    out["creditAmount"] = capo_billing.types.amount.serialize_aws_json_1_0(
        value["credit_amount"]
    )
    if "description" in value:
        out["description"] = value["description"]
    out["accountId"] = value["account_id"]
    out["appliedServiceName"] = value["applied_service_name"]
    out["billingMonth"] = value["billing_month"]
    out["isEstimatedBill"] = value["is_estimated_bill"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreditAllocationHistoryEntry:
    out: CreditAllocationHistoryEntry = {}  # type: ignore[typeddict-item]
    if data.get("creditId") is not None:
        out["credit_id"] = data["creditId"]
    else:
        out["credit_id"] = ""
    if data.get("creditAmount") is not None:
        import capo_billing.types.amount

        out["credit_amount"] = capo_billing.types.amount.deserialize_aws_json_1_0(
            data["creditAmount"]
        )
    else:
        raise DeserializationError(
            "CreditAllocationHistoryEntry.credit_amount required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("appliedServiceName") is not None:
        out["applied_service_name"] = data["appliedServiceName"]
    else:
        out["applied_service_name"] = ""
    if data.get("billingMonth") is not None:
        out["billing_month"] = data["billingMonth"]
    else:
        out["billing_month"] = ""
    if data.get("isEstimatedBill") is not None:
        out["is_estimated_bill"] = data["isEstimatedBill"]
    else:
        out["is_estimated_bill"] = False
    return out
