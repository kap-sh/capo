"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#SearchRasterDataCollectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.data_collection_arn
    import capo_sagemaker_geospatial.types.next_token
    import capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input


class SearchRasterDataCollectionInput(TypedDict, closed=True):
    arn: "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn"
    """<p>The Amazon Resource Name (ARN) of the raster data collection.</p>"""
    raster_data_collection_query: "capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input.RasterDataCollectionQueryWithBandFilterInput"
    """<p>RasterDataCollectionQuery consisting of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterest.html">AreaOfInterest(AOI)</a>, <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_PropertyFilter.html">PropertyFilters</a> and <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TimeRangeFilterInput.html">TimeRangeFilterInput</a> used in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html">SearchRasterDataCollection</a>.</p>"""
    next_token: NotRequired["capo_sagemaker_geospatial.types.next_token.NextToken"]
    """<p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRasterDataCollectionInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input

    out["RasterDataCollectionQuery"] = (
        capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input.serialize_json(
            value["raster_data_collection_query"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchRasterDataCollectionInput:
    out: SearchRasterDataCollectionInput = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("SearchRasterDataCollectionInput.arn required")
    if data.get("RasterDataCollectionQuery") is not None:
        import capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input

        out["raster_data_collection_query"] = (
            capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input.deserialize_json(
                data["RasterDataCollectionQuery"]
            )
        )
    else:
        raise DeserializationError(
            "SearchRasterDataCollectionInput.raster_data_collection_query required"
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
