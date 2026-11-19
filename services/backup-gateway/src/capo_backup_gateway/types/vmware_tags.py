"""Generated from Smithy shape ``com.amazonaws.backupgateway#VmwareTags``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup_gateway.types.vmware_tag

VmwareTags: TypeAlias = list["capo_backup_gateway.types.vmware_tag.VmwareTag"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VmwareTags) -> list:
    import capo_backup_gateway.types.vmware_tag

    out: list = []
    for item in value:
        out.append(capo_backup_gateway.types.vmware_tag.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> VmwareTags:
    import capo_backup_gateway.types.vmware_tag

    out: VmwareTags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_backup_gateway.types.vmware_tag.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: VmwareTags) -> list:
    import capo_backup_gateway.types.vmware_tag

    out: list = []
    for item in value:
        out.append(capo_backup_gateway.types.vmware_tag.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> VmwareTags:
    import capo_backup_gateway.types.vmware_tag

    out: VmwareTags = []
    for item in data:
        if item is None:
            continue
        out.append(capo_backup_gateway.types.vmware_tag.deserialize_cbor(item))
    return out
