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


class JobConfigInputBandMathConfigMember(TypedDict, closed=True):
    BandMathConfig: (
        "capo_sagemaker_geospatial.types.band_math_config_input.BandMathConfigInput"
    )


class JobConfigInputResamplingConfigMember(TypedDict, closed=True):
    ResamplingConfig: (
        "capo_sagemaker_geospatial.types.resampling_config_input.ResamplingConfigInput"
    )


class JobConfigInputTemporalStatisticsConfigMember(TypedDict, closed=True):
    TemporalStatisticsConfig: "capo_sagemaker_geospatial.types.temporal_statistics_config_input.TemporalStatisticsConfigInput"


class JobConfigInputCloudRemovalConfigMember(TypedDict, closed=True):
    CloudRemovalConfig: "capo_sagemaker_geospatial.types.cloud_removal_config_input.CloudRemovalConfigInput"


class JobConfigInputZonalStatisticsConfigMember(TypedDict, closed=True):
    ZonalStatisticsConfig: "capo_sagemaker_geospatial.types.zonal_statistics_config_input.ZonalStatisticsConfigInput"


class JobConfigInputGeoMosaicConfigMember(TypedDict, closed=True):
    GeoMosaicConfig: (
        "capo_sagemaker_geospatial.types.geo_mosaic_config_input.GeoMosaicConfigInput"
    )


class JobConfigInputStackConfigMember(TypedDict, closed=True):
    StackConfig: "capo_sagemaker_geospatial.types.stack_config_input.StackConfigInput"


class JobConfigInputCloudMaskingConfigMember(TypedDict, closed=True):
    CloudMaskingConfig: "capo_sagemaker_geospatial.types.cloud_masking_config_input.CloudMaskingConfigInput"


class JobConfigInputLandCoverSegmentationConfigMember(TypedDict, closed=True):
    LandCoverSegmentationConfig: "capo_sagemaker_geospatial.types.land_cover_segmentation_config_input.LandCoverSegmentationConfigInput"


JobConfigInput: TypeAlias = (
    JobConfigInputBandMathConfigMember
    | JobConfigInputResamplingConfigMember
    | JobConfigInputTemporalStatisticsConfigMember
    | JobConfigInputCloudRemovalConfigMember
    | JobConfigInputZonalStatisticsConfigMember
    | JobConfigInputGeoMosaicConfigMember
    | JobConfigInputStackConfigMember
    | JobConfigInputCloudMaskingConfigMember
    | JobConfigInputLandCoverSegmentationConfigMember
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
