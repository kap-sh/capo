"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingLoggingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.event_source_mapping_system_log_level


class EventSourceMappingLoggingConfig(TypedDict, closed=True):
    system_log_level: NotRequired[
        "capo_lambda.types.event_source_mapping_system_log_level.EventSourceMappingSystemLogLevel"
    ]
    """<p> The log level you want your event source mapping to use. Lambda event poller only sends system logs at the selected level of detail and lower, where <code>DEBUG</code> is the highest level and <code>WARN</code> is the lowest. For more information about these metrics, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html"> Event source mapping logging</a>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceMappingLoggingConfig) -> dict:
    out: dict = {}
    if "system_log_level" in value:
        import capo_lambda.types.event_source_mapping_system_log_level

        out["SystemLogLevel"] = (
            capo_lambda.types.event_source_mapping_system_log_level.serialize_json(
                value["system_log_level"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventSourceMappingLoggingConfig:
    out: EventSourceMappingLoggingConfig = {}  # type: ignore[typeddict-item]
    if data.get("SystemLogLevel") is not None:
        import capo_lambda.types.event_source_mapping_system_log_level

        out["system_log_level"] = (
            capo_lambda.types.event_source_mapping_system_log_level.deserialize_json(
                data["SystemLogLevel"]
            )
        )
    return out
