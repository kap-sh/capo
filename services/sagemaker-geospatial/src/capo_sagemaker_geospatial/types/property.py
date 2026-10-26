"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#Property``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError, SerializationError
from capo_sagemaker_geospatial.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.eo_cloud_cover_input
    import capo_sagemaker_geospatial.types.landsat_cloud_cover_land_input
    import capo_sagemaker_geospatial.types.platform_input
    import capo_sagemaker_geospatial.types.view_off_nadir_input
    import capo_sagemaker_geospatial.types.view_sun_azimuth_input
    import capo_sagemaker_geospatial.types.view_sun_elevation_input


class _Property_EoCloudCover(TypedDict, closed=True):
    EoCloudCover: (
        "capo_sagemaker_geospatial.types.eo_cloud_cover_input.EoCloudCoverInput"
    )


class _Property_ViewOffNadir(TypedDict, closed=True):
    ViewOffNadir: (
        "capo_sagemaker_geospatial.types.view_off_nadir_input.ViewOffNadirInput"
    )


class _Property_ViewSunAzimuth(TypedDict, closed=True):
    ViewSunAzimuth: (
        "capo_sagemaker_geospatial.types.view_sun_azimuth_input.ViewSunAzimuthInput"
    )


class _Property_ViewSunElevation(TypedDict, closed=True):
    ViewSunElevation: (
        "capo_sagemaker_geospatial.types.view_sun_elevation_input.ViewSunElevationInput"
    )


class _Property_Platform(TypedDict, closed=True):
    Platform: "capo_sagemaker_geospatial.types.platform_input.PlatformInput"


class _Property_LandsatCloudCoverLand(TypedDict, closed=True):
    LandsatCloudCoverLand: "capo_sagemaker_geospatial.types.landsat_cloud_cover_land_input.LandsatCloudCoverLandInput"


Property: TypeAlias = (
    _Property_EoCloudCover
    | _Property_ViewOffNadir
    | _Property_ViewSunAzimuth
    | _Property_ViewSunElevation
    | _Property_Platform
    | _Property_LandsatCloudCoverLand
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Property) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Property: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "EoCloudCover" in value:
        import capo_sagemaker_geospatial.types.eo_cloud_cover_input

        return {
            "EoCloudCover": capo_sagemaker_geospatial.types.eo_cloud_cover_input.serialize_json(
                value["EoCloudCover"]
            )
        }
    elif "ViewOffNadir" in value:
        import capo_sagemaker_geospatial.types.view_off_nadir_input

        return {
            "ViewOffNadir": capo_sagemaker_geospatial.types.view_off_nadir_input.serialize_json(
                value["ViewOffNadir"]
            )
        }
    elif "ViewSunAzimuth" in value:
        import capo_sagemaker_geospatial.types.view_sun_azimuth_input

        return {
            "ViewSunAzimuth": capo_sagemaker_geospatial.types.view_sun_azimuth_input.serialize_json(
                value["ViewSunAzimuth"]
            )
        }
    elif "ViewSunElevation" in value:
        import capo_sagemaker_geospatial.types.view_sun_elevation_input

        return {
            "ViewSunElevation": capo_sagemaker_geospatial.types.view_sun_elevation_input.serialize_json(
                value["ViewSunElevation"]
            )
        }
    elif "Platform" in value:
        import capo_sagemaker_geospatial.types.platform_input

        return {
            "Platform": capo_sagemaker_geospatial.types.platform_input.serialize_json(
                value["Platform"]
            )
        }
    elif "LandsatCloudCoverLand" in value:
        import capo_sagemaker_geospatial.types.landsat_cloud_cover_land_input

        return {
            "LandsatCloudCoverLand": capo_sagemaker_geospatial.types.landsat_cloud_cover_land_input.serialize_json(
                value["LandsatCloudCoverLand"]
            )
        }
    else:
        raise SerializationError("Property: no variant present")


def deserialize_json(data: dict) -> Property:
    if data.get("EoCloudCover") is not None:
        import capo_sagemaker_geospatial.types.eo_cloud_cover_input

        return {
            "EoCloudCover": capo_sagemaker_geospatial.types.eo_cloud_cover_input.deserialize_json(
                data["EoCloudCover"]
            )
        }
    elif data.get("ViewOffNadir") is not None:
        import capo_sagemaker_geospatial.types.view_off_nadir_input

        return {
            "ViewOffNadir": capo_sagemaker_geospatial.types.view_off_nadir_input.deserialize_json(
                data["ViewOffNadir"]
            )
        }
    elif data.get("ViewSunAzimuth") is not None:
        import capo_sagemaker_geospatial.types.view_sun_azimuth_input

        return {
            "ViewSunAzimuth": capo_sagemaker_geospatial.types.view_sun_azimuth_input.deserialize_json(
                data["ViewSunAzimuth"]
            )
        }
    elif data.get("ViewSunElevation") is not None:
        import capo_sagemaker_geospatial.types.view_sun_elevation_input

        return {
            "ViewSunElevation": capo_sagemaker_geospatial.types.view_sun_elevation_input.deserialize_json(
                data["ViewSunElevation"]
            )
        }
    elif data.get("Platform") is not None:
        import capo_sagemaker_geospatial.types.platform_input

        return {
            "Platform": capo_sagemaker_geospatial.types.platform_input.deserialize_json(
                data["Platform"]
            )
        }
    elif data.get("LandsatCloudCoverLand") is not None:
        import capo_sagemaker_geospatial.types.landsat_cloud_cover_land_input

        return {
            "LandsatCloudCoverLand": capo_sagemaker_geospatial.types.landsat_cloud_cover_land_input.deserialize_json(
                data["LandsatCloudCoverLand"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Property: no recognized variant key")
