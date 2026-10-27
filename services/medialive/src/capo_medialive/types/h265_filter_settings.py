"""Generated from Smithy shape ``com.amazonaws.medialive#H265FilterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.auto_filter_settings
    import capo_medialive.types.bandwidth_reduction_filter_settings
    import capo_medialive.types.none_filter_settings
    import capo_medialive.types.perceptual_filter_settings
    import capo_medialive.types.temporal_filter_settings


class H265FilterSettings(TypedDict, closed=True):
    temporal_filter_settings: NotRequired[
        "capo_medialive.types.temporal_filter_settings.TemporalFilterSettings"
    ]
    bandwidth_reduction_filter_settings: NotRequired[
        "capo_medialive.types.bandwidth_reduction_filter_settings.BandwidthReductionFilterSettings"
    ]
    auto_filter_settings: NotRequired[
        "capo_medialive.types.auto_filter_settings.AutoFilterSettings"
    ]
    none_filter_settings: NotRequired[
        "capo_medialive.types.none_filter_settings.NoneFilterSettings"
    ]
    perceptual_filter_settings: NotRequired[
        "capo_medialive.types.perceptual_filter_settings.PerceptualFilterSettings"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: H265FilterSettings) -> dict:
    out: dict = {}
    if "temporal_filter_settings" in value:
        import capo_medialive.types.temporal_filter_settings

        out["temporalFilterSettings"] = (
            capo_medialive.types.temporal_filter_settings.serialize_json(
                value["temporal_filter_settings"]
            )
        )
    if "bandwidth_reduction_filter_settings" in value:
        import capo_medialive.types.bandwidth_reduction_filter_settings

        out["bandwidthReductionFilterSettings"] = (
            capo_medialive.types.bandwidth_reduction_filter_settings.serialize_json(
                value["bandwidth_reduction_filter_settings"]
            )
        )
    if "auto_filter_settings" in value:
        import capo_medialive.types.auto_filter_settings

        out["autoFilterSettings"] = (
            capo_medialive.types.auto_filter_settings.serialize_json(
                value["auto_filter_settings"]
            )
        )
    if "none_filter_settings" in value:
        import capo_medialive.types.none_filter_settings

        out["noneFilterSettings"] = (
            capo_medialive.types.none_filter_settings.serialize_json(
                value["none_filter_settings"]
            )
        )
    if "perceptual_filter_settings" in value:
        import capo_medialive.types.perceptual_filter_settings

        out["perceptualFilterSettings"] = (
            capo_medialive.types.perceptual_filter_settings.serialize_json(
                value["perceptual_filter_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> H265FilterSettings:
    out: H265FilterSettings = {}  # type: ignore[typeddict-item]
    if data.get("temporalFilterSettings") is not None:
        import capo_medialive.types.temporal_filter_settings

        out["temporal_filter_settings"] = (
            capo_medialive.types.temporal_filter_settings.deserialize_json(
                data["temporalFilterSettings"]
            )
        )
    if data.get("bandwidthReductionFilterSettings") is not None:
        import capo_medialive.types.bandwidth_reduction_filter_settings

        out["bandwidth_reduction_filter_settings"] = (
            capo_medialive.types.bandwidth_reduction_filter_settings.deserialize_json(
                data["bandwidthReductionFilterSettings"]
            )
        )
    if data.get("autoFilterSettings") is not None:
        import capo_medialive.types.auto_filter_settings

        out["auto_filter_settings"] = (
            capo_medialive.types.auto_filter_settings.deserialize_json(
                data["autoFilterSettings"]
            )
        )
    if data.get("noneFilterSettings") is not None:
        import capo_medialive.types.none_filter_settings

        out["none_filter_settings"] = (
            capo_medialive.types.none_filter_settings.deserialize_json(
                data["noneFilterSettings"]
            )
        )
    if data.get("perceptualFilterSettings") is not None:
        import capo_medialive.types.perceptual_filter_settings

        out["perceptual_filter_settings"] = (
            capo_medialive.types.perceptual_filter_settings.deserialize_json(
                data["perceptualFilterSettings"]
            )
        )
    return out
