"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementInvitationsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account_id_or_alias_list
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.engagement_identifiers
    import capo_partnercentral_selling.types.engagement_invitations_payload_type
    import capo_partnercentral_selling.types.invitation_status_list
    import capo_partnercentral_selling.types.opportunity_engagement_invitation_sort
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.participant_type


class ListEngagementInvitationsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog from which to list the engagement invitations. Use <code>AWS</code> for production invitations or <code>Sandbox</code> for testing environments.</p>"""
    max_results: NotRequired["capo_partnercentral_selling.types.page_size.PageSize"]
    """<p>Specifies the maximum number of engagement invitations to return in the response. If more results are available, a pagination token will be provided.</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used to retrieve additional pages of results when the response to a previous request was truncated. Pass this token to continue listing invitations from where the previous call left off.</p>"""
    sort: NotRequired[
        "capo_partnercentral_selling.types.opportunity_engagement_invitation_sort.OpportunityEngagementInvitationSort"
    ]
    """<p>Specifies the sorting options for listing engagement invitations. Invitations can be sorted by fields such as <code>InvitationDate</code> or <code>Status</code> to help partners view results in their preferred order.</p>"""
    payload_type: NotRequired[
        "capo_partnercentral_selling.types.engagement_invitations_payload_type.EngagementInvitationsPayloadType"
    ]
    """<p>Defines the type of payload associated with the engagement invitations to be listed. The attributes in this payload help decide on acceptance or rejection of the invitation.</p>"""
    participant_type: (
        "capo_partnercentral_selling.types.participant_type.ParticipantType"
    )
    """<p>Specifies the type of participant for which to list engagement invitations. Identifies the role of the participant.</p>"""
    status: NotRequired[
        "capo_partnercentral_selling.types.invitation_status_list.InvitationStatusList"
    ]
    """<p> Status values to filter the invitations. </p>"""
    engagement_identifier: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
    ]
    """<p> Retrieves a list of engagement invitation summaries based on specified filters. The ListEngagementInvitations operation allows you to view all invitations that you have sent or received. You must specify the ParticipantType to filter invitations where you are either the SENDER or the RECEIVER. Invitations will automatically expire if not accepted within 15 days. </p>"""
    sender_aws_account_id: NotRequired[
        "capo_partnercentral_selling.types.aws_account_id_or_alias_list.AwsAccountIdOrAliasList"
    ]
    """<p> List of sender AWS account IDs to filter the invitations. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementInvitationsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort" in value:
        import capo_partnercentral_selling.types.opportunity_engagement_invitation_sort

        out["Sort"] = (
            capo_partnercentral_selling.types.opportunity_engagement_invitation_sort.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    if "payload_type" in value:
        import capo_partnercentral_selling.types.engagement_invitations_payload_type

        out["PayloadType"] = (
            capo_partnercentral_selling.types.engagement_invitations_payload_type.serialize_aws_json_1_0(
                value["payload_type"]
            )
        )
    import capo_partnercentral_selling.types.participant_type

    out["ParticipantType"] = (
        capo_partnercentral_selling.types.participant_type.serialize_aws_json_1_0(
            value["participant_type"]
        )
    )
    if "status" in value:
        import capo_partnercentral_selling.types.invitation_status_list

        out["Status"] = (
            capo_partnercentral_selling.types.invitation_status_list.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "engagement_identifier" in value:
        import capo_partnercentral_selling.types.engagement_identifiers

        out["EngagementIdentifier"] = (
            capo_partnercentral_selling.types.engagement_identifiers.serialize_aws_json_1_0(
                value["engagement_identifier"]
            )
        )
    if "sender_aws_account_id" in value:
        import capo_partnercentral_selling.types.aws_account_id_or_alias_list

        out["SenderAwsAccountId"] = (
            capo_partnercentral_selling.types.aws_account_id_or_alias_list.serialize_aws_json_1_0(
                value["sender_aws_account_id"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementInvitationsRequest:
    out: ListEngagementInvitationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListEngagementInvitationsRequest.catalog required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Sort") is not None:
        import capo_partnercentral_selling.types.opportunity_engagement_invitation_sort

        out["sort"] = (
            capo_partnercentral_selling.types.opportunity_engagement_invitation_sort.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    if data.get("PayloadType") is not None:
        import capo_partnercentral_selling.types.engagement_invitations_payload_type

        out["payload_type"] = (
            capo_partnercentral_selling.types.engagement_invitations_payload_type.deserialize_aws_json_1_0(
                data["PayloadType"]
            )
        )
    if data.get("ParticipantType") is not None:
        import capo_partnercentral_selling.types.participant_type

        out["participant_type"] = (
            capo_partnercentral_selling.types.participant_type.deserialize_aws_json_1_0(
                data["ParticipantType"]
            )
        )
    else:
        raise DeserializationError(
            "ListEngagementInvitationsRequest.participant_type required"
        )
    if data.get("Status") is not None:
        import capo_partnercentral_selling.types.invitation_status_list

        out["status"] = (
            capo_partnercentral_selling.types.invitation_status_list.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("EngagementIdentifier") is not None:
        import capo_partnercentral_selling.types.engagement_identifiers

        out["engagement_identifier"] = (
            capo_partnercentral_selling.types.engagement_identifiers.deserialize_aws_json_1_0(
                data["EngagementIdentifier"]
            )
        )
    if data.get("SenderAwsAccountId") is not None:
        import capo_partnercentral_selling.types.aws_account_id_or_alias_list

        out["sender_aws_account_id"] = (
            capo_partnercentral_selling.types.aws_account_id_or_alias_list.deserialize_aws_json_1_0(
                data["SenderAwsAccountId"]
            )
        )
    return out


def redact_sensitive(value: ListEngagementInvitationsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sender_aws_account_id" in value:
        import capo_partnercentral_selling.types.aws_account_id_or_alias_list

        out["sender_aws_account_id"] = (
            capo_partnercentral_selling.types.aws_account_id_or_alias_list.redact_sensitive(
                value["sender_aws_account_id"]
            )
        )
    return out
