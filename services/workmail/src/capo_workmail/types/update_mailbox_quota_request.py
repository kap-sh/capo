"""Generated from Smithy shape ``com.amazonaws.workmail#UpdateMailboxQuotaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.mailbox_quota
    import capo_workmail.types.organization_id


class UpdateMailboxQuotaRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization that contains the user for whom to update the mailbox quota.</p>"""
    user_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifer for the user for whom to update the mailbox quota.</p> <p>The identifier can be the <i>UserId</i>, <i>Username</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>User ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: user@domain.tld</p> </li> <li> <p>User name: user</p> </li> </ul>"""
    mailbox_quota: "capo_workmail.types.mailbox_quota.MailboxQuota"
    """<p>The updated mailbox quota, in MB, for the specified user.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMailboxQuotaRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["UserId"] = value["user_id"]
    out["MailboxQuota"] = value["mailbox_quota"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMailboxQuotaRequest:
    out: UpdateMailboxQuotaRequest = {}  # type: ignore[typeddict-item]
    if data.get("OrganizationId") is not None:
        out["organization_id"] = data["OrganizationId"]
    else:
        out["organization_id"] = ""
    if data.get("UserId") is not None:
        out["user_id"] = data["UserId"]
    else:
        out["user_id"] = ""
    if data.get("MailboxQuota") is not None:
        out["mailbox_quota"] = data["MailboxQuota"]
    else:
        out["mailbox_quota"] = 0
    return out
