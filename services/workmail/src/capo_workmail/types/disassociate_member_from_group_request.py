"""Generated from Smithy shape ``com.amazonaws.workmail#DisassociateMemberFromGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.organization_id


class DisassociateMemberFromGroupRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the group exists.</p>"""
    group_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier for the group from which members are removed.</p> <p>The identifier can accept <i>GroupId</i>, <i>Groupname</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Group ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: group@domain.tld</p> </li> <li> <p>Group name: group</p> </li> </ul>"""
    member_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier for the member to be removed from the group.</p> <p>The member ID can accept <i>UserID or GroupId</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Member ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: member@domain.tld</p> </li> <li> <p>Member name: member</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateMemberFromGroupRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["GroupId"] = value["group_id"]
    out["MemberId"] = value["member_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateMemberFromGroupRequest:
    out: DisassociateMemberFromGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("GroupId") is not None:
        out["group_id"] = data["GroupId"]
    else:
        out["group_id"] = ""
    if data.get("MemberId") is not None:
        out["member_id"] = data["MemberId"]
    else:
        out["member_id"] = ""
    return out
