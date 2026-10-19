"""Generated from Smithy shape ``com.amazonaws.appsync#LogConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.boolean
    import capo_appsync.types.field_log_level
    import capo_appsync.types.string


class LogConfig(TypedDict, closed=True):
    field_log_level: "capo_appsync.types.field_log_level.FieldLogLevel"
    """<p>The field logging level. Values can be NONE, ERROR, or ALL.</p> <ul> <li> <p> <b>NONE</b>: No field-level logs are captured.</p> </li> <li> <p> <b>ERROR</b>: Logs the following information only for the fields that are in error:</p> <ul> <li> <p>The error section in the server response.</p> </li> <li> <p>Field-level errors.</p> </li> <li> <p>The generated request/response functions that got resolved for error fields.</p> </li> </ul> </li> <li> <p> <b>ALL</b>: The following information is logged for all fields in the query:</p> <ul> <li> <p>Field-level tracing information.</p> </li> <li> <p>The generated request/response functions that got resolved for each field.</p> </li> </ul> </li> </ul>"""
    cloud_watch_logs_role_arn: "capo_appsync.types.string.String"
    """<p>The service role that AppSync assumes to publish to CloudWatch logs in your account.</p>"""
    exclude_verbose_content: "capo_appsync.types.boolean.Boolean"
    """<p>Set to TRUE to exclude sections that contain information such as headers, context, and evaluated mapping templates, regardless of logging level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogConfig) -> dict:
    out: dict = {}
    import capo_appsync.types.field_log_level

    out["fieldLogLevel"] = capo_appsync.types.field_log_level.serialize_json(
        value["field_log_level"]
    )
    out["cloudWatchLogsRoleArn"] = value["cloud_watch_logs_role_arn"]
    out["excludeVerboseContent"] = value.get("exclude_verbose_content", False)
    return out


def deserialize_json(data: dict) -> LogConfig:
    out: LogConfig = {}  # type: ignore[typeddict-item]
    if data.get("fieldLogLevel") is not None:
        import capo_appsync.types.field_log_level

        out["field_log_level"] = capo_appsync.types.field_log_level.deserialize_json(
            data["fieldLogLevel"]
        )
    else:
        import typing

        out["field_log_level"] = typing.cast(
            "capo_appsync.types.field_log_level.FieldLogLevel", ""
        )
    if data.get("cloudWatchLogsRoleArn") is not None:
        out["cloud_watch_logs_role_arn"] = data["cloudWatchLogsRoleArn"]
    else:
        out["cloud_watch_logs_role_arn"] = ""
    if data.get("excludeVerboseContent") is not None:
        out["exclude_verbose_content"] = data["excludeVerboseContent"]
    else:
        out["exclude_verbose_content"] = False
    return out
