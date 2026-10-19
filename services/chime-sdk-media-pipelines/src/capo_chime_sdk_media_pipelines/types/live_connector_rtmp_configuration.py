"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorRTMPConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.audio_channels_option
    import capo_chime_sdk_media_pipelines.types.audio_sample_rate_option
    import capo_chime_sdk_media_pipelines.types.sensitive_string


class LiveConnectorRTMPConfiguration(TypedDict, closed=True):
    url: "capo_chime_sdk_media_pipelines.types.sensitive_string.SensitiveString"
    """<p>The URL of the RTMP configuration.</p>"""
    audio_channels: NotRequired[
        "capo_chime_sdk_media_pipelines.types.audio_channels_option.AudioChannelsOption"
    ]
    """<p>The audio channels set for the RTMP configuration</p>"""
    audio_sample_rate: NotRequired[
        "capo_chime_sdk_media_pipelines.types.audio_sample_rate_option.AudioSampleRateOption"
    ]
    """<p>The audio sample rate set for the RTMP configuration. Default: 48000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LiveConnectorRTMPConfiguration) -> dict:
    out: dict = {}
    out["Url"] = value["url"]
    if "audio_channels" in value:
        import capo_chime_sdk_media_pipelines.types.audio_channels_option

        out["AudioChannels"] = (
            capo_chime_sdk_media_pipelines.types.audio_channels_option.serialize_json(
                value["audio_channels"]
            )
        )
    if "audio_sample_rate" in value:
        out["AudioSampleRate"] = value["audio_sample_rate"]
    return out


def deserialize_json(data: dict) -> LiveConnectorRTMPConfiguration:
    out: LiveConnectorRTMPConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    if data.get("AudioChannels") is not None:
        import capo_chime_sdk_media_pipelines.types.audio_channels_option

        out["audio_channels"] = (
            capo_chime_sdk_media_pipelines.types.audio_channels_option.deserialize_json(
                data["AudioChannels"]
            )
        )
    if data.get("AudioSampleRate") is not None:
        out["audio_sample_rate"] = data["AudioSampleRate"]
    return out


def redact_sensitive(value: LiveConnectorRTMPConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "url" in value:
        out["url"] = "*** Sensitive Data Redacted ***"
    return out
