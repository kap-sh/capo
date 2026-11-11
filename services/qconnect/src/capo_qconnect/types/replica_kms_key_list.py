"""Generated from Smithy shape ``com.amazonaws.qconnect#ReplicaKmsKeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qconnect.types.replica_kms_key

ReplicaKmsKeyList: TypeAlias = list["capo_qconnect.types.replica_kms_key.ReplicaKmsKey"]


# --- restJson1 ser/de ---
def serialize_json(value: ReplicaKmsKeyList) -> list:
    import capo_qconnect.types.replica_kms_key

    out: list = []
    for item in value:
        out.append(capo_qconnect.types.replica_kms_key.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReplicaKmsKeyList:
    import capo_qconnect.types.replica_kms_key

    out: ReplicaKmsKeyList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_qconnect.types.replica_kms_key.deserialize_json(item))
    return out
