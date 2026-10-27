"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentRestrictions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.investment_restriction

InvestmentRestrictions: TypeAlias = list[
    "capo_billing.types.investment_restriction.InvestmentRestriction"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentRestrictions) -> list:
    import capo_billing.types.investment_restriction

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.investment_restriction.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InvestmentRestrictions:
    import capo_billing.types.investment_restriction

    out: InvestmentRestrictions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.investment_restriction.deserialize_aws_json_1_0(item)
        )
    return out
