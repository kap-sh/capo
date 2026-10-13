"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSinkList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.concatenation_sink

ConcatenationSinkList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.concatenation_sink.ConcatenationSink"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSinkList) -> list:
    import capo_chime_sdk_media_pipelines.types.concatenation_sink

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.concatenation_sink.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConcatenationSinkList:
    import capo_chime_sdk_media_pipelines.types.concatenation_sink

    out: ConcatenationSinkList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_media_pipelines.types.concatenation_sink.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ConcatenationSinkList) -> list[Any]:
    import capo_chime_sdk_media_pipelines.types.concatenation_sink

    return [
        capo_chime_sdk_media_pipelines.types.concatenation_sink.redact_sensitive(item)
        for item in value
    ]
