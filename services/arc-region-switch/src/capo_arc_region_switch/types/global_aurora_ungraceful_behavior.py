"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GlobalAuroraUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

GlobalAuroraUngracefulBehavior: TypeAlias = Literal["failover",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalAuroraUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GlobalAuroraUngracefulBehavior:
    return cast(GlobalAuroraUngracefulBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GlobalAuroraUngracefulBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> GlobalAuroraUngracefulBehavior:
    return cast(GlobalAuroraUngracefulBehavior, data)
