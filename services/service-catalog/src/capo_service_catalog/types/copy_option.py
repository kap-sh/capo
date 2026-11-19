"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CopyOption``."""

from typing import Literal, TypeAlias, cast

CopyOption: TypeAlias = Literal["CopyTags",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CopyOption:
    return cast(CopyOption, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CopyOption) -> str:
    return value


def deserialize_cbor(data: str) -> CopyOption:
    return cast(CopyOption, data)
