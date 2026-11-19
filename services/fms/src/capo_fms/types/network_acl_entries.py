"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fms.types.network_acl_entry

NetworkAclEntries: TypeAlias = list["capo_fms.types.network_acl_entry.NetworkAclEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclEntries) -> list:
    import capo_fms.types.network_acl_entry

    out: list = []
    for item in value:
        out.append(capo_fms.types.network_acl_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NetworkAclEntries:
    import capo_fms.types.network_acl_entry

    out: NetworkAclEntries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.network_acl_entry.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkAclEntries) -> list:
    import capo_fms.types.network_acl_entry

    out: list = []
    for item in value:
        out.append(capo_fms.types.network_acl_entry.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> NetworkAclEntries:
    import capo_fms.types.network_acl_entry

    out: NetworkAclEntries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_fms.types.network_acl_entry.deserialize_cbor(item))
    return out
