"""Generated from Smithy shape ``com.amazonaws.medialive#AacSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__double
    import capo_medialive.types.aac_coding_mode
    import capo_medialive.types.aac_input_type
    import capo_medialive.types.aac_profile
    import capo_medialive.types.aac_rate_control_mode
    import capo_medialive.types.aac_raw_format
    import capo_medialive.types.aac_spec
    import capo_medialive.types.aac_vbr_quality


class AacSettings(TypedDict, closed=True):
    bitrate: NotRequired["capo_medialive.types.__double.__double"]
    """Average bitrate in bits/second. Valid values depend on rate control mode and profile."""
    coding_mode: NotRequired["capo_medialive.types.aac_coding_mode.AacCodingMode"]
    """Mono, Stereo, or 5.1 channel layout. Valid values depend on rate control mode and profile. The adReceiverMix setting receives a stereo description plus control track and emits a mono AAC encode of the description track, with control data emitted in the PES header as per ETSI TS 101 154 Annex E."""
    input_type: NotRequired["capo_medialive.types.aac_input_type.AacInputType"]
    """Set to "broadcasterMixedAd" when input contains pre-mixed main audio + AD (narration) as a stereo pair. The Audio Type field (audioType) will be set to 3, which signals to downstream systems that this stream contains "broadcaster mixed AD". Note that the input received by the encoder must contain pre-mixed audio; the encoder does not perform the mixing. The values in audioTypeControl and audioType (in AudioDescription) are ignored when set to broadcasterMixedAd. Leave set to "normal" when input does not contain pre-mixed audio + AD."""
    profile: NotRequired["capo_medialive.types.aac_profile.AacProfile"]
    """AAC Profile."""
    rate_control_mode: NotRequired[
        "capo_medialive.types.aac_rate_control_mode.AacRateControlMode"
    ]
    """Rate Control Mode."""
    raw_format: NotRequired["capo_medialive.types.aac_raw_format.AacRawFormat"]
    """Sets LATM / LOAS AAC output for raw containers."""
    sample_rate: NotRequired["capo_medialive.types.__double.__double"]
    """Sample rate in Hz. Valid values depend on rate control mode and profile."""
    spec: NotRequired["capo_medialive.types.aac_spec.AacSpec"]
    """Use MPEG-2 AAC audio instead of MPEG-4 AAC audio for raw or MPEG-2 Transport Stream containers."""
    vbr_quality: NotRequired["capo_medialive.types.aac_vbr_quality.AacVbrQuality"]
    """VBR Quality Level - Only used if rateControlMode is VBR."""


# --- restJson1 ser/de ---
def serialize_json(value: AacSettings) -> dict:
    out: dict = {}
    if "bitrate" in value:
        out["bitrate"] = (
            "NaN"
            if value["bitrate"] != value["bitrate"]
            else "Infinity"
            if value["bitrate"] == float("inf")
            else "-Infinity"
            if value["bitrate"] == float("-inf")
            else value["bitrate"]
        )
    if "coding_mode" in value:
        import capo_medialive.types.aac_coding_mode

        out["codingMode"] = capo_medialive.types.aac_coding_mode.serialize_json(
            value["coding_mode"]
        )
    if "input_type" in value:
        import capo_medialive.types.aac_input_type

        out["inputType"] = capo_medialive.types.aac_input_type.serialize_json(
            value["input_type"]
        )
    if "profile" in value:
        import capo_medialive.types.aac_profile

        out["profile"] = capo_medialive.types.aac_profile.serialize_json(
            value["profile"]
        )
    if "rate_control_mode" in value:
        import capo_medialive.types.aac_rate_control_mode

        out["rateControlMode"] = (
            capo_medialive.types.aac_rate_control_mode.serialize_json(
                value["rate_control_mode"]
            )
        )
    if "raw_format" in value:
        import capo_medialive.types.aac_raw_format

        out["rawFormat"] = capo_medialive.types.aac_raw_format.serialize_json(
            value["raw_format"]
        )
    if "sample_rate" in value:
        out["sampleRate"] = (
            "NaN"
            if value["sample_rate"] != value["sample_rate"]
            else "Infinity"
            if value["sample_rate"] == float("inf")
            else "-Infinity"
            if value["sample_rate"] == float("-inf")
            else value["sample_rate"]
        )
    if "spec" in value:
        import capo_medialive.types.aac_spec

        out["spec"] = capo_medialive.types.aac_spec.serialize_json(value["spec"])
    if "vbr_quality" in value:
        import capo_medialive.types.aac_vbr_quality

        out["vbrQuality"] = capo_medialive.types.aac_vbr_quality.serialize_json(
            value["vbr_quality"]
        )
    return out


def deserialize_json(data: dict) -> AacSettings:
    out: AacSettings = {}  # type: ignore[typeddict-item]
    if data.get("bitrate") is not None:
        out["bitrate"] = float(data["bitrate"])
    if data.get("codingMode") is not None:
        import capo_medialive.types.aac_coding_mode

        out["coding_mode"] = capo_medialive.types.aac_coding_mode.deserialize_json(
            data["codingMode"]
        )
    if data.get("inputType") is not None:
        import capo_medialive.types.aac_input_type

        out["input_type"] = capo_medialive.types.aac_input_type.deserialize_json(
            data["inputType"]
        )
    if data.get("profile") is not None:
        import capo_medialive.types.aac_profile

        out["profile"] = capo_medialive.types.aac_profile.deserialize_json(
            data["profile"]
        )
    if data.get("rateControlMode") is not None:
        import capo_medialive.types.aac_rate_control_mode

        out["rate_control_mode"] = (
            capo_medialive.types.aac_rate_control_mode.deserialize_json(
                data["rateControlMode"]
            )
        )
    if data.get("rawFormat") is not None:
        import capo_medialive.types.aac_raw_format

        out["raw_format"] = capo_medialive.types.aac_raw_format.deserialize_json(
            data["rawFormat"]
        )
    if data.get("sampleRate") is not None:
        out["sample_rate"] = float(data["sampleRate"])
    if data.get("spec") is not None:
        import capo_medialive.types.aac_spec

        out["spec"] = capo_medialive.types.aac_spec.deserialize_json(data["spec"])
    if data.get("vbrQuality") is not None:
        import capo_medialive.types.aac_vbr_quality

        out["vbr_quality"] = capo_medialive.types.aac_vbr_quality.deserialize_json(
            data["vbrQuality"]
        )
    return out
