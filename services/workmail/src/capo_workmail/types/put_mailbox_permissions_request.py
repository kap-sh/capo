"""Generated from Smithy shape ``com.amazonaws.workmail#PutMailboxPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.organization_id
    import capo_workmail.types.permission_values


class PutMailboxPermissionsRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier of the organization under which the user, group, or resource exists.</p>"""
    entity_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the user or resource for which to update mailbox permissions.</p> <p>The identifier can be <i>UserId, ResourceID, or Group Id</i>, <i>Username, Resourcename, or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>"""
    grantee_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier of the user, group, or resource to which to grant the permissions.</p> <p>The identifier can be <i>UserId, ResourceID, or Group Id</i>, <i>Username, Resourcename, or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Grantee ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: grantee@domain.tld</p> </li> <li> <p>Grantee name: grantee</p> </li> </ul>"""
    permission_values: "capo_workmail.types.permission_values.PermissionValues"
    """<p>The permissions granted to the grantee. SEND_AS allows the grantee to send email as the owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF allows the grantee to send email on behalf of the owner of the mailbox (the grantee is not mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee full access to the mailbox, irrespective of other folder-level permissions set on the mailbox.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutMailboxPermissionsRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["EntityId"] = value["entity_id"]
    out["GranteeId"] = value["grantee_id"]
    import capo_workmail.types.permission_values

    out["PermissionValues"] = (
        capo_workmail.types.permission_values.serialize_aws_json_1_1(
            value["permission_values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutMailboxPermissionsRequest:
    out: PutMailboxPermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    else:
        out["entity_id"] = ""
    if data.get("GranteeId") is not None:
        out["grantee_id"] = data["GranteeId"]
    else:
        out["grantee_id"] = ""
    if data.get("PermissionValues") is not None:
        import capo_workmail.types.permission_values

        out["permission_values"] = (
            capo_workmail.types.permission_values.deserialize_aws_json_1_1(
                data["PermissionValues"]
            )
        )
    else:
        out["permission_values"] = []
    return out
