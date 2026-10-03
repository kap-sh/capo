"""Generated from Smithy shape ``com.amazonaws.medialive#FrameCaptureGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.frame_capture_cdn_settings
    import capo_medialive.types.output_location_ref


class FrameCaptureGroupSettings(TypedDict, closed=True):
    destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """The destination for the frame capture files. Either the URI for an Amazon S3 bucket and object, plus a file name prefix (for example, s3ssl://sportsDelivery/highlights/20180820/curling-) or the URI for a MediaStore container, plus a file name prefix (for example, mediastoressl://sportsDelivery/20180820/curling-). The final file names consist of the prefix from the destination field (for example, "curling-") + name modifier + the counter (5 digits, starting from 00001) + extension (which is always .jpg). For example, curling-low.00001.jpg"""
    frame_capture_cdn_settings: NotRequired[
        "capo_medialive.types.frame_capture_cdn_settings.FrameCaptureCdnSettings"
    ]
    """Parameters that control interactions with the CDN."""


# --- restJson1 ser/de ---
def serialize_json(value: FrameCaptureGroupSettings) -> dict:
    out: dict = {}
    if "destination" in value:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    if "frame_capture_cdn_settings" in value:
        import capo_medialive.types.frame_capture_cdn_settings

        out["frameCaptureCdnSettings"] = (
            capo_medialive.types.frame_capture_cdn_settings.serialize_json(
                value["frame_capture_cdn_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FrameCaptureGroupSettings:
    out: FrameCaptureGroupSettings = {}  # type: ignore[typeddict-item]
    if data.get("destination") is not None:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.deserialize_json(
            data["destination"]
        )
    if data.get("frameCaptureCdnSettings") is not None:
        import capo_medialive.types.frame_capture_cdn_settings

        out["frame_capture_cdn_settings"] = (
            capo_medialive.types.frame_capture_cdn_settings.deserialize_json(
                data["frameCaptureCdnSettings"]
            )
        )
    return out
