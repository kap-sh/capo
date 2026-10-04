"""Generated from Smithy shape ``com.amazonaws.identitystore#CreateGroupMembershipResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_arn
    import capo_identitystore.types.resource_id


class CreateGroupMembershipResponse(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    membership_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a newly created <code>GroupMembership</code> in an identity store.</p>"""
    membership_arn: "capo_identitystore.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the newly created group membership in the identity store. For example, <code>arn:aws:identitystore:::membership/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateGroupMembershipResponse) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["MembershipId"] = value["membership_id"]
    out["MembershipArn"] = value["membership_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateGroupMembershipResponse:
    out: CreateGroupMembershipResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "CreateGroupMembershipResponse.identity_store_id required"
        )
    if data.get("MembershipId") is not None:
        out["membership_id"] = data["MembershipId"]
    else:
        raise DeserializationError(
            "CreateGroupMembershipResponse.membership_id required"
        )
    if data.get("MembershipArn") is not None:
        out["membership_arn"] = data["MembershipArn"]
    else:
        raise DeserializationError(
            "CreateGroupMembershipResponse.membership_arn required"
        )
    return out
