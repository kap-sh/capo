"""Generated from Smithy shape ``com.amazonaws.billing#AttestationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_billing.types.attestation_value
    import capo_billing.types.investment_distributions


class AttestationDetails(TypedDict, closed=True):
    attestation_value: "capo_billing.types.attestation_value.AttestationValue"
    """<p>The value being attested, expressed as either a monetary amount or one or more quantities. Exactly one form is set.</p>"""
    investment_distributions: NotRequired[
        "capo_billing.types.investment_distributions.InvestmentDistributions"
    ]
    """<p>The distribution of the resulting investment across the eligible investment accounts on the contract. If you omit this value, the full investment is allocated to the single eligible investment account on the contract. This value is required when multiple investment accounts are eligible. When you provide this value, the sum of all distributions must equal the resulting monetary investment value (the attested amount, or the value computed from the attested quantities using the investment multipliers). The list contains at most 200 distributions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttestationDetails) -> dict:
    out: dict = {}
    import capo_billing.types.attestation_value

    out["attestationValue"] = (
        capo_billing.types.attestation_value.serialize_aws_json_1_0(
            value["attestation_value"]
        )
    )
    if "investment_distributions" in value:
        import capo_billing.types.investment_distributions

        out["investmentDistributions"] = (
            capo_billing.types.investment_distributions.serialize_aws_json_1_0(
                value["investment_distributions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AttestationDetails:
    out: AttestationDetails = {}  # type: ignore[typeddict-item]
    if data.get("attestationValue") is not None:
        import capo_billing.types.attestation_value

        out["attestation_value"] = (
            capo_billing.types.attestation_value.deserialize_aws_json_1_0(
                data["attestationValue"]
            )
        )
    else:
        out["attestation_value"] = {"$unknown": {"name": ""}}
    if data.get("investmentDistributions") is not None:
        import capo_billing.types.investment_distributions

        out["investment_distributions"] = (
            capo_billing.types.investment_distributions.deserialize_aws_json_1_0(
                data["investmentDistributions"]
            )
        )
    return out
