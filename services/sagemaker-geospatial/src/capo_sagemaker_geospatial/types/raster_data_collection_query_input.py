"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#RasterDataCollectionQueryInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.area_of_interest
    import capo_sagemaker_geospatial.types.data_collection_arn
    import capo_sagemaker_geospatial.types.property_filters
    import capo_sagemaker_geospatial.types.time_range_filter_input


class RasterDataCollectionQueryInput(TypedDict, closed=True):
    raster_data_collection_arn: (
        "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn"
    )
    """<p>The Amazon Resource Name (ARN) of the raster data collection.</p>"""
    time_range_filter: (
        "capo_sagemaker_geospatial.types.time_range_filter_input.TimeRangeFilterInput"
    )
    """<p>The TimeRange Filter used in the RasterDataCollection Query.</p>"""
    area_of_interest: NotRequired[
        "capo_sagemaker_geospatial.types.area_of_interest.AreaOfInterest"
    ]
    """<p>The area of interest being queried for the raster data collection.</p>"""
    property_filters: NotRequired[
        "capo_sagemaker_geospatial.types.property_filters.PropertyFilters"
    ]
    """<p>The list of Property filters used in the Raster Data Collection Query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RasterDataCollectionQueryInput) -> dict:
    out: dict = {}
    out["RasterDataCollectionArn"] = value["raster_data_collection_arn"]
    import capo_sagemaker_geospatial.types.time_range_filter_input

    out["TimeRangeFilter"] = (
        capo_sagemaker_geospatial.types.time_range_filter_input.serialize_json(
            value["time_range_filter"]
        )
    )
    if "area_of_interest" in value:
        import capo_sagemaker_geospatial.types.area_of_interest

        out["AreaOfInterest"] = (
            capo_sagemaker_geospatial.types.area_of_interest.serialize_json(
                value["area_of_interest"]
            )
        )
    if "property_filters" in value:
        import capo_sagemaker_geospatial.types.property_filters

        out["PropertyFilters"] = (
            capo_sagemaker_geospatial.types.property_filters.serialize_json(
                value["property_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> RasterDataCollectionQueryInput:
    out: RasterDataCollectionQueryInput = {}  # type: ignore[typeddict-item]
    if data.get("RasterDataCollectionArn") is not None:
        out["raster_data_collection_arn"] = data["RasterDataCollectionArn"]
    else:
        out["raster_data_collection_arn"] = ""
    if data.get("TimeRangeFilter") is not None:
        import capo_sagemaker_geospatial.types.time_range_filter_input

        out["time_range_filter"] = (
            capo_sagemaker_geospatial.types.time_range_filter_input.deserialize_json(
                data["TimeRangeFilter"]
            )
        )
    else:
        raise DeserializationError(
            "RasterDataCollectionQueryInput.time_range_filter required"
        )
    if data.get("AreaOfInterest") is not None:
        import capo_sagemaker_geospatial.types.area_of_interest

        out["area_of_interest"] = (
            capo_sagemaker_geospatial.types.area_of_interest.deserialize_json(
                data["AreaOfInterest"]
            )
        )
    if data.get("PropertyFilters") is not None:
        import capo_sagemaker_geospatial.types.property_filters

        out["property_filters"] = (
            capo_sagemaker_geospatial.types.property_filters.deserialize_json(
                data["PropertyFilters"]
            )
        )
    return out


def redact_sensitive(value: RasterDataCollectionQueryInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "time_range_filter" in value:
        out["time_range_filter"] = "*** Sensitive Data Redacted ***"
    if "area_of_interest" in value:
        import capo_sagemaker_geospatial.types.area_of_interest

        out["area_of_interest"] = (
            capo_sagemaker_geospatial.types.area_of_interest.redact_sensitive(
                value["area_of_interest"]
            )
        )
    return out
