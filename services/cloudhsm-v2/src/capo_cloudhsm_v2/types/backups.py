"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Backups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.backup

Backups: TypeAlias = list["capo_cloudhsm_v2.types.backup.Backup"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Backups) -> list:
    import capo_cloudhsm_v2.types.backup

    out: list = []
    for item in value:
        out.append(capo_cloudhsm_v2.types.backup.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Backups:
    import capo_cloudhsm_v2.types.backup

    out: Backups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudhsm_v2.types.backup.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Backups) -> list:
    import capo_cloudhsm_v2.types.backup

    out: list = []
    for item in value:
        out.append(capo_cloudhsm_v2.types.backup.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Backups:
    import capo_cloudhsm_v2.types.backup

    out: Backups = []
    for item in data:
        if item is None:
            continue
        out.append(capo_cloudhsm_v2.types.backup.deserialize_cbor(item))
    return out
