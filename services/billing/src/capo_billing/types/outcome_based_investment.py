"""Generated from Smithy shape ``com.amazonaws.billing#OutcomeBasedInvestment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.amount
    import capo_billing.types.identifier_string
    import capo_billing.types.interval
    import capo_billing.types.investment_multipliers
    import capo_billing.types.investment_restrictions


class OutcomeBasedInvestment(TypedDict, closed=True):
    investment_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the investment, as returned by <code>ListContractualInvestments</code>. This value is 1–36 characters.</p>"""
    outcome_description: "str"
    """<p>The description of what must be completed to attest the outcome. This value is 1–2048 characters.</p>"""
    attestation_window: "capo_billing.types.interval.Interval"
    """<p>The time window, expressed as an interval with inclusive start and end dates, during which outcomes can be attested to.</p>"""
    investment_restrictions: NotRequired[
        "capo_billing.types.investment_restrictions.InvestmentRestrictions"
    ]
    """<p>The restrictions that cap the value that can be disbursed for the investment. The list contains at most 10 restrictions.</p>"""
    investment_multipliers: NotRequired[
        "capo_billing.types.investment_multipliers.InvestmentMultipliers"
    ]
    """<p>The multipliers used to compute the investment value from the attestation input. The list contains at most 200 multipliers. Multipliers are derived from the terms of the private pricing contract.</p>"""
    disbursed_value: "capo_billing.types.amount.Amount"
    """<p>The total value already disbursed against the investment. This value can be distributed among the investment accounts distribution.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OutcomeBasedInvestment) -> dict:
    out: dict = {}
    out["investmentId"] = value["investment_id"]
    out["outcomeDescription"] = value["outcome_description"]
    import capo_billing.types.interval

    out["attestationWindow"] = capo_billing.types.interval.serialize_aws_json_1_0(
        value["attestation_window"]
    )
    if "investment_restrictions" in value:
        import capo_billing.types.investment_restrictions

        out["investmentRestrictions"] = (
            capo_billing.types.investment_restrictions.serialize_aws_json_1_0(
                value["investment_restrictions"]
            )
        )
    if "investment_multipliers" in value:
        import capo_billing.types.investment_multipliers

        out["investmentMultipliers"] = (
            capo_billing.types.investment_multipliers.serialize_aws_json_1_0(
                value["investment_multipliers"]
            )
        )
    import capo_billing.types.amount

    out["disbursedValue"] = capo_billing.types.amount.serialize_aws_json_1_0(
        value["disbursed_value"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OutcomeBasedInvestment:
    out: OutcomeBasedInvestment = {}  # type: ignore[typeddict-item]
    if data.get("investmentId") is not None:
        out["investment_id"] = data["investmentId"]
    else:
        out["investment_id"] = ""
    if data.get("outcomeDescription") is not None:
        out["outcome_description"] = data["outcomeDescription"]
    else:
        out["outcome_description"] = ""
    if data.get("attestationWindow") is not None:
        import capo_billing.types.interval

        out["attestation_window"] = (
            capo_billing.types.interval.deserialize_aws_json_1_0(
                data["attestationWindow"]
            )
        )
    else:
        raise DeserializationError("OutcomeBasedInvestment.attestation_window required")
    if data.get("investmentRestrictions") is not None:
        import capo_billing.types.investment_restrictions

        out["investment_restrictions"] = (
            capo_billing.types.investment_restrictions.deserialize_aws_json_1_0(
                data["investmentRestrictions"]
            )
        )
    if data.get("investmentMultipliers") is not None:
        import capo_billing.types.investment_multipliers

        out["investment_multipliers"] = (
            capo_billing.types.investment_multipliers.deserialize_aws_json_1_0(
                data["investmentMultipliers"]
            )
        )
    if data.get("disbursedValue") is not None:
        import capo_billing.types.amount

        out["disbursed_value"] = capo_billing.types.amount.deserialize_aws_json_1_0(
            data["disbursedValue"]
        )
    else:
        raise DeserializationError("OutcomeBasedInvestment.disbursed_value required")
    return out
