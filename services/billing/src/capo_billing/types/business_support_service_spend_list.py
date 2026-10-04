"""Generated from Smithy shape ``com.amazonaws.billing#BusinessSupportServiceSpendList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.business_support_service_spend

BusinessSupportServiceSpendList: TypeAlias = list[
    "capo_billing.types.business_support_service_spend.BusinessSupportServiceSpend"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BusinessSupportServiceSpendList) -> list:
    import capo_billing.types.business_support_service_spend

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.business_support_service_spend.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BusinessSupportServiceSpendList:
    import capo_billing.types.business_support_service_spend

    out: BusinessSupportServiceSpendList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billing.types.business_support_service_spend.deserialize_aws_json_1_0(
                item
            )
        )
    return out
