"""Generated from Smithy shape ``com.amazonaws.quicksight#VideoExtractionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.video_extraction_status
    import capo_quicksight.types.video_extraction_type


class VideoExtractionConfiguration(TypedDict, closed=True):
    video_extraction_status: (
        "capo_quicksight.types.video_extraction_status.VideoExtractionStatus"
    )
    """<p>The status of video extraction. Valid values are ENABLED and DISABLED.</p>"""
    video_extraction_type: NotRequired[
        "capo_quicksight.types.video_extraction_type.VideoExtractionType"
    ]
    """<p>The type of video extraction to perform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoExtractionConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.video_extraction_status

    out["videoExtractionStatus"] = (
        capo_quicksight.types.video_extraction_status.serialize_json(
            value["video_extraction_status"]
        )
    )
    if "video_extraction_type" in value:
        import capo_quicksight.types.video_extraction_type

        out["videoExtractionType"] = (
            capo_quicksight.types.video_extraction_type.serialize_json(
                value["video_extraction_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> VideoExtractionConfiguration:
    out: VideoExtractionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("videoExtractionStatus") is not None:
        import capo_quicksight.types.video_extraction_status

        out["video_extraction_status"] = (
            capo_quicksight.types.video_extraction_status.deserialize_json(
                data["videoExtractionStatus"]
            )
        )
    else:
        import typing

        out["video_extraction_status"] = typing.cast(
            "capo_quicksight.types.video_extraction_status.VideoExtractionStatus", ""
        )
    if data.get("videoExtractionType") is not None:
        import capo_quicksight.types.video_extraction_type

        out["video_extraction_type"] = (
            capo_quicksight.types.video_extraction_type.deserialize_json(
                data["videoExtractionType"]
            )
        )
    return out
