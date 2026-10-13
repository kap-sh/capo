"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionTypeDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_account.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_account.types.aws_account_id
    import capo_partnercentral_account.types.connection_type_status
    import capo_partnercentral_account.types.date_time
    import capo_partnercentral_account.types.email
    import capo_partnercentral_account.types.participant
    import capo_partnercentral_account.types.sensitive_unicode_string


class ConnectionTypeDetail(TypedDict, closed=True):
    created_at: "capo_partnercentral_account.types.date_time.DateTime"
    """<p>The timestamp when this connection type was created.</p>"""
    inviter_email: "capo_partnercentral_account.types.email.Email"
    """<p>The email address of the person who initiated this connection type.</p>"""
    inviter_name: "capo_partnercentral_account.types.sensitive_unicode_string.SensitiveUnicodeString"
    """<p>The name of the person who initiated this connection type.</p>"""
    status: (
        "capo_partnercentral_account.types.connection_type_status.ConnectionTypeStatus"
    )
    """<p>The current status of this connection type.</p>"""
    canceled_at: NotRequired["capo_partnercentral_account.types.date_time.DateTime"]
    """<p>The timestamp when this connection type was cancelled, if applicable.</p>"""
    canceled_by: NotRequired[
        "capo_partnercentral_account.types.aws_account_id.AwsAccountId"
    ]
    """<p>The AWS account ID of the participant who cancelled this connection type.</p>"""
    other_participant: "capo_partnercentral_account.types.participant.Participant"
    """<p>Information about the other participant in this connection type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionTypeDetail) -> dict:
    out: dict = {}
    import capo_partnercentral_account.types.date_time

    out["CreatedAt"] = (
        capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
            value["created_at"]
        )
    )
    out["InviterEmail"] = value["inviter_email"]
    out["InviterName"] = value["inviter_name"]
    import capo_partnercentral_account.types.connection_type_status

    out["Status"] = (
        capo_partnercentral_account.types.connection_type_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    if "canceled_at" in value:
        import capo_partnercentral_account.types.date_time

        out["CanceledAt"] = (
            capo_partnercentral_account.types.date_time.serialize_aws_json_1_0(
                value["canceled_at"]
            )
        )
    if "canceled_by" in value:
        out["CanceledBy"] = value["canceled_by"]
    import capo_partnercentral_account.types.participant

    out["OtherParticipant"] = (
        capo_partnercentral_account.types.participant.serialize_aws_json_1_0(
            value["other_participant"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionTypeDetail:
    out: ConnectionTypeDetail = {}  # type: ignore[typeddict-item]
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["created_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("ConnectionTypeDetail.created_at required")
    if data.get("InviterEmail") is not None:
        out["inviter_email"] = data["InviterEmail"]
    else:
        raise DeserializationError("ConnectionTypeDetail.inviter_email required")
    if data.get("InviterName") is not None:
        out["inviter_name"] = data["InviterName"]
    else:
        raise DeserializationError("ConnectionTypeDetail.inviter_name required")
    if data.get("Status") is not None:
        import capo_partnercentral_account.types.connection_type_status

        out["status"] = (
            capo_partnercentral_account.types.connection_type_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ConnectionTypeDetail.status required")
    if data.get("CanceledAt") is not None:
        import capo_partnercentral_account.types.date_time

        out["canceled_at"] = (
            capo_partnercentral_account.types.date_time.deserialize_aws_json_1_0(
                data["CanceledAt"]
            )
        )
    if data.get("CanceledBy") is not None:
        out["canceled_by"] = data["CanceledBy"]
    if data.get("OtherParticipant") is not None:
        import capo_partnercentral_account.types.participant

        out["other_participant"] = (
            capo_partnercentral_account.types.participant.deserialize_aws_json_1_0(
                data["OtherParticipant"]
            )
        )
    else:
        raise DeserializationError("ConnectionTypeDetail.other_participant required")
    return out


def redact_sensitive(value: ConnectionTypeDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inviter_name" in value:
        out["inviter_name"] = "*** Sensitive Data Redacted ***"
    return out
