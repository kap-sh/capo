"""Generated from Smithy shape ``com.amazonaws.identitystore#IdentityStore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_arn
    import capo_identitystore.types.identity_store_id


class IdentityStore(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    identity_store_arn: "capo_identitystore.types.identity_store_arn.IdentityStoreArn"
    """<p>The Amazon Resource Name (ARN) of the identity store. For example, <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityStore) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["IdentityStoreArn"] = value["identity_store_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityStore:
    out: IdentityStore = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("IdentityStore.identity_store_id required")
    if data.get("IdentityStoreArn") is not None:
        out["identity_store_arn"] = data["IdentityStoreArn"]
    else:
        raise DeserializationError("IdentityStore.identity_store_arn required")
    return out
