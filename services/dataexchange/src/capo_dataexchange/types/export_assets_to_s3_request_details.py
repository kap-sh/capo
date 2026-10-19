"""Generated from Smithy shape ``com.amazonaws.dataexchange#ExportAssetsToS3RequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.export_server_side_encryption
    import capo_dataexchange.types.id
    import capo_dataexchange.types.list_of_asset_destination_entry


class ExportAssetsToS3RequestDetails(TypedDict, closed=True):
    asset_destinations: "capo_dataexchange.types.list_of_asset_destination_entry.ListOfAssetDestinationEntry"
    """<p>The destination for the asset.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this export job.</p>"""
    encryption: NotRequired[
        "capo_dataexchange.types.export_server_side_encryption.ExportServerSideEncryption"
    ]
    """<p>Encryption configuration for the export job.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this export request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportAssetsToS3RequestDetails) -> dict:
    out: dict = {}
    import capo_dataexchange.types.list_of_asset_destination_entry

    out["AssetDestinations"] = (
        capo_dataexchange.types.list_of_asset_destination_entry.serialize_json(
            value["asset_destinations"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    if "encryption" in value:
        import capo_dataexchange.types.export_server_side_encryption

        out["Encryption"] = (
            capo_dataexchange.types.export_server_side_encryption.serialize_json(
                value["encryption"]
            )
        )
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ExportAssetsToS3RequestDetails:
    out: ExportAssetsToS3RequestDetails = {}  # type: ignore[typeddict-item]
    if data.get("AssetDestinations") is not None:
        import capo_dataexchange.types.list_of_asset_destination_entry

        out["asset_destinations"] = (
            capo_dataexchange.types.list_of_asset_destination_entry.deserialize_json(
                data["AssetDestinations"]
            )
        )
    else:
        out["asset_destinations"] = []
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("Encryption") is not None:
        import capo_dataexchange.types.export_server_side_encryption

        out["encryption"] = (
            capo_dataexchange.types.export_server_side_encryption.deserialize_json(
                data["Encryption"]
            )
        )
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        out["revision_id"] = ""
    return out
