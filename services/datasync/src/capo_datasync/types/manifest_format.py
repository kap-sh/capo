"""Generated from Smithy shape ``com.amazonaws.datasync#ManifestFormat``."""

from typing import Literal, TypeAlias, cast

ManifestFormat: TypeAlias = Literal["CSV",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManifestFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManifestFormat:
    return cast(ManifestFormat, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ManifestFormat) -> str:
    return value


def deserialize_cbor(data: str) -> ManifestFormat:
    return cast(ManifestFormat, data)
