"""Generated from Smithy shape ``com.amazonaws.codeconnections#RepositorySyncEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.repository_sync_event

RepositorySyncEventList: TypeAlias = list[
    "capo_codeconnections.types.repository_sync_event.RepositorySyncEvent"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncEventList) -> list:
    import capo_codeconnections.types.repository_sync_event

    out: list = []
    for item in value:
        out.append(
            capo_codeconnections.types.repository_sync_event.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RepositorySyncEventList:
    import capo_codeconnections.types.repository_sync_event

    out: RepositorySyncEventList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codeconnections.types.repository_sync_event.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RepositorySyncEventList) -> list:
    import capo_codeconnections.types.repository_sync_event

    out: list = []
    for item in value:
        out.append(
            capo_codeconnections.types.repository_sync_event.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> RepositorySyncEventList:
    import capo_codeconnections.types.repository_sync_event

    out: RepositorySyncEventList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codeconnections.types.repository_sync_event.deserialize_cbor(item)
        )
    return out
