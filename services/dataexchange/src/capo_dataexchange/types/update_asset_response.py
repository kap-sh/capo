"""Generated from Smithy shape ``com.amazonaws.dataexchange#UpdateAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.arn
    import capo_dataexchange.types.asset_details
    import capo_dataexchange.types.asset_name
    import capo_dataexchange.types.asset_type
    import capo_dataexchange.types.id
    import capo_dataexchange.types.timestamp


class UpdateAssetResponse(TypedDict, closed=True):
    arn: NotRequired["capo_dataexchange.types.arn.Arn"]
    """<p>The ARN for the asset.</p>"""
    asset_details: NotRequired["capo_dataexchange.types.asset_details.AssetDetails"]
    """<p>Details about the asset.</p>"""
    asset_type: NotRequired["capo_dataexchange.types.asset_type.AssetType"]
    """<p>The type of asset that is added to a data set.</p>"""
    created_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the asset was created, in ISO 8601 format.</p>"""
    data_set_id: NotRequired["capo_dataexchange.types.id.Id"]
    """<p>The unique identifier for the data set associated with this asset.</p>"""
    id: NotRequired["capo_dataexchange.types.id.Id"]
    """<p>The unique identifier for the asset.</p>"""
    name: NotRequired["capo_dataexchange.types.asset_name.AssetName"]
    """<p>The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target Amazon S3 object key. When importing from Amazon API Gateway API, the API name is used as the asset name. When importing from Amazon Redshift, the datashare name is used as the asset name. When importing from AWS Lake Formation, the static values of "Database(s) included in the LF-tag policy"- or "Table(s) included in LF-tag policy" are used as the asset name.</p>"""
    revision_id: NotRequired["capo_dataexchange.types.id.Id"]
    """<p>The unique identifier for the revision associated with this asset.</p>"""
    source_id: NotRequired["capo_dataexchange.types.id.Id"]
    """<p>The asset ID of the owned asset corresponding to the entitled asset being viewed. This parameter is returned when an asset owner is viewing the entitled copy of its owned asset.</p>"""
    updated_at: NotRequired["capo_dataexchange.types.timestamp.Timestamp"]
    """<p>The date and time that the asset was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssetResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "asset_details" in value:
        import capo_dataexchange.types.asset_details

        out["AssetDetails"] = capo_dataexchange.types.asset_details.serialize_json(
            value["asset_details"]
        )
    if "asset_type" in value:
        out["AssetType"] = value["asset_type"]
    if "created_at" in value:
        import capo_dataexchange.types.timestamp

        out["CreatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "revision_id" in value:
        out["RevisionId"] = value["revision_id"]
    if "source_id" in value:
        out["SourceId"] = value["source_id"]
    if "updated_at" in value:
        import capo_dataexchange.types.timestamp

        out["UpdatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAssetResponse:
    out: UpdateAssetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("AssetDetails") is not None:
        import capo_dataexchange.types.asset_details

        out["asset_details"] = capo_dataexchange.types.asset_details.deserialize_json(
            data["AssetDetails"]
        )
    if data.get("AssetType") is not None:
        out["asset_type"] = data["AssetType"]
    if data.get("CreatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["created_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    if data.get("SourceId") is not None:
        out["source_id"] = data["SourceId"]
    if data.get("UpdatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["updated_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    return out
