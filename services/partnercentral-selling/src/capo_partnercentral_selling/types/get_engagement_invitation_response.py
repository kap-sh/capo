"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetEngagementInvitationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.date_time
    import capo_partnercentral_selling.types.engagement_description
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier
    import capo_partnercentral_selling.types.engagement_invitation_payload_type
    import capo_partnercentral_selling.types.engagement_member_summaries
    import capo_partnercentral_selling.types.engagement_title
    import capo_partnercentral_selling.types.enrichment_context
    import capo_partnercentral_selling.types.invitation_message
    import capo_partnercentral_selling.types.invitation_status
    import capo_partnercentral_selling.types.payload
    import capo_partnercentral_selling.types.receiver
    import capo_partnercentral_selling.types.rejection_reason_string


class GetEngagementInvitationResponse(TypedDict, closed=True):
    arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) that identifies the engagement invitation.</p>"""
    payload_type: NotRequired[
        "capo_partnercentral_selling.types.engagement_invitation_payload_type.EngagementInvitationPayloadType"
    ]
    """<p>The type of payload contained in the engagement invitation, indicating what data or context the payload covers.</p>"""
    id: "capo_partnercentral_selling.types.engagement_invitation_arn_or_identifier.EngagementInvitationArnOrIdentifier"
    """<p>Unique identifier assigned to the engagement invitation being retrieved.</p>"""
    engagement_id: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The identifier of the engagement associated with this invitation.This ID links the invitation to its corresponding engagement.</p>"""
    engagement_title: NotRequired[
        "capo_partnercentral_selling.types.engagement_title.EngagementTitle"
    ]
    """<p>The title of the engagement invitation, summarizing the purpose or objectives of the opportunity shared by AWS.</p>"""
    status: NotRequired[
        "capo_partnercentral_selling.types.invitation_status.InvitationStatus"
    ]
    """<p>The current status of the engagement invitation.</p>"""
    invitation_date: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>The date when the engagement invitation was sent to the partner.</p>"""
    expiration_date: NotRequired["capo_partnercentral_selling.types.date_time.DateTime"]
    """<p>Indicates the date on which the engagement invitation will expire if not accepted by the partner.</p>"""
    sender_aws_account_id: NotRequired[
        "capo_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>Specifies the AWS Account ID of the sender, which identifies the AWS team responsible for sharing the engagement invitation.</p>"""
    sender_company_name: NotRequired["str"]
    """<p>The name of the AWS organization or team that sent the engagement invitation.</p>"""
    receiver: NotRequired["capo_partnercentral_selling.types.receiver.Receiver"]
    """<p>Information about the partner organization or team that received the engagement invitation, including contact details and identifiers.</p>"""
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Indicates the catalog from which the engagement invitation details are retrieved. This field helps in identifying the appropriate catalog (e.g., <code>AWS</code> or <code>Sandbox</code>) used in the request.</p>"""
    rejection_reason: NotRequired[
        "capo_partnercentral_selling.types.rejection_reason_string.RejectionReasonString"
    ]
    """<p>If the engagement invitation was rejected, this field specifies the reason provided by the partner for the rejection.</p>"""
    payload: NotRequired["capo_partnercentral_selling.types.payload.Payload"]
    """<p>Details of the engagement invitation payload, including specific data relevant to the invitation's contents, such as customer information and opportunity insights.</p>"""
    invitation_message: NotRequired[
        "capo_partnercentral_selling.types.invitation_message.InvitationMessage"
    ]
    """<p>The message sent to the invited partner when the invitation was created.</p>"""
    engagement_description: NotRequired[
        "capo_partnercentral_selling.types.engagement_description.EngagementDescription"
    ]
    """<p>The description of the engagement associated with this invitation.</p>"""
    existing_members: NotRequired[
        "capo_partnercentral_selling.types.engagement_member_summaries.EngagementMemberSummaries"
    ]
    """<p>A list of active members currently part of the Engagement. This array contains a maximum of 10 members, each represented by an object with the following properties.</p> <ul> <li> <p>CompanyName: The name of the member's company.</p> </li> <li> <p>WebsiteUrl: The website URL of the member's company.</p> </li> </ul>"""
    enrichment_context: NotRequired[
        "capo_partnercentral_selling.types.enrichment_context.EnrichmentContext"
    ]
    """<p>The enrichment data for the engagement associated with this invitation. You can view propensity scores, program eligibility, and lead readiness assessments before taking action on the invitation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEngagementInvitationResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "payload_type" in value:
        import capo_partnercentral_selling.types.engagement_invitation_payload_type

        out["PayloadType"] = (
            capo_partnercentral_selling.types.engagement_invitation_payload_type.serialize_aws_json_1_0(
                value["payload_type"]
            )
        )
    out["Id"] = value["id"]
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "engagement_title" in value:
        out["EngagementTitle"] = value["engagement_title"]
    if "status" in value:
        import capo_partnercentral_selling.types.invitation_status

        out["Status"] = (
            capo_partnercentral_selling.types.invitation_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "invitation_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["InvitationDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["invitation_date"]
            )
        )
    if "expiration_date" in value:
        import capo_partnercentral_selling.types.date_time

        out["ExpirationDate"] = (
            capo_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["expiration_date"]
            )
        )
    if "sender_aws_account_id" in value:
        out["SenderAwsAccountId"] = value["sender_aws_account_id"]
    if "sender_company_name" in value:
        out["SenderCompanyName"] = value["sender_company_name"]
    if "receiver" in value:
        import capo_partnercentral_selling.types.receiver

        out["Receiver"] = (
            capo_partnercentral_selling.types.receiver.serialize_aws_json_1_0(
                value["receiver"]
            )
        )
    out["Catalog"] = value["catalog"]
    if "rejection_reason" in value:
        out["RejectionReason"] = value["rejection_reason"]
    if "payload" in value:
        import capo_partnercentral_selling.types.payload

        out["Payload"] = (
            capo_partnercentral_selling.types.payload.serialize_aws_json_1_0(
                value["payload"]
            )
        )
    if "invitation_message" in value:
        out["InvitationMessage"] = value["invitation_message"]
    if "engagement_description" in value:
        out["EngagementDescription"] = value["engagement_description"]
    if "existing_members" in value:
        import capo_partnercentral_selling.types.engagement_member_summaries

        out["ExistingMembers"] = (
            capo_partnercentral_selling.types.engagement_member_summaries.serialize_aws_json_1_0(
                value["existing_members"]
            )
        )
    if "enrichment_context" in value:
        import capo_partnercentral_selling.types.enrichment_context

        out["EnrichmentContext"] = (
            capo_partnercentral_selling.types.enrichment_context.serialize_aws_json_1_0(
                value["enrichment_context"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEngagementInvitationResponse:
    out: GetEngagementInvitationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("PayloadType") is not None:
        import capo_partnercentral_selling.types.engagement_invitation_payload_type

        out["payload_type"] = (
            capo_partnercentral_selling.types.engagement_invitation_payload_type.deserialize_aws_json_1_0(
                data["PayloadType"]
            )
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("EngagementId") is not None:
        out["engagement_id"] = data["EngagementId"]
    if data.get("EngagementTitle") is not None:
        out["engagement_title"] = data["EngagementTitle"]
    if data.get("Status") is not None:
        import capo_partnercentral_selling.types.invitation_status

        out["status"] = (
            capo_partnercentral_selling.types.invitation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("InvitationDate") is not None:
        import capo_partnercentral_selling.types.date_time

        out["invitation_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["InvitationDate"]
            )
        )
    if data.get("ExpirationDate") is not None:
        import capo_partnercentral_selling.types.date_time

        out["expiration_date"] = (
            capo_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["ExpirationDate"]
            )
        )
    if data.get("SenderAwsAccountId") is not None:
        out["sender_aws_account_id"] = data["SenderAwsAccountId"]
    if data.get("SenderCompanyName") is not None:
        out["sender_company_name"] = data["SenderCompanyName"]
    if data.get("Receiver") is not None:
        import capo_partnercentral_selling.types.receiver

        out["receiver"] = (
            capo_partnercentral_selling.types.receiver.deserialize_aws_json_1_0(
                data["Receiver"]
            )
        )
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("RejectionReason") is not None:
        out["rejection_reason"] = data["RejectionReason"]
    if data.get("Payload") is not None:
        import capo_partnercentral_selling.types.payload

        out["payload"] = (
            capo_partnercentral_selling.types.payload.deserialize_aws_json_1_0(
                data["Payload"]
            )
        )
    if data.get("InvitationMessage") is not None:
        out["invitation_message"] = data["InvitationMessage"]
    if data.get("EngagementDescription") is not None:
        out["engagement_description"] = data["EngagementDescription"]
    if data.get("ExistingMembers") is not None:
        import capo_partnercentral_selling.types.engagement_member_summaries

        out["existing_members"] = (
            capo_partnercentral_selling.types.engagement_member_summaries.deserialize_aws_json_1_0(
                data["ExistingMembers"]
            )
        )
    if data.get("EnrichmentContext") is not None:
        import capo_partnercentral_selling.types.enrichment_context

        out["enrichment_context"] = (
            capo_partnercentral_selling.types.enrichment_context.deserialize_aws_json_1_0(
                data["EnrichmentContext"]
            )
        )
    return out


def redact_sensitive(value: GetEngagementInvitationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sender_aws_account_id" in value:
        out["sender_aws_account_id"] = "*** Sensitive Data Redacted ***"
    if "receiver" in value:
        import capo_partnercentral_selling.types.receiver

        out["receiver"] = capo_partnercentral_selling.types.receiver.redact_sensitive(
            value["receiver"]
        )
    if "payload" in value:
        import capo_partnercentral_selling.types.payload

        out["payload"] = capo_partnercentral_selling.types.payload.redact_sensitive(
            value["payload"]
        )
    if "invitation_message" in value:
        out["invitation_message"] = "*** Sensitive Data Redacted ***"
    if "existing_members" in value:
        import capo_partnercentral_selling.types.engagement_member_summaries

        out["existing_members"] = (
            capo_partnercentral_selling.types.engagement_member_summaries.redact_sensitive(
                value["existing_members"]
            )
        )
    if "enrichment_context" in value:
        import capo_partnercentral_selling.types.enrichment_context

        out["enrichment_context"] = (
            capo_partnercentral_selling.types.enrichment_context.redact_sensitive(
                value["enrichment_context"]
            )
        )
    return out
