"""Generated from Smithy shape ``com.amazonaws.billing#Investments``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.investment

Investments: TypeAlias = list["capo_billing.types.investment.Investment"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Investments) -> list:
    import capo_billing.types.investment

    out: list = []
    for item in value:
        out.append(capo_billing.types.investment.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Investments:
    import capo_billing.types.investment

    out: Investments = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.investment.deserialize_aws_json_1_0(item))
    return out
