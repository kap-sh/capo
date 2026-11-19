"""Generated from Smithy shape ``com.amazonaws.acmpca#KeyAlgorithm``."""

from typing import Literal, TypeAlias, cast

KeyAlgorithm: TypeAlias = Literal[
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "EC_prime256v1",
    "EC_secp384r1",
    "EC_secp521r1",
    "ML_DSA_44",
    "ML_DSA_65",
    "ML_DSA_87",
    "SM2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyAlgorithm:
    return cast(KeyAlgorithm, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: KeyAlgorithm) -> str:
    return value


def deserialize_cbor(data: str) -> KeyAlgorithm:
    return cast(KeyAlgorithm, data)
