"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentMultipliers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.investment_multiplier

InvestmentMultipliers: TypeAlias = list[
    "capo_billing.types.investment_multiplier.InvestmentMultiplier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentMultipliers) -> list:
    import capo_billing.types.investment_multiplier

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.investment_multiplier.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InvestmentMultipliers:
    import capo_billing.types.investment_multiplier

    out: InvestmentMultipliers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.investment_multiplier.deserialize_aws_json_1_0(item)
        )
    return out
