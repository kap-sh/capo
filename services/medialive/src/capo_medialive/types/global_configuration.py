"""Generated from Smithy shape ``com.amazonaws.medialive#GlobalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min_negative60_max60
    import capo_medialive.types.global_configuration_input_end_action
    import capo_medialive.types.global_configuration_low_framerate_inputs
    import capo_medialive.types.global_configuration_output_locking_mode
    import capo_medialive.types.global_configuration_output_timing_source
    import capo_medialive.types.input_loss_behavior
    import capo_medialive.types.output_locking_settings


class GlobalConfiguration(TypedDict, closed=True):
    initial_audio_gain: NotRequired[
        "capo_medialive.types.__integer_min_negative60_max60.__integerMinNegative60Max60"
    ]
    """Value to set the initial audio gain for the Live Event."""
    input_end_action: NotRequired[
        "capo_medialive.types.global_configuration_input_end_action.GlobalConfigurationInputEndAction"
    ]
    """Indicates the action to take when the current input completes (e.g. end-of-file). When switchAndLoopInputs is configured the encoder will restart at the beginning of the first input. When "none" is configured the encoder will transcode either black, a solid color, or a user specified slate images per the "Input Loss Behavior" configuration until the next input switch occurs (which is controlled through the Channel Schedule API)."""
    input_loss_behavior: NotRequired[
        "capo_medialive.types.input_loss_behavior.InputLossBehavior"
    ]
    """Settings for system actions when input is lost."""
    output_locking_mode: NotRequired[
        "capo_medialive.types.global_configuration_output_locking_mode.GlobalConfigurationOutputLockingMode"
    ]
    """Indicates how MediaLive pipelines are synchronized. PIPELINE_LOCKING - MediaLive will attempt to synchronize the output of each pipeline to the other. EPOCH_LOCKING - MediaLive will attempt to synchronize the output of each pipeline to the Unix epoch. DISABLED - MediaLive will not attempt to synchronize the output of pipelines. We advise against disabling output locking because it has negative side effects in most workflows. For more information, see the section about output locking (pipeline locking) in the Medialive user guide."""
    output_timing_source: NotRequired[
        "capo_medialive.types.global_configuration_output_timing_source.GlobalConfigurationOutputTimingSource"
    ]
    """Indicates whether the rate of frames emitted by the Live encoder should be paced by its system clock (which optionally may be locked to another source via NTP) or should be locked to the clock of the source that is providing the input stream."""
    support_low_framerate_inputs: NotRequired[
        "capo_medialive.types.global_configuration_low_framerate_inputs.GlobalConfigurationLowFramerateInputs"
    ]
    """Adjusts video input buffer for streams with very low video framerates. This is commonly set to enabled for music channels with less than one video frame per second."""
    output_locking_settings: NotRequired[
        "capo_medialive.types.output_locking_settings.OutputLockingSettings"
    ]
    """Advanced output locking settings"""


# --- restJson1 ser/de ---
def serialize_json(value: GlobalConfiguration) -> dict:
    out: dict = {}
    if "initial_audio_gain" in value:
        out["initialAudioGain"] = value["initial_audio_gain"]
    if "input_end_action" in value:
        import capo_medialive.types.global_configuration_input_end_action

        out["inputEndAction"] = (
            capo_medialive.types.global_configuration_input_end_action.serialize_json(
                value["input_end_action"]
            )
        )
    if "input_loss_behavior" in value:
        import capo_medialive.types.input_loss_behavior

        out["inputLossBehavior"] = (
            capo_medialive.types.input_loss_behavior.serialize_json(
                value["input_loss_behavior"]
            )
        )
    if "output_locking_mode" in value:
        import capo_medialive.types.global_configuration_output_locking_mode

        out["outputLockingMode"] = (
            capo_medialive.types.global_configuration_output_locking_mode.serialize_json(
                value["output_locking_mode"]
            )
        )
    if "output_timing_source" in value:
        import capo_medialive.types.global_configuration_output_timing_source

        out["outputTimingSource"] = (
            capo_medialive.types.global_configuration_output_timing_source.serialize_json(
                value["output_timing_source"]
            )
        )
    if "support_low_framerate_inputs" in value:
        import capo_medialive.types.global_configuration_low_framerate_inputs

        out["supportLowFramerateInputs"] = (
            capo_medialive.types.global_configuration_low_framerate_inputs.serialize_json(
                value["support_low_framerate_inputs"]
            )
        )
    if "output_locking_settings" in value:
        import capo_medialive.types.output_locking_settings

        out["outputLockingSettings"] = (
            capo_medialive.types.output_locking_settings.serialize_json(
                value["output_locking_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GlobalConfiguration:
    out: GlobalConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("initialAudioGain") is not None:
        out["initial_audio_gain"] = data["initialAudioGain"]
    if data.get("inputEndAction") is not None:
        import capo_medialive.types.global_configuration_input_end_action

        out["input_end_action"] = (
            capo_medialive.types.global_configuration_input_end_action.deserialize_json(
                data["inputEndAction"]
            )
        )
    if data.get("inputLossBehavior") is not None:
        import capo_medialive.types.input_loss_behavior

        out["input_loss_behavior"] = (
            capo_medialive.types.input_loss_behavior.deserialize_json(
                data["inputLossBehavior"]
            )
        )
    if data.get("outputLockingMode") is not None:
        import capo_medialive.types.global_configuration_output_locking_mode

        out["output_locking_mode"] = (
            capo_medialive.types.global_configuration_output_locking_mode.deserialize_json(
                data["outputLockingMode"]
            )
        )
    if data.get("outputTimingSource") is not None:
        import capo_medialive.types.global_configuration_output_timing_source

        out["output_timing_source"] = (
            capo_medialive.types.global_configuration_output_timing_source.deserialize_json(
                data["outputTimingSource"]
            )
        )
    if data.get("supportLowFramerateInputs") is not None:
        import capo_medialive.types.global_configuration_low_framerate_inputs

        out["support_low_framerate_inputs"] = (
            capo_medialive.types.global_configuration_low_framerate_inputs.deserialize_json(
                data["supportLowFramerateInputs"]
            )
        )
    if data.get("outputLockingSettings") is not None:
        import capo_medialive.types.output_locking_settings

        out["output_locking_settings"] = (
            capo_medialive.types.output_locking_settings.deserialize_json(
                data["outputLockingSettings"]
            )
        )
    return out
