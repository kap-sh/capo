"""Generated from Smithy shape ``com.amazonaws.iot#SetV2LoggingOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.disable_all_logs
    import capo_iot.types.log_event_configurations
    import capo_iot.types.log_level


class SetV2LoggingOptionsRequest(TypedDict, closed=True):
    role_arn: NotRequired["capo_iot.types.aws_arn.AwsArn"]
    """<p>The ARN of the role that allows IoT to write to Cloudwatch logs.</p>"""
    default_log_level: NotRequired["capo_iot.types.log_level.LogLevel"]
    """<p>The default logging level.</p>"""
    disable_all_logs: NotRequired["capo_iot.types.disable_all_logs.DisableAllLogs"]
    """<p>If true all logs are disabled. The default is false.</p>"""
    event_configurations: NotRequired[
        "capo_iot.types.log_event_configurations.LogEventConfigurations"
    ]
    """<p> The list of event configurations that override account-level logging. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SetV2LoggingOptionsRequest) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "default_log_level" in value:
        import capo_iot.types.log_level

        out["defaultLogLevel"] = capo_iot.types.log_level.serialize_json(
            value["default_log_level"]
        )
    if "disable_all_logs" in value:
        out["disableAllLogs"] = value["disable_all_logs"]
    if "event_configurations" in value:
        import capo_iot.types.log_event_configurations

        out["eventConfigurations"] = (
            capo_iot.types.log_event_configurations.serialize_json(
                value["event_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> SetV2LoggingOptionsRequest:
    out: SetV2LoggingOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("defaultLogLevel") is not None:
        import capo_iot.types.log_level

        out["default_log_level"] = capo_iot.types.log_level.deserialize_json(
            data["defaultLogLevel"]
        )
    if data.get("disableAllLogs") is not None:
        out["disable_all_logs"] = data["disableAllLogs"]
    if data.get("eventConfigurations") is not None:
        import capo_iot.types.log_event_configurations

        out["event_configurations"] = (
            capo_iot.types.log_event_configurations.deserialize_json(
                data["eventConfigurations"]
            )
        )
    return out
