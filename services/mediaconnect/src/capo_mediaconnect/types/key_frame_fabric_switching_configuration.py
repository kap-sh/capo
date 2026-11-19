"""Generated from Smithy shape ``com.amazonaws.mediaconnect#KeyFrameFabricSwitchingConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class KeyFrameFabricSwitchingConfiguration(TypedDict, closed=True):
    key_frame_wait_milliseconds: NotRequired["int"]
    """<p>The maximum time, in milliseconds, that the router output waits for a key frame on the new input before it switches. Set this value to at least the GOP (Group of Pictures) duration of your content, which your upstream encoder determines. If the wait time is shorter than the GOP duration, MediaConnect makes a best effort to switch without a key frame. The default is 3000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyFrameFabricSwitchingConfiguration) -> dict:
    out: dict = {}
    if "key_frame_wait_milliseconds" in value:
        out["keyFrameWaitMilliseconds"] = value["key_frame_wait_milliseconds"]
    return out


def deserialize_json(data: dict) -> KeyFrameFabricSwitchingConfiguration:
    out: KeyFrameFabricSwitchingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("keyFrameWaitMilliseconds") is not None:
        out["key_frame_wait_milliseconds"] = data["keyFrameWaitMilliseconds"]
    return out
