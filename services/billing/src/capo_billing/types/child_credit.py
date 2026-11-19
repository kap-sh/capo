"""Generated from Smithy shape ``com.amazonaws.billing#ChildCredit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.credit_id
    import capo_billing.types.decimal_amount_string


class ChildCredit(TypedDict, closed=True):
    credit_id: NotRequired["capo_billing.types.credit_id.CreditId"]
    """<p>The ID of the new credit. A dry run omits this field.</p>"""
    amount: "capo_billing.types.decimal_amount_string.DecimalAmountString"
    """<p>The amount of the new credit.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChildCredit) -> dict:
    out: dict = {}
    if "credit_id" in value:
        out["creditId"] = value["credit_id"]
    out["amount"] = value["amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ChildCredit:
    out: ChildCredit = {}  # type: ignore[typeddict-item]
    if data.get("creditId") is not None:
        out["credit_id"] = data["creditId"]
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    else:
        out["amount"] = ""
    return out
