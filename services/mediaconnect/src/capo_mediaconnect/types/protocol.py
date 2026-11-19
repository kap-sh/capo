"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Protocol``."""

from typing import Literal, TypeAlias, cast

Protocol: TypeAlias = Literal[
    "zixi-push",
    "rtp-fec",
    "rtp",
    "zixi-pull",
    "rist",
    "st2110-jpegxs",
    "cdi",
    "srt-listener",
    "srt-caller",
    "fujitsu-qos",
    "udp",
    "ndi-speed-hq",
    "rtmp-push",
]


# --- restJson1 ser/de ---
def serialize_json(value: Protocol) -> str:
    return value


def deserialize_json(data: str) -> Protocol:
    return cast(Protocol, data)
