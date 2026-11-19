"""Generated from Smithy shape ``com.amazonaws.appstream#ThemeStyling``."""

from typing import Literal, TypeAlias, cast

ThemeStyling: TypeAlias = Literal[
    "LIGHT_BLUE",
    "BLUE",
    "PINK",
    "RED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThemeStyling) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ThemeStyling:
    return cast(ThemeStyling, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThemeStyling) -> str:
    return value


def deserialize_cbor(data: str) -> ThemeStyling:
    return cast(ThemeStyling, data)
