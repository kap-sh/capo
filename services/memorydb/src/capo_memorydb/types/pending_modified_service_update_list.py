"""Generated from Smithy shape ``com.amazonaws.memorydb#PendingModifiedServiceUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.pending_modified_service_update

PendingModifiedServiceUpdateList: TypeAlias = list[
    "capo_memorydb.types.pending_modified_service_update.PendingModifiedServiceUpdate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingModifiedServiceUpdateList) -> list:
    import capo_memorydb.types.pending_modified_service_update

    out: list = []
    for item in value:
        out.append(
            capo_memorydb.types.pending_modified_service_update.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PendingModifiedServiceUpdateList:
    import capo_memorydb.types.pending_modified_service_update

    out: PendingModifiedServiceUpdateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_memorydb.types.pending_modified_service_update.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PendingModifiedServiceUpdateList) -> list:
    import capo_memorydb.types.pending_modified_service_update

    out: list = []
    for item in value:
        out.append(
            capo_memorydb.types.pending_modified_service_update.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> PendingModifiedServiceUpdateList:
    import capo_memorydb.types.pending_modified_service_update

    out: PendingModifiedServiceUpdateList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_memorydb.types.pending_modified_service_update.deserialize_cbor(item)
        )
    return out
