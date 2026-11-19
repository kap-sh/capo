"""Generated from Smithy shape ``com.amazonaws.mediaconnect#PidMapRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconnect.types.pid_map_rule

PidMapRules: TypeAlias = list["capo_mediaconnect.types.pid_map_rule.PidMapRule"]


# --- restJson1 ser/de ---
def serialize_json(value: PidMapRules) -> list:
    import capo_mediaconnect.types.pid_map_rule

    out: list = []
    for item in value:
        out.append(capo_mediaconnect.types.pid_map_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> PidMapRules:
    import capo_mediaconnect.types.pid_map_rule

    out: PidMapRules = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mediaconnect.types.pid_map_rule.deserialize_json(item))
    return out
