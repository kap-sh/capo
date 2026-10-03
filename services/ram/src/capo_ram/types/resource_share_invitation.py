"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareInvitation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.date_time
    import capo_ram.types.resource_share_association_list
    import capo_ram.types.resource_share_invitation_status
    import capo_ram.types.string


class ResourceShareInvitation(TypedDict, closed=True):
    resource_share_invitation_arn: NotRequired["capo_ram.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the invitation.</p>"""
    resource_share_name: NotRequired["capo_ram.types.string.String"]
    """<p>The name of the resource share.</p>"""
    resource_share_arn: NotRequired["capo_ram.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the resource share</p>"""
    sender_account_id: NotRequired["capo_ram.types.string.String"]
    """<p>The ID of the Amazon Web Services account that sent the invitation.</p>"""
    receiver_account_id: NotRequired["capo_ram.types.string.String"]
    """<p>The ID of the Amazon Web Services account that received the invitation.</p>"""
    invitation_timestamp: NotRequired["capo_ram.types.date_time.DateTime"]
    """<p>The date and time when the invitation was sent.</p>"""
    status: NotRequired[
        "capo_ram.types.resource_share_invitation_status.ResourceShareInvitationStatus"
    ]
    """<p>The current status of the invitation.</p>"""
    resource_share_associations: NotRequired[
        "capo_ram.types.resource_share_association_list.ResourceShareAssociationList"
    ]
    """<p>To view the resources associated with a pending resource share invitation, use <a>ListPendingInvitationResources</a>.</p>"""
    receiver_arn: NotRequired["capo_ram.types.string.String"]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the IAM user or role that received the invitation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareInvitation) -> dict:
    out: dict = {}
    if "resource_share_invitation_arn" in value:
        out["resourceShareInvitationArn"] = value["resource_share_invitation_arn"]
    if "resource_share_name" in value:
        out["resourceShareName"] = value["resource_share_name"]
    if "resource_share_arn" in value:
        out["resourceShareArn"] = value["resource_share_arn"]
    if "sender_account_id" in value:
        out["senderAccountId"] = value["sender_account_id"]
    if "receiver_account_id" in value:
        out["receiverAccountId"] = value["receiver_account_id"]
    if "invitation_timestamp" in value:
        import capo_ram.types.date_time

        out["invitationTimestamp"] = capo_ram.types.date_time.serialize_json(
            value["invitation_timestamp"]
        )
    if "status" in value:
        import capo_ram.types.resource_share_invitation_status

        out["status"] = capo_ram.types.resource_share_invitation_status.serialize_json(
            value["status"]
        )
    if "resource_share_associations" in value:
        import capo_ram.types.resource_share_association_list

        out["resourceShareAssociations"] = (
            capo_ram.types.resource_share_association_list.serialize_json(
                value["resource_share_associations"]
            )
        )
    if "receiver_arn" in value:
        out["receiverArn"] = value["receiver_arn"]
    return out


def deserialize_json(data: dict) -> ResourceShareInvitation:
    out: ResourceShareInvitation = {}  # type: ignore[typeddict-item]
    if data.get("resourceShareInvitationArn") is not None:
        out["resource_share_invitation_arn"] = data["resourceShareInvitationArn"]
    if data.get("resourceShareName") is not None:
        out["resource_share_name"] = data["resourceShareName"]
    if data.get("resourceShareArn") is not None:
        out["resource_share_arn"] = data["resourceShareArn"]
    if data.get("senderAccountId") is not None:
        out["sender_account_id"] = data["senderAccountId"]
    if data.get("receiverAccountId") is not None:
        out["receiver_account_id"] = data["receiverAccountId"]
    if data.get("invitationTimestamp") is not None:
        import capo_ram.types.date_time

        out["invitation_timestamp"] = capo_ram.types.date_time.deserialize_json(
            data["invitationTimestamp"]
        )
    if data.get("status") is not None:
        import capo_ram.types.resource_share_invitation_status

        out["status"] = (
            capo_ram.types.resource_share_invitation_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("resourceShareAssociations") is not None:
        import capo_ram.types.resource_share_association_list

        out["resource_share_associations"] = (
            capo_ram.types.resource_share_association_list.deserialize_json(
                data["resourceShareAssociations"]
            )
        )
    if data.get("receiverArn") is not None:
        out["receiver_arn"] = data["receiverArn"]
    return out
