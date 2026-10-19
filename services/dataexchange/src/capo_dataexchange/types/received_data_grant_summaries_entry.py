"""Generated from Smithy shape ``com.amazonaws.dataexchange#ReceivedDataGrantSummariesEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.arn
    import capo_dataexchange.types.data_grant_acceptance_state
    import capo_dataexchange.types.data_grant_name
    import capo_dataexchange.types.id
    import capo_dataexchange.types.receiver_principal
    import capo_dataexchange.types.sender_principal
    import capo_dataexchange.types.timestamp


class ReceivedDataGrantSummariesEntry(TypedDict, closed=True):
    name: "capo_dataexchange.types.data_grant_name.DataGrantName"
    """<p>The name of the data grant.</p>"""
    sender_principal: "capo_dataexchange.types.sender_principal.SenderPrincipal"
    """<p>The Amazon Web Services account ID of the data grant sender.</p>"""
    receiver_principal: "capo_dataexchange.types.receiver_principal.ReceiverPrincipal"
    """<p>The Amazon Web Services account ID of the data grant receiver.</p>"""
    acceptance_state: (
        "capo_dataexchange.types.data_grant_acceptance_state.DataGrantAcceptanceState"
    )
    """<p>The acceptance state of the data grant.</p>"""
    accepted_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when the data grant was accepted.</p>"""
    ends_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when access to the associated data set ends.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data set associated to the data grant.</p>"""
    id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data grant.</p>"""
    arn: "capo_dataexchange.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data grant.</p>"""
    created_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was created.</p>"""
    updated_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReceivedDataGrantSummariesEntry) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["SenderPrincipal"] = value["sender_principal"]
    out["ReceiverPrincipal"] = value["receiver_principal"]
    out["AcceptanceState"] = value["acceptance_state"]
    if "accepted_at" in value:
        import capo_dataexchange.types.timestamp

        out["AcceptedAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["accepted_at"]
        )
    if "ends_at" in value:
        import capo_dataexchange.types.timestamp

        out["EndsAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["ends_at"]
        )
    out["DataSetId"] = value["data_set_id"]
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    import capo_dataexchange.types.timestamp

    out["CreatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_dataexchange.types.timestamp

    out["UpdatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ReceivedDataGrantSummariesEntry:
    out: ReceivedDataGrantSummariesEntry = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("SenderPrincipal") is not None:
        out["sender_principal"] = data["SenderPrincipal"]
    else:
        out["sender_principal"] = ""
    if data.get("ReceiverPrincipal") is not None:
        out["receiver_principal"] = data["ReceiverPrincipal"]
    else:
        out["receiver_principal"] = ""
    if data.get("AcceptanceState") is not None:
        out["acceptance_state"] = data["AcceptanceState"]
    else:
        out["acceptance_state"] = ""
    if data.get("AcceptedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["accepted_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["AcceptedAt"]
        )
    if data.get("EndsAt") is not None:
        import capo_dataexchange.types.timestamp

        out["ends_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["EndsAt"]
        )
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("CreatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["created_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("UpdatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["updated_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
