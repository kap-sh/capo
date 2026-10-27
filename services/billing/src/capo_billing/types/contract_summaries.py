"""Generated from Smithy shape ``com.amazonaws.billing#ContractSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.contract_summary

ContractSummaries: TypeAlias = list[
    "capo_billing.types.contract_summary.ContractSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContractSummaries) -> list:
    import capo_billing.types.contract_summary

    out: list = []
    for item in value:
        out.append(capo_billing.types.contract_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ContractSummaries:
    import capo_billing.types.contract_summary

    out: ContractSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_billing.types.contract_summary.deserialize_aws_json_1_0(item))
    return out
