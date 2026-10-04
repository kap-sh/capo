"""Generated from Smithy shape ``com.amazonaws.billing#BusinessSupportAccountChargeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.business_support_account_charge

BusinessSupportAccountChargeList: TypeAlias = list[
    "capo_billing.types.business_support_account_charge.BusinessSupportAccountCharge"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessSupportAccountChargeList) -> list:
    import capo_billing.types.business_support_account_charge

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.business_support_account_charge.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BusinessSupportAccountChargeList:
    import capo_billing.types.business_support_account_charge

    out: BusinessSupportAccountChargeList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.business_support_account_charge.deserialize_aws_json_1_0(
                item
            )
        )
    return out
