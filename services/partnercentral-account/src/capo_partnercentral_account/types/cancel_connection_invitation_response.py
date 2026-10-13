"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#CancelConnectionInvitationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.connection_id
    import capo_partnercentral_account.types.connection_invitation_arn
    import capo_partnercentral_account.types.connection_invitation_id
    import capo_partnercentral_account.types.connection_type
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.email
    import capo_partnercentral_account.types.invitation_status
    import capo_partnercentral_account.types.participant_identifier
    import capo_partnercentral_account.types.participant_type
    import capo_partnercentral_account.types.sensitive_unicode_string
    import capo_partnercentral_account.types.unicode_string_including_new_line


class CancelConnectionInvitationResponse(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection invitation was canceled.</p>"""
    id: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId"
    """<p>The unique identifier of the canceled connection invitation.</p>"""
    arn: "capo_partnercentral_account.types.connection_invitation_arn.ConnectionInvitationArn"
    """<p>The Amazon Resource Name (ARN) of the canceled connection invitation.</p>"""
    connection_id: NotRequired[
        "capo_partnercentral_account.types.connection_id.ConnectionId"
    ]
    """<p>The identifier of the connection associated with the canceled invitation.</p>"""
    connection_type: "capo_partnercentral_account.types.connection_type.ConnectionType"
    """<p>The type of connection that was being invited for.</p>"""
    created_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection invitation was originally created.</p>"""
    updated_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection invitation was last updated (canceled).</p>"""
    expires_at: NotRequired["capo_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when the connection invitation would have expired if not canceled.</p>"""
    other_participant_identifier: (
        "capo_partnercentral_account.types.participant_identifier.ParticipantIdentifier"
    )
    """<p>The identifier of the other participant who was invited to connect.</p>"""
    participant_type: (
        "capo_partnercentral_account.types.participant_type.ParticipantType"
    )
    """<p>The type of participant (inviter or invitee) in the connection invitation.</p>"""
    status: "capo_partnercentral_account.types.invitation_status.InvitationStatus"
    """<p>The current status of the connection invitation (canceled).</p>"""
    invitation_message: "capo_partnercentral_account.types.unicode_string_including_new_line.UnicodeStringIncludingNewLine"
    """<p>The message that was included with the original connection invitation.</p>"""
    inviter_email: "capo_partnercentral_account.types.email.Email"
    """<p>The email address of the person who sent the connection invitation.</p>"""
    inviter_name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The name of the person who sent the connection invitation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelConnectionInvitationResponse) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    if "connection_id" in value:
        out["ConnectionId"] = value["connection_id"]
    import capo_partnercentral_account.types.connection_type

    out["ConnectionType"] = (
        capo_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
            value["connection_type"]
        )
    )
    import capo_partnercentral_account.types.date_time

    out["CreatedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    import capo_partnercentral_account.types.date_time

    out["UpdatedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["updated_at"]
        )
    )
    if "expires_at" in value:
        import capo_partnercentral_account.types.date_time

        out["ExpiresAt"] = (
            capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    out["OtherParticipantIdentifier"] = value["other_participant_identifier"]
    import capo_partnercentral_account.types.participant_type

    out["ParticipantType"] = (
        capo_partnercentral_account.types.participant_type.serialize_aws_json_1_0(
            value["participant_type"]
        )
    )
    import capo_partnercentral_account.types.invitation_status

    out["Status"] = (
        capo_partnercentral_account.types.invitation_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    out["InvitationMessage"] = value["invitation_message"]
    out["InviterEmail"] = value["inviter_email"]
    out["InviterName"] = value["inviter_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelConnectionInvitationResponse:
    out: CancelConnectionInvitationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.catalog required"
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("CancelConnectionInvitationResponse.id required")
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("CancelConnectionInvitationResponse.arn required")
    if data.get("ConnectionId") is not None:
        out["connection_id"] = data["ConnectionId"]
    if data.get("ConnectionType") is not None:
        import capo_partnercentral_account.types.connection_type

        out["connection_type"] = (
            capo_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                data["ConnectionType"]
            )
        )
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.connection_type required"
        )
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["created_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.created_at required"
        )
    if data.get("UpdatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["updated_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.updated_at required"
        )
    if data.get("ExpiresAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["expires_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["ExpiresAt"]
            )
        )
    if data.get("OtherParticipantIdentifier") is not None:
        out["other_participant_identifier"] = data["OtherParticipantIdentifier"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.other_participant_identifier required"
        )
    if data.get("ParticipantType") is not None:
        import capo_partnercentral_account.types.participant_type

        out["participant_type"] = (
            capo_partnercentral_account.types.participant_type.deserialize_aws_json_1_0(
                data["ParticipantType"]
            )
        )
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.participant_type required"
        )
    if data.get("Status") is not None:
        import capo_partnercentral_account.types.invitation_status

        out["status"] = (
            capo_partnercentral_account.types.invitation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("CancelConnectionInvitationResponse.status required")
    if data.get("InvitationMessage") is not None:
        out["invitation_message"] = data["InvitationMessage"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.invitation_message required"
        )
    if data.get("InviterEmail") is not None:
        out["inviter_email"] = data["InviterEmail"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.inviter_email required"
        )
    if data.get("InviterName") is not None:
        out["inviter_name"] = data["InviterName"]
    else:
        raise DeserializationError(
            "CancelConnectionInvitationResponse.inviter_name required"
        )
    return out


def redact_sensitive(value: CancelConnectionInvitationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inviter_name" in value:
        out["inviter_name"] = "*** Sensitive Data Redacted ***"
    return out
