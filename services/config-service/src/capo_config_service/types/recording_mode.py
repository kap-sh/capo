"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingMode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.recording_frequency
    import capo_config_service.types.recording_mode_overrides


class RecordingMode(TypedDict, closed=True):
    recording_frequency: (
        "capo_config_service.types.recording_frequency.RecordingFrequency"
    )
    """<p>The default recording frequency that Config uses to record configuration changes.</p> <important> <p>Daily recording cannot be specified for the following resource types:</p> <ul> <li> <p> <code>AWS::Config::ResourceCompliance</code> </p> </li> <li> <p> <code>AWS::Config::ConformancePackCompliance</code> </p> </li> <li> <p> <code>AWS::Config::ConfigurationRecorder</code> </p> </li> </ul> <p>For the <b>allSupported</b> (<code>ALL_SUPPORTED_RESOURCE_TYPES</code>) recording strategy, these resource types will be set to Continuous recording.</p> </important>"""
    recording_mode_overrides: NotRequired[
        "capo_config_service.types.recording_mode_overrides.RecordingModeOverrides"
    ]
    """<p>An array of <code>recordingModeOverride</code> objects for you to specify your overrides for the recording mode. The <code>recordingModeOverride</code> object in the <code>recordingModeOverrides</code> array consists of three fields: a <code>description</code>, the new <code>recordingFrequency</code>, and an array of <code>resourceTypes</code> to override.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordingMode) -> dict:
    out: dict = {}
    import capo_config_service.types.recording_frequency

    out["recordingFrequency"] = (
        capo_config_service.types.recording_frequency.serialize_aws_json_1_1(
            value["recording_frequency"]
        )
    )
    if "recording_mode_overrides" in value:
        import capo_config_service.types.recording_mode_overrides

        out["recordingModeOverrides"] = (
            capo_config_service.types.recording_mode_overrides.serialize_aws_json_1_1(
                value["recording_mode_overrides"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordingMode:
    out: RecordingMode = {}  # type: ignore[typeddict-item]
    if data.get("recordingFrequency") is not None:
        import capo_config_service.types.recording_frequency

        out["recording_frequency"] = (
            capo_config_service.types.recording_frequency.deserialize_aws_json_1_1(
                data["recordingFrequency"]
            )
        )
    else:
        import typing

        out["recording_frequency"] = typing.cast(
            "capo_config_service.types.recording_frequency.RecordingFrequency", ""
        )
    if data.get("recordingModeOverrides") is not None:
        import capo_config_service.types.recording_mode_overrides

        out["recording_mode_overrides"] = (
            capo_config_service.types.recording_mode_overrides.deserialize_aws_json_1_1(
                data["recordingModeOverrides"]
            )
        )
    return out
