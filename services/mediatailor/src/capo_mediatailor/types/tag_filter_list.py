"""Generated from Smithy shape ``com.amazonaws.mediatailor#TagFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.hls_tag_name

TagFilterList: TypeAlias = list["capo_mediatailor.types.hls_tag_name.HlsTagName"]


# --- restJson1 ser/de ---
def serialize_json(value: TagFilterList) -> list:
    import capo_mediatailor.types.hls_tag_name

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.hls_tag_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagFilterList:
    import capo_mediatailor.types.hls_tag_name

    out: TagFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mediatailor.types.hls_tag_name.deserialize_json(item))
    return out
