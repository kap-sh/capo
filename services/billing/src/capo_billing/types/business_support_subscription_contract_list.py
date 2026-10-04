"""Generated from Smithy shape ``com.amazonaws.billing#BusinessSupportSubscriptionContractList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.business_support_subscription_contract

BusinessSupportSubscriptionContractList: TypeAlias = list[
    "capo_billing.types.business_support_subscription_contract.BusinessSupportSubscriptionContract"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessSupportSubscriptionContractList) -> list:
    import capo_billing.types.business_support_subscription_contract

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.business_support_subscription_contract.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BusinessSupportSubscriptionContractList:
    import capo_billing.types.business_support_subscription_contract

    out: BusinessSupportSubscriptionContractList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.business_support_subscription_contract.deserialize_aws_json_1_0(
                item
            )
        )
    return out
