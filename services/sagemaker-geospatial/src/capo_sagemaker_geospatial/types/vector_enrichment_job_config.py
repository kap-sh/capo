"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#VectorEnrichmentJobConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError, SerializationError
from capo_sagemaker_geospatial.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.map_matching_config
    import capo_sagemaker_geospatial.types.reverse_geocoding_config


class VectorEnrichmentJobConfigReverseGeocodingConfigMember(TypedDict, closed=True):
    ReverseGeocodingConfig: "capo_sagemaker_geospatial.types.reverse_geocoding_config.ReverseGeocodingConfig"


class VectorEnrichmentJobConfigMapMatchingConfigMember(TypedDict, closed=True):
    MapMatchingConfig: (
        "capo_sagemaker_geospatial.types.map_matching_config.MapMatchingConfig"
    )


VectorEnrichmentJobConfig: TypeAlias = (
    VectorEnrichmentJobConfigReverseGeocodingConfigMember
    | VectorEnrichmentJobConfigMapMatchingConfigMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: VectorEnrichmentJobConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"VectorEnrichmentJobConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ReverseGeocodingConfig" in value:
        import capo_sagemaker_geospatial.types.reverse_geocoding_config

        return {
            "ReverseGeocodingConfig": capo_sagemaker_geospatial.types.reverse_geocoding_config.serialize_json(
                value["ReverseGeocodingConfig"]
            )
        }
    elif "MapMatchingConfig" in value:
        import capo_sagemaker_geospatial.types.map_matching_config

        return {
            "MapMatchingConfig": capo_sagemaker_geospatial.types.map_matching_config.serialize_json(
                value["MapMatchingConfig"]
            )
        }
    else:
        raise SerializationError("VectorEnrichmentJobConfig: no variant present")


def deserialize_json(data: dict) -> VectorEnrichmentJobConfig:
    if data.get("ReverseGeocodingConfig") is not None:
        import capo_sagemaker_geospatial.types.reverse_geocoding_config

        return {
            "ReverseGeocodingConfig": capo_sagemaker_geospatial.types.reverse_geocoding_config.deserialize_json(
                data["ReverseGeocodingConfig"]
            )
        }
    elif data.get("MapMatchingConfig") is not None:
        import capo_sagemaker_geospatial.types.map_matching_config

        return {
            "MapMatchingConfig": capo_sagemaker_geospatial.types.map_matching_config.deserialize_json(
                data["MapMatchingConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "VectorEnrichmentJobConfig: no recognized variant key"
        )
