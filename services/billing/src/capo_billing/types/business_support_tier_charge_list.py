"""Generated from Smithy shape ``com.amazonaws.billing#BusinessSupportTierChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.business_support_tier_charge

BusinessSupportTierChargeList: TypeAlias = list[
    "capo_billing.types.business_support_tier_charge.BusinessSupportTierCharge"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessSupportTierChargeList) -> list:
    import capo_billing.types.business_support_tier_charge

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.business_support_tier_charge.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BusinessSupportTierChargeList:
    import capo_billing.types.business_support_tier_charge

    out: BusinessSupportTierChargeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.business_support_tier_charge.deserialize_aws_json_1_0(
                item
            )
        )
    return out
