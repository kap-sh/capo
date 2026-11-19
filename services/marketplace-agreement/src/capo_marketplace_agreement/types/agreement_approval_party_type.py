"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalPartyType``."""

from typing import Literal, TypeAlias, cast

AgreementApprovalPartyType: TypeAlias = Literal[
    "REQUESTER",
    "AWS_ORGANIZATION_ADMIN",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalPartyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AgreementApprovalPartyType:
    return cast(AgreementApprovalPartyType, data)
