"""Generated from Smithy shape ``com.amazonaws.organizations#ResponsibilityTransfer``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.handshake_id
    import capo_organizations.types.responsibility_transfer_arn
    import capo_organizations.types.responsibility_transfer_id
    import capo_organizations.types.responsibility_transfer_name
    import capo_organizations.types.responsibility_transfer_status
    import capo_organizations.types.responsibility_transfer_type
    import capo_organizations.types.timestamp
    import capo_organizations.types.transfer_participant


class ResponsibilityTransfer(TypedDict, closed=True):
    arn: NotRequired[
        "capo_organizations.types.responsibility_transfer_arn.ResponsibilityTransferArn"
    ]
    """<p>Amazon Resource Name (ARN) for the transfer.</p>"""
    name: NotRequired[
        "capo_organizations.types.responsibility_transfer_name.ResponsibilityTransferName"
    ]
    """<p>Name assigned to the transfer.</p>"""
    id: NotRequired[
        "capo_organizations.types.responsibility_transfer_id.ResponsibilityTransferId"
    ]
    """<p>ID for the transfer.</p>"""
    type: NotRequired[
        "capo_organizations.types.responsibility_transfer_type.ResponsibilityTransferType"
    ]
    """<p>The type of transfer. Currently, only <code>BILLING</code> is supported.</p>"""
    status: NotRequired[
        "capo_organizations.types.responsibility_transfer_status.ResponsibilityTransferStatus"
    ]
    """<p>Status for the transfer.</p>"""
    source: NotRequired[
        "capo_organizations.types.transfer_participant.TransferParticipant"
    ]
    """<p>Account that allows another account external to its organization to manage the specified responsibilities for the organization.</p>"""
    target: NotRequired[
        "capo_organizations.types.transfer_participant.TransferParticipant"
    ]
    """<p>Account that manages the specified responsibilities for another organization.</p>"""
    start_timestamp: NotRequired["capo_organizations.types.timestamp.Timestamp"]
    """<p>Timestamp when the transfer starts.</p>"""
    end_timestamp: NotRequired["capo_organizations.types.timestamp.Timestamp"]
    """<p>Timestamp when the transfer ends.</p>"""
    active_handshake_id: NotRequired[
        "capo_organizations.types.handshake_id.HandshakeId"
    ]
    """<p>ID for the handshake of the transfer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResponsibilityTransfer) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "type" in value:
        import capo_organizations.types.responsibility_transfer_type

        out["Type"] = (
            capo_organizations.types.responsibility_transfer_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "status" in value:
        import capo_organizations.types.responsibility_transfer_status

        out["Status"] = (
            capo_organizations.types.responsibility_transfer_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "source" in value:
        import capo_organizations.types.transfer_participant

        out["Source"] = (
            capo_organizations.types.transfer_participant.serialize_aws_json_1_1(
                value["source"]
            )
        )
    if "target" in value:
        import capo_organizations.types.transfer_participant

        out["Target"] = (
            capo_organizations.types.transfer_participant.serialize_aws_json_1_1(
                value["target"]
            )
        )
    if "start_timestamp" in value:
        import capo_organizations.types.timestamp

        out["StartTimestamp"] = (
            capo_organizations.types.timestamp.serialize_aws_json_1_1(
                value["start_timestamp"]
            )
        )
    if "end_timestamp" in value:
        import capo_organizations.types.timestamp

        out["EndTimestamp"] = capo_organizations.types.timestamp.serialize_aws_json_1_1(
            value["end_timestamp"]
        )
    if "active_handshake_id" in value:
        out["ActiveHandshakeId"] = value["active_handshake_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResponsibilityTransfer:
    out: ResponsibilityTransfer = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_organizations.types.responsibility_transfer_type

        out["type"] = (
            capo_organizations.types.responsibility_transfer_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("Status") is not None:
        import capo_organizations.types.responsibility_transfer_status

        out["status"] = (
            capo_organizations.types.responsibility_transfer_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Source") is not None:
        import capo_organizations.types.transfer_participant

        out["source"] = (
            capo_organizations.types.transfer_participant.deserialize_aws_json_1_1(
                data["Source"]
            )
        )
    if data.get("Target") is not None:
        import capo_organizations.types.transfer_participant

        out["target"] = (
            capo_organizations.types.transfer_participant.deserialize_aws_json_1_1(
                data["Target"]
            )
        )
    if data.get("StartTimestamp") is not None:
        import capo_organizations.types.timestamp

        out["start_timestamp"] = (
            capo_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["StartTimestamp"]
            )
        )
    if data.get("EndTimestamp") is not None:
        import capo_organizations.types.timestamp

        out["end_timestamp"] = (
            capo_organizations.types.timestamp.deserialize_aws_json_1_1(
                data["EndTimestamp"]
            )
        )
    if data.get("ActiveHandshakeId") is not None:
        out["active_handshake_id"] = data["ActiveHandshakeId"]
    return out


def redact_sensitive(value: ResponsibilityTransfer) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "source" in value:
        import capo_organizations.types.transfer_participant

        out["source"] = capo_organizations.types.transfer_participant.redact_sensitive(
            value["source"]
        )
    if "target" in value:
        import capo_organizations.types.transfer_participant

        out["target"] = capo_organizations.types.transfer_participant.redact_sensitive(
            value["target"]
        )
    return out
