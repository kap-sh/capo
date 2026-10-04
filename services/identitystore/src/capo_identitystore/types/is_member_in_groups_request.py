"""Generated from Smithy shape ``com.amazonaws.identitystore#IsMemberInGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.group_ids
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.member_id


class IsMemberInGroupsRequest(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p> <p>You can specify the identity store by ID or by Amazon Resource Name (ARN). For example, identity store ID <code>d-1234567890</code> or identity store ARN <code>arn:aws:identitystore::111122223333:identitystore/d-1234567890</code>.</p>"""
    member_id: "capo_identitystore.types.member_id.MemberId"
    """<p>An object containing the identifier of a group member.</p>"""
    group_ids: "capo_identitystore.types.group_ids.GroupIds"
    """<p>A list of identifiers for groups in the identity store.</p> <p>You can specify each group by ID or by Amazon Resource Name (ARN). For example, group ID <code>a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code> or group ARN <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsMemberInGroupsRequest) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    import capo_identitystore.types.member_id

    out["MemberId"] = capo_identitystore.types.member_id.serialize_aws_json_1_1(
        value["member_id"]
    )
    import capo_identitystore.types.group_ids

    out["GroupIds"] = capo_identitystore.types.group_ids.serialize_aws_json_1_1(
        value["group_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IsMemberInGroupsRequest:
    out: IsMemberInGroupsRequest = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("IsMemberInGroupsRequest.identity_store_id required")
    if data.get("MemberId") is not None:
        import capo_identitystore.types.member_id

        out["member_id"] = capo_identitystore.types.member_id.deserialize_aws_json_1_1(
            data["MemberId"]
        )
    else:
        raise DeserializationError("IsMemberInGroupsRequest.member_id required")
    if data.get("GroupIds") is not None:
        import capo_identitystore.types.group_ids

        out["group_ids"] = capo_identitystore.types.group_ids.deserialize_aws_json_1_1(
            data["GroupIds"]
        )
    else:
        raise DeserializationError("IsMemberInGroupsRequest.group_ids required")
    return out
