"""Generated from Smithy shape ``com.amazonaws.medialive#HlsOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.__string_min1
    import capo_medialive.types.hls_h265_packaging_type
    import capo_medialive.types.hls_settings


class HlsOutputSettings(TypedDict, closed=True):
    h265_packaging_type: NotRequired[
        "capo_medialive.types.hls_h265_packaging_type.HlsH265PackagingType"
    ]
    """Only applicable when this output is referencing an H.265 video description. Specifies whether MP4 segments should be packaged as HEV1 or HVC1."""
    hls_settings: NotRequired["capo_medialive.types.hls_settings.HlsSettings"]
    """Settings regarding the underlying stream. These settings are different for audio-only outputs."""
    name_modifier: NotRequired["capo_medialive.types.__string_min1.__stringMin1"]
    r"""String concatenated to the end of the destination filename. Accepts \"Format Identifiers\":#formatIdentifierParameters."""
    segment_modifier: NotRequired["capo_medialive.types.__string.__string"]
    """String concatenated to end of segment filenames."""


# --- restJson1 ser/de ---
def serialize_json(value: HlsOutputSettings) -> dict:
    out: dict = {}
    if "h265_packaging_type" in value:
        import capo_medialive.types.hls_h265_packaging_type

        out["h265PackagingType"] = (
            capo_medialive.types.hls_h265_packaging_type.serialize_json(
                value["h265_packaging_type"]
            )
        )
    if "hls_settings" in value:
        import capo_medialive.types.hls_settings

        out["hlsSettings"] = capo_medialive.types.hls_settings.serialize_json(
            value["hls_settings"]
        )
    if "name_modifier" in value:
        out["nameModifier"] = value["name_modifier"]
    if "segment_modifier" in value:
        out["segmentModifier"] = value["segment_modifier"]
    return out


def deserialize_json(data: dict) -> HlsOutputSettings:
    out: HlsOutputSettings = {}  # type: ignore[typeddict-item]
    if data.get("h265PackagingType") is not None:
        import capo_medialive.types.hls_h265_packaging_type

        out["h265_packaging_type"] = (
            capo_medialive.types.hls_h265_packaging_type.deserialize_json(
                data["h265PackagingType"]
            )
        )
    if data.get("hlsSettings") is not None:
        import capo_medialive.types.hls_settings

        out["hls_settings"] = capo_medialive.types.hls_settings.deserialize_json(
            data["hlsSettings"]
        )
    if data.get("nameModifier") is not None:
        out["name_modifier"] = data["nameModifier"]
    if data.get("segmentModifier") is not None:
        out["segment_modifier"] = data["segmentModifier"]
    return out
