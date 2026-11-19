"""Generated from Smithy shape ``com.amazonaws.health#OrganizationTagType``."""

from typing import Literal, TypeAlias, cast

OrganizationTagType: TypeAlias = Literal[
    "ORGANIZATION_RESOURCE_TAG",
    "ORGANIZATION_ACCOUNT_TAG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationTagType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OrganizationTagType:
    return cast(OrganizationTagType, data)
