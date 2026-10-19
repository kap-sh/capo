"""Generated from Smithy shape ``com.amazonaws.workmail#UpdatePrimaryEmailAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.email_address
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.organization_id


class UpdatePrimaryEmailAddressRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The organization that contains the user, group, or resource to update.</p>"""
    entity_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The user, group, or resource to update.</p> <p>The identifier can accept <i>UseriD, ResourceId, or GroupId</i>, <i>Username, Resourcename, or Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012, r-0123456789a0123456789b0123456789, or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>"""
    email: "capo_workmail.types.email_address.EmailAddress"
    """<p>The value of the email to be updated as primary.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePrimaryEmailAddressRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["EntityId"] = value["entity_id"]
    out["Email"] = value["email"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePrimaryEmailAddressRequest:
    out: UpdatePrimaryEmailAddressRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    else:
        out["entity_id"] = ""
    if data.get("Email") is not None:
        out["email"] = data["Email"]
    else:
        out["email"] = ""
    return out
