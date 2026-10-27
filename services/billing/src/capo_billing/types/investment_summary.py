"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.amount
    import capo_billing.types.identifier_string
    import capo_billing.types.investment_type


class InvestmentSummary(TypedDict, closed=True):
    investment_summary_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the investment summary. Pass this value to <code>ListContractualInvestments</code> to list the investments within the summary, and to <code>CreateContractualInvestmentAttestation</code> to attest an investment. This value is 1–36 characters.</p>"""
    investment_name: "str"
    """<p>The name of the investment summary, used to reference the investment against a term in the physical contract. This value is 1–400 characters.</p>"""
    investment_type: "capo_billing.types.investment_type.InvestmentType"
    """<p>The type of the investment summary. Valid values are <code>MILESTONE_BASED</code> and <code>OUTCOME_BASED</code>. <code>OUTCOME_BASED</code> investments can be attested to, upon completion of outcomes. <code>MILESTONE_BASED</code> are automatically triggered by Amazon Web Services, based on the time schedule in the contract.</p>"""
    max_allowed_investment_disbursement_value: NotRequired[
        "capo_billing.types.amount.Amount"
    ]
    """<p>The maximum monetary value that can be disbursed against the investment summary, inclusive of all outcomes combined under the summary.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentSummary) -> dict:
    out: dict = {}
    out["investmentSummaryId"] = value["investment_summary_id"]
    out["investmentName"] = value["investment_name"]
    import capo_billing.types.investment_type

    out["investmentType"] = capo_billing.types.investment_type.serialize_aws_json_1_0(
        value["investment_type"]
    )
    if "max_allowed_investment_disbursement_value" in value:
        import capo_billing.types.amount

        out["maxAllowedInvestmentDisbursementValue"] = (
            capo_billing.types.amount.serialize_aws_json_1_0(
                value["max_allowed_investment_disbursement_value"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvestmentSummary:
    out: InvestmentSummary = {}  # type: ignore[typeddict-item]
    if data.get("investmentSummaryId") is not None:
        out["investment_summary_id"] = data["investmentSummaryId"]
    else:
        out["investment_summary_id"] = ""
    if data.get("investmentName") is not None:
        out["investment_name"] = data["investmentName"]
    else:
        out["investment_name"] = ""
    if data.get("investmentType") is not None:
        import capo_billing.types.investment_type

        out["investment_type"] = (
            capo_billing.types.investment_type.deserialize_aws_json_1_0(
                data["investmentType"]
            )
        )
    else:
        import typing

        out["investment_type"] = typing.cast(
            "capo_billing.types.investment_type.InvestmentType", ""
        )
    if data.get("maxAllowedInvestmentDisbursementValue") is not None:
        import capo_billing.types.amount

        out["max_allowed_investment_disbursement_value"] = (
            capo_billing.types.amount.deserialize_aws_json_1_0(
                data["maxAllowedInvestmentDisbursementValue"]
            )
        )
    return out
