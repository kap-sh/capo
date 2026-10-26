"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#JobConfigInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError, SerializationError
from capo_sagemaker_geospatial.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.band_math_config_input
    import capo_sagemaker_geospatial.types.cloud_masking_config_input
    import capo_sagemaker_geospatial.types.cloud_removal_config_input
    import capo_sagemaker_geospatial.types.geo_mosaic_config_input
    import capo_sagemaker_geospatial.types.land_cover_segmentation_config_input
    import capo_sagemaker_geospatial.types.resampling_config_input
    import capo_sagemaker_geospatial.types.stack_config_input
    import capo_sagemaker_geospatial.types.temporal_statistics_config_input
    import capo_sagemaker_geospatial.types.zonal_statistics_config_input


class _JobConfigInput_BandMathConfig(TypedDict, closed=True):
    BandMathConfig: (
        "capo_sagemaker_geospatial.types.band_math_config_input.BandMathConfigInput"
    )


class _JobConfigInput_ResamplingConfig(TypedDict, closed=True):
    ResamplingConfig: (
        "capo_sagemaker_geospatial.types.resampling_config_input.ResamplingConfigInput"
    )


class _JobConfigInput_TemporalStatisticsConfig(TypedDict, closed=True):
    TemporalStatisticsConfig: "capo_sagemaker_geospatial.types.temporal_statistics_config_input.TemporalStatisticsConfigInput"


class _JobConfigInput_CloudRemovalConfig(TypedDict, closed=True):
    CloudRemovalConfig: "capo_sagemaker_geospatial.types.cloud_removal_config_input.CloudRemovalConfigInput"


class _JobConfigInput_ZonalStatisticsConfig(TypedDict, closed=True):
    ZonalStatisticsConfig: "capo_sagemaker_geospatial.types.zonal_statistics_config_input.ZonalStatisticsConfigInput"


class _JobConfigInput_GeoMosaicConfig(TypedDict, closed=True):
    GeoMosaicConfig: (
        "capo_sagemaker_geospatial.types.geo_mosaic_config_input.GeoMosaicConfigInput"
    )


class _JobConfigInput_StackConfig(TypedDict, closed=True):
    StackConfig: "capo_sagemaker_geospatial.types.stack_config_input.StackConfigInput"


class _JobConfigInput_CloudMaskingConfig(TypedDict, closed=True):
    CloudMaskingConfig: "capo_sagemaker_geospatial.types.cloud_masking_config_input.CloudMaskingConfigInput"


class _JobConfigInput_LandCoverSegmentationConfig(TypedDict, closed=True):
    LandCoverSegmentationConfig: "capo_sagemaker_geospatial.types.land_cover_segmentation_config_input.LandCoverSegmentationConfigInput"


JobConfigInput: TypeAlias = (
    _JobConfigInput_BandMathConfig
    | _JobConfigInput_ResamplingConfig
    | _JobConfigInput_TemporalStatisticsConfig
    | _JobConfigInput_CloudRemovalConfig
    | _JobConfigInput_ZonalStatisticsConfig
    | _JobConfigInput_GeoMosaicConfig
    | _JobConfigInput_StackConfig
    | _JobConfigInput_CloudMaskingConfig
    | _JobConfigInput_LandCoverSegmentationConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: JobConfigInput) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"JobConfigInput: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "BandMathConfig" in value:
        import capo_sagemaker_geospatial.types.band_math_config_input

        return {
            "BandMathConfig": capo_sagemaker_geospatial.types.band_math_config_input.serialize_json(
                value["BandMathConfig"]
            )
        }
    elif "ResamplingConfig" in value:
        import capo_sagemaker_geospatial.types.resampling_config_input

        return {
            "ResamplingConfig": capo_sagemaker_geospatial.types.resampling_config_input.serialize_json(
                value["ResamplingConfig"]
            )
        }
    elif "TemporalStatisticsConfig" in value:
        import capo_sagemaker_geospatial.types.temporal_statistics_config_input

        return {
            "TemporalStatisticsConfig": capo_sagemaker_geospatial.types.temporal_statistics_config_input.serialize_json(
                value["TemporalStatisticsConfig"]
            )
        }
    elif "CloudRemovalConfig" in value:
        import capo_sagemaker_geospatial.types.cloud_removal_config_input

        return {
            "CloudRemovalConfig": capo_sagemaker_geospatial.types.cloud_removal_config_input.serialize_json(
                value["CloudRemovalConfig"]
            )
        }
    elif "ZonalStatisticsConfig" in value:
        import capo_sagemaker_geospatial.types.zonal_statistics_config_input

        return {
            "ZonalStatisticsConfig": capo_sagemaker_geospatial.types.zonal_statistics_config_input.serialize_json(
                value["ZonalStatisticsConfig"]
            )
        }
    elif "GeoMosaicConfig" in value:
        import capo_sagemaker_geospatial.types.geo_mosaic_config_input

        return {
            "GeoMosaicConfig": capo_sagemaker_geospatial.types.geo_mosaic_config_input.serialize_json(
                value["GeoMosaicConfig"]
            )
        }
    elif "StackConfig" in value:
        import capo_sagemaker_geospatial.types.stack_config_input

        return {
            "StackConfig": capo_sagemaker_geospatial.types.stack_config_input.serialize_json(
                value["StackConfig"]
            )
        }
    elif "CloudMaskingConfig" in value:
        import capo_sagemaker_geospatial.types.cloud_masking_config_input

        return {
            "CloudMaskingConfig": capo_sagemaker_geospatial.types.cloud_masking_config_input.serialize_json(
                value["CloudMaskingConfig"]
            )
        }
    elif "LandCoverSegmentationConfig" in value:
        import capo_sagemaker_geospatial.types.land_cover_segmentation_config_input

        return {
            "LandCoverSegmentationConfig": capo_sagemaker_geospatial.types.land_cover_segmentation_config_input.serialize_json(
                value["LandCoverSegmentationConfig"]
            )
        }
    else:
        raise SerializationError("JobConfigInput: no variant present")


