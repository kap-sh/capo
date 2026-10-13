"""Generated from Smithy shape ``com.amazonaws.medialive#DescribeInputDeviceThumbnailResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__long
    import capo_medialive.types.__string
    import capo_medialive.types.__timestamp
    import capo_medialive.types.content_type
    import capo_medialive.types.input_device_thumbnail


class DescribeInputDeviceThumbnailResponse(TypedDict, closed=True):
    body: "capo_medialive.types.input_device_thumbnail.InputDeviceThumbnail"
    """The binary data for the thumbnail that the Link device has most recently sent to MediaLive."""
    content_type: NotRequired["capo_medialive.types.content_type.ContentType"]
    """Specifies the media type of the thumbnail."""
    content_length: NotRequired["capo_medialive.types.__long.__long"]
    """The length of the content."""
    e_tag: NotRequired["capo_medialive.types.__string.__string"]
    """The unique, cacheable version of this thumbnail."""
    last_modified: NotRequired["capo_medialive.types.__timestamp.__timestamp"]
    """The date and time the thumbnail was last updated at the device."""


def redact_sensitive(value: DescribeInputDeviceThumbnailResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "body" in value:
        out["body"] = "*** Streaming Data Redacted ***"
    return out
