"""Generated from Smithy shape ``com.amazonaws.identitystore#DescribeGroupMembershipRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_id


class DescribeGroupMembershipRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>"""
    membership_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a <code>GroupMembership</code> in an identity store.</p> <p>You can specify the group membership by ID or by Amazon Resource Name (ARN). For example, membership ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code> or membership ARN <code>arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGroupMembershipRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["MembershipId"] = value["membership_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGroupMembershipRequest:
    out: DescribeGroupMembershipRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "DescribeGroupMembershipRequest.identity_store_id required"
        )
    if data.get("MembershipId") is not None:
        out["membership_id"] = data["MembershipId"]
    else:
        raise DeserializationError(
            "DescribeGroupMembershipRequest.membership_id required"
        )
    return out
