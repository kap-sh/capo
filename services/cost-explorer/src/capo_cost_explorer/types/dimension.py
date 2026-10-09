"""Generated from Smithy shape ``com.amazonaws.costexplorer#Dimension``."""

from typing import Literal, TypeAlias, cast

Dimension: TypeAlias = Literal[
    "AZ",
    "INSTANCE_TYPE",
    "LINKED_ACCOUNT",
    "PAYER_ACCOUNT",
    "LINKED_ACCOUNT_NAME",
    "OPERATION",
    "PURCHASE_TYPE",
    "REGION",
    "SERVICE",
    "SERVICE_CODE",
    "USAGE_TYPE",
    "USAGE_TYPE_GROUP",
    "RECORD_TYPE",
    "OPERATING_SYSTEM",
    "TENANCY",
    "SCOPE",
    "PLATFORM",
    "SUBSCRIPTION_ID",
    "LEGAL_ENTITY_NAME",
    "DEPLOYMENT_OPTION",
    "DATABASE_ENGINE",
    "CACHE_ENGINE",
    "INSTANCE_TYPE_FAMILY",
    "BILLING_ENTITY",
    "RESERVATION_ID",
    "RESOURCE_ID",
    "RIGHTSIZING_TYPE",
    "SAVINGS_PLANS_TYPE",
    "SAVINGS_PLAN_ARN",
    "PAYMENT_OPTION",
    "AGREEMENT_END_DATE_TIME_AFTER",
    "AGREEMENT_END_DATE_TIME_BEFORE",
    "INVOICING_ENTITY",
    "ANOMALY_TOTAL_IMPACT_ABSOLUTE",
    "ANOMALY_TOTAL_IMPACT_PERCENTAGE",
    "PRODUCT_ATTRIBUTE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Dimension) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Dimension:
    return cast(Dimension, data)
