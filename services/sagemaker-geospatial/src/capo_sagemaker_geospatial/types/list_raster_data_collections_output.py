"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListRasterDataCollectionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.data_collections_list
    import capo_sagemaker_geospatial.types.next_token


class ListRasterDataCollectionsOutput(TypedDict, closed=True):
    raster_data_collection_summaries: (
        "capo_sagemaker_geospatial.types.data_collections_list.DataCollectionsList"
    )
    """<p>Contains summary information about the raster data collection.</p>"""
    next_token: NotRequired["capo_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRasterDataCollectionsOutput) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial.types.data_collections_list

    out["RasterDataCollectionSummaries"] = (
        capo_sagemaker_geospatial.types.data_collections_list.serialize_json(
            value["raster_data_collection_summaries"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRasterDataCollectionsOutput:
    out: ListRasterDataCollectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("RasterDataCollectionSummaries") is not None:
        import capo_sagemaker_geospatial.types.data_collections_list

        out["raster_data_collection_summaries"] = (
            capo_sagemaker_geospatial.types.data_collections_list.deserialize_json(
                data["RasterDataCollectionSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListRasterDataCollectionsOutput.raster_data_collection_summaries required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListRasterDataCollectionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "next_token" in value:
        out["next_token"] = "*** Sensitive Data Redacted ***"
    return out
