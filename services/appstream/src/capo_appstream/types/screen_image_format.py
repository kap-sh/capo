"""Generated from Smithy shape ``com.amazonaws.appstream#ScreenImageFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The image format for agent screen captures.</p> <ul> <li> <p>PNG - PNG format.</p> </li> <li> <p>JPEG - JPEG format.</p> </li> </ul>"""
ScreenImageFormat: TypeAlias = Literal[
    "PNG",
    "JPEG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScreenImageFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScreenImageFormat:
    return cast(ScreenImageFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScreenImageFormat) -> str:
    return value


def deserialize_cbor(data: str) -> ScreenImageFormat:
    return cast(ScreenImageFormat, data)