def deserialize_json(data: dict) -> JobConfigInput:
    if data.get("BandMathConfig") is not None:
        import capo_sagemaker_geospatial.types.band_math_config_input

        return {
            "BandMathConfig": capo_sagemaker_geospatial.types.band_math_config_input.deserialize_json(
                data["BandMathConfig"]
            )
        }
    elif data.get("ResamplingConfig") is not None:
        import capo_sagemaker_geospatial.types.resampling_config_input

        return {
            "ResamplingConfig": capo_sagemaker_geospatial.types.resampling_config_input.deserialize_json(
                data["ResamplingConfig"]
            )
        }
    elif data.get("TemporalStatisticsConfig") is not None:
        import capo_sagemaker_geospatial.types.temporal_statistics_config_input

        return {
            "TemporalStatisticsConfig": capo_sagemaker_geospatial.types.temporal_statistics_config_input.deserialize_json(
                data["TemporalStatisticsConfig"]
            )
        }
    elif data.get("CloudRemovalConfig") is not None:
        import capo_sagemaker_geospatial.types.cloud_removal_config_input

        return {
            "CloudRemovalConfig": capo_sagemaker_geospatial.types.cloud_removal_config_input.deserialize_json(
                data["CloudRemovalConfig"]
            )
        }
    elif data.get("ZonalStatisticsConfig") is not None:
        import capo_sagemaker_geospatial.types.zonal_statistics_config_input

        return {
            "ZonalStatisticsConfig": capo_sagemaker_geospatial.types.zonal_statistics_config_input.deserialize_json(
                data["ZonalStatisticsConfig"]
            )
        }
    elif data.get("GeoMosaicConfig") is not None:
        import capo_sagemaker_geospatial.types.geo_mosaic_config_input

        return {
            "GeoMosaicConfig": capo_sagemaker_geospatial.types.geo_mosaic_config_input.deserialize_json(
                data["GeoMosaicConfig"]
            )
        }
    elif data.get("StackConfig") is not None:
        import capo_sagemaker_geospatial.types.stack_config_input

        return {
            "StackConfig": capo_sagemaker_geospatial.types.stack_config_input.deserialize_json(
                data["StackConfig"]
            )
        }
    elif data.get("CloudMaskingConfig") is not None:
        import capo_sagemaker_geospatial.types.cloud_masking_config_input

        return {
            "CloudMaskingConfig": capo_sagemaker_geospatial.types.cloud_masking_config_input.deserialize_json(
                data["CloudMaskingConfig"]
            )
        }
    elif data.get("LandCoverSegmentationConfig") is not None:
        import capo_sagemaker_geospatial.types.land_cover_segmentation_config_input

        return {
            "LandCoverSegmentationConfig": capo_sagemaker_geospatial.types.land_cover_segmentation_config_input.deserialize_json(
                data["LandCoverSegmentationConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("JobConfigInput: no recognized variant key")
