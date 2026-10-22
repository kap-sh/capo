"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseReducer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.noise_reducer_filter
    import capo_mediaconvert.types.noise_reducer_filter_settings
    import capo_mediaconvert.types.noise_reducer_spatial_filter_settings
    import capo_mediaconvert.types.noise_reducer_temporal_filter_settings


class NoiseReducer(TypedDict, closed=True):
    filter: NotRequired[
        "capo_mediaconvert.types.noise_reducer_filter.NoiseReducerFilter"
    ]
    """Use Noise reducer filter to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer. * Bilateral preserves edges while reducing noise. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) do convolution filtering. * Conserve does min/max noise reduction. * Spatial does frequency-domain filtering based on JND principles. * Temporal optimizes video quality for complex motion. * Perceptual exploits perceptual masking, avoiding encoding bits spent on imperceptible detail. * None disables noise reduction, including the perceptual filter that MediaConvert otherwise applies by default for AVC, HEVC, AV1, MPEG-2, VP8, and VP9 outputs. MediaConvert doesn't apply that default to mezzanine and archival outputs (AVC-Intra, XAVC, Apple ProRes, VC3, Uncompressed), to frame capture outputs, or to outputs that use Dolby Vision, which doesn't support any noise reducer."""
    filter_settings: NotRequired[
        "capo_mediaconvert.types.noise_reducer_filter_settings.NoiseReducerFilterSettings"
    ]
    """Settings for a noise reducer filter"""
    spatial_filter_settings: NotRequired[
        "capo_mediaconvert.types.noise_reducer_spatial_filter_settings.NoiseReducerSpatialFilterSettings"
    ]
    """Noise reducer filter settings for spatial filter."""
    temporal_filter_settings: NotRequired[
        "capo_mediaconvert.types.noise_reducer_temporal_filter_settings.NoiseReducerTemporalFilterSettings"
    ]
    """Noise reducer filter settings for temporal filter."""


# --- restJson1 ser/de ---
def serialize_json(value: NoiseReducer) -> dict:
    out: dict = {}
    if "filter" in value:
        import capo_mediaconvert.types.noise_reducer_filter

        out["filter"] = capo_mediaconvert.types.noise_reducer_filter.serialize_json(
            value["filter"]
        )
    if "filter_settings" in value:
        import capo_mediaconvert.types.noise_reducer_filter_settings

        out["filterSettings"] = (
            capo_mediaconvert.types.noise_reducer_filter_settings.serialize_json(
                value["filter_settings"]
            )
        )
    if "spatial_filter_settings" in value:
        import capo_mediaconvert.types.noise_reducer_spatial_filter_settings

        out["spatialFilterSettings"] = (
            capo_mediaconvert.types.noise_reducer_spatial_filter_settings.serialize_json(
                value["spatial_filter_settings"]
            )
        )
    if "temporal_filter_settings" in value:
        import capo_mediaconvert.types.noise_reducer_temporal_filter_settings

        out["temporalFilterSettings"] = (
            capo_mediaconvert.types.noise_reducer_temporal_filter_settings.serialize_json(
                value["temporal_filter_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> NoiseReducer:
    out: NoiseReducer = {}  # type: ignore[typeddict-item]
    if data.get("filter") is not None:
        import capo_mediaconvert.types.noise_reducer_filter

        out["filter"] = capo_mediaconvert.types.noise_reducer_filter.deserialize_json(
            data["filter"]
        )
    if data.get("filterSettings") is not None:
        import capo_mediaconvert.types.noise_reducer_filter_settings

        out["filter_settings"] = (
            capo_mediaconvert.types.noise_reducer_filter_settings.deserialize_json(
                data["filterSettings"]
            )
        )
    if data.get("spatialFilterSettings") is not None:
        import capo_mediaconvert.types.noise_reducer_spatial_filter_settings

        out["spatial_filter_settings"] = (
            capo_mediaconvert.types.noise_reducer_spatial_filter_settings.deserialize_json(
                data["spatialFilterSettings"]
            )
        )
    if data.get("temporalFilterSettings") is not None:
        import capo_mediaconvert.types.noise_reducer_temporal_filter_settings

        out["temporal_filter_settings"] = (
            capo_mediaconvert.types.noise_reducer_temporal_filter_settings.deserialize_json(
                data["temporalFilterSettings"]
            )
        )
    return out
