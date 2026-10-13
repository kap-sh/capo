"""Generated from Smithy shape ``com.amazonaws.mgn#WavesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.wave

WavesList: TypeAlias = list["capo_mgn.types.wave.Wave"]


# --- restJson1 ser/de ---
def serialize_json(value: WavesList) -> list:
    import capo_mgn.types.wave

    out: list = []
    for item in value:
        out.append(capo_mgn.types.wave.serialize_json(item))
    return out


def deserialize_json(data: list) -> WavesList:
    import capo_mgn.types.wave

    out: WavesList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.wave.deserialize_json(item))
    return out


def redact_sensitive(value: WavesList) -> list[Any]:
    import capo_mgn.types.wave

    return [capo_mgn.types.wave.redact_sensitive(item) for item in value]
