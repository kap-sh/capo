"""Generated from Smithy shape ``com.amazonaws.backupgateway#Hypervisors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup_gateway.types.hypervisor

Hypervisors: TypeAlias = list["capo_backup_gateway.types.hypervisor.Hypervisor"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Hypervisors) -> list:
    import capo_backup_gateway.types.hypervisor

    out: list = []
    for item in value:
        out.append(capo_backup_gateway.types.hypervisor.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> Hypervisors:
    import capo_backup_gateway.types.hypervisor

    out: Hypervisors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_backup_gateway.types.hypervisor.deserialize_aws_json_1_0(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Hypervisors) -> list:
    import capo_backup_gateway.types.hypervisor

    out: list = []
    for item in value:
        out.append(capo_backup_gateway.types.hypervisor.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> Hypervisors:
    import capo_backup_gateway.types.hypervisor

    out: Hypervisors = []
    for item in data:
        if item is None:
            continue
        out.append(capo_backup_gateway.types.hypervisor.deserialize_cbor(item))
    return out
