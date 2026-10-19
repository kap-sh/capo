"""Generated from Smithy shape ``com.amazonaws.iotevents#LoggingOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.amazon_resource_name
    import capo_iot_events.types.detector_debug_options
    import capo_iot_events.types.logging_enabled
    import capo_iot_events.types.logging_level


class LoggingOptions(TypedDict, closed=True):
    role_arn: "capo_iot_events.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the role that grants permission to AWS IoT Events to perform logging.</p>"""
    level: "capo_iot_events.types.logging_level.LoggingLevel"
    """<p>The logging level.</p>"""
    enabled: "capo_iot_events.types.logging_enabled.LoggingEnabled"
    """<p>If TRUE, logging is enabled for AWS IoT Events.</p>"""
    detector_debug_options: NotRequired[
        "capo_iot_events.types.detector_debug_options.DetectorDebugOptions"
    ]
    """<p>Information that identifies those detector models and their detectors (instances) for which the logging level is given.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingOptions) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    import capo_iot_events.types.logging_level

    out["level"] = capo_iot_events.types.logging_level.serialize_json(value["level"])
    out["enabled"] = value.get("enabled", False)
    if "detector_debug_options" in value:
        import capo_iot_events.types.detector_debug_options

        out["detectorDebugOptions"] = (
            capo_iot_events.types.detector_debug_options.serialize_json(
                value["detector_debug_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> LoggingOptions:
    out: LoggingOptions = {}  # type: ignore[typeddict-item]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    if data.get("level") is not None:
        import capo_iot_events.types.logging_level

        out["level"] = capo_iot_events.types.logging_level.deserialize_json(
            data["level"]
        )
    else:
        import typing

        out["level"] = typing.cast(
            "capo_iot_events.types.logging_level.LoggingLevel", ""
        )
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("detectorDebugOptions") is not None:
        import capo_iot_events.types.detector_debug_options

        out["detector_debug_options"] = (
            capo_iot_events.types.detector_debug_options.deserialize_json(
                data["detectorDebugOptions"]
            )
        )
    return out
