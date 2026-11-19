"""Generated from Smithy shape ``com.amazonaws.codedeploy#BundleType``."""

from typing import Literal, TypeAlias, cast

BundleType: TypeAlias = Literal[
    "tar",
    "tgz",
    "zip",
    "YAML",
    "JSON",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BundleType:
    return cast(BundleType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BundleType) -> str:
    return value


def deserialize_cbor(data: str) -> BundleType:
    return cast(BundleType, data)
