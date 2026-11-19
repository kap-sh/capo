"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ApprovalRequirement``."""

from typing import Literal, TypeAlias, cast

ApprovalRequirement: TypeAlias = Literal[
    "REQUIRED",
    "NOT_REQUIRED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ApprovalRequirement) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ApprovalRequirement:
    return cast(ApprovalRequirement, data)
