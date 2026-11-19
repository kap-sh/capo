"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeAttribute``."""

from typing import Literal, TypeAlias, cast

ThemeAttribute: TypeAlias = Literal["FOOTER_LINKS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThemeAttribute) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThemeAttribute:
    return cast(ThemeAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThemeAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> ThemeAttribute:
    return cast(ThemeAttribute, data)
