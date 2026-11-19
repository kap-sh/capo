"""Generated from Smithy shape ``com.amazonaws.gamelift#LocationUpdateStatus``."""

from typing import Literal, TypeAlias, cast

LocationUpdateStatus: TypeAlias = Literal["PENDING_UPDATE",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LocationUpdateStatus:
    return cast(LocationUpdateStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LocationUpdateStatus) -> str:
    return value


def deserialize_cbor(data: str) -> LocationUpdateStatus:
    return cast(LocationUpdateStatus, data)
