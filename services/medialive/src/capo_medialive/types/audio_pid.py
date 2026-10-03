"""Generated from Smithy shape ``com.amazonaws.medialive#AudioPid``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max8191
    import capo_medialive.types.audio_dolby_e_decode
    import capo_medialive.types.audio_pre_mixer_settings


class AudioPid(TypedDict, closed=True):
    dolby_e_decode: NotRequired[
        "capo_medialive.types.audio_dolby_e_decode.AudioDolbyEDecode"
    ]
    """Configure decoding options for Dolby E streams - these should be Dolby E frames carried in PCM streams tagged with SMPTE-337. When using the 'pids' array, if this field is not specified and Dolby E content is present, the decoder will extract the specified program. To maintain legacy behavior (allPrograms), explicitly set programSelection to "allChannels"."""
    pid: NotRequired["capo_medialive.types.__integer_min0_max8191.__integerMin0Max8191"]
    """PID value from within a source."""
    premix_settings: NotRequired[
        "capo_medialive.types.audio_pre_mixer_settings.AudioPreMixerSettings"
    ]
    """Optional audio pre-mixer settings for this PID. When specified, allows per-PID audio processing including channel remixing, gain adjustment, and loudness normalization before interleaving."""


# --- restJson1 ser/de ---
def serialize_json(value: AudioPid) -> dict:
    out: dict = {}
    if "dolby_e_decode" in value:
        import capo_medialive.types.audio_dolby_e_decode

        out["dolbyEDecode"] = capo_medialive.types.audio_dolby_e_decode.serialize_json(
            value["dolby_e_decode"]
        )
    if "pid" in value:
        out["pid"] = value["pid"]
    if "premix_settings" in value:
        import capo_medialive.types.audio_pre_mixer_settings

        out["premixSettings"] = (
            capo_medialive.types.audio_pre_mixer_settings.serialize_json(
                value["premix_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioPid:
    out: AudioPid = {}  # type: ignore[typeddict-item]
    if data.get("dolbyEDecode") is not None:
        import capo_medialive.types.audio_dolby_e_decode

        out["dolby_e_decode"] = (
            capo_medialive.types.audio_dolby_e_decode.deserialize_json(
                data["dolbyEDecode"]
            )
        )
    if data.get("pid") is not None:
        out["pid"] = data["pid"]
    if data.get("premixSettings") is not None:
        import capo_medialive.types.audio_pre_mixer_settings

        out["premix_settings"] = (
            capo_medialive.types.audio_pre_mixer_settings.deserialize_json(
                data["premixSettings"]
            )
        )
    return out
