"""Generated from Smithy shape ``com.amazonaws.kms#KeyUsageType``."""

from typing import Literal, TypeAlias, cast

KeyUsageType: TypeAlias = Literal[
    "SIGN_VERIFY",
    "ENCRYPT_DECRYPT",
    "GENERATE_VERIFY_MAC",
    "KEY_AGREEMENT",
    "ENCAPSULATE_DECAPSULATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyUsageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyUsageType:
    return cast(KeyUsageType, data)
