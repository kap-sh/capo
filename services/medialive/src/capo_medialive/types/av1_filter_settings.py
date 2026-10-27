"""Generated from Smithy shape ``com.amazonaws.medialive#Av1FilterSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.auto_filter_settings
    import capo_medialive.types.none_filter_settings
    import capo_medialive.types.perceptual_filter_settings


class Av1FilterSettings(TypedDict, closed=True):
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
def serialize_json(value: Av1FilterSettings) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> Av1FilterSettings:
    out: Av1FilterSettings = {}  # type: ignore[typeddict-item]
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
