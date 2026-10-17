"""Generated from Smithy shape ``com.amazonaws.mediaconnect#NdiSourceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.ndi_audio_reference_level


class NdiSourceSettings(TypedDict, closed=True):
    source_name: NotRequired["str"]
    """<p> The exact name of an existing NDI sender that's registered with your discovery server. If included, the format of this name must be <code>MACHINENAME (ProgramName)</code>. </p>"""
    audio_reference_level: NotRequired[
        "capo_mediaconnect.types.ndi_audio_reference_level.NdiAudioReferenceLevel"
    ]
    """<p>The audio reference level of the NDI sender, in decibels relative to full scale (dBFS). Common values are <code>-20</code> (NDI and SMPTE) and <code>-18</code> (EBU). If you don't specify this field, MediaConnect uses <code>-20</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NdiSourceSettings) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["sourceName"] = value["source_name"]
    if "audio_reference_level" in value:
        out["audioReferenceLevel"] = value["audio_reference_level"]
    return out


def deserialize_json(data: dict) -> NdiSourceSettings:
    out: NdiSourceSettings = {}  # type: ignore[typeddict-item]
    if data.get("sourceName") is not None:
        out["source_name"] = data["sourceName"]
    if data.get("audioReferenceLevel") is not None:
        out["audio_reference_level"] = data["audioReferenceLevel"]
    return out
