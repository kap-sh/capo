"""Generated from Smithy shape ``com.amazonaws.licensemanager#GrantType``."""

from typing import Literal, TypeAlias, cast

GrantType: TypeAlias = Literal[
    "BuyerGrant",
    "DelegateGrant",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GrantType:
    return cast(GrantType, data)
