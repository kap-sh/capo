"""Generated from Smithy shape ``com.amazonaws.identitystore#GetGroupMembershipIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.member_id
    import capo_identitystore.types.resource_id


class GetGroupMembershipIdRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>"""
    group_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>"""
    member_id: "capo_identitystore.types.member_id.MemberId"
    """<p>An object that contains the identifier of a group member. Setting the <code>UserID</code> field to the specific identifier for a user indicates that the user is a member of the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGroupMembershipIdRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["GroupId"] = value["group_id"]
    import capo_identitystore.types.member_id

    out["MemberId"] = capo_identitystore.types.member_id.serialize_aws_json_1_1(
        value["member_id"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGroupMembershipIdRequest:
    out: GetGroupMembershipIdRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError(
            "GetGroupMembershipIdRequest.identity_store_id required"
        )
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("GetGroupMembershipIdRequest.group_id required")
    if data.get("MemberId") is not None:
        import capo_identitystore.types.member_id

        out["member_id"] = capo_identitystore.types.member_id.deserialize_aws_json_1_1(
            data["MemberId"]
        )
    else:
        raise DeserializationError("GetGroupMembershipIdRequest.member_id required")
    return out
