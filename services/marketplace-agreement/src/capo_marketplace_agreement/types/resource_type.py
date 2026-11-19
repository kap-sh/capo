"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "Agreement",
    "AgreementRequest",
    "AgreementProposal",
    "Charge",
    "PaymentRequest",
    "Invoice",
    "AgreementCancellationRequest",
    "BillingAdjustmentRequest",
    "AgreementApproval",
    "AgreementRequestApprovalPlan",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceType:
    return cast(ResourceType, data)
