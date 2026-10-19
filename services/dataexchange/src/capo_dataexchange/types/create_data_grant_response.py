"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateDataGrantResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.arn
    import capo_dataexchange.types.data_grant_acceptance_state
    import capo_dataexchange.types.data_grant_description
    import capo_dataexchange.types.data_grant_name
    import capo_dataexchange.types.grant_distribution_scope
    import capo_dataexchange.types.id
    import capo_dataexchange.types.map_of__string
    import capo_dataexchange.types.receiver_principal
    import capo_dataexchange.types.sender_principal
    import capo_dataexchange.types.timestamp


class CreateDataGrantResponse(TypedDict, closed=True):
    name: "capo_dataexchange.types.data_grant_name.DataGrantName"
    """<p>The name of the data grant.</p>"""
    sender_principal: "capo_dataexchange.types.sender_principal.SenderPrincipal"
    """<p>The Amazon Web Services account ID of the data grant sender.</p>"""
    receiver_principal: "capo_dataexchange.types.receiver_principal.ReceiverPrincipal"
    """<p>The Amazon Web Services account ID of the data grant receiver.</p>"""
    description: NotRequired[
        "capo_dataexchange.types.data_grant_description.DataGrantDescription"
    ]
    """<p>The description of the data grant.</p>"""
    acceptance_state: (
        "capo_dataexchange.types.data_grant_acceptance_state.DataGrantAcceptanceState"
    )
    """<p>The acceptance state of the data grant.</p>"""
    accepted_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when the data grant was accepted.</p>"""
    ends_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when access to the associated data set ends.</p>"""
    grant_distribution_scope: (
        "capo_dataexchange.types.grant_distribution_scope.GrantDistributionScope"
    )
    """<p>The distribution scope for the data grant.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data set associated to the data grant.</p>"""
    source_data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data set used to create the data grant.</p>"""
    id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data grant.</p>"""
    arn: "capo_dataexchange.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the data grant.</p>"""
    created_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was created.</p>"""
    updated_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The timestamp of when the data grant was last updated.</p>"""
    tags: NotRequired["capo_dataexchange.types.map_of__string.MapOf__string"]
    """<p>The tags associated to the data grant. A tag is a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataGrantResponse) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["SenderPrincipal"] = value["sender_principal"]
    out["ReceiverPrincipal"] = value["receiver_principal"]
    if "description" in value:
        out["Description"] = value["description"]
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
    out["GrantDistributionScope"] = value["grant_distribution_scope"]
    out["DataSetId"] = value["data_set_id"]
    out["SourceDataSetId"] = value["source_data_set_id"]
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
    if "tags" in value:
        import capo_dataexchange.types.map_of__string

        out["Tags"] = capo_dataexchange.types.map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataGrantResponse:
    out: CreateDataGrantResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("Description") is not None:
        out["description"] = data["Description"]
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
    if data.get("GrantDistributionScope") is not None:
        out["grant_distribution_scope"] = data["GrantDistributionScope"]
    else:
        out["grant_distribution_scope"] = ""
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("SourceDataSetId") is not None:
        out["source_data_set_id"] = data["SourceDataSetId"]
    else:
        out["source_data_set_id"] = ""
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
    if data.get("Tags") is not None:
        import capo_dataexchange.types.map_of__string

        out["tags"] = capo_dataexchange.types.map_of__string.deserialize_json(
            data["Tags"]
        )
    return out
