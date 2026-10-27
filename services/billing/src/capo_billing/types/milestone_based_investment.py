"""Generated from Smithy shape ``com.amazonaws.billing#MilestoneBasedInvestment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.amount
    import capo_billing.types.identifier_string


class MilestoneBasedInvestment(TypedDict, closed=True):
    investment_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the investment, as returned by <code>ListContractualInvestments</code>. This value is 1–36 characters.</p>"""
    investment_value: "capo_billing.types.amount.Amount"
    """<p>The total value of the investment, including its currency and amount.</p>"""
    investment_disbursed_at: "datetime.datetime"
    """<p>The date on which the investment is disbursed to the investment accounts.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MilestoneBasedInvestment) -> dict:
    out: dict = {}
    out["investmentId"] = value["investment_id"]
    import capo_billing.types.amount

    out["investmentValue"] = capo_billing.types.amount.serialize_aws_json_1_0(
        value["investment_value"]
    )
    import capo_billing.types._prelude.timestamp

    out["investmentDisbursedAt"] = (
        capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
            value["investment_disbursed_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MilestoneBasedInvestment:
    out: MilestoneBasedInvestment = {}  # type: ignore[typeddict-item]
    if data.get("investmentId") is not None:
        out["investment_id"] = data["investmentId"]
    else:
        out["investment_id"] = ""
    if data.get("investmentValue") is not None:
        import capo_billing.types.amount

        out["investment_value"] = capo_billing.types.amount.deserialize_aws_json_1_0(
            data["investmentValue"]
        )
    else:
        raise DeserializationError("MilestoneBasedInvestment.investment_value required")
    if data.get("investmentDisbursedAt") is not None:
        import capo_billing.types._prelude.timestamp

        out["investment_disbursed_at"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["investmentDisbursedAt"]
            )
        )
    else:
        import datetime

        out["investment_disbursed_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
