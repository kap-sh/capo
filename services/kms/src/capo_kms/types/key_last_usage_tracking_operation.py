"""Generated from Smithy shape ``com.amazonaws.kms#KeyLastUsageTrackingOperation``."""

from typing import Literal, TypeAlias, cast

KeyLastUsageTrackingOperation: TypeAlias = Literal[
    "Decrypt",
    "DeriveSharedSecret",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateDataKeyWithoutPlaintext",
    "GenerateMac",
    "ReEncrypt",
    "Sign",
    "Verify",
    "VerifyMac",
    "Encapsulate",
    "Decapsulate",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyLastUsageTrackingOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyLastUsageTrackingOperation:
    return cast(KeyLastUsageTrackingOperation, data)
