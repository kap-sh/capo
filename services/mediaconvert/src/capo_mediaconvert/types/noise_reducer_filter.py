"""Generated from Smithy shape ``com.amazonaws.mediaconvert#NoiseReducerFilter``."""

from typing import Literal, TypeAlias, cast

"""Use Noise reducer filter to select one of the following spatial image filtering functions. To use this setting, you must also enable Noise reducer. * Bilateral preserves edges while reducing noise. * Mean (softest), Gaussian, Lanczos, and Sharpen (sharpest) do convolution filtering. * Conserve does min/max noise reduction. * Spatial does frequency-domain filtering based on JND principles. * Temporal optimizes video quality for complex motion. * Perceptual exploits perceptual masking, avoiding encoding bits spent on imperceptible detail. * None disables noise reduction, including the perceptual filter that MediaConvert otherwise applies by default for AVC, HEVC, AV1, MPEG-2, VP8, and VP9 outputs. MediaConvert doesn't apply that default to mezzanine and archival outputs (AVC-Intra, XAVC, Apple ProRes, VC3, Uncompressed), to frame capture outputs, or to outputs that use Dolby Vision, which doesn't support any noise reducer."""
NoiseReducerFilter: TypeAlias = Literal[
    "BILATERAL",
    "MEAN",
    "GAUSSIAN",
    "LANCZOS",
    "SHARPEN",
    "CONSERVE",
    "SPATIAL",
    "TEMPORAL",
    "PERCEPTUAL",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: NoiseReducerFilter) -> str:
    return value


def deserialize_json(data: str) -> NoiseReducerFilter:
    return cast(NoiseReducerFilter, data)
