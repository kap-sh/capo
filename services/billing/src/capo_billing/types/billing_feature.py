"""Generated from Smithy shape ``com.amazonaws.billing#BillingFeature``."""

from typing import Literal, TypeAlias, cast

BillingFeature: TypeAlias = Literal[
    "RI_SHARING",
    "RI_SHARING_HISTORY",
    "CREDIT_SHARING",
    "CREDIT_SHARING_HISTORY",
    "CREDIT_LEVEL_SHARING",
    "BILLING_ALERTS",
    "CREDIT_PREFERENCE_OPTIONS",
    "BENEFIT_LEVEL_SHARING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingFeature) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingFeature:
    return cast(BillingFeature, data)
