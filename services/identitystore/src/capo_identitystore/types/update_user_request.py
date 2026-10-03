"""Generated from Smithy shape ``com.amazonaws.identitystore#UpdateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.attribute_operations
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_id


class UpdateUserRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    user_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a user in the identity store.</p>"""
    operations: "capo_identitystore.types.attribute_operations.AttributeOperations"
    """<p>A list of <code>AttributeOperation</code> objects to apply to the requested user. These operations might add, replace, or remove an attribute. For more information on the attributes that can be added, replaced, or removed, see <a href="https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_User.html">User</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateUserRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["UserId"] = value["user_id"]
    import capo_identitystore.types.attribute_operations

    out["Operations"] = (
        capo_identitystore.types.attribute_operations.serialize_aws_json_1_1(
            value["operations"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateUserRequest:
    out: UpdateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("UpdateUserRequest.identity_store_id required")
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        raise DeserializationError("UpdateUserRequest.user_id required")
    if data.get("Operations") is not None:
        import capo_identitystore.types.attribute_operations

        out["operations"] = (
            capo_identitystore.types.attribute_operations.deserialize_aws_json_1_1(
                data["Operations"]
            )
        )
    else:
        raise DeserializationError("UpdateUserRequest.operations required")
    return out
