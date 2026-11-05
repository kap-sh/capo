"""Generated from Smithy shape ``com.amazonaws.s3tables#CompressionCodec``."""

from typing import Literal, TypeAlias, cast

CompressionCodec: TypeAlias = Literal[
    "zstd",
    "snappy",
    "gzip",
    "uncompressed",
]


# --- restJson1 ser/de ---
def serialize_json(value: CompressionCodec) -> str:
    return value


def deserialize_json(data: str) -> CompressionCodec:
    return cast(CompressionCodec, data)
