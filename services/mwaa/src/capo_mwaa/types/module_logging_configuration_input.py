"""Generated from Smithy shape ``com.amazonaws.mwaa#ModuleLoggingConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.logging_enabled
    import capo_mwaa.types.logging_level


class ModuleLoggingConfigurationInput(TypedDict, closed=True):
    enabled: "capo_mwaa.types.logging_enabled.LoggingEnabled"
    """<p>Indicates whether to enable the Apache Airflow log type (e.g. <code>DagProcessingLogs</code>).</p>"""
    log_level: "capo_mwaa.types.logging_level.LoggingLevel"
    """<p>Defines the Apache Airflow log level (e.g. <code>INFO</code>) to send to CloudWatch Logs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModuleLoggingConfigurationInput) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    out["LogLevel"] = value["log_level"]
    return out


def deserialize_json(data: dict) -> ModuleLoggingConfigurationInput:
    out: ModuleLoggingConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    else:
        out["enabled"] = False
    if data.get("LogLevel") is not None:
        out["log_level"] = data["LogLevel"]
    else:
        out["log_level"] = ""
    return out
