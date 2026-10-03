"""Generated from Smithy shape ``com.amazonaws.rds#EC2SecurityGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class EC2SecurityGroup(TypedDict, closed=True):
    status: NotRequired["capo_rds.types.string.String"]
    """<p>Provides the status of the EC2 security group. Status can be "authorizing", "authorized", "revoking", and "revoked".</p>"""
    ec2_security_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the name of the EC2 security group.</p>"""
    ec2_security_group_id: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the id of the EC2 security group.</p>"""
    ec2_security_group_owner_id: NotRequired["capo_rds.types.string.String"]
    """<p>Specifies the Amazon Web Services ID of the owner of the EC2 security group specified in the <code>EC2SecurityGroupName</code> field.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: EC2SecurityGroup, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))
    if "ec2_security_group_name" in value:
        pairs.append(
            (f"{key_prefix}EC2SecurityGroupName", str(value["ec2_security_group_name"]))
        )
    if "ec2_security_group_id" in value:
        pairs.append(
            (f"{key_prefix}EC2SecurityGroupId", str(value["ec2_security_group_id"]))
        )
    if "ec2_security_group_owner_id" in value:
        pairs.append(
            (
                f"{key_prefix}EC2SecurityGroupOwnerId",
                str(value["ec2_security_group_owner_id"]),
            )
        )


def deserialize_query(el: Element) -> EC2SecurityGroup:
    out: EC2SecurityGroup = {}  # type: ignore[typeddict-item]
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    child_ec2_security_group_name = el.find("EC2SecurityGroupName")
    if child_ec2_security_group_name is not None:
        out["ec2_security_group_name"] = str(child_ec2_security_group_name.text or "")
    child_ec2_security_group_id = el.find("EC2SecurityGroupId")
    if child_ec2_security_group_id is not None:
        out["ec2_security_group_id"] = str(child_ec2_security_group_id.text or "")
    child_ec2_security_group_owner_id = el.find("EC2SecurityGroupOwnerId")
    if child_ec2_security_group_owner_id is not None:
        out["ec2_security_group_owner_id"] = str(
            child_ec2_security_group_owner_id.text or ""
        )
    return out
