"""Generated from Smithy shape ``com.amazonaws.memorydb#SecurityGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.security_group_membership

SecurityGroupMembershipList: TypeAlias = list[
    "capo_memorydb.types.security_group_membership.SecurityGroupMembership"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupMembershipList) -> list:
    import capo_memorydb.types.security_group_membership

    out: list = []
    for item in value:
        out.append(
            capo_memorydb.types.security_group_membership.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityGroupMembershipList:
    import capo_memorydb.types.security_group_membership

    out: SecurityGroupMembershipList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_memorydb.types.security_group_membership.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SecurityGroupMembershipList) -> list:
    import capo_memorydb.types.security_group_membership

    out: list = []
    for item in value:
        out.append(capo_memorydb.types.security_group_membership.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> SecurityGroupMembershipList:
    import capo_memorydb.types.security_group_membership

    out: SecurityGroupMembershipList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_memorydb.types.security_group_membership.deserialize_cbor(item))
    return out
