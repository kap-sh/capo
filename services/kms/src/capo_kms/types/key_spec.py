"""Generated from Smithy shape ``com.amazonaws.kms#KeySpec``."""

from typing import Literal, TypeAlias, cast

KeySpec: TypeAlias = Literal[
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "ECC_NIST_P256",
    "ECC_NIST_P384",
    "ECC_NIST_P521",
    "ECC_SECG_P256K1",
    "SYMMETRIC_DEFAULT",
    "HMAC_224",
    "HMAC_256",
    "HMAC_384",
    "HMAC_512",
    "SM2",
    "ML_DSA_44",
    "ML_DSA_65",
    "ML_DSA_87",
    "ECC_NIST_EDWARDS25519",
    "ML_KEM_512",
    "ML_KEM_768",
    "ML_KEM_1024",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeySpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeySpec:
    return cast(KeySpec, data)
