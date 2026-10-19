"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#S3Detail``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.string


class S3Detail(TypedDict, closed=True):
    recording_prefix: "capo_ivs_realtime.types.string.String"
    """<p>The S3 bucket prefix under which the recording is stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Detail) -> dict:
    out: dict = {}
    out["recordingPrefix"] = value["recording_prefix"]
    return out


def deserialize_json(data: dict) -> S3Detail:
    out: S3Detail = {}  # type: ignore[typeddict-item]
    if data.get("recordingPrefix") is not None:
        out["recording_prefix"] = data["recordingPrefix"]
    else:
        out["recording_prefix"] = ""
    return out
