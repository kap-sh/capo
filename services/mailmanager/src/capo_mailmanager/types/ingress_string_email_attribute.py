"""Generated from Smithy shape ``com.amazonaws.mailmanager#IngressStringEmailAttribute``."""

from typing import Literal, TypeAlias, cast

IngressStringEmailAttribute: TypeAlias = Literal["RECIPIENT",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngressStringEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> IngressStringEmailAttribute:
    return cast(IngressStringEmailAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IngressStringEmailAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> IngressStringEmailAttribute:
    return cast(IngressStringEmailAttribute, data)
