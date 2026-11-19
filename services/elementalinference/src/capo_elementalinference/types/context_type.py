"""Generated from Smithy shape ``com.amazonaws.elementalinference#ContextType``."""

from typing import Literal, TypeAlias, cast

"""<p>One kind of media context that a function reads. Elemental Inference derives this value from the media paths that the request expression references: </p> <ul> <li> <p>FRAMES – Derived from media.frames.</p> </li> <li> <p>SUBTITLES – Derived from media.transcript.</p> </li> <li> <p>CONTEXTUAL_METADATA – Derived from media.contextual.</p> </li> <li> <p>CLIP_METADATA – Derived from media.clip.</p> </li> </ul> <p>A request expression can reference at most one of SUBTITLES, CONTEXTUAL_METADATA, and CLIP_METADATA, in addition to FRAMES. </p>"""
ContextType: TypeAlias = Literal[
    "FRAMES",
    "SUBTITLES",
    "CONTEXTUAL_METADATA",
    "CLIP_METADATA",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContextType) -> str:
    return value


def deserialize_json(data: str) -> ContextType:
    return cast(ContextType, data)
