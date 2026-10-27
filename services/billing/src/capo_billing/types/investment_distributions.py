"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentDistributions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.investment_distribution

InvestmentDistributions: TypeAlias = list[
    "capo_billing.types.investment_distribution.InvestmentDistribution"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentDistributions) -> list:
    import capo_billing.types.investment_distribution

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.investment_distribution.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InvestmentDistributions:
    import capo_billing.types.investment_distribution

    out: InvestmentDistributions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.investment_distribution.deserialize_aws_json_1_0(item)
        )
    return out
