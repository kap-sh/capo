"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterInputThumbnailDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mediaconnect.types.router_input_messages


class RouterInputThumbnailDetails(TypedDict, closed=True):
    thumbnail_messages: (
        "capo_mediaconnect.types.router_input_messages.RouterInputMessages"
    )
    """<p>The messages associated with the router input thumbnail.</p>"""
    thumbnail: NotRequired["bytes"]
    """<p>The thumbnail image, encoded as a Base64-encoded binary data object.</p>"""
    timecode: NotRequired["str"]
    """<p>The timecode associated with the thumbnail.</p>"""
    timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp associated with the thumbnail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouterInputThumbnailDetails) -> dict:
    out: dict = {}
    import capo_mediaconnect.types.router_input_messages

    out["thumbnailMessages"] = (
        capo_mediaconnect.types.router_input_messages.serialize_json(
            value["thumbnail_messages"]
        )
    )
    if "thumbnail" in value:
        import capo_mediaconnect.types._prelude.blob

        out["thumbnail"] = capo_mediaconnect.types._prelude.blob.serialize_json(
            value["thumbnail"]
        )
    if "timecode" in value:
        out["timecode"] = value["timecode"]
    if "timestamp" in value:
        import capo_mediaconnect._protocol.serialize

        out["timestamp"] = capo_mediaconnect._protocol.serialize.fmt_date_time(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> RouterInputThumbnailDetails:
    out: RouterInputThumbnailDetails = {}  # type: ignore[typeddict-item]
    if data.get("thumbnailMessages") is not None:
        import capo_mediaconnect.types.router_input_messages

        out["thumbnail_messages"] = (
            capo_mediaconnect.types.router_input_messages.deserialize_json(
                data["thumbnailMessages"]
            )
        )
    else:
        out["thumbnail_messages"] = []
    if data.get("thumbnail") is not None:
        import capo_mediaconnect.types._prelude.blob

        out["thumbnail"] = capo_mediaconnect.types._prelude.blob.deserialize_json(
            data["thumbnail"]
        )
    if data.get("timecode") is not None:
        out["timecode"] = data["timecode"]
    if data.get("timestamp") is not None:
        import datetime

        out["timestamp"] = datetime.datetime.fromisoformat(
            data["timestamp"].replace("Z", "+00:00")
        )
    return out
