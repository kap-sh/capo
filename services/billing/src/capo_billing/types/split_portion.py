"""Generated from Smithy shape ``com.amazonaws.billing#SplitPortion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.decimal_amount_string


class SplitPortion(TypedDict, closed=True):
    amount: "capo_billing.types.decimal_amount_string.DecimalAmountString"
    """<p>The amount of the new credit, in the currency of the credit that you split. The amount must be at least 100.00 in that currency. For example, if the credit is in USD, the amount must be at least USD $100.00.</p>"""
    description: NotRequired["str"]
    """<p>The description of the new credit. If you omit it, the new credit gets the original credit's description followed by its position in the request, for example <code>MAP credit - 1/3</code>. If you split that credit again, the name extends, for example <code>MAP credit - 1/3 - 2/2</code>. A generated name is at most 93 characters. If it would be longer, the name keeps only the beginning of the original description.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SplitPortion) -> dict:
    out: dict = {}
    out["amount"] = value["amount"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SplitPortion:
    out: SplitPortion = {}  # type: ignore[typeddict-item]
    if data.get("amount") is not None:
        out["amount"] = data["amount"]
    else:
        out["amount"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
