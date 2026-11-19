"""Generated from Smithy shape ``com.amazonaws.directoryservice#Snapshots``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service.types.snapshot

Snapshots: TypeAlias = list["capo_directory_service.types.snapshot.Snapshot"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshots) -> list:
    import capo_directory_service.types.snapshot

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.snapshot.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Snapshots:
    import capo_directory_service.types.snapshot

    out: Snapshots = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.snapshot.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Snapshots) -> list:
    import capo_directory_service.types.snapshot

    out: list = []
    for item in value:
        out.append(capo_directory_service.types.snapshot.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Snapshots:
    import capo_directory_service.types.snapshot

    out: Snapshots = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service.types.snapshot.deserialize_cbor(item))
    return out
