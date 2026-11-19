"""Generated from Smithy shape ``com.amazonaws.directconnect#NniPartnerType``."""

from typing import Literal, TypeAlias, cast

NniPartnerType: TypeAlias = Literal[
    "v1",
    "v2",
    "nonPartner",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NniPartnerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NniPartnerType:
    return cast(NniPartnerType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NniPartnerType) -> str:
    return value


def deserialize_cbor(data: str) -> NniPartnerType:
    return cast(NniPartnerType, data)
