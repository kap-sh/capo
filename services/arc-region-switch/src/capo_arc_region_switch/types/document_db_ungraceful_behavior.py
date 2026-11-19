"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#DocumentDbUngracefulBehavior``."""

from typing import Literal, TypeAlias, cast

DocumentDbUngracefulBehavior: TypeAlias = Literal["failover",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DocumentDbUngracefulBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DocumentDbUngracefulBehavior:
    return cast(DocumentDbUngracefulBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentDbUngracefulBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> DocumentDbUngracefulBehavior:
    return cast(DocumentDbUngracefulBehavior, data)
