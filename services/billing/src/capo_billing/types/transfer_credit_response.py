"""Generated from Smithy shape ``com.amazonaws.billing#TransferCreditResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.credit_id
    import capo_billing.types.decimal_amount_string


class TransferCreditResponse(TypedDict, closed=True):
    source_credit_id: "capo_billing.types.credit_id.CreditId"
    """<p>The ID of the transferred credit. The credit keeps this ID.</p>"""
    new_credit_id: NotRequired["capo_billing.types.credit_id.CreditId"]
    """<p>Always the same as <code>sourceCreditId</code>, because a transfer moves the credit and creates no new one. A dry run omits this field.</p>"""
    destination_account_id: "capo_billing.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID that owns the credit after the transfer.</p>"""
    amount: "capo_billing.types.decimal_amount_string.DecimalAmountString"
    """<p>The available balance of the credit, which is its remaining balance minus any amount reserved for a bill that isn't finalized.</p>"""
    dry_run: "bool"
    """<p>Specifies whether the request was a dry run. If <code>true</code>, the operation didn't change the credit.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransferCreditResponse) -> dict:
    out: dict = {}
    out["sourceCreditId"] = value["source_credit_id"]
    if "new_credit_id" in value:
        out["newCreditId"] = value["new_credit_id"]
    out["destinationAccountId"] = value["destination_account_id"]
    out["amount"] = value["amount"]
    out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TransferCreditResponse:
    out: TransferCreditResponse = {}  # type: ignore[typeddict-item]
    if data.get("sourceCreditId") is not None:
        out["source_credit_id"] = data["sourceCreditId"]
    else:
        out["source_credit_id"] = ""
    if data.get("newCreditId") is not None:
        out["new_credit_id"] = data["newCreditId"]
    if data.get("destinationAccountId") is not None:
        out["destination_account_id"] = data["destinationAccountId"]
    else:
        out["destination_account_id"] = ""
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    else:
        out["amount"] = ""
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    else:
        out["dry_run"] = False
    return out
