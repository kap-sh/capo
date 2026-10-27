"""Generated from Smithy shape ``com.amazonaws.billing#ContractRestrictions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.contract_restriction

ContractRestrictions: TypeAlias = list[
    "capo_billing.types.contract_restriction.ContractRestriction"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContractRestrictions) -> list:
    import capo_billing.types.contract_restriction

    out: list = []
    for item in value:
        out.append(capo_billing.types.contract_restriction.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ContractRestrictions:
    import capo_billing.types.contract_restriction

    out: ContractRestrictions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.contract_restriction.deserialize_aws_json_1_0(item)
        )
    return out
