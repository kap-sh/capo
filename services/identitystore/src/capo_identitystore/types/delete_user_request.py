"""Generated from Smithy shape ``com.amazonaws.identitystore#DeleteUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_id
    import capo_identitystore.types.resource_revision


class DeleteUserRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>"""
    user_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a user in the identity store.</p> <p>You can specify the user by ID or by Amazon Resource Name (ARN). For example, user ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code> or user ARN <code>arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p>"""
    revision: NotRequired["capo_identitystore.types.resource_revision.ResourceRevision"]
    """<p>The expected current revision of the user. When you provide this value, the user is deleted only if it matches the current revision of the user in the identity store. If the value doesn't match, the operation fails with a <code>ConflictException</code>. If you don't provide this value, the user is deleted regardless of its current revision.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteUserRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["UserId"] = value["user_id"]
    if "revision" in value:
        out["Revision"] = value["revision"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteUserRequest:
    out: DeleteUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("DeleteUserRequest.identity_store_id required")
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("DeleteUserRequest.user_id required")
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    return out
