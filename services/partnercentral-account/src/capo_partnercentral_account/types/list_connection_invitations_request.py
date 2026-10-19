"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ListConnectionInvitationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.connection_type
    import capo_partnercentral_account.types.invitation_status
    import capo_partnercentral_account.types.max_results
    import capo_partnercentral_account.types.next_token
    import capo_partnercentral_account.types.participant_identifier_list
    import capo_partnercentral_account.types.participant_type


class ListConnectionInvitationsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""
    next_token: NotRequired["capo_partnercentral_account.types.next_token.NextToken"]
    """<p>The token for retrieving the next page of results in paginated responses.</p>"""
    connection_type: NotRequired[
        "capo_partnercentral_account.types.connection_type.ConnectionType"
    ]
    """<p>Filter results by connection type (e.g., reseller, distributor, technology partner).</p>"""
    max_results: NotRequired["capo_partnercentral_account.types.max_results.MaxResults"]
    """<p>The maximum number of connection invitations to return in a single response.</p>"""
    other_participant_identifiers: NotRequired[
        "capo_partnercentral_account.types.participant_identifier_list.ParticipantIdentifierList"
    ]
    """<p>Filter results by specific participant identifiers.</p>"""
    participant_type: NotRequired[
        "capo_partnercentral_account.types.participant_type.ParticipantType"
    ]
    """<p>Filter results by participant type (inviter or invitee).</p>"""
    status: NotRequired[
        "capo_partnercentral_account.types.invitation_status.InvitationStatus"
    ]
    """<p>Filter results by invitation status (pending, accepted, rejected, canceled, expired).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListConnectionInvitationsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "connection_type" in value:
        import capo_partnercentral_account.types.connection_type

        out["ConnectionType"] = (
            capo_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
                value["connection_type"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "other_participant_identifiers" in value:
        import capo_partnercentral_account.types.participant_identifier_list

        out["OtherParticipantIdentifiers"] = (
            capo_partnercentral_account.types.participant_identifier_list.serialize_aws_json_1_0(
                value["other_participant_identifiers"]
            )
        )
    if "participant_type" in value:
        import capo_partnercentral_account.types.participant_type

        out["ParticipantType"] = (
            capo_partnercentral_account.types.participant_type.serialize_aws_json_1_0(
                value["participant_type"]
            )
        )
    if "status" in value:
        import capo_partnercentral_account.types.invitation_status

        out["Status"] = (
            capo_partnercentral_account.types.invitation_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListConnectionInvitationsRequest:
    out: ListConnectionInvitationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("ConnectionType") is not None:
        import capo_partnercentral_account.types.connection_type

        out["connection_type"] = (
            capo_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                data["ConnectionType"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("OtherParticipantIdentifiers") is not None:
        import capo_partnercentral_account.types.participant_identifier_list

        out["other_participant_identifiers"] = (
            capo_partnercentral_account.types.participant_identifier_list.deserialize_aws_json_1_0(
                data["OtherParticipantIdentifiers"]
            )
        )
    if data.get("ParticipantType") is not None:
        import capo_partnercentral_account.types.participant_type

        out["participant_type"] = (
            capo_partnercentral_account.types.participant_type.deserialize_aws_json_1_0(
                data["ParticipantType"]
            )
        )
    if data.get("Status") is not None:
        import capo_partnercentral_account.types.invitation_status

        out["status"] = (
            capo_partnercentral_account.types.invitation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    return out
