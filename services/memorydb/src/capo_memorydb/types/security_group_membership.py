"""Generated from Smithy shape ``com.amazonaws.memorydb#SecurityGroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.string


class SecurityGroupMembership(TypedDict, closed=True):
    security_group_id: NotRequired["capo_memorydb.types.string.String"]
    """<p>The identifier of the security group.</p>"""
    status: NotRequired["capo_memorydb.types.string.String"]
    """<p>The status of the security group membership. The status changes whenever a security group is modified, or when the security groups assigned to a cluster are modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityGroupMembership) -> dict:
    out: dict = {}
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SecurityGroupMembership:
    out: SecurityGroupMembership = {}  # type: ignore[typeddict-item]
    if data.get("SecurityGroupId") is not None:
        out["security_group_id"] = data["SecurityGroupId"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SecurityGroupMembership) -> dict:
    out: dict = {}
    if "security_group_id" in value:
        out["SecurityGroupId"] = value["security_group_id"]
    if "status" in value:
        out["Status"] = value["status"]
    return out


def deserialize_cbor(data: dict) -> SecurityGroupMembership:
    out: SecurityGroupMembership = {}  # type: ignore[typeddict-item]
    if data.get("SecurityGroupId") is not None:
        out["security_group_id"] = data["SecurityGroupId"]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    return out
