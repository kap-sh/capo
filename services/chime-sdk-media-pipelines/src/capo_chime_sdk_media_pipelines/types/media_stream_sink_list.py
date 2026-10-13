"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#MediaStreamSinkList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.media_stream_sink

MediaStreamSinkList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.media_stream_sink.MediaStreamSink"
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaStreamSinkList) -> list:
    import capo_chime_sdk_media_pipelines.types.media_stream_sink

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.media_stream_sink.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MediaStreamSinkList:
    import capo_chime_sdk_media_pipelines.types.media_stream_sink

    out: MediaStreamSinkList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_media_pipelines.types.media_stream_sink.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: MediaStreamSinkList) -> list[Any]:
    import capo_chime_sdk_media_pipelines.types.media_stream_sink

    return [
        capo_chime_sdk_media_pipelines.types.media_stream_sink.redact_sensitive(item)
        for item in value
    ]
