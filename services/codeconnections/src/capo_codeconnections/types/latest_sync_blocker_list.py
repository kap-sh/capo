"""Generated from Smithy shape ``com.amazonaws.codeconnections#LatestSyncBlockerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codeconnections.types.sync_blocker

LatestSyncBlockerList: TypeAlias = list[
    "capo_codeconnections.types.sync_blocker.SyncBlocker"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LatestSyncBlockerList) -> list:
    import capo_codeconnections.types.sync_blocker

    out: list = []
    for item in value:
        out.append(capo_codeconnections.types.sync_blocker.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> LatestSyncBlockerList:
    import capo_codeconnections.types.sync_blocker

    out: LatestSyncBlockerList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codeconnections.types.sync_blocker.deserialize_aws_json_1_0(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LatestSyncBlockerList) -> list:
    import capo_codeconnections.types.sync_blocker

    out: list = []
    for item in value:
        out.append(capo_codeconnections.types.sync_blocker.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> LatestSyncBlockerList:
    import capo_codeconnections.types.sync_blocker

    out: LatestSyncBlockerList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codeconnections.types.sync_blocker.deserialize_cbor(item))
    return out
