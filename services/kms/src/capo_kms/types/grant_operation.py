"""Generated from Smithy shape ``com.amazonaws.kms#GrantOperation``."""

from typing import Literal, TypeAlias, cast

GrantOperation: TypeAlias = Literal[
    "Decrypt",
    "Encrypt",
    "GenerateDataKey",
    "GenerateDataKeyWithoutPlaintext",
    "ReEncryptFrom",
    "ReEncryptTo",
    "Sign",
    "Verify",
    "GetPublicKey",
    "CreateGrant",
    "RetireGrant",
    "DescribeKey",
    "GenerateDataKeyPair",
    "GenerateDataKeyPairWithoutPlaintext",
    "GenerateMac",
    "VerifyMac",
    "DeriveSharedSecret",
    "Encapsulate",
    "Decapsulate",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantOperation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GrantOperation:
    return cast(GrantOperation, data)
