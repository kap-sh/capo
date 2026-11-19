"""Generated from Smithy shape ``com.amazonaws.health#AccountTagType``."""

from typing import Literal, TypeAlias, cast

AccountTagType: TypeAlias = Literal["ACCOUNT_RESOURCE_TAG",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountTagType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountTagType:
    return cast(AccountTagType, data)
