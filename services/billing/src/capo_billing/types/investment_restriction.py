"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentRestriction``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.amount


class InvestmentRestriction(TypedDict, closed=True):
    amount: "capo_billing.types.amount.Amount"
    """<p>The maximum monetary amount allowed under the restriction.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentRestriction) -> dict:
    out: dict = {}
    import capo_billing.types.amount

    out["amount"] = capo_billing.types.amount.serialize_aws_json_1_0(value["amount"])
    return out


def deserialize_aws_json_1_0(data: dict) -> InvestmentRestriction:
    out: InvestmentRestriction = {}  # type: ignore[typeddict-item]
    if data.get("amount") is not None:
        import capo_billing.types.amount

        out["amount"] = capo_billing.types.amount.deserialize_aws_json_1_0(
            data["amount"]
        )
    else:
        raise DeserializationError("InvestmentRestriction.amount required")
    return out
