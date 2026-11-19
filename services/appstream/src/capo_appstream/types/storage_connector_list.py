"""Generated from Smithy shape ``com.amazonaws.appstream#StorageConnectorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.storage_connector

StorageConnectorList: TypeAlias = list[
    "capo_appstream.types.storage_connector.StorageConnector"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StorageConnectorList) -> list:
    import capo_appstream.types.storage_connector

    out: list = []
    for item in value:
        out.append(capo_appstream.types.storage_connector.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StorageConnectorList:
    import capo_appstream.types.storage_connector

    out: StorageConnectorList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_appstream.types.storage_connector.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StorageConnectorList) -> list:
    import capo_appstream.types.storage_connector

    out: list = []
    for item in value:
        out.append(capo_appstream.types.storage_connector.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> StorageConnectorList:
    import capo_appstream.types.storage_connector

    out: StorageConnectorList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appstream.types.storage_connector.deserialize_cbor(item))
    return out
