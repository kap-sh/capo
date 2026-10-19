"""Generated from Smithy shape ``com.amazonaws.dataexchange#CreateDataGrantRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.data_grant_name
    import capo_dataexchange.types.description
    import capo_dataexchange.types.grant_distribution_scope
    import capo_dataexchange.types.id
    import capo_dataexchange.types.map_of__string
    import capo_dataexchange.types.receiver_principal
    import capo_dataexchange.types.timestamp


class CreateDataGrantRequest(TypedDict, closed=True):
    name: "capo_dataexchange.types.data_grant_name.DataGrantName"
    """<p>The name of the data grant.</p>"""
    grant_distribution_scope: (
        "capo_dataexchange.types.grant_distribution_scope.GrantDistributionScope"
    )
    """<p>The distribution scope of the data grant.</p>"""
    receiver_principal: "capo_dataexchange.types.receiver_principal.ReceiverPrincipal"
    """<p>The Amazon Web Services account ID of the data grant receiver.</p>"""
    source_data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The ID of the data set used to create the data grant.</p>"""
    ends_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The timestamp of when access to the associated data set ends.</p>"""
    description: NotRequired["capo_dataexchange.types.description.Description"]
    """<p>The description of the data grant.</p>"""
    tags: NotRequired["capo_dataexchange.types.map_of__string.MapOf__string"]
    """<p>The tags to add to the data grant. A tag is a key-value pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataGrantRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["GrantDistributionScope"] = value["grant_distribution_scope"]
    out["ReceiverPrincipal"] = value["receiver_principal"]
    out["SourceDataSetId"] = value["source_data_set_id"]
    if "ends_at" in value:
        import capo_dataexchange.types.timestamp

        out["EndsAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["ends_at"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_dataexchange.types.map_of__string

        out["Tags"] = capo_dataexchange.types.map_of__string.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataGrantRequest:
    out: CreateDataGrantRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("GrantDistributionScope") is not None:
        out["grant_distribution_scope"] = data["GrantDistributionScope"]
    else:
        out["grant_distribution_scope"] = ""
    if data.get("ReceiverPrincipal") is not None:
        out["receiver_principal"] = data["ReceiverPrincipal"]
    else:
        out["receiver_principal"] = ""
    if data.get("SourceDataSetId") is not None:
        out["source_data_set_id"] = data["SourceDataSetId"]
    else:
        out["source_data_set_id"] = ""
    if data.get("EndsAt") is not None:
        import capo_dataexchange.types.timestamp

        out["ends_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["EndsAt"]
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_dataexchange.types.map_of__string

        out["tags"] = capo_dataexchange.types.map_of__string.deserialize_json(
            data["Tags"]
        )
    return out
