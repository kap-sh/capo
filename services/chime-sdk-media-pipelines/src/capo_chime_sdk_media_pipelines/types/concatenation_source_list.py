"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSourceList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.concatenation_source

ConcatenationSourceList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.concatenation_source.ConcatenationSource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSourceList) -> list:
    import capo_chime_sdk_media_pipelines.types.concatenation_source

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.concatenation_source.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConcatenationSourceList:
    import capo_chime_sdk_media_pipelines.types.concatenation_source

    out: ConcatenationSourceList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_chime_sdk_media_pipelines.types.concatenation_source.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ConcatenationSourceList) -> list[Any]:
    import capo_chime_sdk_media_pipelines.types.concatenation_source

    return [
        capo_chime_sdk_media_pipelines.types.concatenation_source.redact_sensitive(item)
        for item in value
    ]
