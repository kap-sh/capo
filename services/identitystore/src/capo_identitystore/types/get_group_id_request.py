"""Generated from Smithy shape ``com.amazonaws.identitystore#GetGroupIdRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.alternate_identifier
    import capo_identitystore.types.identity_store_id


class GetGroupIdRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>"""
    alternate_identifier: (
        "capo_identitystore.types.alternate_identifier.AlternateIdentifier"
    )
    """<p>A unique identifier for a user or group that is not the primary identifier. This value can be an identifier from an external identity provider (IdP) that is associated with the user, the group, or a unique attribute. For the unique attribute, the only valid path is <code> displayName</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetGroupIdRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    import capo_identitystore.types.alternate_identifier

    out["AlternateIdentifier"] = (
        capo_identitystore.types.alternate_identifier.serialize_aws_json_1_1(
            value["alternate_identifier"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetGroupIdRequest:
    out: GetGroupIdRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("GetGroupIdRequest.identity_store_id required")
    if data.get("AlternateIdentifier") is not None:
        import capo_identitystore.types.alternate_identifier

        out["alternate_identifier"] = (
            capo_identitystore.types.alternate_identifier.deserialize_aws_json_1_1(
                data["AlternateIdentifier"]
            )
        )
    else:
        raise DeserializationError("GetGroupIdRequest.alternate_identifier required")
    return out
