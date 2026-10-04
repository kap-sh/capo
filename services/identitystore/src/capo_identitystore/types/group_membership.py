"""Generated from Smithy shape ``com.amazonaws.identitystore#GroupMembership``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.date_type
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.member_id
    import capo_identitystore.types.resource_arn
    import capo_identitystore.types.resource_id
    import capo_identitystore.types.string_type


class GroupMembership(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    membership_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a <code>GroupMembership</code> object in an identity store.</p>"""
    membership_arn: "capo_identitystore.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the group membership in the identity store. For example, <code>arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code>.</p>"""
    group_id: NotRequired["capo_identitystore.types.resource_id.ResourceId"]
    """<p>The identifier for a group in the identity store.</p>"""
    member_id: NotRequired["capo_identitystore.types.member_id.MemberId"]
    """<p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>"""
    created_at: NotRequired["capo_identitystore.types.date_type.DateType"]
    """<p>The date and time the group membership was created.</p>"""
    updated_at: NotRequired["capo_identitystore.types.date_type.DateType"]
    """<p>The date and time the group membership was last updated.</p>"""
    created_by: NotRequired["capo_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that created the group membership.</p>"""
    updated_by: NotRequired["capo_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that last updated the group membership.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroupMembership) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["MembershipId"] = value["membership_id"]
    out["MembershipArn"] = value["membership_arn"]
    if "group_id" in value:
        out["GroupId"] = value["group_id"]
    if "member_id" in value:
        import capo_identitystore.types.member_id

        out["MemberId"] = capo_identitystore.types.member_id.serialize_aws_json_1_1(
            value["member_id"]
        )
    if "created_at" in value:
        import capo_identitystore.types.date_type

        out["CreatedAt"] = capo_identitystore.types.date_type.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_identitystore.types.date_type

        out["UpdatedAt"] = capo_identitystore.types.date_type.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GroupMembership:
    out: GroupMembership = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("GroupMembership.identity_store_id required")
    if data.get("MembershipId") is not None:
        out["membership_id"] = data["MembershipId"]
    else:
        raise DeserializationError("GroupMembership.membership_id required")
    if data.get("MembershipArn") is not None:
        out["membership_arn"] = data["MembershipArn"]
    else:
        raise DeserializationError("GroupMembership.membership_arn required")
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    if data.get("MemberId") is not None:
        import capo_identitystore.types.member_id

        out["member_id"] = capo_identitystore.types.member_id.deserialize_aws_json_1_1(
            data["MemberId"]
        )
    if data.get("CreatedAt") is not None:
        import capo_identitystore.types.date_type

        out["created_at"] = capo_identitystore.types.date_type.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_identitystore.types.date_type

        out["updated_at"] = capo_identitystore.types.date_type.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("UpdatedBy") is not None:
        out["updated_by"] = data["UpdatedBy"]
    return out
