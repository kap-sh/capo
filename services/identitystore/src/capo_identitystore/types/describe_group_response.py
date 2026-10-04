"""Generated from Smithy shape ``com.amazonaws.identitystore#DescribeGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_identitystore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_identitystore.types.date_type
    import capo_identitystore.types.external_ids
    import capo_identitystore.types.group_display_name
    import capo_identitystore.types.identity_store_id
    import capo_identitystore.types.resource_arn
    import capo_identitystore.types.resource_id
    import capo_identitystore.types.resource_revision
    import capo_identitystore.types.sensitive_string_type
    import capo_identitystore.types.string_type


class DescribeGroupResponse(TypedDict, closed=True):
    identity_store_id: "capo_identitystore.types.identity_store_id.IdentityStoreId"
    """<p>The globally unique identifier for the identity store.</p>"""
    group_id: "capo_identitystore.types.resource_id.ResourceId"
    """<p>The identifier for a group in the identity store.</p>"""
    group_arn: "capo_identitystore.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the group in the identity store. For example, <code>arn:aws:identitystore:::group/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222</code>.</p>"""
    revision: "capo_identitystore.types.resource_revision.ResourceRevision"
    """<p>The current revision of the group in the identity store. This value changes each time the group is modified.</p>"""
    display_name: NotRequired[
        "capo_identitystore.types.group_display_name.GroupDisplayName"
    ]
    """<p>The group’s display name value. The length limit is 1,024 characters. This value can consist of letters, accented characters, symbols, numbers, punctuation, tab, new line, carriage return, space, and nonbreaking space in this attribute. This value is specified at the time that the group is created and stored as an attribute of the group object in the identity store.</p>"""
    external_ids: NotRequired["capo_identitystore.types.external_ids.ExternalIds"]
    """<p>A list of <code>ExternalId</code> objects that contains the identifiers issued to this resource by an external identity provider.</p>"""
    description: NotRequired[
        "capo_identitystore.types.sensitive_string_type.SensitiveStringType"
    ]
    """<p>A string containing a description of the group.</p>"""
    created_at: NotRequired["capo_identitystore.types.date_type.DateType"]
    """<p>The date and time the group was created.</p>"""
    updated_at: NotRequired["capo_identitystore.types.date_type.DateType"]
    """<p>The date and time the group was last updated.</p>"""
    created_by: NotRequired["capo_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that created the group.</p>"""
    updated_by: NotRequired["capo_identitystore.types.string_type.StringType"]
    """<p>The identifier of the user or system that last updated the group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGroupResponse) -> dict:
    out: dict = {}
    out["IdentityStoreId"] = value["identity_store_id"]
    out["GroupId"] = value["group_id"]
    out["GroupArn"] = value["group_arn"]
    out["Revision"] = value["revision"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "external_ids" in value:
        import capo_identitystore.types.external_ids

        out["ExternalIds"] = (
            capo_identitystore.types.external_ids.serialize_aws_json_1_1(
                value["external_ids"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import capo_identitystore.types.date_type

        out["CreatedAt"] = capo_identitystore.types.date_type.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_identitystore.types.date_type

        out["UpdatedAt"] = capo_identitystore.types.date_type.serialize_aws_json_1_1(
            value["updated_at"]
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "updated_by" in value:
        out["UpdatedBy"] = value["updated_by"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGroupResponse:
    out: DescribeGroupResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    else:
        raise DeserializationError("DescribeGroupResponse.identity_store_id required")
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        raise DeserializationError("DescribeGroupResponse.group_id required")
    if data.get("GroupArn") is not None:
        out["group_arn"] = data["GroupArn"]
    else:
        raise DeserializationError("DescribeGroupResponse.group_arn required")
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    else:
        raise DeserializationError("DescribeGroupResponse.revision required")
    if data.get("DisplayName") is not None:
        out["display_name"] = data["DisplayName"]
    if data.get("ExternalIds") is not None:
        import capo_identitystore.types.external_ids

        out["external_ids"] = (
            capo_identitystore.types.external_ids.deserialize_aws_json_1_1(
                data["ExternalIds"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedAt") is not None:
        import capo_identitystore.types.date_type

        out["created_at"] = capo_identitystore.types.date_type.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_identitystore.types.date_type

        out["updated_at"] = capo_identitystore.types.date_type.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("UpdatedBy") is not None:
        out["updated_by"] = data["UpdatedBy"]
    return out
