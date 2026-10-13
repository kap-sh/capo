"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#InputConfigOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.earth_observation_job_arn
    import capo_sagemaker_geospatial.types.raster_data_collection_query_output


class InputConfigOutput(TypedDict, closed=True):
    previous_earth_observation_job_arn: NotRequired[
        "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the previous Earth Observation job.</p>"""
    raster_data_collection_query: NotRequired[
        "capo_sagemaker_geospatial.types.raster_data_collection_query_output.RasterDataCollectionQueryOutput"
    ]
    """<p>The structure representing the RasterDataCollection Query consisting of the Area of Interest, RasterDataCollectionArn, RasterDataCollectionName, TimeRange, and Property Filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputConfigOutput) -> dict:
    out: dict = {}
    if "previous_earth_observation_job_arn" in value:
        out["PreviousEarthObservationJobArn"] = value[
            "previous_earth_observation_job_arn"
        ]
    if "raster_data_collection_query" in value:
        import capo_sagemaker_geospatial.types.raster_data_collection_query_output

        out["RasterDataCollectionQuery"] = (
            capo_sagemaker_geospatial.types.raster_data_collection_query_output.serialize_json(
                value["raster_data_collection_query"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputConfigOutput:
    out: InputConfigOutput = {}  # type: ignore[typeddict-item]
    if data.get("PreviousEarthObservationJobArn") is not None:
        out["previous_earth_observation_job_arn"] = data[
            "PreviousEarthObservationJobArn"
        ]
    if data.get("RasterDataCollectionQuery") is not None:
        import capo_sagemaker_geospatial.types.raster_data_collection_query_output

        out["raster_data_collection_query"] = (
            capo_sagemaker_geospatial.types.raster_data_collection_query_output.deserialize_json(
                data["RasterDataCollectionQuery"]
            )
        )
    return out


def redact_sensitive(value: InputConfigOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "raster_data_collection_query" in value:
        import capo_sagemaker_geospatial.types.raster_data_collection_query_output

        out["raster_data_collection_query"] = (
            capo_sagemaker_geospatial.types.raster_data_collection_query_output.redact_sensitive(
                value["raster_data_collection_query"]
            )
        )
    return out
