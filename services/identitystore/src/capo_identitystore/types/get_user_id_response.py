"""Generated from Smithy shape ``com.amazonaws.identitystore#GetUserIdResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_arn
    import capo_identitystore.types.resource_id


class GetUserIdResponse(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    user_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a user in the identity store.</p>"""
    user_arn: "capo_identitystore.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the user in the identity store. For example, <code>arn:aws:identitystore:::user/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetUserIdResponse) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["UserId"] = value["user_id"]
    out["UserArn"] = value["user_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetUserIdResponse:
    out: GetUserIdResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        out["identity_store_id"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    if data.get("UserArn") is not None:
        out["user_arn"] = data["UserArn"]
    else:
        out["user_arn"] = ""
    return out
