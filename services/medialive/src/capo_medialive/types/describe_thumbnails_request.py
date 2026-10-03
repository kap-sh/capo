"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeThumbnailsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string


class DescribeThumbnailsRequest(TypedDict, closed=True):
    channel_id: "capo_medialive.types.__string.__string"
    """Unique ID of the channel"""
    pipeline_id: NotRequired["capo_medialive.types.__string.__string"]
    """Pipeline ID ("0" or "1")"""
    thumbnail_type: NotRequired["capo_medialive.types.__string.__string"]
    """thumbnail type"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeThumbnailsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeThumbnailsRequest:
    out: DescribeThumbnailsRequest = {}  # type: ignore[typeddict-item]
    return out
