"""Generated from Smithy shape ``com.amazonaws.appstream#StorageConnectorType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of storage connector.</p>"""
StorageConnectorType: TypeAlias = Literal[
    "HOMEFOLDERS",
    "GOOGLE_DRIVE",
    "ONE_DRIVE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnectorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StorageConnectorType:
    return cast(StorageConnectorType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StorageConnectorType) -> str:
    return value


def deserialize_cbor(data: str) -> StorageConnectorType:
    return cast(StorageConnectorType, data)
