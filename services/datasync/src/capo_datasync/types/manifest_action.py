"""Generated from Smithy shape ``com.amazonaws.datasync#ManifestAction``."""

from typing import Literal, TypeAlias, cast

ManifestAction: TypeAlias = Literal["TRANSFER",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManifestAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManifestAction:
    return cast(ManifestAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ManifestAction) -> str:
    return value


def deserialize_cbor(data: str) -> ManifestAction:
    return cast(ManifestAction, data)
