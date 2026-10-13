"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#InputConfigInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.earth_observation_job_arn
    import capo_sagemaker_geospatial.types.raster_data_collection_query_input


class InputConfigInput(TypedDict, closed=True):
    previous_earth_observation_job_arn: NotRequired[
        "capo_sagemaker_geospatial.types.earth_observation_job_arn.EarthObservationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the previous Earth Observation job.</p>"""
    raster_data_collection_query: NotRequired[
        "capo_sagemaker_geospatial.types.raster_data_collection_query_input.RasterDataCollectionQueryInput"
    ]
    """<p>The structure representing the RasterDataCollection Query consisting of the Area of Interest, RasterDataCollectionArn,TimeRange and Property Filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputConfigInput) -> dict:
    out: dict = {}
    if "previous_earth_observation_job_arn" in value:
        out["PreviousEarthObservationJobArn"] = value[
            "previous_earth_observation_job_arn"
        ]
    if "raster_data_collection_query" in value:
        import capo_sagemaker_geospatial.types.raster_data_collection_query_input

        out["RasterDataCollectionQuery"] = (
            capo_sagemaker_geospatial.types.raster_data_collection_query_input.serialize_json(
                value["raster_data_collection_query"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputConfigInput:
    out: InputConfigInput = {}  # type: ignore[typeddict-item]
    if data.get("PreviousEarthObservationJobArn") is not None:
        out["previous_earth_observation_job_arn"] = data[
            "PreviousEarthObservationJobArn"
        ]
    if data.get("RasterDataCollectionQuery") is not None:
        import capo_sagemaker_geospatial.types.raster_data_collection_query_input

        out["raster_data_collection_query"] = (
            capo_sagemaker_geospatial.types.raster_data_collection_query_input.deserialize_json(
                data["RasterDataCollectionQuery"]
            )
        )
    return out


def redact_sensitive(value: InputConfigInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "raster_data_collection_query" in value:
        import capo_sagemaker_geospatial.types.raster_data_collection_query_input

        out["raster_data_collection_query"] = (
            capo_sagemaker_geospatial.types.raster_data_collection_query_input.redact_sensitive(
                value["raster_data_collection_query"]
            )
        )
    return out
