"""Generated from Smithy shape ``com.amazonaws.identitystore#UpdateGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_arn
    import capo_identitystore.types.resource_id
    import capo_identitystore.types.resource_revision


class UpdateGroupResponse(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    group_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a group in the identity store.</p>"""
    group_arn: "capo_identitystore.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the group in the identity store. For example, <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>"""
    revision: "capo_identitystore.types.resource_revision.ResourceRevision"
    """<p>The revision of the group after the requested update is applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGroupResponse) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["GroupId"] = value["group_id"]
    out["GroupArn"] = value["group_arn"]
    out["Revision"] = value["revision"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGroupResponse:
    out: UpdateGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("UpdateGroupResponse.identity_store_id required")
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("UpdateGroupResponse.group_id required")
    if data.get("GroupArn") is not None:
        out["group_arn"] = data["GroupArn"]
    else:
        raise DeserializationError("UpdateGroupResponse.group_arn required")
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    else:
        raise DeserializationError("UpdateGroupResponse.revision required")
    return out
