"""Generated from Smithy shape ``com.amazonaws.configservice#RecordingModeOverride``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.description
    import capo_config_service.types.recording_frequency
    import capo_config_service.types.recording_mode_resource_types_list


class RecordingModeOverride(TypedDict, closed=True):
    description: NotRequired["capo_config_service.types.description.Description"]
    """<p>A description that you provide for the override.</p>"""
    resource_types: "capo_config_service.types.recording_mode_resource_types_list.RecordingModeResourceTypesList"
    """<p>A comma-separated list that specifies which resource types Config includes in the override.</p> <important> <p>Daily recording cannot be specified for the following resource types:</p> <ul> <li> <p> <code>AWS::Config::ResourceCompliance</code> </p> </li> <li> <p> <code>AWS::Config::ConformancePackCompliance</code> </p> </li> <li> <p> <code>AWS::Config::ConfigurationRecorder</code> </p> </li> </ul> </important>"""
    recording_frequency: (
        "capo_config_service.types.recording_frequency.RecordingFrequency"
    )
    """<p>The recording frequency that will be applied to all the resource types specified in the override.</p> <ul> <li> <p>Continuous recording allows you to record configuration changes continuously whenever a change occurs.</p> </li> <li> <p>Daily recording allows you to receive a configuration item (CI) representing the most recent state of your resources over the last 24-hour period, only if it’s different from the previous CI recorded. </p> </li> </ul> <note> <p>Firewall Manager depends on continuous recording to monitor your resources. If you are using Firewall Manager, it is recommended that you set the recording frequency to Continuous.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordingModeOverride) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_config_service.types.recording_mode_resource_types_list

    out["resourceTypes"] = (
        capo_config_service.types.recording_mode_resource_types_list.serialize_aws_json_1_1(
            value["resource_types"]
        )
    )
    import capo_config_service.types.recording_frequency

    out["recordingFrequency"] = (
        capo_config_service.types.recording_frequency.serialize_aws_json_1_1(
            value["recording_frequency"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordingModeOverride:
    out: RecordingModeOverride = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("resourceTypes") is not None:
        import capo_config_service.types.recording_mode_resource_types_list

        out["resource_types"] = (
            capo_config_service.types.recording_mode_resource_types_list.deserialize_aws_json_1_1(
                data["resourceTypes"]
            )
        )
    else:
        out["resource_types"] = []
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
    return out
