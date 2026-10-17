"""Generated from Smithy shape ``com.amazonaws.lambdaweb#LoggingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_web.types.application_log_level
    import capo_lambda_web.types.system_log_level


class LoggingConfig(TypedDict, closed=True):
    log_group: NotRequired["str"]
    """<p>The name of the Amazon CloudWatch Logs log group the web function sends logs to. If you don't specify a value, the default is <code>/aws/lambda/web/{functionName}</code>, and this default is returned in the response.</p>"""
    application_log_level: NotRequired[
        "capo_lambda_web.types.application_log_level.ApplicationLogLevel"
    ]
    """<p>The log level for application logs emitted by the web function. If you don't specify a value, the default is <code>INFO</code>, and this default is returned in the response.</p>"""
    system_log_level: NotRequired[
        "capo_lambda_web.types.system_log_level.SystemLogLevel"
    ]
    """<p>The log level for system logs emitted by the Lambda runtime. If you don't specify a value, the default is <code>INFO</code>, and this default is returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LoggingConfig) -> dict:
    out: dict = {}
    if "log_group" in value:
        out["logGroup"] = value["log_group"]
    if "application_log_level" in value:
        import capo_lambda_web.types.application_log_level

        out["applicationLogLevel"] = (
            capo_lambda_web.types.application_log_level.serialize_json(
                value["application_log_level"]
            )
        )
    if "system_log_level" in value:
        import capo_lambda_web.types.system_log_level

        out["systemLogLevel"] = capo_lambda_web.types.system_log_level.serialize_json(
            value["system_log_level"]
        )
    return out


def deserialize_json(data: dict) -> LoggingConfig:
    out: LoggingConfig = {}  # type: ignore[typeddict-item]
    if data.get("logGroup") is not None:
        out["log_group"] = data["logGroup"]
    if data.get("applicationLogLevel") is not None:
        import capo_lambda_web.types.application_log_level

        out["application_log_level"] = (
            capo_lambda_web.types.application_log_level.deserialize_json(
                data["applicationLogLevel"]
            )
        )
    if data.get("systemLogLevel") is not None:
        import capo_lambda_web.types.system_log_level

        out["system_log_level"] = (
            capo_lambda_web.types.system_log_level.deserialize_json(
                data["systemLogLevel"]
            )
        )
    return out
