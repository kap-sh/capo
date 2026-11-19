"""Generated from Smithy shape ``com.amazonaws.mediatailor#HlsTagName``."""

from typing import Literal, TypeAlias, cast

"""<p>The name of an HLS tag that an <code>HLS_TAG_PROCESSOR</code> function can match. The only supported value is <code>EXT-X-DATERANGE</code>.</p>"""
HlsTagName: TypeAlias = Literal["EXT-X-DATERANGE",]


# --- restJson1 ser/de ---
def serialize_json(value: HlsTagName) -> str:
    return value


def deserialize_json(data: str) -> HlsTagName:
    return cast(HlsTagName, data)
