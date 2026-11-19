"""Generated from Smithy shape ``com.amazonaws.pi#FeatureStatus``."""

from typing import Literal, TypeAlias, cast

FeatureStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "UNSUPPORTED",
    "ENABLED_PENDING_REBOOT",
    "DISABLED_PENDING_REBOOT",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeatureStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeatureStatus:
    return cast(FeatureStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FeatureStatus) -> str:
    return value


def deserialize_cbor(data: str) -> FeatureStatus:
    return cast(FeatureStatus, data)
