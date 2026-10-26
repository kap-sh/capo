"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionTypeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.connection_type_status
    import capo_partnercentral_account.types.participant


class ConnectionTypeSummary(TypedDict, closed=True):
    status: (
        "capo_partnercentral_account.types.connection_type_status.ConnectionTypeStatus"
    )
    """<p>The current status of this connection type (active, canceled, etc.).</p>"""
    other_participant: "capo_partnercentral_account.types.participant.Participant"
    """<p>Information about the other participant in this connection type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionTypeSummary) -> dict:
    out: dict = {}
    import capo_partnercentral_account.types.connection_type_status

    out["Status"] = (
        capo_partnercentral_account.types.connection_type_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import capo_partnercentral_account.types.participant

    out["OtherParticipant"] = (
        capo_partnercentral_account.types.participant.serialize_aws_json_1_0(
            value["other_participant"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionTypeSummary:
    out: ConnectionTypeSummary = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_partnercentral_account.types.connection_type_status

        out["status"] = (
            capo_partnercentral_account.types.connection_type_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_account.types.connection_type_status.ConnectionTypeStatus",
            "",
        )
    if data.get("OtherParticipant") is not None:
        import capo_partnercentral_account.types.participant

        out["other_participant"] = (
            capo_partnercentral_account.types.participant.deserialize_aws_json_1_0(
                data["OtherParticipant"]
            )
        )
    else:
        out["other_participant"] = {"$unknown": {"name": ""}}
    return out
