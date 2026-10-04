"""Generated from Smithy shape ``com.amazonaws.identitystore#UpdateGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.attribute_operations
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_id
    import capo_identitystore.types.resource_revision


class UpdateGroupRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>"""
    group_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a group in the identity store.</p> <p>You can specify the group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>"""
    operations: "capo_identitystore.types.attribute_operations.AttributeOperations"
    """<p>A list of <code>AttributeOperation</code> objects to apply to the requested group. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_Group.html">Group</a>.</p>"""
    revision: NotRequired["capo_identitystore.types.resource_revision.ResourceRevision"]
    """<p>The expected current revision of the group. When you provide this value, the update is applied only if it matches the current revision of the group in the identity store, which prevents you from overwriting concurrent changes. If the value doesn't match, the operation fails with a <code>ConflictException</code>. If you don't provide this value, the update is applied unconditionally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGroupRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["GroupId"] = value["group_id"]
    import capo_identitystore.types.attribute_operations

    out["Operations"] = (
        capo_identitystore.types.attribute_operations.serialize_aws_json_1_1(
            value["operations"]
        )
    )
    if "revision" in value:
        out["Revision"] = value["revision"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGroupRequest:
    out: UpdateGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("UpdateGroupRequest.identity_store_id required")
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("UpdateGroupRequest.group_id required")
    if data.get("Operations") is not None:
        import capo_identitystore.types.attribute_operations

        out["operations"] = (
            capo_identitystore.types.attribute_operations.deserialize_aws_json_1_1(
                data["Operations"]
            )
        )
    else:
        raise DeserializationError("UpdateGroupRequest.operations required")
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    return out
