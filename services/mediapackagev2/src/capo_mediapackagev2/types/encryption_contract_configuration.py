"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#EncryptionContractConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.preset_speke20_audio
    import capo_mediapackagev2.types.preset_speke20_video


class EncryptionContractConfiguration(TypedDict, closed=True):
    preset_speke20_audio: (
        "capo_mediapackagev2.types.preset_speke20_audio.PresetSpeke20Audio"
    )
    """<p>A collection of audio encryption presets.</p> <p>Value description: </p> <ul> <li> <p>PRESET-AUDIO-1 - Use one content key to encrypt all of the audio tracks in your stream.</p> </li> <li> <p>PRESET-AUDIO-2 - Use one content key to encrypt all of the stereo audio tracks and one content key to encrypt all of the multichannel audio tracks.</p> </li> <li> <p>PRESET-AUDIO-3 - Use one content key to encrypt all of the stereo audio tracks, one content key to encrypt all of the multichannel audio tracks with 3 to 6 channels, and one content key to encrypt all of the multichannel audio tracks with more than 6 channels.</p> </li> <li> <p>SHARED - Use the same content key for all of the audio and video tracks in your stream.</p> </li> <li> <p>UNENCRYPTED - Don't encrypt any of the audio tracks in your stream.</p> </li> </ul>"""
    preset_speke20_video: (
        "capo_mediapackagev2.types.preset_speke20_video.PresetSpeke20Video"
    )
    """<p>A collection of video encryption presets.</p> <p>Value description: </p> <ul> <li> <p>PRESET-VIDEO-1 - Use one content key to encrypt all of the video tracks in your stream.</p> </li> <li> <p>PRESET-VIDEO-2 - Use one content key to encrypt all of the SD video tracks and one content key for all HD and higher resolutions video tracks.</p> </li> <li> <p>PRESET-VIDEO-3 - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks and one content key for all UHD video tracks.</p> </li> <li> <p>PRESET-VIDEO-4 - Use one content key to encrypt all of the SD video tracks, one content key for HD video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.</p> </li> <li> <p>PRESET-VIDEO-5 - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.</p> </li> <li> <p>PRESET-VIDEO-6 - Use one content key to encrypt all of the SD video tracks, one content key for HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.</p> </li> <li> <p>PRESET-VIDEO-7 - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks and one content key for all UHD video tracks.</p> </li> <li> <p>PRESET-VIDEO-8 - Use one content key to encrypt all of the SD+HD1 video tracks, one content key for HD2 video tracks, one content key for all UHD1 video tracks and one content key for all UHD2 video tracks.</p> </li> <li> <p>SHARED - Use the same content key for all of the video and audio tracks in your stream.</p> </li> <li> <p>UNENCRYPTED - Don't encrypt any of the video tracks in your stream.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionContractConfiguration) -> dict:
    out: dict = {}
    import capo_mediapackagev2.types.preset_speke20_audio

    out["PresetSpeke20Audio"] = (
        capo_mediapackagev2.types.preset_speke20_audio.serialize_json(
            value["preset_speke20_audio"]
        )
    )
    import capo_mediapackagev2.types.preset_speke20_video

    out["PresetSpeke20Video"] = (
        capo_mediapackagev2.types.preset_speke20_video.serialize_json(
            value["preset_speke20_video"]
        )
    )
    return out


def deserialize_json(data: dict) -> EncryptionContractConfiguration:
    out: EncryptionContractConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("PresetSpeke20Audio") is not None:
        import capo_mediapackagev2.types.preset_speke20_audio

        out["preset_speke20_audio"] = (
            capo_mediapackagev2.types.preset_speke20_audio.deserialize_json(
                data["PresetSpeke20Audio"]
            )
        )
    else:
        import typing

        out["preset_speke20_audio"] = typing.cast(
            "capo_mediapackagev2.types.preset_speke20_audio.PresetSpeke20Audio", ""
        )
    if data.get("PresetSpeke20Video") is not None:
        import capo_mediapackagev2.types.preset_speke20_video

        out["preset_speke20_video"] = (
            capo_mediapackagev2.types.preset_speke20_video.deserialize_json(
                data["PresetSpeke20Video"]
            )
        )
    else:
        import typing

        out["preset_speke20_video"] = typing.cast(
            "capo_mediapackagev2.types.preset_speke20_video.PresetSpeke20Video", ""
        )
    return out
