"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionInvitationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog
    import capo_partnercentral_account.types.connection_id
    import capo_partnercentral_account.types.connection_invitation_arn
    import capo_partnercentral_account.types.connection_invitation_id
    import capo_partnercentral_account.types.connection_type
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.invitation_status
    import capo_partnercentral_account.types.participant_identifier
    import capo_partnercentral_account.types.participant_type


class ConnectionInvitationSummary(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier where the connection invitation exists.</p>"""
    id: "capo_partnercentral_account.types.connection_invitation_id.ConnectionInvitationId"
    """<p>The unique identifier of the connection invitation.</p>"""
    arn: "capo_partnercentral_account.types.connection_invitation_arn.ConnectionInvitationArn"
    """<p>The Amazon Resource Name (ARN) of the connection invitation.</p>"""
    connection_id: NotRequired[
        "capo_partnercentral_account.types.connection_id.ConnectionId"
    ]
    """<p>The identifier of the connection associated with this invitation.</p>"""
    connection_type: "capo_partnercentral_account.types.connection_type.ConnectionType"
    """<p>The type of connection being requested in the invitation.</p>"""
    created_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection invitation was created.</p>"""
    updated_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when the connection invitation was last updated.</p>"""
    expires_at: NotRequired["capo_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when the connection invitation will expire.</p>"""
    other_participant_identifier: (
        "capo_partnercentral_account.types.participant_identifier.ParticipantIdentifier"
    )
    """<p>The identifier of the other participant in the connection invitation.</p>"""
    participant_type: (
        "capo_partnercentral_account.types.participant_type.ParticipantType"
    )
    """<p>The type of participant (inviter or invitee) in the connection invitation.</p>"""
    status: "capo_partnercentral_account.types.invitation_status.InvitationStatus"
    """<p>The current status of the connection invitation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionInvitationSummary) -> dict:
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
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionInvitationSummary:
    out: ConnectionInvitationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
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
        import typing

        out["connection_type"] = typing.cast(
            "capo_partnercentral_account.types.connection_type.ConnectionType", ""
        )
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["created_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("UpdatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["updated_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["UpdatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
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
        out["other_participant_identifier"] = ""
    if data.get("ParticipantType") is not None:
        import capo_partnercentral_account.types.participant_type

        out["participant_type"] = (
            capo_partnercentral_account.types.participant_type.deserialize_aws_json_1_0(
                data["ParticipantType"]
            )
        )
    else:
        import typing

        out["participant_type"] = typing.cast(
            "capo_partnercentral_account.types.participant_type.ParticipantType", ""
        )
    if data.get("Status") is not None:
        import capo_partnercentral_account.types.invitation_status

        out["status"] = (
            capo_partnercentral_account.types.invitation_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_account.types.invitation_status.InvitationStatus", ""
        )
    return out
