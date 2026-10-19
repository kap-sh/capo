"""Generated from Smithy shape ``com.amazonaws.dataexchange#ImportAssetsFromRedshiftDataSharesRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.id
    import capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry


class ImportAssetsFromRedshiftDataSharesRequestDetails(TypedDict, closed=True):
    asset_sources: "capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry.ListOfRedshiftDataShareAssetSourceEntry"
    """<p>A list of Amazon Redshift datashare assets.</p>"""
    data_set_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the data set associated with this import job.</p>"""
    revision_id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the revision associated with this import job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportAssetsFromRedshiftDataSharesRequestDetails) -> dict:
    out: dict = {}
    import capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry

    out["AssetSources"] = (
        capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry.serialize_json(
            value["asset_sources"]
        )
    )
    out["DataSetId"] = value["data_set_id"]
    out["RevisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> ImportAssetsFromRedshiftDataSharesRequestDetails:
    out: ImportAssetsFromRedshiftDataSharesRequestDetails = {}  # type: ignore[typeddict-item]
    if data.get("AssetSources") is not None:
        import capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry

        out["asset_sources"] = (
            capo_dataexchange.types.list_of_redshift_data_share_asset_source_entry.deserialize_json(
                data["AssetSources"]
            )
        )
    else:
        out["asset_sources"] = []
    if data.get("DataSetId") is not None:
        out["data_set_id"] = data["DataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("RevisionId") is not None:
        out["revision_id"] = data["RevisionId"]
    else:
        out["revision_id"] = ""
    return out
