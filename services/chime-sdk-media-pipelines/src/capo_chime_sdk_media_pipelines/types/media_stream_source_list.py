"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamSourceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_stream_source

MediaStreamSourceList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.media_stream_source.MediaStreamSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSourceList) -> list:
    import capo_chime_sdk_media_pipelines.types.media_stream_source

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.media_stream_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MediaStreamSourceList:
    import capo_chime_sdk_media_pipelines.types.media_stream_source

    out: MediaStreamSourceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_media_pipelines.types.media_stream_source.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: MediaStreamSourceList) -> list[Any]:
    import capo_chime_sdk_media_pipelines.types.media_stream_source

    return [
        capo_chime_sdk_media_pipelines.types.media_stream_source.redact_sensitive(item)
        for item in value
    ]
