"""Generated from Smithy shape ``com.amazonaws.dataexchange#DataSetEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.arn
    import capo_dataexchange.types.asset_type
    import capo_dataexchange.types.description
    import capo_dataexchange.types.id
    import capo_dataexchange.types.name
    import capo_dataexchange.types.origin
    import capo_dataexchange.types.origin_details
    import capo_dataexchange.types.timestamp


class DataSetEntry(TypedDict, closed=True):
    arn: "capo_dataexchange.types.arn.Arn"
    """<p>The ARN for the data set.</p>"""
    asset_type: "capo_dataexchange.types.asset_type.AssetType"
    """<p>The type of asset that is added to a data set.</p>"""
    created_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the data set was created, in ISO 8601 format.</p>"""
    description: "capo_dataexchange.types.description.Description"
    """<p>The description for the data set.</p>"""
    id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set.</p>"""
    name: "capo_dataexchange.types.name.Name"
    """<p>The name of the data set.</p>"""
    origin: "capo_dataexchange.types.origin.Origin"
    """<p>A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).</p>"""
    origin_details: NotRequired["capo_dataexchange.types.origin_details.OriginDetails"]
    """<p>If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.</p>"""
    source_id: NotRequired["capo_dataexchange.types.id.Id"]
    """<p>The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.</p>"""
    updated_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the data set was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetEntry) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["AssetType"] = value["asset_type"]
    import capo_dataexchange.types.timestamp

    out["CreatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    out["Description"] = value["description"]
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    out["Origin"] = value["origin"]
    if "origin_details" in value:
        import capo_dataexchange.types.origin_details

        out["OriginDetails"] = capo_dataexchange.types.origin_details.serialize_json(
            value["origin_details"]
        )
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    import capo_dataexchange.types.timestamp

    out["UpdatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> DataSetEntry:
    out: DataSetEntry = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("AssetType") is not None:
        out["asset_type"] = data["AssetType"]
    else:
        out["asset_type"] = ""
    if data.get("CreatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["created_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Origin") is not None:
        out["origin"] = data["Origin"]
    else:
        out["origin"] = ""
    if data.get("OriginDetails") is not None:
        import capo_dataexchange.types.origin_details

        out["origin_details"] = capo_dataexchange.types.origin_details.deserialize_json(
            data["OriginDetails"]
        )
    if data.get("SourceId") is not None:
        out["source_id"] = data["SourceId"]
    if data.get("UpdatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["updated_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
