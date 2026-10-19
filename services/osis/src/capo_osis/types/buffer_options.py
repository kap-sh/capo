"""Generated from Smithy shape ``com.amazonaws.osis#BufferOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_osis.types.boolean


class BufferOptions(TypedDict, closed=True):
    persistent_buffer_enabled: "capo_osis.types.boolean.Boolean"
    """<p>Whether persistent buffering should be enabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BufferOptions) -> dict:
    out: dict = {}
    out["PersistentBufferEnabled"] = value["persistent_buffer_enabled"]
    return out


def deserialize_json(data: dict) -> BufferOptions:
    out: BufferOptions = {}  # type: ignore[typeddict-item]
    if data.get("PersistentBufferEnabled") is not None:
        out["persistent_buffer_enabled"] = data["PersistentBufferEnabled"]
    else:
        out["persistent_buffer_enabled"] = False
    return out
