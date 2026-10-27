"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentDistribution``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.account_id
    import capo_billing.types.amount


class InvestmentDistribution(TypedDict, closed=True):
    account_id: "capo_billing.types.account_id.AccountId"
    """<p>The recipient Amazon Web Services account ID that receives this portion of the investment. This must be one of the eligible investment accounts on the contract.</p>"""
    investment_amount: "capo_billing.types.amount.Amount"
    """<p>The monetary value allocated to the recipient account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentDistribution) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_billing.types.amount

    out["investmentAmount"] = capo_billing.types.amount.serialize_aws_json_1_0(
        value["investment_amount"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvestmentDistribution:
    out: InvestmentDistribution = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("investmentAmount") is not None:
        import capo_billing.types.amount

        out["investment_amount"] = capo_billing.types.amount.deserialize_aws_json_1_0(
            data["investmentAmount"]
        )
    else:
        raise DeserializationError("InvestmentDistribution.investment_amount required")
    return out
